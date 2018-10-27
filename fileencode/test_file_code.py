import codecs
import os
import chardet


def main():
    '''批量转换文件文本便秘'''
    dir = './txt'
    files = os.listdir(dir)
    for str in files:
        filename = os.path.join(dir, str)

        data = readfile(filename)
        # 获取文件现有编码
        old_encode = chardet.detect(data).get('encoding')
        # 转utf-8编码
        new_encode = 'utf-8'
        writefile(filename, data.decode(old_encode), new_encode)

        # writefile(filename, data, new_encode)


def readfile(filepath):
    print(filepath)
    with codecs.open(filepath, 'rb') as f:
        return f.read()


def writefile(filePath, u, encoding):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)


def read():
    dir = './txt'
    files = os.listdir(dir)
    for str in files:
        filename = os.path.join(dir, str)
        with open(filename, 'r') as f:
            for line in f.readlines():
                print(line)


if __name__ == '__main__':
    # main()
    read()