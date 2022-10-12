このリポジトリはインターン先の勉強会のため作成されました．（勉強会当日までは暫定の内容です）

# 環境構築
本リポジトリにディレクトリを移動させ以下のコードを実行してください．

```
pyenv install 3.10.6
pyenv virtualenv 3.10.6 intro-pyspark
pyenv local intro-pyspark  
pip install poetry
poetry init
poetry add pyspark 
poetry add "pyspark[sql]"
poetry add  plotly 
```

# 参考資料
https://spark.apache.org/docs/latest/api/python/getting_started/index.html