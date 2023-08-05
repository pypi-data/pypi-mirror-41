mold fold
===

> fold is a mold command for managing project scaffold templates

## USAGE
`$ mold fold [--flags] [task] [options]`

## SYNOPSIS  
A mold fold is are directory template. You can use mold fold load or create a directory and later when you want copy of that directory you can take it into your current directory.

## EXAMPLES
To load a fold run   
<span />`$ mold fold load ./react-boiler`  
To export a fold run   
<span />`$ mold fold take react-boiler ./peronal-blog`  

# TASKS
* [list](fold_list_help.md) -- will print a list of your folds
* [make](fold_make_help.md) -- will create a fold using $EDITOR
* [load](fold_load_help.md) -- will copy an a dir into $MOLD_ROOT
* [edit](fold_edit_help.md) -- will edit a fold with $EDITOR
* [drop](fold_drop_help.md) -- will delete a fold
* [take](fold_take_help.md) -- copy a fold into your current directory
