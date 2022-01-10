FROM python:3.9-buster

RUN apt update -y && apt install coreutils sudo -y 
SHELL ["/bin/bash", "-c"]

# Install Lib Pack


# Apply os tools settings
COPY _infra/get-started-mini-lib/task.ensure-base-os-tools.sh /_infra/get-started-mini-lib/task.ensure-base-os-tools.sh

RUN /bin/bash \
    /_infra/get-started-mini-lib/task.ensure-base-os-tools.sh \
    install-all

# Apply dev tools settings
COPY _infra/get-started-mini-lib/task.ensure-base-dev-space.sh.yml /_infra/get-started-mini-lib/task.ensure-base-dev-space.sh.yml
RUN task -t \
    /_infra/get-started-mini-lib/task.ensure-base-dev-space.sh.yml \
    install-all

# # apply package managers 
# COPY _infra/get-started-mini-lib/install_conda_mini.tasks.yml /_infra/get-started-mini-lib/install_conda_mini.tasks.yml
# RUN task -t \
#     /_infra/get-started-mini-lib/install_conda_mini.tasks.yml \
#     install-all

COPY version/deps /version/deps
RUN  echo "Installing python deps" \
      && pip install -r /version/deps/deps.pip.run.broad.list.txt \
      && pip install -r /version/deps/deps.pip.test.broad.list.txt

ENV PATH PATH:$HOME/.local/bin
RUN pip install pdm