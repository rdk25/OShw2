import sys
import os
import fileinput

class Shell:
    """ Simple Python shell """

def repl():
    prompt = '> '
    cmd = ''
    sys.stdout.write(prompt)
    sys.stdout.flush()
    for line in sys.stdin:
        words = line.split()
        if len(words) == 0:
            pass
        elif words[0] == newfs:
            if words[3] == None:
                FS = FileSystem.createFileSystem(words[1],words[2])
            else:
                FS = FileSystem.createFileSystem(words[1],words[2])
            Blockdevice.close() #IDK IF THIS IS RIGHT - ASK DYLAN??????????????????????????
            
        elif words[0] == mount:
        
        elif words[0] == blockmap:
            i = 0
                map = ""
                for block in BLOCKMAP??????????????????????????????
                    if i == 64:
                        print(map)
                        map = ""
                    if i%7 == 0:
                        map = map + "|"
                    map = map + str(block)
                    i += 1
                print(map)                          
            
        elif words[0] == alloc_block:
            BlockMap.alloc_block(blockdevice)?????????????????????
        
        elif words[0] == free_block:
            
        elif words[0] == inode_map:
            for inode in
            
        elif words[0] == alloc_inode:
        
        elif words[0] == free_inode:
            
            
        elif words[0] in ('exit', 'quit'):
            break
        elif words[0] in ('ls', 'dir'):
            print("show current directory's contents")
        elif words[0] == 'cat':
            print("if argument is a file, print it, else report a nice error")
        elif words[0] == 'mkdir':
            print("create an empty directory goes here")
        elif words[0] == 'touch':
            print("create an empty file goes here")
        elif words[0] == 'cd':
            print("cd implementation goes here")
        elif words[0] == 'echo':
            print("echo implementation goes here")
        elif words[0] == 'pwd':
            print("pwd implementation goes here")
        else:
            print("unknown command {}".format(words[0]))

        sys.stdout.write(prompt)
        sys.stdout.flush()

    # all done, clean exit
    print("bye!")

assert sys.version_info >= (3,0), "This program requires Python 3"

if __name__ == '__main__':
    repl()
