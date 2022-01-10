FROM gitpod/workspace-full

# Install Lib Pack
SHELL ["/bin/bash", "-c"]

RUN sudo apt update -y && sudo apt install python3-pip -y 

# Apply os tools settings
COPY _infra/get-started-mini-lib/task.ensure-base-os-tools.sh /_infra/get-started-mini-lib/task.ensure-base-os-tools.sh
RUN bash \
    /_infra/get-started-mini-lib/task.ensure-base-os-tools.sh \
    install-all

# Apply dev tools settings
COPY _infra/get-started-mini-lib/task.ensure-base-dev-space.sh.yml /_infra/get-started-mini-lib/task.ensure-base-dev-space.sh.yml
RUN task -t \
    /_infra/get-started-mini-lib/task.ensure-base-dev-space.sh.yml \
    install-all

# apply package managers 
COPY _infra/get-started-mini-lib/install_conda_mini.tasks.yml /_infra/get-started-mini-lib/install_conda_mini.tasks.yml
RUN task -t \
    /_infra/get-started-mini-lib/install_conda_mini.tasks.yml \
    install-all
# /home/gitpod/.pyenv/shims/pip
RUN pip install pdm
ENV PATH PATH:$HOME/.local/bin

COPY version/deps /version/deps
RUN  echo "Installing python deps" \
      && pip install pdm \
      && pip install -r /version/deps/deps.pip.run.broad.list.txt \
      && pip install -r /version/deps/deps.pip.test.broad.list.txt
