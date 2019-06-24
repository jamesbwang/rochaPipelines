import pandas as pd
import sys
fileName = boundsFile = sys.argv[1]
bed = pd.read_csv(fileName, sep="\t", names= ["chromosome", "start", "end"])
returnData = pd.DataFrame({"chr1": [],"start1": [],"end1": [],"chr2": [],"start2": [],"end2": []})
for index, row in bed.iterrows():
#     if index %2 == 0:
#         returnData = pd.concat([returnData, pd.DataFrame({"chr1": [row["chromosome"]],"start1": [int(row["start"])],"end1": [int(row["end"])],"chr2": [""],"start2": [""],"end2": [""]})])
#     else:
#         returnData.iloc[-1, 3] = row["chromosome"]
#         returnData.iloc[-1,4] = int(row["start"])
#         returnData.iloc[-1,5] = int(row["end"])
    returnData = pd.concat([returnData, pd.DataFrame({"chr1": [row["chromosome"]],"start1": [int(row["start"])],"end1": [int(row["end"])],"chr2": [row["chromosome"]],"start2": [int(row["start"])],"end2": [int(row["end"])]})])
returnData.to_csv(fileName[:-4] + ".bedpe", sep='\t', na_rep='', float_format='%.f', columns=None, header=False, index=False, index_label=None, mode='w', encoding="ascii", compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, tupleize_cols=None, date_format=None, doublequote=True, escapechar=None, decimal='.')
