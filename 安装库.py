import subprocess
import sys

# 检查pip是否已安装
if not subprocess.run([sys.executable, '-m', 'pip', '--version'], stdout=subprocess.PIPE, text=True).returncode == 0:
    print("pip is not installed. Installing pip...")
    subprocess.run([sys.executable, '-m', 'ensurepip'], check=True)

# 安装requirements.txt中的依赖项
subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)