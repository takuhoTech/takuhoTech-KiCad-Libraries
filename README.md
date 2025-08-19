# takuhoTech-KiCad-Libraries
KiCad symbol & footprint libraries with lib-table generator

`table_generator.pyw` を実行すると, このスクリプトが置かれているディレクトリ以下にある `.kicad_sym`ファイル（シンボルライブラリ）および `.pretty`フォルダ（フットプリントライブラリ）を検索し, KiCad用のライブラリテーブルを自動で生成します.

## How to use
1. `table_generator.pyw` を実行します.
2. ファイル選択ダイアログで `.kicad_pro`ファイル（KiCadプロジェクトファイル）を選択します.
3. プロジェクトフォルダに `sym-lib-table`（シンボルライブラリテーブル）と `fp-lib-table`（フットプリントライブラリテーブル）が生成されます.
4. KiCadの「パスを設定」で環境変数を設定します.
   
   名前は `KICAD_USER_LIB_DIR`
   
   パスは `D:\GitHub\takuhoTech-KiCad-Libraries` のように `table_generator.pyw` が置かれているディレクトリを設定してください.

   異なる環境で同じライブラリテーブルを使えるようにするために環境変数を利用しています.
