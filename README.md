# rochaPipelines
Backup repository for Lab Rocha's Pipelienes, will make public once relevant data is removed and such

## current scripts:
### 1. script to reverse non-TAD boundaries to TAD boundaries
Named boundsToTADS.py, this script converts tab-separated files for non-TAD boundaries to TAD .bed files. Usage is as follows:
'''
python3 boundsToTADS.py boundsFile.tsv chromSizes.sizes
'''

### 2. script to convert .bed files to .bedpd files
Named BedToBedpd.py, this script converts bed files to bedpd files for TAD annotation in [HiGlass](https://higlass.io). NOTE: because of poor documentation, Broad's iGV and HiGlass treat .bedpd files differenly. visualizing these .bed files in iGV will not work. Usage is as follows:
'''
python3 BedToBedpd.py bedfile.bed
'''

### 3. script to (somewhat) efficiently calculate the fraction of targeted sequences in Capture-HiC protocols. Mirrors notebook of same name in the folder. Use before marking up .bed files for visualization to generate .pkl files. Usage is as follows:
'''
python3 InteractionScore.py oligoFile.tsv readData.tsv pklPath.pkl fileToWriteTo.txt
'''

### 4. script to use in conjunction to script #4 to mark up .bed files illustrating each interaction for each territory. Run script #3 for .pkl generation. Mirrors notebook of same name in the folder. Use for visualization in iGV, run script #5 for visualization in both iGV and HiGlass. Usage is as follows:
'''
python3 EnhancedBed.py pickled_interactions.pkl oligo_interactions.pkl 

'''
