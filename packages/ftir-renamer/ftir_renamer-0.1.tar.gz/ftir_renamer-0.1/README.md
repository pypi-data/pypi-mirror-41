FTIR File Renamer
==============
### Introduction

Renames files from the FTIR based on strict naming scheme

### Installation

From the command line in the folder in which you would like to install the program:

`pip install ftir_renamer`

### Requirements
- Unix-like environment
- Spreadsheet of FTIR-related metadata
- The .FTIR output files corresponding to the FTIR IDs in the spreadsheet

### Required Arguments

-s
The path of the folder containing the FTIR output files
-f 
Absolute path to the spreadsheet containing the FTIR metadata
-o
The absolute path of the folder to store the renamed files

### Running 

##### Example command to run the script

`renamer.py -f /path/to/FTIR.xlsx -s /path/to/files -o /path/to/outputs`
    
##### Usage

```
usage: renamer.py [-h] -s SEQUENCEPATH -f FILENAME -o OUTPUTPATH

Rename files for FTIR experiments using strict naming scheme

  -h, --help            show this help message and exit
required arguments:
  -s SEQUENCEPATH, --sequencepath SEQUENCEPATH
                        Path of .spc files to process.
  -f FILENAME, --filename FILENAME
                        Name of .xls(x) file with renaming information. Must
                        conform to agreed upon format (see README for
                        additional information). This file must be in the
                        path.
  -o OUTPUTPATH, --outputpath OUTPUTPATH
                        Optionally specify the folder in which the renamed
                        files are to be stored. Provide thefull path e.g.
                        /path/to/output/files
```
