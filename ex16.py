from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want to do that, hit CRTL-C (^C)."
print "If you do want that, hit RRTURN."

raw_input("?")

print "Openning the file..."
target = open(filename, 'w')

print "Truncating thr file. Goodbye!"
target.truncate()

print "Now I'm going to ask you 3 lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
#target.write("{0}\n{1}\n{2}\n".format(line1, line2, line3))
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()
