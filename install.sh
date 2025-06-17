#!/bin/bash
set -e
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" >/dev/null 2>&1 && pwd )"

# Install python and dependencies to specified position
[ -f Miniconda3-latest-Linux-x86_64.sh ] || wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
[ -d miniconda ] || bash ./Miniconda3-latest-Linux-x86_64.sh -b -p $script_dir/miniconda
$script_dir/miniconda/bin/conda create \
    --prefix $script_dir/python-occlum -y \
    python=3.9.11

# Install BigDL LLM
#$script_dir/python-occlum/bin/pip install torch==2.2.1 --index-url https://download.pytorch.org/whl/cpu
# $script_dir/python-occlum/bin/pip install --pre --upgrade ipex-llm[all] ipex-llm[serving]
# $script_dir/python-occlum/bin/pip install intel-extension-for-pytorch
# $script_dir/python-occlum/bin/pip install transformers_stream_generator einops tiktoken
#$script_dir/python-occlum/bin/pip install tiktoken
#$script_dir/python-occlum/bin/pip install requests
#$script_dir/python-occlum/bin/pip install numpy~=1.24.0
#$script_dir/python-occlum/bin/pip install blobfile

$script_dir/python-occlum/bin/pip install -r requirements.txt

# 读取./config/deps.json中的依赖项， 利用$script_dir/python-occlum/bin/pip install xxxx安装
