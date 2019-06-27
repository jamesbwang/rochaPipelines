import sys

# data to abstract as system arguments in script
# TODO: include the chr number as a system argument
oligos = sys.argv[1]
data = sys.argv[2]
pickle = sys.argv[3]
aux = sys.argv[4]

from os import path
import pandas as pd


 #proof found here: https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
def range_intersect(range1, range2):
    return range1[0] <= range2[1] and range2[0] <= range1[1]

#case 1: building the entire thing from scratch
if not path.exists(pickle) or not path.exists(aux):
    #reading in the dataFrames is really heavy and can cause memory errors...
    oligoTable = pd.read_csv(oligos, sep="\t", header=None, usecols=[0,1,2,3])
    dataTable = pd.read_csv(data, sep=" ", header=None, usecols=[1,2,5,6], prefix="X")
    
    #...but necessary to get the total number of interactions in the file
    interactionCount = dataTable.shape[0]
    #write interaction counts to file for further calculations
    with open(aux, "w") as f:
        f.write("Number of total read interactions: " + str(interactionCount) + "\n")
 
   #initial filter applied and instantly saved to .pkl file to save overhead later on
    dataTable.query("X1 == 'chr8' | X5 == 'chr8'", inplace=True)
    dataTable.to_pickle(pickle, compression='infer', protocol=4)

else:
    #interaction Counts: read from the existing file
    interactionCount = -1
    with open(aux, "r") as f:
         s = f.read()
         interactionCount = int(s[34:s.find("\n")])
    
    #read space-negligible DataFrame
    oligoTable = pd.read_csv(oligos, sep="\t", header=None, usecols=[0,1,2,3])
    
    #read pkl
    dataTable = pd.read_pickle(pickle, compression='infer')

## construct the boundaries for further filtering
boundsTable = pd.DataFrame({"lowerBound":[], "upperBound":[]})
prevValue = -1

for oligo in oligoTable.itertuples():
    if oligo[0] %2 == 0:
        prevValue = oligo[3]
    else:
        boundsTable = pd.concat([boundsTable, pd.DataFrame({"lowerBound":[int(prevValue)], "upperBound":[int(oligo[4])]})])
#pickle to save computation later
boundsTable.to_pickle(oligos + ".pkl", compression='infer', protocol=4)
del oligoTable

## count interactions for targeted interaction
targetedInteractionCount = 0
doubleInteractionCount = 0
# implementation: brute force, but since territories=4, not too much of a big deal. 
# TODO: implement binary search over these ranges if territory numbers grow to be too big
for interaction in dataTable.itertuples():
    for bound in boundsTable.itertuples():
        # checks both interactor and interactee for fulfillment of criteria
        if (range_intersect((interaction[2], interaction[2]+51), (bound[1], bound[2])) and interaction[1] == "chr8"):
            targetedInteractionCount += 1
        if (range_intersect((interaction[4], interaction[4]+51), (bound[1], bound[2])) and interaction[3] == "chr8"):
            targetedInteractionCount += 1 
# write results to file
with open(aux, "a") as f:
        f.write("Number of targeted interactions: " + str(targetedInteractionCount) + "\n")
        f.write("Number of double interactions: " + str(doubleInteractionCount) + "\n")
        f.write("Normalized targeted interactions: " + str(targetedInteractionCount/interactionCount) + "\n")
