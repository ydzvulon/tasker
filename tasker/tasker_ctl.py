#!/usr/bin/env python
import os

import fire
import yaml
import sys
from pathlib import Path
from typing import Union, Sequence, Tuple

from tasker_schemas import TaskGoTaskfileUnions, TaskGoTask, TaskGoStepTask
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
                 upath: Union[Path, str] = '.',
                 treedict: Union[dict, list] = None):
        self.tags = {}
        if text:
            data = yaml.safe_load(text)
        elif treedict:
            data = treedict
        elif upath:
            if upath in ['-', '_']:
                data = yaml.safe_load(sys.stdin)
            else:
                resolved_path = upath_to_taskfile(str(upath))
                if not Path(resolved_path).exists():
                    _msg = f"original path {upath} resolved to {resolved_path}. taskfile dont exist "
                    raise ValueError(_msg)
                with open(resolved_path, "r") as fp:
                    data = yaml.safe_load(fp)
        else:
            if not(text or upath or treedict):
                mgs_ = "required one of text or upath or treedict"
                raise ValueError(mgs_)
            raise Exception("unexpected")
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

    def get_section(self, name:str):
        task_obj: TaskGoTask = getattr(self.taskfile_obj, name)
        return task_obj

    def resolve_static_task(self, taskname):
        """
        Start from provided taskname, and create dependency graph for it
        using tree walk-through.
        Args:
            taskname: taskname to unfold

        Returns: dict with keys journey, known and unknown
        """
        return self._resolve_static_task(taskname)

    def _resolve_static_task(self, taskname, world=None) -> dict:
        # TODO: resolve vars
        import copy
        if world is None:
            world = {'unknown': {}, 'known': {}, 'jorney': [], 'full_jorney':[]}
            world['unknown'].update({taskname: {}})
            world['jorney'].append('A_["_init_"] ' + f'--> {taskname}')
            world['full_jorney'].append('A_["_init_"] ' + f'--> {taskname}')

        stage = self.taskfile_obj.tasks[taskname]
        next_stages = {}

        def add_stage_node_to_full_jorney(taskname, next_stage):
            if next_stage not in world['known']:
                world['unknown'].update({next_stage: taskname})
                world['full_jorney'].append(f'{taskname} --> stage("{next_stage}")')
            next_stages.update({next_stage: 'Z_'})

        def add_cmd_node_to_full_jorney(taskname, next_stage):
            if next_stage not in world['known']:
                world['unknown'].update({next_stage: taskname})
                world['full_jorney'].append(f'{taskname} --> cmd("{next_stage}")')
            next_stages.update({next_stage: 'Z_'})

        if isinstance(stage, str):
            stage_new = {
                'origin': copy.deepcopy(stage),
                'body': copy.deepcopy(stage),
            }
            taskname_record = (f'{taskname} -->' + ' Z_["_over"]') # an additional step against duplicates
            if not any(taskname_record in item for item in world['full_jorney']): # if not present, there will be dupes
                world['full_jorney'].append(taskname_record)
            if not any(taskname_record in item for item in world['jorney']): # if not present, there will be dupes
                world['jorney'].append(taskname_record)

        else:
            stage: TaskGoTask
            for cmd_item in stage.cmds:
                if isinstance(cmd_item, TaskGoStepTask):
                    next_stage = cmd_item.task
                    add_stage_node_to_full_jorney(taskname=taskname, next_stage=next_stage)
                elif isinstance(cmd_item, dict) and 'task' in cmd_item:
                    next_stage = cmd_item['task']
                    add_stage_node_to_full_jorney(taskname=taskname, next_stage=next_stage)
                elif isinstance(cmd_item, str) and cmd_item[0:4] == 'task': #experimental, knocks out old test when enabled. why?
                    next_stage = cmd_item[5::] #experimental
                    add_cmd_node_to_full_jorney(taskname=taskname, next_stage=next_stage)
                # bash commands with tasks parsing implemented above
                else:
                    next_stage = None
                if next_stage: # legacy for non-full jorney
                    if next_stage not in world['known']:
                        world['unknown'].update({next_stage: taskname})
                        world['jorney'].append(f'{taskname} --> {next_stage}')
                    next_stages.update({next_stage: 'Z_'})

        world['known'].update({taskname: list(next_stages.keys())})
        if taskname in world['unknown']:
            del world['unknown'][taskname]

        if world['unknown']:
            for _taskname in dict(world['unknown'].items()):
                self._resolve_static_task(_taskname, world=world)
        return world


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
    return TaskfileHandler()


def cli_and_py_billing_sample():
    # ---- python same logic
    origin_cli = """
        python tasker/tasker_ctl.py \
        --upath tests/data/sample-task/Taskfile.yml \
        resolve_static_task --taskname ci-flow jorney
    """
    # ---- python same logic
    from pathlib import Path
    me_ = Path(__file__)
    root_repo = me_.parent.parent
    the_test_taskfile = root_repo / "tests/data/sample-task/Taskfile.yml"
    cli = TaskfileHandler(upath=the_test_taskfile)
    d = cli.resolve_static_task(taskname='ci-flow')
    print(d['jorney'])
    print(d['full_jorney']) # experimental


if __name__ == '__main__':
    print(os.getcwd())
    # exit(0)
    fire.Fire(TaskfileHandler)
    ### Coment out for testing
    # cli_and_py_billing_sample()



