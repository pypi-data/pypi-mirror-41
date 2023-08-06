"""pyxmolpp2.pdb module"""
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
import pyxmolpp2.polymer
import pyxmolpp2.trajectory
__all__  = [
"basic_PdbRecords",
"FieldName",
"PdbException",
"PdbFieldReadError",
"PdbFile",
"PdbRecordType",
"PdbUknownRecord",
"PdbUknownRecordField",
"RecordName",
"StandardPdbRecords",
"AlteredPdbRecords"
]
class basic_PdbRecords():
    def get_record(self, record_name: RecordName) -> PdbRecordType:
        pass
    pass
class FieldName():
    def __init__(self, name: str) -> None:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def __hash__(self) -> int:
        pass
    @property
    def str(self) -> str:
        pass
    pass
class PdbException(Exception, BaseException):
    pass
class PdbFieldReadError(PdbException, Exception, BaseException):
    pass
class PdbFile(pyxmolpp2.trajectory.TrajectoryPortion):
    @overload
    def __init__(self, filename: str, db: basic_PdbRecords) -> None:
        pass
    @overload
    def __init__(self, filename: str) -> None:
        pass
    def close(self) -> None:
        """
Release file handle
"""
    def get_frame(self) -> pyxmolpp2.polymer.Frame:
        """
Read first frame from PDB file
"""
    def get_frames(self) -> List[pyxmolpp2.polymer.Frame]:
        """
Read all frames from PDB file
"""
    def match(self, reference_atoms: pyxmolpp2.polymer.AtomSelection) -> bool:
        """
Checks atom names, residue names and residue ids to match reference_atoms
"""
    def set_coordinates(self, frame_index: int, atoms: pyxmolpp2.polymer.AtomSelection) -> None:
        """
Set atoms coordinates from frame #frame_index
"""
    @property
    def n_atoms_per_frame(self) -> int:
        """Number of atoms in first frame"""
    @property
    def n_frames(self) -> int:
        """Number of frames in PDB file"""
    pass
class PdbRecordType():
    pass
class PdbUknownRecord(PdbException, Exception, BaseException):
    pass
class PdbUknownRecordField(PdbException, Exception, BaseException):
    pass
class RecordName():
    def __init__(self, name: str) -> None:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def __hash__(self) -> int:
        pass
    @property
    def str(self) -> str:
        pass
    pass
class StandardPdbRecords(basic_PdbRecords):
    def get_record(self, record_name: RecordName) -> PdbRecordType:
        pass
    @staticmethod
    def instance() -> basic_PdbRecords:
        pass
    pass
class AlteredPdbRecords(basic_PdbRecords):
    def __init__(self, basic: basic_PdbRecords) -> None:
        pass
    def alter_record(self, record_name: RecordName, field_name: FieldName, colons: List[int]) -> None:
        """
Alter/create PDB record field
"""
    def get_record(self, record_name: RecordName) -> PdbRecordType:
        pass
    pass