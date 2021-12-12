#!/usr/bin/env bash

echo "---
title: ensure-os-pack-tool-task-install
author: yairdar
output:
    html_document:
    toc: true # table of content true
    toc_depth: 3  # upto three depths of headings (specified by #, ## and ###)
    number_sections: true  ## if you want number sections at each table header
    theme: united
---
> `task` tool is used for simple ideomatic api to folders
"

echo "#---- @@act=init stage=ensure-os-tool step=check-tool-task-install"

if [[ "$(task --version | grep 'Task version: v3' | cut -d':' -f1)" == "Task version" ]]
then
    _ospack_tool_task_is_installed=1
else
    _ospack_tool_task_is_installed=0
fi

echo "#---- @@act=over stage=ensure-os-tool step=check-tool-task-install"


echo "#---- @@act=init stage=ensure-os-tool step=tool-task-install"
if [[ "$_ospack_tool_task_is_installed" == "1" ]]; then
    echo "task install-tool-task-install is upto date. version: $(task --version)"
    echo "to force update use --force"
fi
if [[ "$_ospack_tool_task_is_installed" == "0" || "$1" == "--force" ]]; then
    sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
    sudo mv ./bin/task /usr/bin/task && rm -rf ./bin
fi
echo "#---- @@act=over stage=ensure-os-tool step=tool-task-install"
