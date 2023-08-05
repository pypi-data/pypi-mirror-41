# SETUP/LOAD MOLD's BASH RELATED CONFIGURATION
# ADD EXEC TO $PATH
export PATH=$MOLD_ROOT/exec:$PATH

# LOAD MOLD PLUGs
for plug in $MOLD_ROOT/plug/*;do
  source $plug
done

# LOG IF MOLD_DEBUG IS ON 
[[ -n $MOLD_DEBUG ]] && echo "MOLD_LOADED"

# TODO add zsh completion
# Enable bash completion
_mold(){
  MOLD_COMPLETE=$(mold complete $COMP_LINE) 
  if [[ $MOLD_COMPLETE == '__MAGIC_MOLD__' ]]; then 
    for canidate in $(compgen -f $2); do 
      if [[ "$canidate" == "$2"* ]];then
        COMPREPLY+=("$canidate")
      fi 
    done
  else 
    for canidate in $MOLD_COMPLETE; do 
      if [[ "$canidate" == "$2"* ]];then
        COMPREPLY+=("$canidate")
      fi 
    done
  fi
}
complete -F _mold mold
