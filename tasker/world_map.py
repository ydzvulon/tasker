from typing import Dict, List, Any
from pydantic import BaseModel, Field

from tasker_schemas import TaskGoTaskfileUnions, TaskGoTaskUnion, TaskGoStepCmdShadow


class ShadowFile(BaseModel):
    source_upath: str
    text_content: str
    struct_content: str
    referenced_by: List[str]


class ShadowStage(BaseModel):
    source_upath: str
    text_content: str
    struct_content: str
    referenced_by: List[str]
    references_at: List[str]


class ShadowStep(BaseModel):
    source_upath: str
    text_content: str
    struct_content: str
    referenced_by: List[str]
    references_at: List[str]


class WorldPartReflection(BaseModel):
    files: Dict[str, ShadowFile] = []
    stages: Dict[str, ShadowStage] = []
    steps: Dict[str, ShadowStep] = []
    addrbook: Dict[str, Any] = []


class WorldReflectionHolder:
    def __init__(self):
        self.world = WorldPartReflection()

    def absorb_stage(self, name, stage: TaskGoTaskUnion):
        # TODO: - [] check name for collisions
        self.world.stages[name] = ShadowStage(stage)

    def load__task_struct_raw(self, other: TaskGoTaskfileUnions):
        for name, stage in other.tasks:
            self.absorb_stage(name, stage)

    def load_text(self, text: str):
        pass

    def load_file(self, upath: str):
        pass

    def load_state(self, upath: str):
        pass

    def dump_state(self, upath: str):
        pass


#

# def walk_on_tasks(taskdoc: TaskGoTaskfileUnions, stage_name: str, journey: dict = None):
#     journey = journey or dict()
#     stage_body = taskdoc.tasks[stage_name]
#     if isinstance(stage_body, str):
#         stage_body = TaskGoStepCmdShadow(origin=stage_body, body=stage_body)
#     elif

