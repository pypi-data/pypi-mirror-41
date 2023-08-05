mold plug
====

> plug is a mold command for managing shell script plugins

## USAGE
`$ mold plug [task] [file]`

## SYNOPSIS  
mold plugs are shell scripts that will be loaded each time
you create a new shell. Its great place to add ENV var
plugig, aliases, functions, or startup scripts.

### WARNING  
Anything you load as a plug will be sourced by your shell
on load, so be carful to only load files your shell can source.

## EXAMPLES   
create some shell plugins
<span/>`$ mold plug make my-aliases.sh`
<span/>`$ mold plug make git-shortcuts.sh`         
<span/>`$ mold plug load ./git-aware-prompt.sh`

## TASK REFERENCE
* [list](plug_list_help.md) -- will print a list all of your plug files.  
* [make](plug_make_help.md) -- will create a plug using $EDITOR
* [load](plug_load_help.md) -- will copy a plug into $MOLD_ROOT
* [edit](plug_edit_help.md) -- will open a plug using $EDITOR  
* [drop](plug_drop_help.md) -- will delete a plug
