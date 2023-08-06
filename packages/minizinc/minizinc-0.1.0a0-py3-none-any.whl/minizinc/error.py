import re
from pathlib import Path
from typing import NamedTuple, Optional, Sequence


# TODO: Python 3.7 -> @dataclass
class Location(NamedTuple):
    """
    Data class to represent a location within a file
    """
    #: Path to a file
    file: Optional[Path]
    #: Line within the file (default: 0)
    line: int = 0
    #: Columns on the line (default: [])
    columns: Sequence = []

    @classmethod
    def unknown(cls):
        return cls(None)


class MiniZincError(Exception):
    """
    Exception raised for errors raised by the MiniZinc Driver
    """
    #: File location of the error
    location: Location
    #: Explanation of the error
    message: str

    def __init__(self, location: Location, message: str):
        super().__init__(message)
        self.location = location


# TODO: add docstring
class EvaluationError(MiniZincError):
    pass


# TODO: add docstring
class MiniZincAssertionError(EvaluationError):
    pass


# TODO: add docstring
class MiniZincTypeError(MiniZincError):
    pass


# TODO: add docstring
class MiniZincSyntaxError(MiniZincError):
    pass


def parse_error(error_txt: bytes) -> MiniZincError:
    error = MiniZincError
    if b"MiniZinc: evaluation error:" in error_txt:
        error = EvaluationError
        if b"Assertion failed:" in error_txt:
            error = MiniZincAssertionError
    elif b"MiniZinc: type error:" in error_txt:
        error = MiniZincTypeError
    elif b"Error: syntax error" in error_txt:
        error = MiniZincSyntaxError

    location = Location.unknown()
    match = re.search(rb"([^\s]+):(\d+)(.(\d+)-(\d+))?:\s", error_txt)
    if match:
        columns = location.columns
        if match[3]:
            columns = range(int(match[4].decode()), int(match[5].decode()))
        location = Location(Path(match[1].decode()), int(match[2].decode()), columns)

    message = ""
    lst = error_txt.split(b"\n")
    if lst:
        while len(lst) > 1 and lst[-1] == b"":
            lst.pop()
        message = lst[-1].split(b"rror:", 1)[-1].strip()

    return error(location, message.decode())
