import os
import shutil
import fnmatch

def gen_find(filepath,top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepath):
            yield os.path.join(path,name)

# Example use

if __name__ == '__main__':
    src = '/mnt/c/Users/chase.hudson/Desktop/fleet_offers_copy'
    dst = '/mnt/c/Users/chase.hudson/Desktop/fleet_offers_excel'

    filesToMove = gen_find("*.xlsx",src)
    for name in filesToMove:
        shutil.move(name, dst)
        print(len(os.listdir('fleet_offers_excel')))
