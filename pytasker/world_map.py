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


def estiamte_with_skopt():
    import skopt

    from script_step2 import train_evaluate

    SPACE = [
        skopt.space.Real(0.01, 0.5, name='learning_rate', prior='log-uniform'),
        skopt.space.Integer(1, 30, name='max_depth'),
        skopt.space.Integer(2, 100, name='num_leaves'),
        skopt.space.Real(0.1, 1.0, name='feature_fraction', prior='uniform'),
        skopt.space.Real(0.1, 1.0, name='subsample', prior='uniform')]


    @skopt.utils.use_named_args(SPACE)
    def objective(**params):
        return -1.0 * train_evaluate(params)


    results = skopt.forest_minimize(objective, SPACE, n_calls=30, n_random_starts=10)
    best_auc = -1.0 * results.fun
    best_params = results.x

    print('best result: ', best_auc)
    print('best parameters: ', best_params)
