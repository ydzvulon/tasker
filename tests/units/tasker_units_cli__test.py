from pathlib import Path

from loguru import logger
from pytasker.tasker_ctl import TaskerCli, getcli
from functools import lru_cache


@lru_cache(maxsize=1)
def get_data_dir():
    _me_p = Path(__file__)
    _data_p = _me_p.parent.parent.absolute() / 'data'
    return _data_p


def test_empty_init():
    ojb = TaskerCli()
    assert ojb
    cli = getcli()
    assert cli

    # tfh = ojb.get_task_handler(taskfile_path)


def test__list_includes_on_includes_basic():
    # -- arrange
    taskfile_key = 'includes-basic/Taskfile.yml'
    taskfile_path = get_data_dir() / taskfile_key
    ojb = TaskerCli()

    # -- act
    includes = ojb.list_includes(taskfile_path)

    # -- assert
    assert 'subtask' in includes
    assert includes['subtask'] == 'subtask.stam.tasks.yml'


def test__list_tasks_on_includes_basic():
    # -- arrange
    taskfile_key = 'includes-basic/Taskfile.yml'
    taskfile_path = get_data_dir() / taskfile_key
    ojb = TaskerCli()

    # -- act
    tasks_dict = dict(ojb.list_tasks(taskfile_path))

    # -- assert
    print(tasks_dict)
    assert 'info' in tasks_dict
