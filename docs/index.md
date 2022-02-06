# Tasker

**Tasker**  is a ui and dependency analytics tool,
that works with taskfile configurations.

> Develop on [![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/from-referrer/) `or via` https://www.gitpod.io/#https://github.com/ydzvulon/tasker

> Documentaion on [https://yairdar.github.io/tasker/](https://yairdar.github.io/tasker/)

Sample Configurations can be found in

- [in this repo at ./tests/data](./tests/data)
- [in yd-tut-tasks](http://yairdar.github.io/ydu-tasfile-tut)

## Prerequisites

> We use [task go](http://taskfile.dev) for automation
> and couple more tools.

```shell
# install task yq git curl wget 
bash ./_infra/get-started-mini-lib/task.ensure-base-os-tools.sh
```

## Get Started

Create a dev environment

```bash
# To Create A dev/test environment
task venv-resolve

```
### Documentation

```bash
# To see documentation site in the browser run
task docs-builder:serve-source
```

### Data For Tests

In this repo we use data for test from jenlib

- [sample taskfile](./tests/data/sample-task/Taskfile.yml)

 
