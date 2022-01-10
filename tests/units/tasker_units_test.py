import os
from pathlib import Path

from pytest_steps import test_steps
from pytasker import tasker_ctl

# '~/_wd/repos/jenlib'

TASKFILE_TEXT = """
version: "3"
vars:
  a: "3"
tasks:
  first: echo first
  second: echo second
  body:  
    desc: _
    cmds:
      - task report
      - task: finish
        vars: {status: ok}
  finish: echo finish
"""


@test_steps('step_a', 'step_b')
def test_suite__taskerctl_2():
    print("@@act=declare block=step name=test-list-tasks goal='test list_tasks method'")
    hand = tasker_ctl.TaskfileHandler(text=TASKFILE_TEXT)
    expected = ['first', 'second', 'body']
    actual = [it[0] for it in hand.list_tasks()]
    # for it in expected:
    #     assert it in actual
    assert set(expected).intersection(set(actual)) == set(expected)
    yield

    print("@@act=declare block=step name=test-grow-taskworld goal='test list_tasks method'")
    changes = hand.resolve_static_task("body")
    assert changes['jorney'] == ['A_["_init_"] --> body', 'body --> finish', 'finish --> Z_["_over"]']
    yield


def test__tree_dict__resolve_static_task_input_arg_for_tasker_from_scratch():
    # arrange
    treedict = {
        'version': 3,
        'vars': {'AAA': 3, 'BBB': "BBB"},
        'tasks': {
            'one-liner': 'ls .',
            'complex': {
                'desc': '_',
                'cmds': [
                    'ls -alh .',
                    {'task': 'one-liner'}
                ]
            }
        }
    }
    handler = tasker_ctl.TaskfileHandler(treedict=treedict)
    # act
    changes = handler.resolve_static_task('complex')
    expected_journey = [
        'A_["_init_"] --> complex', 'complex --> one-liner', 'one-liner --> Z_["_over"]'
    ]
    assert changes['jorney'] == expected_journey


# TODO: fix it later
def test__tree_dict__input_arg_for_tasker_from_text01():
    import yaml
    text = TASKFILE_TEXT
    treedict = yaml.safe_load(text)

    # dynamicly add more stages to taskfile
    treedict['tasks']['new_task'] = {'task': 'first'}

    handler = tasker_ctl.TaskfileHandler(treedict=treedict)
    actual_tasks = [it[0] for it in handler.list_tasks()]
    assert 'first' in actual_tasks, "Missing orginal task first"
    assert 'new_task' in actual_tasks, "Missing dynamicly added task 'new_task'"


def test__tree_dict__input_arg_for_tasker_from_text02():
    import yaml
    text = TASKFILE_TEXT
    treedict = yaml.safe_load(text)
    # dynamicly add more stages to taskfile
    treedict['tasks']['new_task'] = {'cmds': [{'task': 'first'}]}

    handler = tasker_ctl.TaskfileHandler(treedict=treedict)
    actual_tasks = [it[0] for it in handler.list_tasks()]
    assert 'new_task' in actual_tasks, "Missing dynamicly added task 'new_task'"


def test_suite__taskerctl_2_input_validation(tmpdir):
    # arrange
    print("sadfasdfsldihflsdiuflisdhjlisdjflsdkjfl;ksdkj;j")
    print(os.getcwd())
    pp = Path('.') / '__tmp__' / '__tmp__'
    pp.mkdir(exist_ok=True, parents=True)
    os.chdir(str(pp))
    try:
        # act
        hand = tasker_ctl.TaskfileHandler()
        assert False
    except ValueError as err:
        err_str = str(err)
        # assert
        assert "original path . resolved to Taskfile.yml. taskfile dont exist" in err_str
    except Exception as ex:
        print(ex)


def test_suite__taskerctl_2_input_validation_02():
    # arrange
    import pytest
    with pytest.raises(ValueError) as excinfo:
        hand = tasker_ctl.TaskfileHandler()


def test_recursion_depth():
    import pytest
    # arrange
    def f():
        f()

    with pytest.raises(RuntimeError) as excinfo:
        f()
    assert "maximum recursion" in str(excinfo.value)


def test_recursion_depth_exc():
    def f():
        f()

    try:
        f()
    except RuntimeError as ex:
        assert "maximum recursion" in str(ex)


if __name__ == '__main__':
    import fire

    fire.Fire()
