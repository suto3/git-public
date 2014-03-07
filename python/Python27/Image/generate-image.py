#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
画像ファイルを作成する
'''

import Image

def make_image(screen, bgcolor, filename):
    img = Image.new('RGB', screen,bgcolor)
    img.save(filename)

if __name__ == '__main__':
    # 画像のサイズ
    screen = (1024,768)

    # 画像の背景色（RGB）
    bgcolor=(0xdd,0xdd,0xdd)

    # 保存するファイル名（ファイル形式は、拡張子から自動的に判別する）
    filename = "pil-01.png"
    make_image(screen, bgcolor, filename)

#EOF
