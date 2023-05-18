from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStatsResp(_message.Message):
    __slots__ = ["statsEntities"]
    STATSENTITIES_FIELD_NUMBER: _ClassVar[int]
    statsEntities: _containers.RepeatedCompositeFieldContainer[StatsEntity]
    def __init__(self, statsEntities: _Optional[_Iterable[_Union[StatsEntity, _Mapping]]] = ...) -> None: ...

class SearchReq(_message.Message):
    __slots__ = ["search"]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    search: str
    def __init__(self, search: _Optional[str] = ...) -> None: ...

class StatsEntity(_message.Message):
    __slots__ = ["CockSize", "FirstName", "LastName", "Username", "id"]
    COCKSIZE_FIELD_NUMBER: _ClassVar[int]
    CockSize: int
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    FirstName: str
    ID_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    LastName: str
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    Username: str
    id: int
    def __init__(self, id: _Optional[int] = ..., Username: _Optional[str] = ..., FirstName: _Optional[str] = ..., LastName: _Optional[str] = ..., CockSize: _Optional[int] = ...) -> None: ...
