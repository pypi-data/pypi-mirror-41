# mold
> A CLI for managing dotfiles, shell scripts, executables, project scaffolds, and file templates  

## USAGE
`$ mold [--flags] [command] [...options]`

## SYNOPSIS
 mold uses a git repository called a mold root to store and track system configuration files. The mold root is configured using the environment variable $MOLD\_ROOT and unless you have a custom install it will be set to $HOME/.mold

<span classname='newline'/>

 mold splits the files it tracks into the following classifications conf, plug, exec, file, and fold. Each of theses classifications is has different behaviors and gets its own subdirectory in $MOLD\_ROOT for storing content. Below are descriptions of the unique behaviors of each mold classification.

<span classname='newline'/>

[conf](./conf) files are dotfiles that are hard linked to the $HOME directory.

[plug](./plug) files are shell scripts that will be sourced each time a new shell is loaded.

[exec]('./exec) files will be added to a directory on $PATH.  

[leaf](./leaf) files are file asset templates that you can want to future projects.   

[fold](./fold) templates are project directory scaffolds, they are files but for whole directories.  

<span classname='newline'/>

Each of mold's file classifications has a "command" that and "tasks" that allow you to create, read, update, and destroy classification specific content. The mold commands are the name of the classification. The following example demonstrates using the **conf** command with **make** task to create a .bashrc file   
e.g. `$ mold conf make .bashrc`

<span classname='newline'/>

The mold commands [conf](./conf), [plug](./plug), [exec]('./exec), [leaf](./leaf), and [fold](./fold) each the following tasks for managing content.  

* **make** - will create content  
* **load** - will copy or download content into the $MOLD\_ROOT  
* **edit** - will open content using $EDITOR  
* **drop** - will remove content  
* **list** - will list the classification's content  

<span classname='newline'/>

[file](./file_help.md) and [fold](./fold_help.md) also have a **take** task for exorting content into the current directory.

## INSTALL
To install a $MOLD\_ROOT for the first time run  
`$ mold --install` and follow along with the interactive installer.

For custom installations see the mold github repository  
https://github.com/slugbyte/mold

<span classname='newline'/>

#### SETUP FROM AN EXISTING MOLD\_ROOT REPOSITORY
To install an existing MOLD\_ROOT run   
`$ mold --clone [GIT_URI]`

## CONFIGURATION
#### GIT REMOTE
To change your $MOLD\_ROOT's git remote origin run   
<span/>`$ mold --set-remote [GIT_URI]`

<span classname='newline'/>

#### TEXT EDITOR
To change the text editor mold uses for editing file and git commits set the $EDITOR in your shell configuration.  
e.g. `export EDITOR = /usr/local/bin/vim`

## FLAGS
mold flags are boolean values that can turn on and off different behaviors. The order flags are passed into mold does not matter.

* **-v** will create verbose output
* **--color** will force color output even with piped output  
* **-h**, **--help**, and **help** will print help 

## HELP
To find information about a mold comand or task just add **help**, **--help**, or **-h** anywhere and a help dialog will be printed.   
`mold help`, `mold --help`, and `mold -h` are identical.

Because help is treated as a flag the order of the help arguments do not matter.  
`mold help conf make` and `mold conf make --help` are identical.

## MOLD COMMANDS
* [--version](./--version) -- Print mold's version
* [help](./README.md) -- show this help 
* [root](./root) -- Setup and manage the MOLD\_ROOT
* [sync](./sync) -- Manage MOLD\_ROOT's git
* [fold](./fold) -- Manage project scaffolding templates
* [leaf](./leaf) -- Manage file asset templates
* [plug](./plug) -- Manage shell script plugins
* [conf](./conf) -- Manage configuration files
* [exec](./exec) -- Manage executables

<3 Bug reports are much appreciated https://github.com/slugbyte/mold/issues
