"""The BackendGroup for the dummy backend."""
from typing import Mapping

from j5.backends import Backend, BackendGroup
from j5.boards import Board
from j5.boards.j5 import DemoBoard

from .demo import DemoBoardDummyBackend


class DummyBackendGroup(BackendGroup):
    """The backends for the dummy environment."""

    @property
    def board_backend_mapping(self) -> Mapping[Board, Backend]:
        """The supported boards for this backend group."""
        return {DemoBoard: DemoBoardDummyBackend}   # type: ignore
