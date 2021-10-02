from loguru import logger
from pytest_steps import test_steps
import taskerctl

# '~/_wd/repos/jenlib'

TASKFILE_TEXT = """\
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
"""


@test_steps('step_a', 'step_b', 'step_c')
def test_suite__taskerctl():

    print("@@act=declare block=step name=test-list-tasks goal='test list_tasks method'")
    hand = taskerctl.TaskHandler(text=TASKFILE_TEXT)
    expected = ['first', 'second', 'body']
    actual = [it[0] for it in hand.list_tasks()]
    assert set(expected) == set(actual)
    yield

    print("@@act=declare block=step name=test-grow-taskworld goal='test list_tasks method'")
    changes = hand.ingrain()
    assert not False  # replace with your logic
    intermediate_a = 'hello'
    yield

    # Step B
    print("step b")
    assert not False  # replace with your logic
    yield

    # Step C
    print("step c")
    new_text = intermediate_a + " ... augmented"
    print(new_text)
    assert len(new_text) == 19
    yield
