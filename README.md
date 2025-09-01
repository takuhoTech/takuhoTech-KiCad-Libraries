# takuhoTech-KiCad-Libraries
KiCad symbol & footprint & design-block libraries with lib-table generator

## Overview
複数のKiCadプロジェクト間で（グローバルライブラリを使わずに）共通の部品ライブラリを管理するためのツールです.

ライブラリテーブルの手動入力が一切不要になります. 画像のテーブルのライブラリ名とパスは全て自動で入力されたものです.

<img width="757" height="313" alt="image" src="https://github.com/user-attachments/assets/f7891152-8964-4a21-b111-2ebbee7cef40" />

## Usage
`table_generator.pyw` を実行すると, このスクリプトが置かれているディレクトリ以下にある次のファイルとフォルダを検索し, KiCad用のライブラリテーブルを自動で生成します.

- `.kicad_sym`ファイル（シンボルライブラリ）
- `.pretty`フォルダ（フットプリントライブラリ）
- `.kicad_blocks`フォルダ（デザインブロックライブラリ）

## Features
1. `table_generator.pyw` を実行します.
2. ファイル選択ダイアログで `.kicad_pro`ファイル（KiCadプロジェクトファイル）を選択します.
3. プロジェクトフォルダに次のファイルが生成されます.
   - `sym-lib-table`（シンボルライブラリテーブル）
   - `fp-lib-table`（フットプリントライブラリテーブル）
   - `design-block-lib-table`（デザインブロックライブラリテーブル）
   
   既存のライブラリテーブルは上書きされるので注意してください. 見つかったライブラリの数が表示されています.
   
   <img width="295" height="197" alt="image" src="https://github.com/user-attachments/assets/4ae793d1-303a-4c20-8e66-22eebcc3884e" />
   
5. KiCadの「パスを設定」で環境変数を設定します.
   
   名前は `KICAD_USER_LIB_DIR`
   
   パスは `D:\GitHub\takuhoTech-KiCad-Libraries` のように `table_generator.pyw` が置かれているディレクトリを設定してください.

   `takuhoTech-KiCad-Libraries` への絶対パスが異なる複数の環境で同じライブラリテーブルを使えるようにするために環境変数を利用しています.

## 収録ライブラリについて
- 高周波コンポーネントが多めです.
- 部品の種類ごとにカテゴリ分けしてからシンボルとフットプリントに分けることで管理しやすくしています.
     - シンボルとフットプリントに分けてからそれぞれカテゴリ分けしてあっても問題なくライブラリテーブルは生成されます.
- ライブラリ名の末尾に一律で`extlib`を付けることで検索しやすくしています.
- 収録ライブラリが不要な場合は `table_generator.pyw` だけダウンロードして使ってください.

## Reference
詳細は次のブログ記事を参照してください.

https://takuhotech.hatenablog.com/entry/2025/03/10/214504
