#!/bin/bash

## CaTCH       
## Author(s): Yinxiu Zhan
## Contact: yinxiu.zhant@fmi.ch
## This software is distributed without any guarantee under the terms of the GNU General
## Public License, either Version 2, June 1991 or Version 3, June 2007.

##
## First version of converter between HiCPro and CaTCH 

function usage {
    echo -e "usage : hicpro2catch.sh -i INPUT -b BINSIZE -f FILEBIN [-n NORM] [-t TYPE] [-h]"
    echo -e "Use option -h|--help for more information"
}

function help {
    usage;
    echo 
    echo "Generate CaTCH suitable format from HiCPro output"
    echo "See https://github.com/zhanyinx/CaTCH_R for details about CaTCH"
    echo "---------------"
    echo "OPTIONS"
    echo
    echo "   -i|--input INPUT : .matrix file generated by HiC-Pro"
    echo "   -b|--binsize BINSIZE : The binning size of the hicpro matrix"
    echo "   -f|--filebin FILEBIN : File containing genomic coordinate corresponding to bin (the file *_abs.bed that you find it in raw matrix directories from HiC-Pro output"
    echo "   [-n|--norm NORM] : library normalisation, if not defined, sum of all interactions gives tot number of useful reads"
    echo "   [-t|--type TYPE] : cell type"
    echo "   [-h|--help]: help"
    exit;
}

# Transform long options to short ones
for arg in "$@"; do
  shift
  case "$arg" in
      "--input") set -- "$@" "-i" ;;
      "--binsize")   set -- "$@" "-b" ;;
      "--binfile")   set -- "$@" "-f" ;;
      "--norm")   set -- "$@" "-n" ;;
      "--type")   set -- "$@" "-t" ;;
      "--help")   set -- "$@" "-h" ;;
       *)        set -- "$@" "$arg"
  esac
done

binfile=""
bin=""
file=""
TYPE=""
NORM=-1

while getopts ":i:n:b:f:t:h" OPT
do
    case $OPT in
        i) file=$OPTARG;;
        b) bin=$OPTARG;;
        f) binfile=$OPTARG;;
	n) NORM=$OPTARG;;
        t) TYPE=$OPTARG;;
        h) help ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            usage
            exit 1
            ;;
    esac
done

if [ $# -lt 6 ]
then
    usage
    exit
fi


if [[ -z $file ]];
then
    usage
    exit
fi


if [[ -z $binfile ]];
then
    usage
    exit
fi

if [ -f bin ]; then
	rm bin
fi



mkdir tmp
cp $binfile tmp/tmp.dat
cd tmp
	awk '{print $0 > $1".dat"}' tmp.dat
	for files in `ls chr*`; do
        	awk 'BEGIN{min=99999999999999;max=-99}{if($4>max) max=$4; if($4<min) min=$4}END{print $1,min,max}' $files >> ../bin 

	done
cd ..
rm -r tmp

##renorm same number of reads
if ! [ $NORM -eq -1 ]; then
	norm=`awk 'BEGIN{t=0;}{t+=$3}END{print t}' $file`
	awk '{print $1,$2,$3/"'"$norm"'"*"'"$NORM"'"}' $file > appo
	mv appo $file
fi

awk 'BEGIN{fn=0; nchr=0}{

	if(FNR==1) fn++
	if(fn==1){
		chr[nchr]=$1;
		start[nchr]=$2;
		end[nchr]=$3;
		nchr++
	}

	if(fn==2){
		for(i=0;i<nchr;i++){
			if($1>=start[i] && $1<=end[i] && $2>=start[i] && $2<=end[i]){
				#reconvert to zero based bins
			print chr[i],$1-start[i],$2-start[i],$3 > chr[i]".CaTCH" 
			print chr[i],$2-start[i],$1-start[i],$3 > chr[i]".CaTCH"
			}
		}
	}

}' bin $file

##move to random directory the useless files
if ! [ -d random ]; then
	mkdir random
fi

mv *_random* chrUn* chrM* random/

###
echo "The files *.CaTCH can be used as input for CaTCH"

