#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
フィルタ処理
'''
import sys
import Image
import ImageFilter
import ImageOps


def filter(infile, outfile):
    #img = Image.open(infile)
    img = ImageOps.grayscale(Image.open(infile))

    # differrentiate
    #flist = [-1, 0, 1,
    #         -2, 0, 2,
    #         -1, 0, 1]

    # 8傍近接ラプラシアン
    #flist = [1,  1, 1,
    #         1, -8, 1,
    #         1,  1, 1]

    # 4傍近接ラプラシアン
    #flist = [0,  1, 0,
    #         1, -4, 1,
    #         0,  1, 0]
    flist = [-0.1, -0.2, -0.1,
             -0.2, 2.2, -0.2,
             -0.1, -0.2, -0.1]

    #flt = ImageFilter.Kernel((3,3), flist, scale=1, offset=128)
    flt = ImageFilter.Kernel((3, 3), flist, scale=1)
    imgx = img.filter(flt)

    #imgx = img.filter(ImageFilter.EMBOSS)
    #imgx.show()
    imgx.save(outfile)

    return


def usage():
    sys.stderr.write("Usage: %s infile [outfile] \n" % sys.argv[0])
    return

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    # 引数チェック
    if ((argc == 1) or (argc > 3)):
        usage()
        sys.exit(1)
    if (argc > 2):
        outfile = argvs[2]
    else:
        outfile = "output.png"

    infile = argvs[1]

    filter(infile, outfile)

# EOF
