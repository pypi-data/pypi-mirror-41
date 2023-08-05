mold sync
===

> sync is a mold command for controing $MOLD_ROOT's git

#USAGE
`$ mold sync [task] [options] [flags]`

## SYNOPSIS
mold sync is a wrapper for a few git commands. All of the arguments to non-dangerous mold sync tasks are optional. By default commit with out a message arg will open your text editor. push and pull will default to the current branch. diff will defualt HEAD.
Try using the auto task unless you get an git error :)  

### WARNING  
Tasks this start with **--** are slightly dangerous, they have the potentail
to remove data in a way that can not be undone. Use them with caution.  

### DANGEROUS TASKS  
* [--force-push]() [branch],  will `git push origin [branch | HEAD] --force`  
* [--hard-reset]() [hash], will `git reset --hard [hash | HEAD]`  
* [--new-branch]() [name], will `git checkout -b [name]`   
* [--delete-branch]() [name], will `git branch -D [name]`  
* [--checkout]() [name], will `git checkout [name]`  
* [--merge]() [name], will `git merge [name]`  

## EXAMPLE  
Pull add commit and push with commit message.    
<span/>`$ mold sync auto 'Update bashrc'`  
Pull add commit and push but use $EDITOR for commit message.  
<span/>`$ mold sync auto`  

## TASKS
* [add]() will run `git add -A`
* [log]() will run `git log`
* [status]() will run `git status`
* [pull]() [branch] will run `git pull origin [name | current-branch]`
* [push]() [branch] will run `git push origin [branch | HEAD]`
* [branch]() will run `git branch -av`
* [diff]() [arg] will run `git diff [arg]`
* [commit]() [msg] will run `git commit [-m msg]`
* [auto]() will pull, add, commit, and push
