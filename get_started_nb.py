# %%
# !pwd

# %%
# !cd tasker

# %%
import sys

# %%
sys.path.append('tasker')

# %%

# %%

# %%
import tasker_ctl

# %%

# %%
tf_path = 'tests/data/sample-task/Taskfile.yml'
tfh = tasker_ctl.TaskfileHandler(upath=tf_path)

# %%
# tfh.resolve_static_task?

# %%
from pandas import DataFrame

# %%
# !pip install pandas

# %%
import yaml

# %%
# yaml.safe_load?

# %%

# %%
tfh.resolve_static_task('ci-flow')

# %%
ls = tfh.list_tasks()
list(ls)

# %%
tfh.tags

# %%

# %%

# %%
from pathlib import Path

# %%
print(Path(tf_path).read_text())

# %%
tfh.get_section('tasks')

# %%

# %%
tfh.get_section('version')

# %%

# %%
# !python tasker/tasker_ctl.py --upath tests/data/sample-task/Taskfile.yml get-section tasks two

# %%
# !python tasker/tasker_ctl.py --upath tests/data/sample-task/Taskfile.yml get-section vars

# %%
# !python tasker/tasker_ctl.py --upath tests/data/sample-task/Taskfile.yml get-section vars GREETING

# %%
tfh.get_section('vars')

# %%
tfh.get_section('vars')['GREETING']

# %%
tfh.resolve_static_task('three')

# %%
tfh.resolve_static_task('three')['jorney']

# %%
tfh.get_section('tasks')['three'].cmds

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
