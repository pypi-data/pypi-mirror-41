if [ -z "$VIRTUAL_ENV" ] ; then
  _venv_root=$(dirname $(readlink -f $BASH_SOURCE))
  if [ -e $_venv_root/activate ] ; then
    . $_venv_root/activate
  fi
  unset _venv_root
fi
eval $(python -m LbEnv.__main__ --sh "$@")
