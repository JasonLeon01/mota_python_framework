#!/bin/bash
# 这个脚本用于运行同一目录下的 launcher.py 文件

# 检查 Python 是否已安装
if ! command -v python3 &> /dev/null
then
    echo "Python 3 未安装，请先安装 Python 3。"
    exit 1
fi

# 运行同一目录下的 launcher.py
python3 ./launcher.py