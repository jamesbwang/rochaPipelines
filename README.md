# Hi-C Pipelines
Backup repository for Lab Rocha's Pipelines, will make public once relevant data is removed and such

## Pipelines:

## cworld-pipelines
Implementation to convert sparse matrix format to [.my5C file](http://my5c.umassmed.edu/welcome/welcome.php) and to pass it in for the Dekker Lab's implementation of TAD (Topologically Associated Domains) calling

### Requirements:
[Python2](https://www.python.org)

[bedTools](https://bedtools.readthedocs.io/en/latest/)

[R](https://www.r-project.org/)

[perl](https://www.perl.org/)

Build Job Dekker's [dekker-cworld repository](https://github.com/dekkerlab/cworld-dekker.git) and edit the path in ```matrix2my5C``` to the path of the ```matrix2insulations.pl``` script (will push this script to repository for compatibility)

### Usage:
Like the CaTCH Pipeline, cworld-pipelines calls TADs on entire genomes. Generate TADs with the following command:

```
./matrix2my5C matrixDirectory/ sizeFile.sizes absbed.bed binSize
```

matrixDirectory contains the .matrix files output by the CaTCH pipeline. absbed.bed outputs the .abs.bed files output by the CaTCH pipeline as well.

### Future improvements

- [ ] Support for more scripts than just TAD calling/insulation score calculation
- [ ] Speed improvements in matrixTomy5C.py, especially in construction of dense matrix format
- [ ] integration with CaTCH pipeline for a single command efficient and streamlined pipeline

## TADCalling_CaTCH
Given a .hic file generated from HiC-Pro or Juicer, call TAD (Topologically Associated Domains) using the Giorgetti Lab's Reciprocal Insulation Score Algorithm (CaTCH)

### Requirements:
[Python3](https://www.python.org)

[bedTools](https://bedtools.readthedocs.io/en/latest/)

[Juicer Tools](https://github.com/aidenlab/juicer/wiki/Download)

[CaTCH](https://github.com/zhanyinx/CaTCH_R)

Extract the Juicer Tools .jar file to the root package directory.

### Usage:
the CaTCH Pipeline calls TADs on whole genomes. These take the form of a .bedpe file. Generate TAD Calling on the genomes by the folowing command:

```
./Construct_TADs_From_hic hicFile.hic chrom.sizes nChromosomes binSize
```

### Future improvements:
- [ ] create flags specifying type of visualization software (HiGlass or Juicebox)
- [ ] implement performance improvements in converting insulations to .bed files
- [ ] data quality visualization
- [ ] implement parallelization both at the batch job and chromosomal level

## Capture Hi-C
Enriches paired-end sequencing data for gene regions given Capture-HiC oligonucleotide territories and chromosome sizes files.

### Requirements:
[Python3](https://www.python.org)

[bedTools](https://bedtools.readthedocs.io/en/latest/)

### Usage:
Capture-HiC assumes that all enhanced interactions are located in the same chromosome. Pass in the chromosome name to the pipeline e.g. chr8 . Futhermore, pass in the bin size (here: 5000) as follows:
```
./HiC-Capture_Pipeline_SingleJob oligos.tsv interactions.txt chromosomes.sizes chr8 5000
```
All associated .bed, .txt, and .bedgraph outputs will be written to the same directory as ```interactions.txt```

For multiple jobs on the same genomic regions, use the bash command for multiple jobs i.e.
```
./HiC-Capture_Pipeline_MultiJob oligos.tsv chromosomes.sizes chr8 5000
```

Given that all ```interactions.txt``` files are in the same working directory as ```oligos.tsv```, multiple jobs will be created and run in parallel. Note that this script is only compatible with the NIH Biowulf cluster.

### Future improvements:
- [x] create flags specifying bin size
- [x] implement more time-efficient methods for calculating data quality
- [ ] data quality visualization
- [ ] alphanumeric sorting/compatibility with [HiGlass](https://higlass.io) visualization 


## current scripts in HiGlass_scripts:
### 1. script to reverse non-TAD boundaries to TAD boundaries
Named boundsToTADS.py, this script converts tab-separated files for non-TAD boundaries to TAD .bed files. Usage is as follows:
```
python3 boundsToTADS.py boundsFile.tsv chromSizes.sizes
```

### 2. script to convert .bed files to .bedpd files
Named BedToBedpd.py, this script converts bed files to bedpd files for TAD annotation in [HiGlass](https://higlass.io). NOTE: because of poor documentation, Broad's iGV and HiGlass treat .bedpd files differenly. visualizing these .bed files in iGV will not work. Usage is as follows:
```
python3 BedToBedpe.py bedfile.bed
```

### 3. script to (somewhat) efficiently calculate the fraction of targeted sequences in Capture-HiC protocols.

 Mirrors notebook of same name in the folder. Use before marking up .bed files for visualization to generate .pkl files. Usage is as follows:
```
python3 InteractionScore.py oligoFile.tsv readData.tsv pklPath.pkl fileToWriteTo.txt
```

### 4. script to use in conjunction to script #4 to mark up .bed files illustrating each interaction for each territory. 

Run script #3 for .pkl generation. Mirrors notebook of same name in the folder. Use for visualization in iGV, run script #5 for visualization in both iGV and HiGlass. Usage is as follows:
```
python3 EnhancedBed.py pickled_interactions.pkl oligo_interactions.pkl fileToWriteTo.txt
```
