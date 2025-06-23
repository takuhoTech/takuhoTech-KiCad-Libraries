# takuhoTech-KiCad-Libraries
takuhoTech's KiCad Libraries

このリポジトリではfootprintとsymbolは部品ごとに纏めています.
table.pyを実行することで,table.pyが置いてあるディレクトリから下の階層にあるprettyフォルダとkicad_symファイルの相対パスを読み取り,KiCad用のライブラリテーブルを自動で生成することができます.
KiCadやsparkfunのリポジトリなど,footprintとsymbolが別々の枝にあるディレクトリ構造でも問題なく生成できます.

生成したライブラリテーブルをKiCadのプロジェクトフォルダに入れる際は,KiCad側で'KICAD_USER_LIB_DIR'という名前のパスを'D:\GitHub\takuhoTech-KiCad-Libraries'の様に設定してください.（table.pyが置いてある場所）

詳細ははてなブログの記事を参照してください.

https://takuhotech.hatenablog.com/entry/2025/03/10/214504
