#python
import k3d
#
# K-3D Ver.0.8.0.0 用
# テストスクリプト
#
# ファイルをUTF-8で保存すると、日本語のコメントは正常に表示される。
# Unicoe 文字列が使えない。
# 文字列に日本語を書いたら、通った。いいのか、それで。

## 通常のメッセージ
#k3d.ui().message("This is a message!")
k3d.ui().message("This is a メッセージ!")

## 警告メッセージ
#k3d.ui().warning_message("This is a warning message!")
k3d.ui().warning_message("This is a 警告メッセージ!")

## エラーメッセージ
#k3d.ui().error_message("This is an error message!")
k3d.ui().error_message("This is an エラーメッセージ!")

## 選択ボックス
#result = k3d.ui().query_message("Pick one!", ["Choice 1", "Choice 2", "Choice 3"])
result = k3d.ui().query_message("ひとつ選んでね!", ["その壱", "その弐", "その参"])

#k3d.ui().message("You chose " + str(result))
k3d.ui().message("あなたが選んだのは[" + str(result) + "]でした。")

## ファイル選択（読み込み用）
#result = k3d.ui().get_file_path("read", "test", "Choose file to read (doesn't actually read anything):", "")
result = k3d.ui().get_file_path("read", "てすと", "読み込むファイルを選んでね (実際には読み込みません):", "")

#k3d.ui().message("You chose " + str(result))
k3d.ui().message("あなたが選んだファイルは " + str(result) + "でした。")

## ファイル選択（保存用）
#result = k3d.ui().get_file_path("write", "test", "Choose file to write (doesn't actually write anything):", "")
result = k3d.ui().get_file_path("write", "検査", "書き込むファイルを選んでね (実際には書き込みません):", "")

#k3d.ui().message("You chose " + str(result))
k3d.ui().message("あなたが選んだファイルは " + str(result) + "でした。")

#k3d.ui().message("The End")
k3d.ui().message("おしまい")

# user_interface.pyを参考にしました。
# EOF
