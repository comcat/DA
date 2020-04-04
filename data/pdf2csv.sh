#!/bin/bash

td=$(date +%Y%m%d)
day=$((td-1))

pdf=../../../Documents/COVID-19/$day-*.pdf
csv=covid-19-who/$day-outside-cn.csv

echo $pdf
echo $csv

../pdf2csv.py -i $pdf  -o $csv -s 2 -n 5
