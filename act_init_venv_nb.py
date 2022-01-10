# %%
! echo "@@act=init stage=resolve-pip-deps step=install-run-requirerments"
! pip install -r version/deps/deps.pip.run.broad.list.txt
! echo "@@act=over stage=resolve-pip-deps step=... install-run-requirerments result.deps_list=$(echo $(cat version/deps/deps.pip.run.broad.list.txt)) ...!"

# %%
! echo "@@act=init stage=resolve-pip-deps step=install-test-requirerments"
! pip install -r version/deps/deps.pip.test.broad.list.txt
! echo "@@act=over stage=resolve-pip-deps step=... install-test-requirerments result.deps_list=$(echo $(cat version/deps/deps.pip.run.broad.list.txt)) ...!"

# %%
! curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
! which pdm

# %%
! echo export PATH=PATH:$HOME/.local/bin

# %%
