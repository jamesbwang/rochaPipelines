import pandas as pd
import sys

chromPath = sys.argv[1]
sortPath = sys.argv[2]
chrom = set(pd.read_csv(chromPath, sep="\t", header=None, usecols=[0], squeeze=True))
sort = pd.read_csv(sortPath, sep="\t", header=None)
sort[sort[0].isin(chrom)].to_csv(sortPath, header=False, index=False, sep="\t")
