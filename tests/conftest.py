import pytest
import sys
from pathlib import Path

tasker_dir = str((Path(__file__).resolve().parent.parent / 'tasker').resolve())
sys.path.insert(0, tasker_dir)


@pytest.fixture
def input_value():
    input = 39
    return input
