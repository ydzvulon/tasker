# %%
import yaml

# %%

# %%
# !pwd

# %%
import os
os.getcwd()

# %%

# %%
abspath = '/Users/ivanne/_wd/_public_/tasker/tests/data/sample-task/Taskfile.yml'

# %%
the_yaml_relpath = '../tests/data/sample-task/Taskfile.yml'

# %%
import yaml

with open(the_yaml_relpath, "r") as stream:
    try:
        yaml_parsed = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
yaml_parsed

# %%
yaml_parsed['vars']

# %%
yaml_parsed['tasks']

# %%
yaml_parsed['tasks']['ci-flow']

# %%
yaml_parsed['tasks']['ci-flow']['cmds']

# %%
type(yaml_parsed['tasks']['ci-flow']['cmds'])

# %%

# %%

# %%
type(yaml_parsed)

# %%

# %%
p = {}

# %%
p[3] = 5


# %%
p[1] = 2

# %%
print(p.items())

# %%
z = {}

# %%
z[1] = 2

# %%
z[3] = 5

# %%
print(z.items())

# %%

# %%
import json

# %%
print(json.dumps(yaml_parsed, indent=2))

# %%

# %%

# %%

# %%
2**8

# %%
0-255

# %%
ord('a')

# %%
ord('z')

# %%
ord('Z')

# %%
ord('A')

# %%
ord('\n')

# %%
