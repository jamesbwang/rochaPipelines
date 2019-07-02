import pandas as pd
import sys
fileName = boundsFile = sys.argv[1]
bed = pd.read_csv(fileName, sep="\t", names= ["chromosome", "start", "end"])
returnData = pd.DataFrame()
returnData["chr1"] = bed["chromosome"]
returnData["start1"] = bed["start"]
returnData["end1"] = bed["end"]
returnData["chr2"] = bed["chromosome"]
returnData["start2"] = bed["start"]
returnData["end2"] = bed["end"]

returnData.to_csv(fileName[:-4] + ".bedpe", sep='\t', na_rep='', float_format='%.f', columns=None, header=False, index=False, index_label=None, mode='w', encoding="ascii", compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, tupleize_cols=None, date_format=None, doublequote=True, escapechar=None, decimal='.')
