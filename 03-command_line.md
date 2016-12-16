# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. pwd - "print working directory"; gives current directory
> > 2. rmdir - remove directory
> > 3. touch - make an empty file
> > 4. cat - shows the file
> > 5. rm - removes a file
> > 6. mv - moves a file or directory, can also be used to rename a file
> > 7. cp - copies a file to current directory or a specified one
> > 8. Wildcard matching * - can be used to find files with a specified criteria
> > 9. man - get the manual/help for a command
> > 10. echo - writes arguments to standard output

---

###Q2.  List Files in Unix

What do the following commands do:
`ls`
`ls -a`
`ls -l`
`ls -lh`
`ls -lah`
`ls -t`
`ls -Glp`

> > ls - lists directory contents
> > -a - include diectory entries whose names begin with a dot
> > -l - list in long format
> > -lh - long format and uses unit suffixes byte, kilobyte, etc. to reduce number of digits
> > -lah - includes entries that begin with a dot and uses unit suffixes and in long format
> > -t - sort by time modified
> > -Glp - enable colorized output, long format, and writes slash after each filename if it's a directory

---

###Q3.  More List Files in Unix

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 1. -1 - displays each entry on a line
> > 2. -F - flags filenames
> > 3. -L - displays file/directory referenced by a symbolic link
> > 4. -o - long format but without group name
> > 5. -q - displays nonprinting characeters as ?

---

###Q4.  Xargs

What does `xargs` do? Give an example of how to use it.

> > Used to build and execute command lines from standard input. Can be used to manage pipe, funnels in output of one command into another one by one so that it is readable by second command.
> > Example: find /path -type f -print | xargs echo -- would print out each file in the path



