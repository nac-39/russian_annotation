# russian_annotation

### 使い方
1. ```$ git clone git@github.com:nac-39/russian_annotation.git```(SSHの場合)
1. ```$ pip install -r requirements.txt```
2. ```$ flask run```
3. localhost:5000にアクセス

### 特徴
- ロシア語の格・品詞・性・基本形がルビとして本文の下に振られます．
- 単語をダブルクリックすると，基本形を入力した場合の　[http://cblle.tufs.ac.jp/dic/ru/](http://cblle.tufs.ac.jp/dic/ru/)　の検索結果ページに直接飛ぶことができます．

### 使っている技術など
- [pymporphy2](https://pymorphy2.readthedocs.io/en/stable/index.html) - ロシア語の形態素解析パッケージです．
- Flask
  
### その他
直した方がいいところ等あれば気軽に言ってください!!


Copyright (c) 2022 nac-39
Released under the MIT license
https://opensource.org/licenses/mit-license.php
