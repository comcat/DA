

Data Analysis Lab
===================


## pdf2csv

```bash
$ ./pdf2csv.py -i ../../Documents/COVID-19/20200312-sitrep-52-covid-19.pdf -o data/covid-19-who/20200312-outside-cn.csv -s 3 -n 3

$ grep -r Kingdom . | sort -r > uk.csv
```

```vim
# process the 1st column
%s/^\.\/\([0-9]\{8\}\)-[^,]\+/\1/g

# process 0206/3 ~ 0218, 0219 ~ 0227
%s/\(202002[0-9]\+\),\([0-9]\+\)\ *(\([0-9]\+\)),.\+,\([0-9]\+\)\ *(*\([0-9]*\))*$/\1,\2,\3,\4,\5/g

# process the line from 0228
%s/,Local.*//g

# process
%s/\ (\([0-9]\+\))/,\1/g
```

