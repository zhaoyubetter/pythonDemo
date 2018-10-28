# 系统操作模块

# 获取操作系统信息
import os
import platform
import re
import pip

import sys

"""
1.获取操作系统信息
2.获取python信息
3.判断指定库是否安装，如：(pip3, BeautifulSoup)
4.安装指定库，获取关联库信息与版本(通过 pip show moduleName 来获取)
5.修改环境变量
"""

# 操作系统信息
systemdict = {'win32': 'Windows',
              'linux': 'Linux',
              'cygwin': 'Windows/Cygwin',
              'darwin': 'Mac OS X',
              'other': 'Other System'}




def main():
    # print('-------- 系统信息 ------------------------------------------------------------')
    # print(platform.node())  # 网络名称
    # print(platform.processor())
    # print(platform.uname())
    # print(get_system())
    # print(get_version())
    # print(get_architecture())
    # print(get_machine())

    # print('-------- python 信息 ------------------------------------------------------------')
    # show_python_all_info()

    print('======  使用信息 ------------------------------------------------------------')
    print(systemdict.get(platform.system().lower()))  # 操作系统信息
    print(platform.python_version())  # python 版本

    print("======  python 获取当前安装的lib ------------------------------------------------------------")
    # print(get_installed_modules())
    # print(get_installed_modules_pip())  # 返回map
    # print("======  python 判断指定模块是否安装 ------------------------------------------------------------")
    # print(is_module_installed('django'))
    # install_module('Pillow')

    print(sys.path)


def install_module(name):
    """
    python 通过pip3命令安装模块
    :param name:
    :return:
    """
    cmd = 'pip3 install %s' % name  # python3通过脚本安装
    r = os.popen(cmd)
    print(r.read())

def uninstall_module(name):
    """
    移出第三方模块,移出，需要输入确认
    :param name:
    :return:
    """
    cmd = 'pip3 uninstall %s' % name  # python3通过脚本安装
    r = os.popen(cmd)
    print(r.read())

def is_module_installed(name):
    """
    判断模块是否安装
    :param name: 模块名称
    :return: True or False
    """
    modules_dict = get_installed_modules_pip()
    return modules_dict.keys().__contains__(name)


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


def get_installed_modules():
    """
    通过 help('modules') 命令获取当前python中安装的所有module信息（过滤掉所有以 '_'开头的）
    :return: list module
    """

    #  python3 -c 'import pip' # 判断是否安装指定模块
    result = []

    temp = sys.stdout  # 记录当前输出指向，默认是 console
    with open("./outputlog.txt", "w") as f:
        sys.stdout = f  # 输出指向txt文件
        help('modules')  # 将内容输出到文件
        sys.stdout = temp  # 输出重定向回 console

    # 解析文件，从文件中，解析出所有安装的modules
    with open("./outputlog.txt", "r") as f:
        # 从第4行开始读，到空行结束
        for num, line in enumerate(f):
            if len(line.strip()) > 0 and num > 2:
                modules = re.split(r'\s+', line)
                if modules and len(modules) > 1:
                    result.extend(list(filter(lambda m: len(m) > 0 and not m.startswith('_'), modules)))
            elif num > 2:  # 过滤掉空格后面的
                break

    return result


def show_python_all_info():
    '''打印python的全部信息'''
    print('The Python build number and date as strings : [{}]'.format(get_python_build()))
    print('Returns a string identifying the compiler used for compiling Python : [{}]'.format(get_python_compiler()))
    print('Returns a string identifying the Python implementation SCM branch : [{}]'.format(get_python_branch()))
    print('Returns a string identifying the Python implementation : [{}]'.format(get_python_implementation()))
    print('The version of Python ： [{}]'.format(get_python_version()))
    print('Python implementation SCM revision : [{}]'.format(get_python_revision()))
    print('Python version as tuple : [{}]'.format(get_python_version_tuple()))


def get_platform():
    """获取操作系统名称及版本号"""
    # mac Darwin-17.7.0-x86_64-i386-64bit
    return platform.platform()


def get_version():
    """获取操作系统版本号"""
    return platform.version()


def get_architecture():
    """获取操作系统的位数"""
    # ('64bit', '')
    return platform.architecture()


def get_machine():
    """计算机类型"""
    # x86_64
    return platform.machine()


def get_processor():
    """计算机处理器信息"""
    return platform.processor()


def get_system():
    """获取操作系统类型"""
    return platform.system()


# ------------------------------- python 信息 --------------------------------------------
def get_python_build():
    ''' the Python build number and date as strings'''
    return platform.python_build()


def get_python_compiler():
    '''Returns a string identifying the compiler used for compiling Python'''
    return platform.python_compiler()


def get_python_branch():
    '''Returns a string identifying the Python implementation SCM branch'''
    return platform.python_branch()


def get_python_implementation():
    '''Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.'''
    return platform.python_implementation()


def get_python_version():
    '''Returns the Python version as string 'major.minor.patchlevel'
    '''
    return platform.python_version()


def get_python_revision():
    '''Returns a string identifying the Python implementation SCM revision.'''
    return platform.python_revision()


def get_python_version_tuple():
    '''Returns the Python version as tuple (major, minor, patchlevel) of strings'''
    return platform.python_version_tuple()


if __name__ == '__main__':
    main()
