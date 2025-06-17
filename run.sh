#!/bin/bash
set -e

BLUE='\033[1;34m'
NC='\033[0m'

cd occlum_instance
echo -e "${BLUE}occlum run ./src/hello_grpc/service.py${NC}"
HF_DATASETS_CACHE=/root/cache \
       occlum run /bin/python3 ./src/hello_grpc/service.py