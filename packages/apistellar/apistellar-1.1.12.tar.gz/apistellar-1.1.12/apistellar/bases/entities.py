import re
import typing

from enum import Enum
from urllib.parse import unquote
from collections import namedtuple
from flask.sessions import SecureCookieSession

from toolkit import cache_classproperty
from toolkit.settings import SettingsLoader, Settings

from .exceptions import Readonly

Cookie = typing.NewType('Cookie', str)
FormParam = typing.NewType("FormParam", str)
Session = typing.NewType("Session", SecureCookieSession)
MultiPartForm = typing.NewType("MultiPartForm", dict)
UrlEncodeForm = typing.NewType("UrlEncodeForm", dict)
DummyFlaskApp = namedtuple(
    "DummyFlaskApp",
    "session_cookie_name,secret_key,permanent_session_lifetime,config")


class File(object):
    mime_type_regex = re.compile(rb"Content-Type: (\S*)")
    content_length_regex = re.compile(rb"Content-Length: (\d*)")
    disposition_regex = re.compile(rb'Content-Disposition: form-data(?:; name\*?=\"?(?:(?P<name_enc>[\w\-]+?)\'(?P<name_lang>\w*)\')?(?P<name>[^\";]*)\"?)?.*?(?:; filename\*?=\"?(?:(?P<enc>[\w\-]+?)\'(?P<lang>\w*)\')?(?P<filename>[^\"]*?)\"?)?(?:$|\r\n)')

    def __init__(self, stream, receive, boundary, name,
                 filename, mimetype, content_length):
        self.content_length = content_length
        self.mimetype = mimetype
        self.receive = receive
        self.filename = filename
        self.name = name
        self.stream = stream
        self.tmpboundary = b"\r\n--" + boundary
        self.boundary_len = len(self.tmpboundary)
        self._last = b""
        self._size = 0
        self.body_iter = self._iter_content()

    def __aiter__(self):
        return self.body_iter

    def __str__(self):
        return f"<{self.__class__.__name__} " \
               f"name={self.name} " \
               f"filename={self.filename} >"

    __repr__ = __str__

    def iter_content(self):
        return self.body_iter

    async def _iter_content(self):
        stream = self.stream
        while True:
            # 如果存在read过程中剩下的，则直接返回
            if self._last:
                yield self._last
                continue

            index = self.stream.body.find(self.tmpboundary)
            if index != -1:
                # 找到分隔线，返回分隔线前的数据
                # 并将分隔及分隔线后的数据返回给stream
                read, stream.body = stream.body[:index], stream.body[index:]
                self._size += len(read)
                yield read
                if self._last:
                    yield self._last
                break
            else:
                if self.stream.closed:
                    raise RuntimeError("Uncomplete content!")
                # 若没有找到分隔线，为了防止分隔线被读取了一半
                # 选择只返回少于分隔线长度的部分body
                read = stream.body[:-self.boundary_len]
                stream.body = stream.body[-self.boundary_len:]
                self._size += len(read)
                yield read
                await self.get_message(self.receive, stream)

    async def read(self, size=10240):
        read = b""
        assert size > 0, (999, "Read size must > 0")
        while len(read) < size:
            try:
                buffer = await self.body_iter.asend(None)
            except StopAsyncIteration:
                return read
            read = read + buffer
            read, self._last = read[:size], read[size:]
        return read

    @staticmethod
    async def get_message(receive, stream):
        message = await receive()

        if not message['type'] == 'http.request':
            raise RuntimeError(
                f"Unexpected ASGI message type: {message['type']}.")

        if not message.get('more_body', False):
            stream.closed = True
        stream.body += message.get("body", b"")

    def tell(self):
        return self._size

    @classmethod
    async def from_boundary(cls, stream, receive, boundary):
        tmp_boundary = b"--" + boundary
        while not stream.closed:
            await cls.get_message(receive, stream)

            if b"\r\n\r\n" in stream.body and tmp_boundary in stream.body or \
                    stream.closed:
                break

        return cls(
            stream, receive, boundary, *cls.get_headers(stream, tmp_boundary))

    @classmethod
    def get_headers(cls, stream, tmp_boundary):
        end_boundary = tmp_boundary + b"--"
        body = stream.body
        index = body.find(tmp_boundary)
        if index == body.find(end_boundary):
            raise StopAsyncIteration
        body = body[index + len(tmp_boundary):]
        split_index = body.find(b"\r\n\r\n")
        header_str, body = body[:split_index], body[split_index + 4:]
        headers = cls.parse(header_str)
        stream.body = body
        return headers

    @classmethod
    def parse(cls, header_str):
        groups = cls.disposition_regex.search(header_str).groupdict()

        filename = groups["filename"] and unquote(groups["filename"].decode())
        if groups["enc"]:
            filename = filename.encode().decode(groups["enc"].decode())

        name = groups["name"] and unquote(groups["name"].decode())
        if groups["name_enc"]:
            name = name.encode().decode(groups["name_enc"].decode())

        mth = cls.mime_type_regex.search(header_str)
        mimetype = mth and mth.group(1).decode()
        mth = cls.content_length_regex.search(header_str) or 0
        content_length = int(mth and mth.group(1))
        assert name, "FileStream iterated without File consumed. "
        return name, filename, mimetype, content_length


class FileStream(object):

    def __init__(self, receive, boundary):
        self.receive = receive
        self.boundary = boundary
        self.body = b""
        self.closed = False

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await File.from_boundary(self, self.receive, self.boundary)


class InheritType(Enum):
    DUPLICATE = 0  # 重名且类型相符，在参数列表和赋值中不体现，在super中体现
    OVERWRITE = 1  # 重名但是类型不同，全部位置要体现，但是需要父类的参数改名字
    NORMAL = 2  # 正常的情况


class Inject(object):

    def __init__(self, type, default):
        self.annotation = self.type = type
        self.name = type.__name__.lower()
        self.default = default

    def __set__(self, instance, value):
        raise Readonly(f"Readonly object of {self.type.__name__}.")

    def __get__(self, instance, cls):
        if instance:
            return instance.__dict__[self.name]
        else:
            return self


class InjectManager(object):

    def __init__(self, default=None):
        self.default = default

    def __lshift__(self, other):
        return Inject(other, self.default)

    def __call__(self, *, default=None):
        return InjectManager(default)


inject = InjectManager()


class SettingsMixin(object):
    settings_path = None

    def property(func):
        """
        这是一个假的property，它存在的意义在于误导pycharm，
        使cache_classproperty可以像property一样被注释类型。
        :param func:
        :return:
        """
        return func

    @property
    @cache_classproperty
    def settings(cls):
        # type: () -> Settings
        return SettingsLoader().load(cls.settings_path or "settings")

    @classmethod
    def register_path(cls, settings_path):
        cls.settings_path = settings_path


del SettingsMixin.property
