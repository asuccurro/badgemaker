#!/usr/bin/python3
#**************************************
#**    author: Antonella Succurro    **
#**email:asuccurro[AT]protonmail.com **
#**                                  **
#**    created:       2019/12/11     **
#**    last modified: 2019/12/11     **
#************************************

import json
import argparse
import csv
import random
import string
#import unidecode

def main():
    '''
    Reads csv file containing among others the columns "namekey" (string with Title, Name, Surname) and "affkey" (string with Affiliation)
    Produces LaTeX files with N=nbadgesppage boxes with the name and affiliation of the entry
    '''

    args = options()
    infilename = args.infilename
    outfilename = args.outfilename.split('.')
    delimiter = args.delimiter
    removerows = [int(i) for i in args.removerows.split(' ')]
    nbadgesppage = int(args.nbadgesppage)
    namekey = args.namekey
    affkey = args.affkey

    with open(infilename) as infile:
        csvr = csv.reader(infile, delimiter=',')
        l = 0
        c = 0
        ofile = open(f"{outfilename[0]}_1.{outfilename[1]}", 'w')
        for row in csvr:
            if l < 1:
                kn = row.index(namekey)
                ka = row.index(affkey)
            elif l in removerows:
                print(f"Line {l} is to be removed: {row}")
            else:
                c += 1
                if c % nbadgesppage == 0:
                    ofile.close()
                    ofile = open(f"{outfilename[0]}_{int(c/nbadgesppage)+1}.{outfilename[1]}", 'w')
                ofile.write(f"\\myboxI{{\\huge {row[kn]}\\\\[1ex]\\Large {row[ka]} }}\n")
            l+=1

    if c % nbadgesppage > 0:
        ofile.close()
    
    return

def options():
    '''in-line arguments read by the parser'''
    parser = argparse.ArgumentParser(description='Parsing options')
    parser.add_argument('-V', '--verbose', help='increase output verbosity', action='store_true')
    parser.add_argument('-i', '--infilename', help='Input file name', default='participants/list.csv')
    parser.add_argument('-o', '--outfilename', help='Input file name', default='tex/page.tex')
    parser.add_argument('-d', '--delimiter', help='Delimiter of the csv input file, by default ","', default=',')
    parser.add_argument('-r', '--removerows', help='Rows to be removed', default='')
    parser.add_argument('-b', '--nbadgesppage', help='Number of badges per page', default='8')
    parser.add_argument('-n', '--namekey', help='Key for name field', default='name-and-surname')
    parser.add_argument('-a', '--affkey', help='Key for affiliation field', default='affiliation')
    args = parser.parse_args()
    if args.verbose:
        print('Verbosity ON')
        print(args)
    return args

if __name__=="__main__":
    main()
