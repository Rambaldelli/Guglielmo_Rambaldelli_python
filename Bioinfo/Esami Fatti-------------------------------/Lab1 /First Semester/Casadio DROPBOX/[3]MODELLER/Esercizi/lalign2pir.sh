#!/bin/bash

#usage: ./lalign2pir.sh filefromlalign sequence structure outputfile

LALIGNFILE=$1
PNAME1=$2
PNAME2=$3
OUTFILE=$4

echo ">P1;"$2 > $4
echo "sequence:"$2"::::::::" >> $4
cat $LALIGNFILE | grep ^$2 | awk '{print $2}' >> $4
echo >> $4
echo ">P1;"$3 >> $4
echo "structureX:"$3"::::::::" >> $4
cat $LALIGNFILE | grep ^$3 | awk '{print $2}' >> $4
