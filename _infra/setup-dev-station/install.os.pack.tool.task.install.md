---
title: install-os-pack-tool-task-install
author: yairdar
output:
    html_document:
    toc: true # table of content true
    toc_depth: 3  # upto three depths of headings (specified by #, ## and ###)
    number_sections: true  ## if you want number sections at each table header
    theme: united
---

> `task` tool is used for simple ideomatic api to folders

```shell
echo "@@act=init stage=install-os-tool step=tool-task-install
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
sudo mv ./bin/task /usr/bin/task
```
