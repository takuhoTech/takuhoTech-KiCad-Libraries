# takuhoTech-KiCad-Libraries
KiCad symbol & footprint libraries with lib-table generator

## Overview
複数のKiCadプロジェクト間で（グローバルライブラリを使わずに）共通の部品ライブラリを使うためのツールです.

ライブラリテーブルの手動入力が一切不要になります. 画像のテーブルのライブラリ名とパスは全て自動で入力されたものです.

<img width="1514" height="996" alt="image" src="https://github.com/user-attachments/assets/3e6103c1-8c46-4056-b2b3-435ff5173972" />

## Usage
`table_generator.pyw` を実行すると, このスクリプトが置かれているディレクトリ以下にある `.kicad_sym`ファイル（シンボルライブラリ）および `.pretty`フォルダ（フットプリントライブラリ）を検索し, KiCad用のライブラリテーブルを自動で生成します.

## Features
1. `table_generator.pyw` を実行します.
2. ファイル選択ダイアログで `.kicad_pro`ファイル（KiCadプロジェクトファイル）を選択します.
3. プロジェクトフォルダに `sym-lib-table`（シンボルライブラリテーブル）と `fp-lib-table`（フットプリントライブラリテーブル）が生成されます. 既存のライブラリテーブルは上書きされるので注意してください.
4. KiCadの「パスを設定」で環境変数を設定します.
   
   名前は `KICAD_USER_LIB_DIR`
   
   パスは `D:\GitHub\takuhoTech-KiCad-Libraries` のように `table_generator.pyw` が置かれているディレクトリを設定してください.

   `takuhoTech-KiCad-Libraries` への絶対パスが異なる複数の環境で同じライブラリテーブルを使えるようにするために環境変数を利用しています.

## Reference
詳細は次のブログ記事を参照してください.

https://takuhotech.hatenablog.com/entry/2025/03/10/214504
