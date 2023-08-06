#!/bin/bash -xe
if [ -z "$RUN_LINTS" ]; then
  pip install -r requirements-dev.txt
  psql -c 'create database pacifica_metadata;' -U postgres
  mysql -e 'CREATE DATABASE pacifica_uniqueid;'
  mysql -e 'CREATE DATABASE pacifica_ingest;'
  export POSTGRES_ENV_POSTGRES_USER=postgres
  export POSTGRES_ENV_POSTGRES_PASSWORD=
  export MYSQL_ENV_MYSQL_USER=travis
  export MYSQL_ENV_MYSQL_PASSWORD=
  pushd travis/archivei
  ArchiveInterfaceServer.py &
  echo $! > archiveinterface.pid
  popd
  pushd travis/uniqueid
  UniqueIDServer.py &
  echo $! > archiveinterface.pid
  popd
  pushd travis/metadata
  MetadataServer.py &
  popd
  MAX_TRIES=60
  HTTP_CODE=$(curl -sL -w "%{http_code}\\n" localhost:8121/keys -o /dev/null || true)
  while [[ $HTTP_CODE != 200 && $MAX_TRIES > 0 ]] ; do
    sleep 1
    HTTP_CODE=$(curl -sL -w "%{http_code}\\n" localhost:8121/keys -o /dev/null || true)
    MAX_TRIES=$(( MAX_TRIES - 1 ))
  done
  TOP_DIR=$PWD
  MD_TEMP=$(mktemp -d)
  git clone https://github.com/pacifica/pacifica-metadata.git ${MD_TEMP}
  pushd ${MD_TEMP}
  python test_files/loadit.py
  popd
  pushd travis/policy
  PolicyServer.py &
  echo $! > PolicyServer.pid
  popd
fi
case "$TRAVIS_PYTHON_VERSION" in
  pypy) export PYPY_VERSION="pypy-2.6.1" ;;
  pypy3) export PYPY_VERSION="pypy3-2.4.0" ;;
esac
if ! [ -z "$PYPY_VERSION" ] ; then
  export PYENV_ROOT="$HOME/.pyenv"
  if [ -f "$PYENV_ROOT/bin/pyenv" ]; then
    pushd "$PYENV_ROOT" && git pull && popd
  else
    rm -rf "$PYENV_ROOT" && git clone --depth 1 https://github.com/yyuu/pyenv.git "$PYENV_ROOT"
  fi
  "$PYENV_ROOT/bin/pyenv" install "$PYPY_VERSION"
  virtualenv --python="$PYENV_ROOT/versions/$PYPY_VERSION/bin/python" "$HOME/virtualenvs/$PYPY_VERSION"
  source "$HOME/virtualenvs/$PYPY_VERSION/bin/activate"
fi
if [ "$RUN_LINTS" = "true" ]; then
  pip install pre-commit
else
  pip install nose pytest
fi
pushd test_data
for x in good bad-proposal bad-mimetype bad-hashsum ; do
  cp metadata-files/${x}-md.json metadata.txt
  tar -cf ${x}.tar metadata.txt data
done
cp metadata-files/bad-json-md.notjson metadata.txt
tar -cf bad-json.tar metadata.txt data
popd
