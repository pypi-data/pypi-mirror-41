mold conf  
====

> conf is a mold command for managing dotfiles  

## USAGE  
`$ mold conf [task] [options] [--flags]`  

## SYNOPSIS  
A mold conf is a dotfile. When you create or load a conf it will be hard linked to your home directory. Hard links are filesystem references to the same file. Editing the file in your home directory will also edit the file in your config repository, and vice versa.  

### NOTE  
If you run the drop task it will only delete the file from
your config repository. It will NOT remove it from your
home directory.  

## EXAMPLES  
To load a your ~/.bashrc into $MOLD_ROOT/conf
<span/>`$ mold conf load ~/.bashrc`    

To edit the .bashrc you have allready loaded  
<span/>`$ mold conf load .bashrc`  

To download a conf into MOLD_ROOT/conf and rename it .tmux.conf  
<span/>`$ mold load load http://www.iexample.com/tmux-config .tmux.conf`  

## TASK REFERENCE
* [list](conf_list_help.md) -- will print a list all of your conf files.  
* [make](conf_make_help.md) -- will create a conf using $EDITOR
* [load](conf_load_help.md) -- will copy a conf into $MOLD_ROOT
* [edit](conf_edit_help.md) -- will open a conf using $EDITOR  
* [drop](conf_drop_help.md) -- will delete a conf
