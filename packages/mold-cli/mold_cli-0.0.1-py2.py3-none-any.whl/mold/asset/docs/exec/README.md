mold exec
====

> exec is a mold command for managing executables

## USAGE
`$ mold exec [--flags] [task] [options]`

## SYNOPSIS
mold execs are executable files that will be stored in
a directory on your $PATH.

<span />

#### NOTE
If your file does not have executable permissions
you will not be able to run it. so remember to chmod 775 it
if you need to.

## EXAMPLES
To create an exec   
<span />`$ mold exec make troll.py`  
To load an exec   
<span />`$ mold load ./a.out fetch-metadata`  

## TASKS
* [list](exec_list_help.md) -- will print a list all of your exec files.  
* [make](exec_list_help.md) -- will create a exec using $EDITOR
* [load](exec_list_help.md) -- will copy a exec into $MOLD_ROOT
* [edit](exec_list_help.md) -- will open a exec using $EDITOR  
* [drop](exec_list_help.md) -- will delete a exec
