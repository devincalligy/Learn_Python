from sys import argv
import os
from os.path import exists

script, from_file, to_file = argv

prompt = "~~~ "


print 'Copying from %s to %s' % (from_file, to_file)

#we could do these two on one like too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)
print "Does the output file exist? %s" % exists(to_file)

if exists(to_file) == True:
    print "It looks like we already have this file, would you like to make an additional copy?"
    results = raw_input("Type yes or no." + prompt)
    if results == 'yes':
        print "Ready, hit RETURN to continue."
        raw_input(prompt)
        out_copy = open(to_file, 'w')
        os.rename(out_copy, "copy.txt")
        out_copy = "copy.txt"
        if os.path.isfile(out_copy):
            expand = 1
            while True:
                expand += 1
                new_file_name = out_copy.split(".txt")[0] + str(expand) + ".txt"
                if os.path.isfile(new_file_name):
                    continue
                else:
                    file_name = new_file_name
                    break
    elif results == 'no':
        print "No worries, hit RETURN to abort."
        raw_input()
        print "smell ya later"
        exit()
    else:
        print "Oh, geez. Just shut the whole computer down, you've broke me."

if exists(to_file) == False:
        print "Ready, hit RETURN to continue, CTRL + C to abort."
        raw_input(prompt)
        out_file = open(to_file, 'w')
        out_file.write(indata)
        out_file.close()
        in_file.close()
        print "Alright, all done."