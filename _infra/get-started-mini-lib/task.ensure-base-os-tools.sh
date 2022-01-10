#!/usr/bin/env bash

# #14
# set -x
set -e

# ###--- PREVENT sudo INSTALL ---
if [ -f $(which sudo || echo _none_) ]; then
    _MAYBE_SUDO_=sudo
else
    _MAYBE_SUDO_=
fi
$_MAYBE_SUDO_ apt update -y

# ### update packages info TODO: check if docker


# _def_minimal_os_took_pack_list__for_dev=""

for _it in curl wget git vim 
do
    if [ -f $(which $_it || echo _none_) ]; then
        echo "$_it is upto date"
    else
        MISSING="$MISSING $_it"
        echo "new MISSING=$MISSING"
    fi
done

if [ "$(echo $MISSING)" != "" ]; then
    $_MAYBE_SUDO_ apt install -y $MISSING
fi


# ###--- install taskfile ---
if [ -f $(which task  || echo _none_ ) ]; then
    echo "os.pack.tool.task.is.present"
else
    pushd /tmp
    echo "Install task exe from web installer of taskfile.dev"
    sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d \
        && $_MAYBE_SUDO_ mv ./bin/task /usr/local/bin/task \
        && rm -rf ./bin \
        && echo "taskfile installed into: /usr/local/bin/task"
    popd
fi

# ###--- install yq4 ---
if [ -f $(which yq || echo _none_ ) ]; then
    echo "os.pack.tool.yq4.is.present"
else
    echo "Install yq from github release"
    wget https://github.com/mikefarah/yq/releases/download/v4.16.1/yq_linux_amd64 \
        &&  chmod +x yq_linux_amd64 \
        &&  $_MAYBE_SUDO_ mv yq_linux_amd64 /usr/local/bin/yq \
        &&  echo "yq4 installed into: /usr/local/bin/yq"
fi

# # ###--- install minio client ---
# if [ -f $(which mc || echo _none_ ) ]; then
#     echo "os.pack.tool.mc.is.present"
# else
#     echo "Install mc from github release"
#     wget https://dl.min.io/client/mc/release/linux-amd64/mc \
#         && chmod +x mc \
#         && $_MAYBE_SUDO_ mv mc /usr/local/bin/mc \
#         && echo "mc installed into: /usr/local/bin/mc"
# fi
