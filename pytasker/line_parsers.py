from functools import singledispatch

from tasker_schemas import UnionCommandType, TaskGoStepCmd


# str, TaskGoStepCmd, TaskGoStepTask, Dict[str, str]

@singledispatch
def recognize_step_any(arg: UnionCommandType, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)
    return arg


@recognize_step_any.register
def recognize_step_bash(arg: str, verbose=False):
    pass

@recognize_step_any.register
def recognize_step_bash(arg: TaskGoStepCmd, verbose=False):
    pass
