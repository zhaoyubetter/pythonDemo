# 系统操作模块

# 获取操作系统信息
import os
import platform
import re

"""
linux下安装：sudo apt-get install python-imaging
"""

# 操作系统信息
_SYSTEM_DICT = {'win32': 'Windows',
                'linux': 'Linux',
                'cygwin': 'Windows/Cygwin',
                'darwin': 'Mac OS X',
                'other': 'Other System'}

# 已安装modules dict {name, version}
_EXISTED_MODULES = None


def main():
    print_system_info()
    need_installed_list = ['python-dateutil', 'pyecharts_snapshot', 'pyecharts', 'django_tables2', 'pdfkit', 'xlrd']
    for m in need_installed_list:
        print('install %s ...' % m)
        if is_module_installed(m):
            print('%s has already installed.' % m)
        else:
            text = install_module(m)
            print(text)



def print_system_info():
    print("操作系统：", _SYSTEM_DICT.get(platform.system().lower()))  # 操作系统信息
    print("Python版本：", platform.python_version())  # python 版本


def install_module(name):
    """
    python 通过pip3命令安装模块
    :param name:
    :return: 安装信息
    """
    cmd = 'pip3 install %s' % name  # python3通过脚本安装
    r = os.popen(cmd)
    return r.read()


def is_module_installed(name):
    """
    判断模块是否安装
    :param name: 模块名称
    :return: True or False
    """
    global _EXISTED_MODULES
    if _EXISTED_MODULES is None:
        _EXISTED_MODULES = get_installed_modules_pip()

    return _EXISTED_MODULES.keys().__contains__(name)


def get_installed_modules_pip():
    """
    通过 pip3 list 命令获取当前python中安装的所有module信息
    :return: map name, version
    """
    result = {}
    cmd = 'pip3 list'  # python
    r = os.popen(cmd)
    text = r.read()
    r.close()
    lines = re.split(r'\n', text)
    for num, l in enumerate(lines):
        if num > 1:
            splits = re.split(r'\s+', l)
            if len(splits) > 1:
                result[splits[0].lower()] = splits[1]
    return result


if __name__ == '__main__':
    main()
