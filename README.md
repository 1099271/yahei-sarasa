# 介绍

本项目通过自动化脚本，获取最新版本的 [更纱黑体 SC](https://gitee.com/lxgw/sarasa-gothic-sc-regular) 字体，并将其中的字体信息修改为"微软雅黑"和"宋体"，以便在 Windows 系统中作为替换字体使用，从而获得更佳的显示效果。

# 环境准备

1.  **Python**: 项目基于 Python 3 编写。
2.  **FontForge**: 字体处理依赖 FontForge。请从 [FontForge 官网](https://fontforge.org/en-US/) 下载并安装。
    - 在 Windows 环境下，安装后需要知道 `ffpython.exe` 的完整路径（例如 `C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe`），并将其填写到 `auto_all.py` 脚本顶部的 `FFPYTHON_PATH` 变量中。
3.  **Python 依赖**: 在项目根目录下，使用标准 Python 环境执行以下命令来安装所需依赖库：
    ```shell
    pip install -r requirements.txt
    ```

# 如何运行

1.  确保已完成上述环境准备。
2.  如果是在 Windows 上，请确认 `auto_all.py` 中的 `FFPYTHON_PATH` 变量已设置为您机器上正确的路径。
3.  使用 **标准 Python 解释器** (而不是 `ffpython`) 运行主脚本：
    ```shell
    python auto_all.py
    ```
4.  脚本执行完毕后，生成的所有字体文件将会位于 `result` 文件夹内。
