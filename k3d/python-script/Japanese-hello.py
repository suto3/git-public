#python
# -*- coding: utf8 -*-
#coding: UTF-8

#
# K-3D Ver.0.8.0.0 用
#
#日本語メッセージ表示のテスト
#

import k3d
import sys
sys.setdefaultencoding('utf-8')

## UnicodeでないASCII文字列 OK
k3d.ui().message("Howdy, World!")

## UnicodeのASCII文字列 NG
k3d.ui().message(u"Howdy, K-3D World!")

## Unicodeの日本語文字列 NG
k3d.ui().message(u"こんにちは、K-3D の世界よ！")


