# Example of Walk Function
# Finds matching files in directories
# Uses Walk to search directories recursively

# usage:
#   python ProblemB.py [dir][numBytes]

import os, sys

class fileDirectory:
    file_ptrs = {}
    pairs = []

    def __init__(self):
        'Constructor'

    def add(self, file):
        f = open(file, 'rb')

        # Adds files to dictionary
        # form: {path : ptr}
        fileDirectory.file_ptrs[file] = f

        tmp = f.read(int(fd.nBytes))

        #Iterate over the file pointers
        for itr in fileDirectory.file_ptrs.iteritems():
            itr[1].seek(0)
            if itr[1].read(int(fd.nBytes)) == tmp \
                and file != itr[0]:
                # Match Found Add to Pair
                t = (itr[0], file)
                fileDirectory.pairs.append(t)


#Global Object
fd = fileDirectory()

# Pairs: List of Touples of matching files
# dr: current directory
# flist: files in current directory
def getlocaldata(rdir, dr, flist):

    for f in flist:

        # get full path name relative to program start
        # function join adds path delimiter
        fullf = os.path.join(dr, f)

        # Relative Path
        rpath = os.path.join(rdir, f)

        if os.path.islink(fullf): continue # don't count linked files
        if os.path.isfile(fullf):

            fd.add(fullf)

        else:
            i = 0

def filePairs(dtree, nBytes):

    fd.nBytes = nBytes

    # Extract root directory as relative
    rdir = rPath(dtree)

    os.path.walk(dtree, getlocaldata, rdir)

    return fd.pairs

def rPath(root):
    out = ''
    for c in reversed(root):
        if c != '/': out += c
        else: break
    return ''.join(reversed(out))

def main():
    try:
        root = sys.argv[1]
        nBytes = sys.argv[2]
    except:
        root = '.'
        nBytes = 0
    report = filePairs(root, nBytes)
    print report


if __name__ == '__main__': main()