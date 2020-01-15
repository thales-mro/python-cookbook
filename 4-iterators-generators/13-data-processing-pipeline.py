import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    """
    Find all filenames in directory tree which corresponds to a shell wildcard pattern
    """
    for path, dirlist, filelist in os.walk(top):
        print(path, dirlist, filelist)
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    """
    Open a sequence of filenames, one by one, generating a file object. The file will be immediately closed when the next iteration has started
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    """
    Chains a sequence of iterators into a unique sequence
    """
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    """
    Looks for a regex pattern into a line sequence
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

def main():
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)

if __name__ == "__main__":
    main()