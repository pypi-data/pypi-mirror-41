from typing import Optional, Union, Dict

from .session import Session
from .folder_type import Folder
from joule import errors


class Stream:
    def __init__(self):
        self._id = None
        self.name = ""
        self.description = ""
        self.datatype = ""
        self.keep_us = -1  # KEEP ALL
        self.is_configured = False
        self.is_source = False
        self.is_destination = False
        self.locked = False
        self.active = False
        self.decimate = True

        self.elements = []

    @property
    def id(self) -> int:
        if self._id is None:
            raise errors.ApiError("this is a local model with no ID. See API docs")
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def layout(self):
        return self.datatype.lower()+'_'+str(len(self.elements))

    def to_json(self) -> Dict:
        return {
            "id": self._id,
            "name": self.name,
            "description": self.description,
            "is_configured": self.is_configured,
            "is_source": self.is_source,
            "is_destination": self.is_destination,
            "datatype": self.datatype,
            "keep_us": self.keep_us,
            "locked": self.locked,
            "active": self.active,
            "decimate": self.decimate,
            "elements": [e.to_json() for e in self.elements]
        }


def from_json(json) -> Stream:
    my_stream = Stream()
    my_stream.id = json['id']
    my_stream.name = json['name']
    my_stream.description = json['description']
    my_stream.datatype = json['datatype']
    my_stream.decimate = json['decimate']
    my_stream.keep_us = json['keep_us']
    my_stream.is_configured = json['is_configured']
    my_stream.is_source = json['is_source']
    my_stream.is_destination = json['is_destination']
    my_stream.locked = json['locked']
    my_stream.active = json['active']
    my_stream.elements = [elem_from_json(item) for item in json['elements']]
    return my_stream


class Element:
    def __init__(self):
        self.id = None
        self.index = None
        self.name = ""
        self.units = ""
        self.plottable = False
        self.display_type = 'continuous'
        self.offset = 0
        self.scale_factor = 1.0
        self.default_max = None
        self.default_min = None

        pass

    def to_json(self) -> Dict:
        return {
            'id': self.id,
            'index': self.index,
            'name': self.name,
            'units': self.units,
            'plottable': self.plottable,
            'display_type': self.display_type,
            'offset': self.offset,
            'scale_factor': self.scale_factor,
            'default_max': self.default_max,
            'default_min': self.default_min
        }

def elem_from_json(json) -> Element:
    my_elem = Element()
    my_elem.id = json['id']
    my_elem.index = json['index']
    my_elem.name = json['name']
    my_elem.units =json['units']
    my_elem.plottable = json['plottable']
    my_elem.display_type = json['display_type']
    my_elem.offset = json['offset']
    my_elem.scale_factor = json['scale_factor']
    my_elem.default_min = json['default_min']
    my_elem.default_max = json['default_max']
    return my_elem


class StreamInfo:
    def __init__(self, start: Optional[int], end: Optional[int], rows: int,
                 total_time: int = 0, bytes: int = 0):
        self.start = start
        self.end = end
        self.rows = rows
        self.bytes = bytes
        self.total_time = total_time

    def __repr__(self):
        return "<StreamInfo start=%r end=%r rows=%r, total_time=%r>" % (
            self.start, self.end, self.rows, self.total_time)


def info_from_json(json) -> StreamInfo:
    if json is not None:

        return StreamInfo(json['start'],
                          json['end'],
                          json['rows'],
                          json['total_time'],
                          json['bytes'])
    else:
        return StreamInfo(None,
                          None,
                          0,
                          0,
                          0)


async def stream_delete(session: Session,
                        stream: Union[Stream, str, int]):
    data = {}
    if type(stream) is Stream:
        data["id"] = stream.id
    elif type(stream) is int:
        data["id"] = stream
    elif type(stream) is str:
        data["path"] = stream
    else:
        raise errors.ApiError("Invalid stream datatype. Must be Stream, Path, or ID")

    await session.delete("/stream.json", data)


async def stream_create(session: Session,
                        stream: Stream, folder: Union[Folder, str, int]) -> Stream:
    data = {"stream": stream.to_json()}

    if type(folder) is Folder:
        data["dest_id"] = folder.id
    elif type(folder) is int:
        data["dest_id"] = folder
    elif type(folder) is str:
        data["dest_path"] = folder
    else:
        raise errors.ApiError("Invalid folder datatype. Must be Folder, Path, or ID")

    resp = await session.post("/stream.json", json=data)
    return from_json(resp)


async def stream_info(session: Session,
                      stream: Union[Stream, str, int]) -> StreamInfo:
    data = {}

    if type(stream) is Stream:
        data["id"] = stream.id
    elif type(stream) is int:
        data["id"] = stream
    elif type(stream) is str:
        data["path"] = stream
    else:
        raise errors.ApiError("Invalid stream datatype. Must be Stream, Path, or ID")

    resp = await session.get("/stream.json", data)
    return info_from_json(resp['data_info'])


async def stream_get(session: Session,
                     stream: Union[Stream, str, int]) -> Stream:
    data = {}

    if type(stream) is Stream:
        data["id"] = stream.id
    elif type(stream) is int:
        data["id"] = stream
    elif type(stream) is str:
        data["path"] = stream
    else:
        raise errors.ApiError("Invalid stream datatype. Must be Stream, Path, or ID")

    resp = await session.get("/stream.json", data)
    return from_json(resp)


async def stream_update(session: Session,
                        stream: Stream) -> None:
    return await session.put("/stream.json", stream.to_json())


async def stream_move(session: Session,
                      source: Union[Stream, str, int],
                      destination: Union[Folder, str, int]) -> None:
    data = {}

    if type(source) is Stream:
        data["src_id"] = source.id
    elif type(source) is int:
        data["src_id"] = source
    elif type(source) is str:
        data["src_path"] = source
    else:
        raise errors.ApiError("Invalid source datatype. Must be Stream, Path, or ID")

    if type(destination) is Folder:
        data["dest_id"] = destination.id
    elif type(destination) is int:
        data["dest_id"] = destination
    elif type(destination) is str:
        data["dest_path"] = destination
    else:
        raise errors.ApiError("Invalid destination datatype. Must be Folder, Path, or ID")
    await session.put("/stream/move.json", data)
