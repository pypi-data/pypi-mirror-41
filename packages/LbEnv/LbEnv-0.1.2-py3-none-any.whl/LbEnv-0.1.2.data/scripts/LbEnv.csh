if ( ! $?VIRTUAL_ENV ) then
  set _me=`readlink -f !:1`
  set _venv_root=`dirname $_me`
  if ( -e $_venv_root/activate.csh ) then
    source $_venv_root/activate.csh
  endif
  unset _me
  unset _venv_root
endif
eval `python -m LbEnv.__main__ --csh !:2*`
