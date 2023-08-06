"""pyxmolpp2.trjtool module"""
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
import pyxmolpp2.polymer
import pyxmolpp2.trajectory
__all__  = [
"DatFile",
"TrjtoolException",
"corrupted_file",
"unexpected_eof"
]
class DatFile(pyxmolpp2.trajectory.TrajectoryPortion):
    def __init__(self, filename: str) -> None:
        pass
    def close(self) -> None:
        """
Release file handle
"""
    def match(self, atoms: pyxmolpp2.polymer.AtomSelection) -> bool:
        """
Checks atom names, residue names and residue ids to match reference_atoms
"""
    def set_coordinates(self, arg0: int, arg1: pyxmolpp2.polymer.AtomSelection, arg2: List[int]) -> None:
        """
Set atoms coordinates from frame #frame_index
"""
    @property
    def n_atoms_per_frame(self) -> int:
        """Number of atoms per frame"""
    @property
    def n_frames(self) -> int:
        """Number of frames in PDB file"""
    pass
class TrjtoolException(Exception, BaseException):
    pass
class corrupted_file(TrjtoolException, Exception, BaseException):
    pass
class unexpected_eof(TrjtoolException, Exception, BaseException):
    pass