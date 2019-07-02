#!/usr/bin/env Rscript
args<- commandArgs(trailingOnly=TRUE)

fileinput<-args[1]
clusterPath<-args[2]
nClusterPath<-args[3]
library(CaTCH)
li = domain.call(fileinput)
nClusters = li[1]
clusters = li[2]
print("Algorithm Completed")
write.table(nClusters, nClusterPath, sep="\t", row.names=F, col.names = F)
write.table(clusters, clusterPath, row.names=F, sep="\t", col.names = F)

