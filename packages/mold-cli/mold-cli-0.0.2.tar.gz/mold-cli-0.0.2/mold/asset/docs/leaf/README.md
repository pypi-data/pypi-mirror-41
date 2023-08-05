mold leaf
====

> leaf is a mold command for managing leaf templates

## USAGE
`$ mold leaf task [options] [--flags]`

## SYNOPSIS  
mold leafs are file templates. 

## EXAMPLES
Load and rename two licenses as leafs.  
<span />`$ mold leaf load ./LICENSE.md mit.md`    
<span />`$ mold leaf load ./LICENSE.md cc-share-alike.md`    
copy a leaf into the current directory.   
<span />`$ mold leaf take mit.md ./LICENSE.md`   

## TASKS
* [list](leaf_list_help.md) -- will print a list of your leafs
* [make](leaf_make_help.md) -- will create a leaf using $EDITOR
* [load](leaf_load_help.md) -- will copy an a leaf into $MOLD\_ROOT
* [edit](leaf_edit_help.md) -- will edit a leaf with $EDITOR
* [drop](leaf_drop_help.md) -- will delete a leaf
* [take](leaf_take_help.md) -- copy a leaf into your current directory
