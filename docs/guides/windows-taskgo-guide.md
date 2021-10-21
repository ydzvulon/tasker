# Task and Windows


On Windows we assume WSL with linux and bash 
so it's the same as linux in docker

> But it's not really on "windows"

## Windows Development Base

On Windows powershell is more in use then bash or cmd.
However, we would like to keep most of `bash` code and
state of mind.

There are several builds of gnu tools for windows,
the most famous is `cygwin` and `migwin`.

We will need a Git For windows

> [Download From git-scm.com Site](https://git-scm.com/download/win)

Git Tools come with `bash`, `ls`, `tee` and of course `git` itself.

Unfortunately it's not enough or comfortable work,
we still miss `xargs` and good-looking terminal.

## Windows Development Cmder

For comfortable shell experience we need

- autocomplete
- search in history
- aliases
- tty

Fortunately [Samuel Vasko](https://github.com/samvasko) created
a composition of con-emu, migwin and cmd dark magic.

This bundle called [Cmder](https://cmder.net/)
and it provides very good shell experience.

> Sample view of console

```bat
C:\Users\user\_wd\_public_\tasker (yairda.parse.sceleton -> origin) 
(base) λ ls
_infra/    _out.log  LICENSE    tasker/       tasks/  tickets/
_layout_/  docs/     README.md  Taskfile.yml  tests/  version/

C:\Users\user\_wd\_public_\tasker (yairda.parse.sceleton -> origin) 
(base) λ ls | xargs -n1 echo
_infra/
_layout_/
_out.log

C:\Users\user\_wd\_public_\tasker (yairda.parse.sceleton -> origin) 
(base) λ 
```

### Cmder's activation in any Cmd Window

There are ways to deeply integrate cmder into VsCode or Pycharm.
Let's start from direct change of cmd to nice shell.

Consider your username is `user` and you upacked cmder to 
`C:\\Users\\user\\Apps\\cmder` folder.

> For cmder activation run 
> `cmd /k C:\\Users\\user\\Apps\\cmder\\vendor\\bin\\vscode_init.cmd`


### Cmder's integration with VsCode

Can I use Cmder's shell with the terminal on Windows?

> Yes, to use the Cmder shell in VS Code, you need to add the following settings to your settings.json file:


```json
{
  "terminal.integrated.profiles.windows": {
    "cmder": {
      "path": "C:\\WINDOWS\\System32\\cmd.exe",
      "args": ["/K", "C:\\cmder\\vendor\\bin\\vscode_init.cmd"]
    }
  },
  "terminal.integrated.defaultProfile.windows": "cmder"
}
```

> More on integration with vscode

- [cmder wiki on vscode](https://github.com/cmderdev/cmder/wiki/Seamless-VS-Code-Integration)
- [cmder vscode 2021](https://dev.to/andrewriveradev/how-to-setup-cmder-in-vscode-in-2021-3nkc)
- [use-cmders-shell-with-the-terminal-on-windows](https://code.visualstudio.com/docs/editor/integrated-terminal#_can-i-use-cmders-shell-with-the-terminal-on-windows)

### Cmder's integration with PyCharm or Idea

> !!! TODO: Please add simple instruction !!!

> More on integration with pycharm

- https://www.jetbrains.com/help/pycharm/terminal-emulator.html#configure-the-terminal-emulator
- https://intellij-support.jetbrains.com/hc/en-us/community/posts/206334729-use-cmder-or-conemu-in-Terminal-without-opening-new-window
- https://stackoverflow.com/questions/66373669/cmder-terminal-integration-into-intellij-webstorm-goland-with-aliases
- https://stackoverflow.com/questions/49615928/how-get-cmder-running-behind-python-debugger-in-intellij-or-pycharm

## Tasker and Cmder

Taskgo has number of tricks to make things easy between posix and windows.

Please see https://taskfile.dev/#/usage?id=gos-template-engine

- `OS`: **os name**
  - `echo '{{if eq OS "windows"}}windows-command{{else}}unix-command{{end}}'`
- `fromSlash`: Opposite of toSlash. Does nothing on Unix, but on **Windows** converts a string from / path format to \\.
  - `echo '{{fromSlash "path/to/file"}}'`
- `exeExt`: Returns the right executable extension for the current OS (".exe" for Windows, "" for others).

### Tasker pitfalls

> color output

when working in cmder taskgo will output colors to console.
to disable it use `set NO_COLOR=1`

## See Also

- https://conemu.github.io/en/wsl.html#start
- https://dev.to/stack-labs/introduction-to-taskfile-a-makefile-alternative-h92
