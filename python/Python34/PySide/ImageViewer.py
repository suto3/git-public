#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PySide import QtCore, QtGui


class ImageViewer(QtGui.QWidget):
    def __init__(self):
        super(ImageViewer, self).__init__()
        self.initUI()

    def initUI(self):
        '''
        ユーザーインターフェースの初期化
        '''
        # 枠なしWindow
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #半透明
        self.setWindowOpacity(0.8)

        self.setWindowTitle('ImageViewer')

        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

        self.imageLabel.setScaledContents(False)

        self.filenameLabel = QtGui.QLabel()

        self.imageLabel.setToolTip("コンテキストメニューで操作してください。")

        # Debug用
        #self.button = QtGui.QPushButton('open')
        #self.button.clicked.connect(self.open)

        #self.quit = QtGui.QPushButton('quit')
        #self.quit.clicked.connect(self.close)

        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.imageLabel)

        # Debug用
        #layout.addWidget(self.filenameLabel)
        #layout.addWidget(self.button)
        #layout.addWidget(self.quit)

        self.setLayout(layout)
        self.setGeometry(50, 50, 250, 250)

    def contextMenuEvent(self, event):
        '''
        コンテキストメニュー
        '''
        menu = QtGui.QMenu(self)
        menu.addAction('Open', self.open)
        menu.addAction('Quit', self.close)
        menu.exec_(event.globalPos())

    def open(self):
        (path, ftype) = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        image = QtGui.QImage(path)
        pixmap = QtGui.QPixmap.fromImage(image)

        self.filenameLabel.setText(os.path.basename(path))

        self.imageLabel.setPixmap(pixmap)
        self.resize(image.size())
        mask = QtGui.QPixmap.fromImage(image.createAlphaMask())
        self.setMask(mask)


def main():
    app = QtGui.QApplication(sys.argv)

    iv = ImageViewer()
    iv.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    import sys
    main()


# EOF
