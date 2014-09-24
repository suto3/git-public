#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
UNIXのcatもどき
'''

import sys


def cat(f):
    '''
    cat 本体
    '''
    fin = open(f, encoding='utf-8')
    lines = fin.readlines()
    for line in lines:
        print(line.strip())
    fin.close()
    return


def main():
    '''
    メイン関数（C言語っぽく）
    1 コマンドライン引数チェック
    2 コマンドライン引数がひとつもなければエラー終了
    3 コマンドライン引数の文字列でcat()を呼ぶ
    '''
    argvs = sys.argv
    argc = len(argvs)

    if (argc == 1):
        usage()
        sys.exit(1)
    # 引数の解析
    # cat(sys.argv[1])
    for arg in sys.argv[1:]:
        # print arg
        cat(arg)


def usage():
    sys.stderr.write("Usage: %s file [file ...]\n" % sys.argv[0])


if __name__ == '__main__':
    main()

#EOF