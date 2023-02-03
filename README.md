# About this repo
This is my repo to play around with python's markovify and markov chain stuff.

# How to use
Since the default Ubuntu repository's MeCab uses **EUC-JP** for encoding, charset conversion is needed:
- First, write in your input to `testin.txt`
- Next, this programme uses `iconv` to convert the text from utf-8 into EUC-JP
- then this calls `mecab` and parses the content, and separates it by word. (`-O wakati`)
- Finally, `iconv` again to convert the output in EUC-JP back into utf-8.

# Requires:
- OS:
  - Pop! OS 22.04 LTS ([see os-release](https://github.com/Ryohskay/markov-playground/blob/main/info/os-release))

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
