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





