このリポジトリはインターン先の勉強会のため作成されました．

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