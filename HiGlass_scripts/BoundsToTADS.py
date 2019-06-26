import sys
import pandas as pd
import numpy as np

boundsFile = sys.argv[1]
sizeFile = sys.argv[2]

bounds = pd.read_csv(boundsFile, sep='\t', names=["chromosome", "begin", "end"])
sizes = pd.read_csv(sizeFile, sep='\t', names=["chromosome", "size"])
bounds = list(bounds.groupby("chromosome"))
boundsList = []
for chromosome in range(len(bounds)):
    beginningdf = pd.DataFrame.from_dict({"chromosome": ["chr"], "begin": [0], "end": [0]})
    enddf = pd.DataFrame.from_dict({"chromosome": ["chr"], "begin": [sizes.iloc[chromosome, 1]], "end": [sizes.iloc[chromosome,1]]})
    boundsList.append(beginningdf.append(bounds[chromosome][1].append(enddf)))
    
    
returnData = pd.DataFrame({"chromosome":[], "begin":[], "end":[]})
for chromosome in range(len(boundsList)):
    prevValue = -1
    for row in boundsList[chromosome].itertuples():
        if row[1] == "chr":
            prevValue = row[3]
            continue
        returnData = pd.concat([returnData, pd.DataFrame({"chromosome": [row[1]], "begin": [prevValue], "end": [row[2]]})])
        prevValue = row[3]
returnData.to_csv(boundsFile[:-4] + "_reversed.bed", sep="\t", header=False, index=False, float_format="%.f", encoding="ascii")
