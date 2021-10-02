#!/usr/bin/env python
import fire
import yaml
import sys
from pathlib import Path
from typing import Union, Sequence, Tuple

from tasker_schemas import TaskGoTaskfileUnions, TaskGoTask
from struct_utils import safe_get
import task_keys
from world_map import WorldPartReflection


def to_dict_if_exists(**kwargs):
    for k, v in kwargs.items():
        if v is not None:
            yield k, v


class TaskfileHandler:
    def __init__(self, *,
                 text: str = None,
                 upath: Path = None,
                 treedict: Union[dict, list] = None):
        self.tags = {}
        if text:
            data = yaml.safe_load(text)
        elif treedict:
            data = treedict
        else:
            with open(upath, "r") as stream:
                data = yaml.safe_load(stream)

        self._data = data
        self.taskfile_obj = TaskGoTaskfileUnions(**data)
        self.world_shadow = WorldPartReflection()

    def list_tasks(self) -> Sequence[Tuple[str, str]]:
        """ Iterates over tasks
        Returns:
            list of tasks
        """
        for (name, task_dict) in self.taskfile_obj.tasks.items():
            yield name, safe_get('desc', task_dict)

    def get_stage(self, name:str):
        task_obj: TaskGoTask = getattr(self.taskfile_obj, name)
        return task_obj

    def resolve_static_task(self, taskname):
        # TODO: resolve vars
        self.world_shadow.get_taskname()
        self.resolve_tasks()

    def resolve_tasks(self):
        self.taskfile_obj.tasks.items()


def upath_to_taskfile(upath: str) -> str:
    if upath == '.':
        return 'Taskfile.yml'
    return upath


# from functools import lru_cache

class TaskerCli:

    def __init__(self):
        pass

    def get_task_handler(self, taskfile=None) -> TaskfileHandler:
        if taskfile in ['-', '_']:
            data = yaml.safe_load(sys.stdin)
        else:
            taskfile = upath_to_taskfile(taskfile)
            with open(taskfile, "r") as stream:
                data = yaml.safe_load(stream)
        res = TaskfileHandler(treedict=data)
        return res

    def list_includes(self, taskfile):
        handler = self.get_task_handler(taskfile=taskfile)
        return handler.taskfile_obj.includes

    def list_tasks(self, taskfile):
        return self.get_task_handler(taskfile).list_tasks()


def getcli():
    return TaskerCli()


if __name__ == '__main__':
    fire.Fire(TaskerCli)
