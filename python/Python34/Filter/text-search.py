#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
テキスト検索
'''

import sys


def search(f, word):
    '''
    テキスト検索本体
    '''
    fin = open(f, encoding='utf-8')
    lines = fin.readlines()
    for line in lines:
        if word in line:
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

    if (argc != 3):
        usage()
        sys.exit(1)
    # 引数の解析
    search(sys.argv[1], sys.argv[2])


def usage():
    sys.stderr.write("Usage: %s file search_keyword \n" % sys.argv[0])


if __name__ == '__main__':
    main()

#EOF