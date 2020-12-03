import os.path as osp
import re

import pandas as pd

data_root = "G:\\dataset\\UCSCexamples"
cli_fn = "GSE121720_series_matrix.txt"
gene_fn = "tpm.txt"

# 处理clinical 数据
cli_data = {}
with open(osp.join(data_root, cli_fn), "r") as f:
    for line in f:
        if line.startswith("!Sample"):
            # 1. 将每一行的第一个元素去除!Sample_作为key，剩下的提取出“”中的部分作为value
            key, value = line.split("\t", maxsplit=1)
            key = key[len("!Sample_"):]
            value = re.findall(r'"(.*?)"', value)

            # 2. 如果value中的元素以xx：yy形式存在，则xx作为其新的变量名
            if all([":" in v for v in value]):
                v1s, v2s = [], []
                for v in value:
                    v1, v2 = v.split(":", maxsplit=1)
                    v1s.append(v1.strip())
                    v2s.append(v2.strip())
                if len(set(v1s)) == 1:
                    key = v1
                    value = v2s

            # 保存到dict中
            cli_data[key] = value
cli_data = pd.DataFrame(cli_data)
# 这里变量名是title，需要对其进行一些处理：包括去掉一些冗余的字符和改一下变量名
cli_data.insert(
    0, "Sample", cli_data["title"].str.split(" ", n=1, expand=True)[0])
cli_data.pop("title")
# 把名称超过255长度的列去掉
bool_index = cli_data.columns.map(lambda x: len(x) < 255)
cli_data = cli_data.loc[:, bool_index]
cli_data.to_csv(osp.join(data_root, "clean_cli.tsv"), sep="\t", index=False)

# 处理RNAseq data（主要为第一列加Sample的column name）
writer = open(osp.join(data_root, "clean_rnaseq.tsv"), "w")
with open(osp.join(data_root, gene_fn), "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            line = "Sample\t" + line
        writer.write(line)
