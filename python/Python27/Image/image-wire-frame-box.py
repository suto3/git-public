#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
ワイヤーフレーム画像を作成する
'''

import Image
import ImageDraw
import ImageFont
import sys


def make_image(screen, prefix, extension, pen_color, bg_color):
    """
    画像ファイルを作成
    """

    # フラットフォーム毎にフォントのパスは違うので、その点を考慮（実は、やっつけ）
    if sys.platform == "darwin":
        # OSX  の場合
        # 日本語フォントはうまく行かなかった
        #FONTPATH = '/Library/Fonts/Osaka.ttf'
        FONTPATH = '/Library/Fonts/Verdana.ttf'
    elif sys.platform == "linux2":
        # Linux の場合
        FONTPATH = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
    else:
        # それ以外はWindowsと判定する（やっつけ）
        # FONTPATH = 'hgrme.ttc'
        FONTPATH = 'C:\WINDOWS\Fonts\MSGOTHIC.ttc'

    # フォントを指定
    font = ImageFont.truetype(FONTPATH, 24, encoding='utf-8')

    img = Image.new('RGB', screen, bg_color)
    x, y = img.size
    u = x - 1
    v = y - 1
    draw = ImageDraw.Draw(img)

    draw.line((0, 0, u, 0), pen_color)
    draw.line((0, 0, u, v), pen_color)
    draw.line((0, 0, 0, v), pen_color)
    draw.line((u, 0, 0, v), pen_color)
    draw.line((u, 0, u, v), pen_color)
    draw.line((0, v, u, v), pen_color)

    #　画像に文字を入れる（やっつけ）
    if x > 63 and y > 24:
        draw.text((2, (y - 24) / 2), str(x) + "x" + str(y),
            font=font, fill=pen_color)

    savefile = prefix + str(x) + "x" + str(y) + extension
    img.save(savefile)

if __name__ == '__main__':
    # 画像のサイズ
    screens = (
        (16, 16),      # favicon
        (32, 32),      # favicon
        (24, 24),      # windows icon
        (48, 48),      # windows icon / avatar
        (96, 96),      # windows icon / avatar
        (64, 64),      # mac icon / avatar
        (128, 128),    # mac icon / avatar
        (100, 100),    # icon / avatar
        (150, 150),    # icon / avatar
        (256, 256),    # icon / avatar ----
        (320, 240),    # QVGA
        (240, 320),    # QVGA
        (640, 480),    # VGA
        (480, 640),    # VGA（縦）
        (800, 600),    # SVGA
        (600, 800),    # SVGA（縦）
        (1024, 768),   # XGA
        (768, 1024),   # XGA（縦）
        (1280, 960),   # Quad-VGA
        (960, 1280),   # Quad-VGA（縦）
        (1600, 1200),  # UXGA
        (1200, 1600),  # UXGA（縦）
        (1280, 720),   # HDTV 720p
        (720, 1280),   # HDTV 720p（縦）
        (1920, 1080),  # HDTV 1080p
        (1080, 1920),  # HDTV 1080p（縦）----
        (88, 31),      # IMU Micro Bar マイクロバー
        (120, 60),     # IMU Button 2 ボタン2
        (160, 600),    # IMU Wide Skyscraper ワイド スカイスクレイパー
        (300, 600),    # IMU Half Page Ad ハーフ ページ
        (180, 150),    # IMU Rectangle レクタングル（小）
        (300, 250),    # IMU Medium Rectangle レクタングル（中）
        (728, 90),     # IMU Leaderboard ビッグバナー
        (120, 90),     # IMU （削除）Button 1 ボタン1
        (120, 240),    # IMU （削除）Vertical Banner 縦長バナー
        (120, 600),    # IMU （削除）Skyscraper スカイスクレイパー
        (125, 125),    # IMU （削除）Square Button スクエア・ボタン、ボタン
        (234, 60),     # IMU （削除）Half Banner ハーフバナー
        (240, 400),    # IMU （削除）Vertical Rectangle 縦レクタングル
        (250, 250),    # IMU （削除）Square Pop-Up スクエア
        (300, 100),    # IMU （削除）3:1 Rectangle 3:1レクタングル
        (336, 280),    # IMU （削除）Large Rectangle ラージ・レクタングル、レクタングル（大）
        (468, 60),     # IMU （削除）Full Banner バナー、フルバナー
        (720, 300),    # IMU （削除）Pop-Under ポップ・アンダー
        (200, 200),    # Google　スクエア（小）
        (970, 90),     # Google　ラージ ビッグバナー、ビッグバナー（大）
        (320, 50),     # Google　モバイル ビッグバナー
        (320, 100),    # Google　モバイル バナー（大）
        (240, 400),    # Google　「レクタングル（縦長）」ロシア
        (980, 120),    # Google　「パノラマ」スウェーデンとフィンランド
        (250, 360),    # Google　「トリプル ワイドスクリーン」スウェーデン
        (930, 180),    # Google　「トップバナー」デンマーク
        (580, 400),    # Google　「ネットボード」ノルウェー
        (750, 100),    # Google　「ビルボード」ポーランド
        (750, 200),    # Google　「ダブル ビルボード」ポーランド
        (750, 300),    # Google　「トリプル ビルボード」ポーランド
        (170, 40),     # banner 詳細不明
        (180, 70),     # banner 詳細不明
        (200, 40),     # banner 日本のCG系に多いバナーサイズだって
        (400, 40)      # banner 日本に多いバナーサイズだって
        )

    # 接頭辞（プレフィクス）を指定
    prefix = "wf-"

    # ファイルの拡張子を指定
    #extension = ".png"
    extension = ".jpg"

    # 描画色（RGB）を指定
    pen_color = (0x00, 0x00, 0xdd)

    # 画像の背景色（RGB）を指定
    bg_color = (0xdd, 0xdd, 0xdd)

    for screen in screens:
        print "size: %d,%d" % (screen[0], screen[1])
        make_image(screen, prefix, extension, pen_color, bg_color)
#EOF
