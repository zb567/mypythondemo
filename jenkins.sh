#!/usr/bin/env bash

# 进入项目目录
cd /root/myjenkins/mypython

# 启动容器
docker compose up -d

## 如果容器已经在运行，可以选择是否重启容器
#docker compose restart mypythonservice

echo '----start container using docker compose----'
