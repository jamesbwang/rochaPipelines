import sys

oligos = sys.argv[1]
data = sys.argv[2]
pickle = sys.argv[3]
aux = sys.argv[4]

from os import path
import pandas as pd

def range_intersect(range1, range2):
    return range1[0] <= range2[1] and range2[0] <= range1[1]

if not path.exists(pickle) or not path.exists(aux):
    oligoTable = pd.read_csv(oligos, sep="\t", header=None, usecols=[0,1,2,3])
    dataTable = pd.read_csv(data, sep=" ", header=None, usecols=[1,2,5,6], prefix="X")
    interactionCount = dataTable.shape[0]
    with open(aux, "w") as f:
        f.write("Number of total read interactions: " + str(interactionCount) + "\n")
    dataTable.query("X1 == 'chr8' | X5 == 'chr8'", inplace=True)
    dataTable.to_pickle(pickle, compression='infer', protocol=4)
else:
    interactionCount = -1
    with open(aux, "r") as f:
         interactionCount = int(f.read()[34:])
    oligoTable = pd.read_csv(oligos, sep="\t", header=None, usecols=[0,1,2,3])
    dataTable = pd.read_pickle(pickle, compression='infer')

boundsTable = pd.DataFrame({"lowerBound":[], "upperBound":[]})
prevValue = -1
for oligo in oligoTable.itertuples():
    if oligo[0] %2 == 0:
        prevValue = oligo[3]
    else:
        boundsTable = pd.concat([boundsTable, pd.DataFrame({"lowerBound":[int(prevValue)], "upperBound":[int(oligo[4])]})])
del oligoTable

targetedInteractionCount = 0
for interaction in dataTable.itertuples():
    for bound in boundsTable.itertuples():
        if range_intersect((interaction[2], interaction[2]+51), (bound[1], bound[2])) or range_intersect((interaction[4], interaction[4]+51), (bound[1], bound[2])):
            targetedInteractionCount += 1
            break
with open(aux, "a") as f:
        f.write("Number of targeted interactions: " + str(targetedInteractionCount) + "\n")
        f.write("Normalized targeted interactions: " + str(targetedInteractionCount/interactionCount) + "\n")
