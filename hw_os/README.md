# <center>UNIX utilities in Python </center>

## Description

This repository is an attempt to make up some popular UNIX-commands in Python
without using subprocess module or external packages. All scripts were tested on __MacOS Monetery 12.01.01__ using __Python 3.9.0__  interpreter.

Here you can find the following utilities:

1) File <font size="4">__wc.py__</font> simulates <font size="4">wc</font> command. It works as original one wc command, it takes an argument as a path to file or take it
   from stdin by default, output sets by default as stdout, you can redirect it by adding __<big>'> filename'</big>__  to the end of the command.
   It can work in pipes and save. Simple example: 
   ```ls ~ | ./wc.py -c``` 
   The following options are available (all three work by default):
   - <font size="4">-l or --lines</font> – lines count
   - <font size="4">-w or --words</font> - words count
   - <font size="4">-c or --bytes</font> - bytes count 
   
2) File <font size="4">__ls.py__</font> works as original one <font size="4"> ls </font> command. It needs a path
to a folder/filer to show its content, by default it sets as '.' – current folder. It can work in pipes,
   and result can be redirected to a file by adding __<big>'> filename'</big> to the end of the command. Simple example ```./ls.py -a ~/Documents```
   It supports only one option:
   - <font size="4">-a</font> - to display all files including the hidden.
   
3) File <font size="4">__rm.py__</font> works as original one <font size="4">rm</font> command. It takes only one argument - path to a folder/file and remove it.
It can remove folders recursively. Simple example: ```./rm.py -r /System``` ( Don't try this at home:) ). It takes only one
   option:
   - <font size="4">-r</font> means remove all content recursively. 
   
4) <font size="4">__sort.py__</font>. It simply sorts file. It works as UNIX-command <font size="4">sort</font>.
It can work in pipes or redirect output to a file. Simple example: ```./ls.py | ./sort.py > sorted_ls.txt```. Unfortunately, It has no options.

5) <font size="4">__grep.py__</font>. It finds all matches in a text or in stdin, it is similar to <font size="4">grep</font>. It can work in pipes.
To now, it can work with regular expressions. To now(14.12) I couldn't color a matched text in terminal, I decided to make it UPPER, this is why it has some problems while finding upper case letter/words.  Simple example ```./grep.py aa test.txt```
   
6) <font size="4">__cat.py__</font>. This script simulates __cat__ UNIX-utility. I reads file and print its content to stdout by default.
You can redirect output to a file and also read from stdin. It works in pipes. Simple example: ```./ls.py | ./cat.py file.txt > new_file.txt```
   
7) <font size="4">__tail.py__</font>. It works as original one __tail__ UNIX-command. It takes input as a file or take it from stdin by default.
Output is in stdout by default, you can redirect it to a file by adding __>__ sign. Simple example: 
   ```./tail.py -n 10 text.txt > text_tail.txt```. It has one optional argument 
   - __-n__. Number of the lines to show. It is __impossible__ to omit __n__ while using
   our command with this option (e.g ./tail -5 - won't work). By default n=10
     
8) <font size="4">__mkdir.py__</font>. This command simply create a directory in the path it took, works as __mkdir__ UNIX-utility. It can create subdirectories.
Simple example: ```./mkdir.py -p ~/Documents/new_folder/subfolder1```. It has an additional option:
   - __-p__ allows creating intermediate directories. 
   
9) <font size="4">__ln.py__</font>. This command works as UNIX __ln__ utility. It creates hardlink by default. It takes input as a file,
and output as a path to a link. Simple example: ```./ln.py -s ~/Documents/text.txt ~/Downloads/t.txt``` It has one optional argument:
   - __-s__ creates a symlink. 
   
10) <font size="4">__cp.py__</font>. This command copies files or a directories to a destination. It takes two required argumens:
input as a file/directory and output as path where to save a file/directory. Generally it works as __cp__ UNIX-command.
    Simple example: ```./cp.py -r dir ./new_dir```
    It has one optional argument:
    - __-r__ allows copying directories.
   
11) <font size="4">__mv.py__</font>. It works as original one __mv__ UNIX-command. It moves a file or a folder from input to
output path. Often it is used just to rename a file/folder.
    
12) <font size="4">__uniq.py__</font>. This script works as original one __uniq__ UNIX-utility. It takes an argument as a file,
or takes it by default as stdin. Output by default set to direct to stdout, you can redirect it wit __">"__ sign. It can work in pipes
    but it has some problems while using in pipes with __head__ command: __the broken pipe__ error appears (Idk why). Simple example ```./uniq.py -u test.txt```
    It has one option:
    - __-u__ means to display only unique lines in a whole file. By default it displays unique neighbors. 
   
## The installation guide
If you want to install this project to your own machine follow these simple steps:
- clone this repository 
```
  git clone https://github.com/keyreallkeyrealenko/UNIX_utilities.git
  ```
- create virtual environment in a current directory and call it __venv__. 
```
python3.9 -m venv venv
```
  
- activate virtual environment 
```
source venv/bin/activate
```
  
- make the scripts executable: ```chmod + x *.py```
  
- and use these scripts as written above

## NOTES 

1) If you want to add all the scripts to PATH variable just run script __install.py__ inside active environment.
Use this command if you're in the directory where all the scripts are located:
   ```
   ./install.py
   ```

2) Many scripts have some problems with __head__ UNIX-utility in pipes. For example:
```cat.py test.txt | head``` It will work but in the end it will raise and error: __Broken pipe__.
   

   
