# Develop in VsCode DevContainer

## Git Credentials

> how to manage git credentials in container both ssh and https:

- https://code.visualstudio.com/docs/remote/containers#_sharing-git-credentials-with-your-container

### Preview

If you do not have your user name or email address set up locally, you may be prompted to do so. You can do this on your local machine by running the following commands:

```
git config --global user.name "Your Name"
git config --global user.email "your.email@address"
```

#### Using Https

If you use HTTPS to clone your repositories and have a 
[credential helper configured](https://help.github.com/articles/caching-your-github-password-in-git)
in your local OS, no further setup is required. 
Credentials you've entered locally will be reused in the container and vice versa.

#### Using SSH

There are some cases when you may be cloning your repository using SSH keys instead of a credential helper. 
To enable this scenario, the extension will automatically forward your local SSH agent if one is running.

You can add your local SSH keys to the agent if it is running by using the ssh-add command. For example, run this from a terminal or PowerShell:

`ssh-add $HOME/.ssh/github_rsa`

```powershell
# Make sure you're running as an Administrator
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
Get-Service ssh-agent

```

```shell
# wsl too
sudo apt install socat
eval "$(ssh-agent -s)"
```

if [ -z "$SSH_AUTH_SOCK" ]; then
   # Check for a currently running instance of the agent
   RUNNING_AGENT="`ps -ax | grep 'ssh-agent -s' | grep -v grep | wc -l | tr -d '[:space:]'`"
   if [ "$RUNNING_AGENT" = "0" ]; then
        # Launch a new instance of the agent
        ssh-agent -s &> $HOME/.ssh/ssh-agent
   fi
   eval `cat $HOME/.ssh/ssh-agent`
fi

