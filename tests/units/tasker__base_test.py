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


def test__to_dict_if_exists_empty():
    # arrange
    from tasker_ctl import to_dict_if_exists
    # act
    inp = {}
    actual = [(k, v) for k, v in to_dict_if_exists(**inp)]
    # assert
    expected = []
    assert expected == actual


def test__to_dict_if_exists_two_values():
    # arrange
    from tasker_ctl import to_dict_if_exists
    # act
    inp1 = dict(arg1=1, arg2="2",
                argNone=None)
    # , argNothing = NotImplemented
    inp2 = {"arg1": 1, "arg2": "2", "argNone": None}
    actual1 = [(k, v) for k, v in to_dict_if_exists(**inp1)]
    actual2 = [(k, v) for k, v in to_dict_if_exists(**inp2)]
    # assert
    expected = [("arg1", 1), ("arg2", "2")]
    assert expected == actual1
    assert expected == actual2
