#!/bin/bash
set -e

BLUE='\033[1;34m'
NC='\033[0m'

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" >/dev/null 2>&1 && pwd )"
python_dir="$script_dir/occlum_instance/image/opt/python-occlum"

function build_instance()
{
  rm -rf occlum_instance && occlum new occlum_instance
  pushd occlum_instance
  rm -rf image
  copy_bom -f ../config/file-cp.yaml --root image --include-dir /opt/occlum/etc/template

  if [ ! -d $python_dir ];then
    echo "Error: cannot stat '$python_dir' directory"
    exit 1
  fi

  # 使用预定义的 Occlum_custom.json 作为配置文件
  cp "$script_dir/config/Occlum.json" Occlum.json  # 注意路径需正确

  occlum build --sgx-mode SIM
  popd
}

build_instance
