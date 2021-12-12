# %%
! echo "@@act=init stage=resolve-pip-deps step=install-run-requirerments"
! pip install -r version/deps/deps.pip.run.broad.list.txt
! echo "@@act=over stage=resolve-pip-deps step=... install-run-requirerments result.deps_list=$(echo $(cat version/deps/deps.pip.run.broad.list.txt)) ...!"

# %%
! echo "@@act=init stage=resolve-pip-deps step=install-test-requirerments"
! pip install -r version/deps/deps.pip.test.broad.list.txt
! echo "@@act=over stage=resolve-pip-deps step=... install-test-requirerments result.deps_list=$(echo $(cat version/deps/deps.pip.run.broad.list.txt)) ...!"

# %%
! curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py  | tee /tmp/get-poetry.py
! which poetry || python /tmp/get-poetry.py

# %%
! echo source $HOME/.poetry/env

# %%
