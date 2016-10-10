#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

del_punc_set = set()
del_punc_set.add('，')
del_punc_set.add('。')
del_punc_set.add('！')
del_punc_set.add('？')
del_punc_set.add(',')
del_punc_set.add('.')
del_punc_set.add('!')
del_punc_set.add('?')
del_punc_set.add('：')
del_punc_set.add('；')
del_punc_set.add('、')
del_punc_set.add('（')
del_punc_set.add('）')
del_punc_set.add('【')
del_punc_set.add('】')
del_punc_set.add('《')
del_punc_set.add('》')
del_punc_set.add('“')
del_punc_set.add('”')
del_punc_set.add('(')
del_punc_set.add(')')
del_punc_set.add('-')
del_punc_set.add('...')
del_punc_set.add('[')
del_punc_set.add(']')
del_punc_set.add('<')
del_punc_set.add('>')
del_punc_set.add('{')
del_punc_set.add('}')
del_punc_set.add('/')
del_punc_set.add('—')
del_punc_set.add('「')
del_punc_set.add('」')
del_punc_set.add('…')

in_root = "topictiling-train/"
out_root = "topictiling-train-filter/"

def get_filename(root_dir):
    return (f for f in os.listdir(root_dir))

def filter(file_name):
    r_file = os.path.join('%s%s' %(in_root, filename))
    w_file = os.path.join('%s%s' %(out_root, filename))
    with open(r_file, "r") as r_fp, open(w_file, "w") as w_fp:
        for line in r_fp:
            arr = line.split(" ")
            tag = True
            t_str = ""
            for i in xrange(len(arr) - 1):
                if arr[i] not in del_punc_set:
                    if tag:
                        tag = False
                        t_str = arr[i]
                    else:
                        t_str += " " + arr[i]
            w_fp.write("%s\n" %t_str)

if __name__ == "__main__":
    filenames = get_filename(in_root)
    for filename in filenames:
        filter(filename)
