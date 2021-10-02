import shlex
from tasker_schemas import UnionCommandType, TaskGoStepCmd, TaskGoStepTask

# class BashGoCmd:


class Task

def recognize_steps(steps):
    pass


def recognize_bash_step(step: str):
    cmd_arr = shlex.split(step.strip())


def recognize_step(step: UnionCommandType):
    if isinstance(step, str):
        cmd_block = step
    elif isinstance(step, TaskGoStepCmd):
        cmd_block = step.cmd
    elif isinstance(step, TaskGoStepTask):
        cmd_block = None




