# 概要
このリポジトリはインターン先の勉強会のため作成されました．Pythonの紹介からPySparkの使い方まで網羅しました．具体的には，pandasとSQL，PySparkの文法をそれぞれ比較し，pandasとPysparkの性質の違いをまとめました．その結果，状況に応じて適切にツールを選ぶ必要があることがわかりました．




# 環境構築
```
brew install pyenv
brew install openjdk8 --csak
pyenv install 3.10.6
pyenv virtualenv 3.10.6 intro-pyspark
pyenv local intro-pyspark  
pip install poetry
poetry init
poetry add pyspark "pyspark[sql]" plotly jupyter
```

# Jupyter Labの開き方
1. `pyenv activate intro-pyspark`と入力し仮想環境下に入る

2. `poetry run jupyter lab`とターミナルで入力

3.  `http://localhost:8888/`をブラウザで開く

# 参考文献

### スライド中の参考文献
[1] https://bookclub.kodansha.co.jp/product?item=0000275420  
[2] https://docs.python.org/ja/3/  
[3] https://pandas.pydata.org/docs/  
[4] https://pandas.pydata.org/docs/user_guide/10min.html  
[5] https://sparkbyexamples.com/pyspark/pandas-vs-pyspark-dataframe-with-examples/amp/  
[6] https://www.ohitori.fun/entry/basic-data-analysis-in-pandas  
[7] https://qiita.com/driller/items/ef8a16be03e146ce2183  
[8] https://blog.serverworks.co.jp/introducing-pyspark-6  
[9] https://qiita.com/yukifddd/items/5668483705ef9d89a0c9  
[10] https://towardsdatascience.com/parallelize-pandas-dataframe-computations-w-spark-dataframe-bba4c924487c

### PySparkによるデータ前処理の例
- 言語処理  
https://techblog.nhn-techorus.com/archives/7301
- テーブルデータ  
https://www.ariseanalytics.com/activities/report/20211210/

### 環境構築について
https://zenn.dev/uenotakato/scraps/a641b32411cbde
