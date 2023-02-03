# About this repo
This is my repo to play around with python's markovify and markov chain stuff.

# How to use
Since the default Ubuntu repository's MeCab uses **EUC-JP** for encoding, charset conversion is needed:
- First, write in your input to `testin.txt`
- Next, this programme uses `iconv` to convert the text from utf-8 into EUC-JP
- then this calls `mecab` and parses the content, and separates it by word. (`-O wakati`)
- Finally, `iconv` again to convert the output in EUC-JP back into utf-8.

# Env:
- OS: Pop! OS 22.04 LTS ([see os-release](https://github.com/Ryohskay/markov-playground/blob/main/info/os-release))
- bash: ^5.1.16
- Python: ^3.10.6
- MeCab: ^0.996
- iconv: ^2.35
- markovify: ^0.9.4


# Requires:
- from /bin/bash
  - [MeCab](https://taku910.github.io/mecab/) available as `mecab`
  - MeCab dictionary
  - `iconv`
- Python (at least on python 3.10):
  - [markovify](https://github.com/jsvine/markovify)

# Other notes:
- NewlineText() on markovify is needed (at least for texts from 青空文庫).

# Resources
- [[Python] MeCab とマルコフ連鎖ライブラリ markovify を使い、文章を学習して自動生成する方法](https://qiita.com/shge/items/fbfce6b54d2e0cc1b382)
- [mecab-python3 GitHub](https://github.com/SamuraiT/mecab-python3)
