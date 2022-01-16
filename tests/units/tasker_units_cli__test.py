from pathlib import Path

from loguru import logger
from pytasker.tasker_ctl import TaskerCli


def test_empty_init():
    ojb = TaskerCli()
    assert ojb


def test_empty_init():
    _me_p = Path(__file__)
    _data_p = _me_p.parent.parent.absolute() / 'data'
    taskfile_key = 'includes-basic/Taskfile.yml'
    taskfile_path = _data_p / taskfile_key

    ojb = TaskerCli()
    tfh = ojb.get_task_handler(taskfile_path)
    print(tfh)

    includes = ojb.list_includes(taskfile_path)
    print(includes)
    assert includes
