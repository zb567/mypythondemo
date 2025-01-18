@echo off
REM 设置提交信息
set /p commit_message="Enter commit message: "

REM 执行 git 操作
git add .
git commit -m "%commit_message%"
git push