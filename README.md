# mota_python_framework

## 需求和安装
Python 3.9.0或更高级的版本，如果使用的不是3.9.0，那么就必须根据[Game-Launcher](https://github.com/JasonLeon01/Game-Launcher)里面的`README.md`指示构建自己的exe。

如果要将项目整体打包为新的exe，则可以安装`pygame`和`psutil`至系统：

```
pip install pygame==2.5.2
pip install psutil==6.0.0
```

同时需删除自带引用`pygame`处前方的

```
sys.path.append(os.path.join(os.getcwd(), 'custom_lib'))
```

否则要安装在项目目录内：

```
pip install pygame==2.5.2 --target=custom_lib
pip install psutil==6.0.0 --target=custom_lib
```

## 注意
调试时可运行`launcher.py`

```
python launcher.py
```

和exe启动器为相同的代码，可以设置断点等。

工程内置了python39的解释器，可以在无python环境下运行exe文件，但是如果想要调试断点等，还是建议安装python，然后运行`launcher.py`

可以通过`nuitka`、`pyinstaller`等方式将工程打包。

通过`mota.exe`和`launcher.py`启动时，相对目录均为相对项目根目录。