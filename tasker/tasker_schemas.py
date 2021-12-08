from dataclasses import dataclass
from typing import List, Dict, Union, Optional
from pydantic import Field, BaseModel


class TaskGoStepCmd(BaseModel):
    """
        task with single command
    """
    cmd: str


class TaskGoStepCmdShadow(BaseModel):
    """
        indicating which task called me
    """
    origin: Union[str, TaskGoStepCmd]
    body: str


class TaskGoStepTask(BaseModel):
    """
        task that calls another task
    """
    task: str
    vars: Optional[Dict[str, str]]



UnionCommandType = Union[str, TaskGoStepCmd, TaskGoStepTask, Dict[str, str]] # receive one of the following task types


class TaskGoTask(BaseModel):
    """
    basic task.
    contain one or  more cmds in a list form.
    possible cmds: str, TaskGoStepCmd, TaskGoStepTask, Dict[str, str]
    """
    desc: Optional[str] = Field(description="description")
    silent: Optional[bool] = Field(False, description="shows commands")
    cmds: List[UnionCommandType]


TaskGoTaskUnion = Union[str, TaskGoTask]


class TaskGoIncludeItem(BaseModel):
    dir: str = '.'
    taskfile: str


TaskGoIncludeItemFull = Union[str, TaskGoIncludeItem]

TaskGoIncludesDict = Dict[str, TaskGoIncludeItem]
TaskGoVarsDict = Dict[str, str] # variables in key:value form
TaskGoTaskDict = Dict[str, TaskGoTaskUnion]


class TaskGoTaskfileUnions(BaseModel):
    """

    """
    version: str
    includes: Optional[TaskGoIncludesDict] = None
    vars: Optional[TaskGoVarsDict] = None
    tasks: Optional[TaskGoTaskDict] = None


class TaskComposition:
    vars: dict
    tasks: dict


class TaskGoTaskfileRepr(BaseModel):
    version: str
    includes: Optional[TaskGoIncludesDict] = None
    vars: Optional[TaskGoVarsDict] = None
    tasks: Optional[TaskGoTaskDict] = None


def next_in_list(k, l: list, remove_pair=False):
    idx_k = l.index(k)
    if k < 0:
        return None
    res = l[idx_k + 1]
    if remove_pair:
        del l[idx_k + 1],
        del l[idx_k]
    return res


def get_from_list(x, ys: list, remove=False):
    """ Returns value from list. Optionally removes.
    Args:
        x: item value
        ys: list
        remove: removes item from list

    Returns:
     item
    """
    res = None
    if x in ys:
        res = x
    if remove:
        ys.remove(x)
    return res


# ---- abstact commands ---


class TaskInvokeFlags(BaseModel):
    output: Optional[str]

    silent: Optional[bool]
    dry: Optional[bool]
    force: Optional[bool]
    summary: Optional[bool]
    parallel: Optional[bool]

    @classmethod
    def from_cmdarr(cls, cmdarr: List[str]):
        from tasker.struct_utils import extradite_tokens_segments
        extract_request = {
            "output": {"nplaces": 2, "aliases": ["--output", "-o"]},
            "dry": {"nplaces": 1, "aliases": ["--dry"]},
            "silent": {"nplaces": 1, "aliases": ["--silent", "-s"]},
            "force": {"nplaces": 1, "aliases": ["--force", "-f"]},
            "summary": {"nplaces": 1, "aliases": ["--summary"]},
            "parallel": {"nplaces": 1, "aliases": ["--parallel", "-p"]}
        }
        extract_result = extradite_tokens_segments(cmdarr, extract_request)
        res = cls(**extract_result)
        return res


class TaskInvokeCmd(BaseModel):
    tool: str = 'task'
    target: str = '.'
    stages_list: List[str]
    vars_dict: Dict[str, str]
    flags: Optional[TaskInvokeFlags]

    @classmethod
    def from_cmd_arr(cls, cmd_arr: List[str]):
        _cmd_arr = list(cmd_arr)
        if not cls.tool == cmd_arr[0]:
            return None
        target = '.'
        if '-d' in cmd_arr:
            target = next_in_list('-d', cmd_arr, remove_pair=True)
        if '-t' in cmd_arr:
            target = next_in_list('-t', cmd_arr, remove_pair=True)


@dataclass
class MatchAliasRule:
    nplaces: int
    aliases: List[str]
