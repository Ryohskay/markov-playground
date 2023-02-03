# How to use
Since the default Ubuntu repository's MeCab uses **EUC-JP** for encoding, charset conversion is needed:
- First, write in your input to `testin.txt`
- Next, this programme uses `iconv` to convert the text from utf-8 into EUC-JP
- then this calls `mecab` and parses the content, and separates it by word. (`-O wakati`)
- Finally, `iconv` again to convert the output in EUC-JP back into utf-8.

# Requires:
- from /bin/bash
  - MeCab available as `mecab`
  - MeCab dictionary
  - `iconv`
- Python (at least on python 3.10):
  - markovify

# Other notes:
- NewlineText() on markovify is needed (at least for texts from 青空文庫).
