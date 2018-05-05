#!bin/bash

/************ Instructions *************/

The first thing your bash script should do is to print the number of
files per directory ( extra points if you show it in a graph with gnu
plot). Something like this ( fake numbers are used )

# Documentation = 1234 files
# arch = 789 files
# block = 876 files

c) What files exist in the Kernel Source code? Let's make your BASH
script print this information as:

# Number of README* (files as README.Locking also count)
# Number of Kconfig files
# Number of Kbuild files
# Number of Makefiles files
# Number of .c files
# Number of .h files
# Number of .pl files
# Number of others files

Total number of files =

d) How many times the library " #include <linux/module.h>" appears in
all the C and H documents you found? Let's make your BASH script print
that:

# Number of times the " #include <linux/module.h>" appears =

e) Copy all the C and H files to these directories

C_FILES
H_FILES

f) Count the number of files in these directories, they should be the
same as the ones we count in section C right? :

# Number of .c files
# Number of .h files


/***************** Write down in the bash  *******************/



find . -type d -print0 | while read -d '' -r dir; do
       files=("$dir"/*)
       printf "%5d files in directory %s\n" "${#files[@]}" "$dir"
done

printf 'number of README:'
find -name *README | wc -l
printf 'number of Kconfig files:'
find -name *Kconfig | wc -l
printf 'number of Kbuild files:'
find -name *Kbuild | wc -l
printf 'number of Makefiles:'
find -name *Makefile | wc -l
printf 'number of C files:'
find -name *.c | wc -l
printf 'number of H files:'
find -name *.h | wc -l
printf 'number of PL files:'
find -name *.pl | wc -l

for file in $(find . -type f);do
       if grep -q "#include <linux/module.h>" $file
       then
       buscarLibreria=$((buscarLibreria+1))
       fi

done

printf 'Archivos que contienen #include <linux/module.h>: %d' "$buscarLibreria"
mkdir -p C_FILES
mkdir -p H_FILES

for fh in $(find -name *.h); do cp $fh H_FILES; done;

for fc in $(find -name *.c); do cp $fc C_FILES; done;

cd H_FILES
printf 'number of H files:'
find -name *.h | wc -l
cd ..
cd C_FILES
printf 'number of C files:'
find -name *.c | wc -l


