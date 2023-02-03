#!/bin/bash
iconv -f utf-8 -t EUC-JP $(pwd)/testin.txt >> testput.txt

mecab $(pwd)/testput.txt -O wakati -o ./out.txt
iconv -f EUC-JP -t utf-8 $(pwd)/out.txt >> ./parsed_out.txt
