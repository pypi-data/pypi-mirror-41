# Compare Microsoft Spreadsheet Files

Look for instances of plagiarism. 

* Compare file meta data [default]
    * File creation time stamp
    * File modification time stamp
    * Author of file creation 
    * Author of last modification of file
* Cell values [optional]
    * Non-formula strings
    * Cell-by-cell values
* Cell layout [optional]
    * Check locations of filled/unfilled cells

Spreadsheet files must be of type `.xlsx`

Results are saved to spreadsheet. 

# Installation and Setup

To install run `pip install --user compsheet` from the terminal. 

To run type 

```bash
python3 -m compsheet
```

followed by the various inputs and flags. It is recommended that the user establish the alias `compsheet` for easy usage. 
To do this, edit the file `.bashrc` from the home directory and add the line 

```bash
alias compsheet='python3 -m compsheet'
```

to the end. One can do this in their favourite editor or simply open a terminal and type 

```bash
echo "alias compsheet='python3 -m compsheet'" >> .bashrc
```
into the prompt and press enter. 

# Some examples of usage:

```bash
# basic usage
python3 -m compsheet    # show help message with no alias
compsheet -h            # show help message with alias set to "compsheet"
compsheet --explain     # print description of table headers
compsheet               # compare all files in current directory

# example compbining various switches
compsheet -v -n 4 -t -o "meta,exact,string" ./dir 
   # [-v]      verbose output: print names of files as they are compared (default: quiet)
   # [-n]      use x processors in multiprocessing                       (default: 1)
   # [-t]      print table summary to stdout                             (default: off)
   # [-o]      do additional optional comparisons                        (default: "meta")
   # [./dir]   path to directory                                         (default: ".")
```
