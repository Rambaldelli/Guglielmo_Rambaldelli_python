#!/bin/bash
seq=$1
eva=$2
job=$3
out=$HOME/Desktop/Bioinfo/Lab1 /Second Semester/1st_module(Capriotti)/ES/output
db=$HOME/Desktop/Bioinfo/Lab1 /Second Semester/1st_module(Capriotti)/ES
blast= blast path
muscle= muscle path

$blast -i $seq -d $db -o $seq.blast -m 8 -e $eva

for i in `cut -d "|" -f 4 $seq.blast`
do
wget -q -O $out/$i.fasta http://www.uniprot.org/uniprot/$i".fasta"
cat $out/$i.fasta
done > $job.fasta

$muscle -in $job.fasta -out $job.aln
