#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
画像をセピア調に変換するフィルタ

第一引数 : 入力ファイル名
第ニ引数 : 出力ファイル名（省略可）

セピアとはイカ墨から作られる黒茶色の絵の具のことで、画像をセピア調にするということは、これで描かれたように見せるということである。 
- グレイスケール化することによって輝度情報を取り出す
- 全体を茶色っぽく変換
'''
import sys
import Image

def grayscale(r,g,b):
    '''
    RGB値をグレースケール（白黒）に変換する
    '''
    # NTSC 系加重平均法
    gray = int(r * 0.298912 + g * 0.586611 + b * 0.114478)
    # 単純平均法
    #gray = int((r+g+b)/3)
    return gray

def sepiatone(r,g,b):
    '''
    RGB値をセピア調に変換する
    セピア調に変換する決まり事はないみたいなので、それっぽくなれば OK.
    '''
    gray = grayscale(r,g,b)
    #sr = int(gray * 0.9);sg = int(gray * 0.7);sb = int(gray * 0.4)
    #sr = gray; sg = int(gray * 0.8);sb = int(gray * 0.6)
    sr = int(gray * 0.8 + 2); sg = int(gray * 0.6 + 2);sb = int(gray * 0.4 + 2)
    return sr,sg,sb

def make_image(infile, outfile):
    '''
    画像をセピア調に変換する
    '''
    img = Image.open(infile)
    img = img.convert("RGB")
    x,y = img.size
    for ly in range( y):
        for lx in range( x):
            r,g,b = img.getpixel((lx, ly))
            sr,sg,sb = sepiatone(r,g,b)
            img.putpixel((lx,ly), (sr,sg,sb))
            # ↓やや色あせた感じにしたい場合
            #img.putpixel((lx,ly), ((r+sr)/2,(g+sg)/2,(b+sb)/2))
    img.save(outfile)
    return

def usage():
    sys.stderr.write("Usage: %s infile [outfile] \n" % sys.argv[0])
    return

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    # 引数チェック
    if ((argc == 1 ) or (argc > 3)):
        usage()
        sys.exit(1)
    if (argc > 2):
        outfile = argvs[2]
    else:
        outfile = "output.png"

    infile = argvs[1]

    make_image(infile , outfile)

# EOF

