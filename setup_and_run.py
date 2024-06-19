import os
import requests
import subprocess
import time
from tqdm import tqdm
import platform
import sys
import webbrowser
import argparse

def install_ollama():
    # 设置下载url
    url = "https://ollama.com/download/OllamaSetup.exe"

    # 获取当前脚本所在的目录
    current_script_directory = os.path.dirname(os.path.abspath(__file__))

    # 构建子目录和文件路径
    download_dir = os.path.join(current_script_directory, 'download')
    os.makedirs(download_dir, exist_ok=True)

    def download_file(url, dest):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 KB
        if total_size == 0:
            print("Warning: The server did not provide the file size.")
            with open(dest, 'wb') as file:
                for data in response.iter_content(block_size):
                    file.write(data)
            return True

        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(dest, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size != 0 and progress_bar.n != total_size:
            print("Error: Something went wrong with the download")
            return False
        return True

    # 下载setup.exe
    setup_file = os.path.join(download_dir, "OllamaSetup.exe")

    print(f"Downloading setup.exe from {url}...")
    if not download_file(url, setup_file):
        print("Failed to download setup.exe")
        exit(1)

    print("Downloaded setup.exe successfully.")

    # 启动安装程序
    print("Starting setup.exe...")
    if platform.system() == "Linux":
        subprocess.run(["chmod", "+x", setup_file], check=True, shell=True)
    subprocess.run([setup_file], check=True)

def install_requirements():
    command = ['pip', 'install', '-r', 'requirements.txt']

    # 安装requirements.txt
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("pip install -r success")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("pip install -r error")
        print(e.stderr)

def ollama_pull_llms():
    # Ollama 拉取模型数据 
    def pull_llm(model_name: str):
        command = ['ollama', 'pull', model_name]
        process = subprocess.Popen(command)
        process.wait()

    pull_llm('llama3')
    pull_llm('qwen2')
    pull_llm('phi3')

def run():
    # 启动后端，打开前端网页
    print("正在运行 main.py ...")
    main_process = subprocess.Popen([sys.executable, 'main.py'])

    time.sleep(2)

    # 打开指定的网址
    url = "http://127.0.0.1:5000/"  # 替换为你要打开的网址
    print(f"正在打开网址: {url}")
    webbrowser.open(url)

if __name__ == "__main__":  
    do_install_ollama = False
    do_install_requirements = True
    do_ollama_pull_llms = True
    do_run = True

    if do_install_ollama:
        install_ollama()
    if do_install_requirements:
        install_requirements()
    if do_ollama_pull_llms:
        ollama_pull_llms()
    if do_run:
        run()