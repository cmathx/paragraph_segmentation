#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
docs = 0
end_punc_set = set()
end_punc_set.add("。")
end_punc_set.add("！")
end_punc_set.add("？")
root_dir = "speech_lda.train/"
for _file in os.listdir(root_dir):
    _path = os.path.join(root_dir, _file)
    with open(_path, "r") as r_fp, open("topictiling-train/%s" %_file, "w") as w_fp:
        for line in r_fp:
            t_str = ""
            line = line.decode("gb18030").encode("utf-8")
            arr = line.split(" ")
            for ele in arr:
                if len(ele) == 0:
                    continue
                ele = ele.strip("\n")
                t_str += ele + " "
                if ele in end_punc_set:
                    w_fp.write("%s\n" %t_str.strip(" "))
                    t_str = ""
    docs += 1
