"""pyxmolpp2.trajectory module"""
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
import pyxmolpp2.polymer
__all__  = [
"Trajectory",
"TrajectoryException",
"TrajectoryPortion",
"TrajectoryRange",
"TrajectorySlice"
]
class Trajectory():
    @overload
    def __getitem__(self, arg0: int) -> pyxmolpp2.polymer.Frame:
        pass
    @overload
    def __getitem__(self, arg0: slice) -> TrajectorySlice:
        pass
    def __init__(self, reference: pyxmolpp2.polymer.Frame, check_portions_to_match_reference: bool = True) -> None:
        pass
    def __iter__(self) -> TrajectoryRange:
        pass
    def __len__(self) -> int:
        """
Returns number of frames in trajectory
"""
    def push_trajectory_portion(self, portion: TrajectoryPortion) -> None:
        """
Add a trajectory portion
"""
    def set_update_list(self, update_list: pyxmolpp2.polymer.AtomSelection) -> None:
        """
Select atoms which will be updated in iterations
"""
    @property
    def n_frames(self) -> int:
        """Returns number of frames in trajectory"""
    @property
    def size(self) -> int:
        """Returns number of frames in trajectory"""
    pass
class TrajectoryException(Exception, BaseException):
    pass
class TrajectoryPortion():
    def close(self) -> None:
        """
Release file handle
"""
    def match(self, atoms: pyxmolpp2.polymer.AtomSelection) -> bool:
        """
Checks atom names, residue names and residue ids to match reference_atoms
"""
    def n_atoms_per_frame(self) -> int:
        """
Number of atoms per frame
"""
    def n_frames(self) -> int:
        """
Number of frames
"""
    def set_coordinates(self, frame_index: int, atoms: pyxmolpp2.polymer.AtomSelection) -> None:
        """
Set atoms coordinates from frame `frame_index`
"""
    pass
class TrajectoryRange():
    def __next__(self) -> pyxmolpp2.polymer.Frame:
        pass
    pass
class TrajectorySlice():
    def __iter__(self) -> TrajectoryRange:
        pass
    def __len__(self) -> int:
        pass
    pass