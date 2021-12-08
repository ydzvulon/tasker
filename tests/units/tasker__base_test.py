from tasker_ctl import TaskfileHandler
from tasker_schemas import TaskGoStepTask


def _aux__assert_step_taskname(step: TaskGoStepTask):
    the_type = type(step.task)
    assert the_type is str


def test__some_tasks_go_step():
    example = {
        'task': 'stampme',
        'vars': {'var1': 'val2'}
    }
    the_it = TaskGoStepTask(**example)
    _aux__assert_step_taskname(the_it)


def test__resolve_static_task():
    from pathlib import Path
    # ---- python same logic
    from pathlib import Path
    me_ = Path(__file__)
    root_repo = me_.parent.parent.parent
    the_test_taskfile = root_repo / "tests/data/sample-task/Taskfile.yml"
    handler = TaskfileHandler(upath=the_test_taskfile)
    the_three = handler.resolve_static_task('three')
    print(the_three)



