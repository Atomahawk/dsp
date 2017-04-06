# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > * `pwd` show current working directory path  
* `mkdir <directory name>` creating a directory
* `rm -r <directory name>` deleting a directory (& all its files).  Also, `rmdir <directory>`
* `touch <filename>` creates a file using `touch` command
* `rm <rm <file_name_1>` deletes a file
*  `mv <file_name_1> <file_rename>` (move) renames a file
* `ls -a`listing hidden files
* `cp <file_name_1> <directory>`copying a file from one directory to another
* `pushd <directory to go to>` takes your current directory and "pushes" it into a list for later, then it changes to another directory. It's like saying, "Save where I am, then go here.
* `popd` takes the last directory you pushed and "pops" it off
* `ctrl-c` interrupts terminal process

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`  - lists files in directory;
`ls -a`  - lists all files, including hidden files;
`ls -l`  - lists all files in long form;
`ls -lh`  - lists files in long form using unit suffixes;
`ls -lah`  - lists all files (including hidden files) in long form using unit suffixes;
`ls -t`  - lists files, sorted by time modified;
`ls -Glp` -lists files in long form, colorized, with '/' after each directory;

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * `ls -m` comma separates the list 
* `ls -lc` long form with timestamp
* `ls -d` displays only directories
* `ls -r` reverses the order
* `ls -1` displays each entry on a line 

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > The `xargs` command (by default) expects the input from stdin, and executes /bin/echo command over the input. When we combine `xargs` with other commands, we can pass new inputs into xargs to chain commands together.  One example is `find . -name "*.txt" | xargs rm -rf` which searches for all text files, passes it into xargs, and continues to execute rm over the text files.

 

