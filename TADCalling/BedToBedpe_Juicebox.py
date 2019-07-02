import pandas as pd
import sys
fileName = boundsFile = sys.argv[1]
bed = pd.read_csv(fileName, sep="\t", names= ["chromosome", "start", "end"])
returnData = pd.DataFrame()
returnData["chr1"] = bed["chromosome"]
returnData["x1"] = bed["start"]
returnData["x2"] = bed["end"]
returnData["chr2"] = bed["chromosome"]
returnData["y1"] = bed["start"]
returnData["y2"] = bed["end"]
returnData["name"] = "."
returnData["score"] = "."
returnData["color"] = "255,0,0"

returnData.to_csv(fileName[:-4] + "_juiced.bedpe", sep='\t', na_rep='', float_format='%.f', columns=None, header=True, index=False, index_label=None, mode='w', encoding="ascii", compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, tupleize_cols=None, date_format=None, doublequote=True, escapechar=None, decimal='.')
