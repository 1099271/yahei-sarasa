import auto_configs as conf
import fetch_original as fetch
import copy_result as copy
import subprocess
import sys

# 您提供的 ffpython.exe 的路径
FFPYTHON_PATH = r"C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe"

def run_with_ffpython(script_name, task):
    """使用 ffpython 执行指定的脚本和任务"""
    try:
        # 使用 subprocess.run 来执行命令，并捕获输出
        # check=True 会在命令返回非零退出码时抛出 CalledProcessError
        result = subprocess.run(
            [FFPYTHON_PATH, script_name, task],
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8' # 指定编码
        )
        print(result.stdout) # 打印标准输出
        if result.stderr:
            print(result.stderr, file=sys.stderr) # 打印标准错误
    except FileNotFoundError:
        print(f"错误: 无法找到 ffpython.exe，请检查路径: {FFPYTHON_PATH}", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"执行 {script_name} 时出错:", file=sys.stderr)
        print(e.stdout)
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    fetch.clear_dir(conf.TEMP_DIR)
    fetch.clear_dir(conf.RESULT_DIR)

    url = fetch.get_latest()
    print('========> Latest url: ' + url)
    path = fetch.download(url)
    print('\n========> Download finished')
    fetch.unzip(path)
    print('========> Unzip finished')

    run_with_ffpython('run_font_generation.py', 'regular')
    print('========> Regular generated')
    run_with_ffpython('run_font_generation.py', 'bold')
    print('========> Bold generated')
    run_with_ffpython('run_font_generation.py', 'light')
    print('========> Light generated')

    run_with_ffpython('run_simsun_generation.py', 'ttc')
    print('========> Simsun ttc generated')
    run_with_ffpython('run_simsun_generation.py', 'ext')
    print('========> Simsun ext generated')

    copy.copy_result()
    print('========> Copy Finished')
