from loguru import logger
from pytest_steps import test_steps
import tasker.tasker_ctl

# '~/_wd/repos/jenlib'

TASKFILE_TEXT_CORRECT = """\
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

TASKFILE_TEXT_INCORRECT = """\
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
      - finish
  finish: echo finish
"""



def test_suite__taskerctl_joreny_base():
    hand = tasker.tasker_ctl.TaskfileHandler(text=TASKFILE_TEXT_CORRECT)
    changes = hand.resolve_static_task("body")
    expected_jorney = ['A_["_init_"] --> body', 'body --> finish', 'finish --> Z_["_over"]'] # this test is broken because the report task is added
    assert changes['jorney'] == expected_jorney


def test_suite__taskerctl_full_jorney():
    # arrange
    hand = tasker.tasker_ctl.TaskfileHandler(text=TASKFILE_TEXT_CORRECT)

    expected_jorney = [
        'A_["_init_"] --> body',
        'body --> cmd("task report")', # should it be "task report" instead?
        'body --> stage("finish")',
        'finish --> Z_["_over"]' # though the report task breaks an old test
    ]
    expected_jorney_other_option = [
        'A_["_init_"] --> body',
        'body --> cmd("task report") --> stage("finish")',
        'finish --> Z_["_over"]'
    ]
    # act
    changes = hand.resolve_static_task("body")

    # assert
    assert changes['full_jorney'] == expected_jorney