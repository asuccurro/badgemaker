# BadgeMaker

1. Have all your participants collected in a csv file (e.g. `participants/list.csv`)
2. Fix the LaTeX template `tex/template_top.tex` to your needs. The current template is for 8 badges of dimension 60mm x 90mm printed on perforated A4 paper
3. Run the python script
4. Run the bash script

## Python script usage

```bash
python create_badges.py 
```

Options:

```bash
  -h, --help            show this help message and exit
  -V, --verbose         increase output verbosity
  -i INFILENAME, --infilename INFILENAME
                        Input file name
  -o OUTFILENAME, --outfilename OUTFILENAME
                        Input file name
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter of the csv input file, by default ","
  -r REMOVEROWS, --removerows REMOVEROWS
                        Rows to be removed
  -b NBADGESPPAGE, --nbadgesppage NBADGESPPAGE
                        Number of badges per page
  -n NAMEKEY, --namekey NAMEKEY
                        Key for name field
  -a AFFKEY, --affkey AFFKEY
                        Key for affiliation field

```
