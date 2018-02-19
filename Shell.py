#Rhody Kaner and Emmett Kahn

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
        elif words[0] in ('exit', 'quit'):
            break 
        elif words[0] in ('ls', 'dir'):
            a = ""
            for item in os.listdir(os.getcwd()):    #concatenates string representations of each item in current directory
                a = a+" "+str(item)               
            print(str(a))                           #prints the string containing every item in directory
        elif words[0] == 'cat': #doesn't work properly
            if os.path.isfile(words[1]):            #reads through a file and concatenates and displays its lines 
                ret = ""
                for word in words[1:]: #this code crashes the program. Bug tests have thus far rendered no helpful data. 
                    os.open(str(word),1) #errors indicate there should be some flag after the first, and it should be an integer. Why does 1 work? what does it mean?
                    lines = os.read(word, 1024) #this line is wrong, we thought os.readlines() worked and turns out it doesn't exist -E
                    a = ""  #in theory, these lines should be fine if I can get the ones before it to work. 
                    for line in lines:
                       a = a+"/n"+str(line)
                       print(a)
                    ret = ret + a + "\n"
                    if words[2] == None:
                       x = open(str(words[1:])+"+w")
                       x.write(ret)
                       x.close()
            else:
                print("Sorry, that is not a file") #displays the contents of the file               
        elif words[0] == 'mkdir':
            os.mkdir(words[1])                      #creates new empty directory with given name
        elif words[0] == 'touch':
            x = open(str(words[1]), "+w")           #creates new empty file with user write access
            x.close()
        elif words[0] == 'cd':
            if len(words) == 1:
                os.chdir("/")                       #if no argument is given, moves to the root
            else:
                os.chdir(words[1])                  #otherwise, moves to the given directory
        elif words[0] == 'echo': 
            a = ""
            for word in words[1:]:
                a = a+" "+str(word)                 #concatenates anything typed after "echo" and prints the resulting string
            print(str(a))
        elif words[0] == 'pwd':
            print(os.getcwd())                      #prints the current path
        else:
            print("unknown command {}".format(words[0]))
        sys.stdout.write(prompt)
        sys.stdout.flush()

    # all done, clean exit
    print("bye!")

assert sys.version_info >= (3,0), "This program requires Python 3"

if __name__ == '__main__':
    repl()
