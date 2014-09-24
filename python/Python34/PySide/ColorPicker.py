#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PySide import QtCore, QtGui
'''
ColorPicker.py
Pyside を使ったカラーピッカー（色選択ツール）
'''


class colorPicker (QtGui.QWidget):

    def __init__(self):
        super(colorPicker, self).__init__()
        self.initUI()

    def initUI(self):
        '''
        ユーザーインターフェースの初期化
        '''
        self.infoLabel = QtGui.QLabel()
        self.colorLabel = QtGui.QLabel()
        self.colorButton = QtGui.QPushButton('QColorDialog.get&Color()')
        self.colorButton.clicked.connect(self.setColor)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.infoLabel)
        layout.addWidget(self.colorLabel)
        layout.addWidget(self.colorButton)

        self.setLayout(layout)
        self.resize(300, 150)
        self.setWindowTitle('Color Picker')

    def setColor(self):
        '''
        ダイアログを出して色選択
        '''
        color = QtGui.QColorDialog.getColor(QtCore.Qt.green, self)
        if color.isValid():
            self.colorLabel.setPalette(QtGui.QPalette(color))
            self.colorLabel.setAutoFillBackground(True)
            self.infoLabel.setText('color(#RGB) = ' + color.name())


def main():
    app = QtGui.QApplication(sys.argv)
    window = colorPicker()
    window.show()
    return app.exec_()

if __name__ == '__main__':
    main()
# EOF
