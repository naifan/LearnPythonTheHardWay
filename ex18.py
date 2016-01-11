# this one is like your scripts with argv
def print_two(*args):
    argv1, argv2 = args
    print "argv1: %r, argv2: %r" % (argv1, argv2)
    
# Ok. that *args is actually pointless, we can just do this.
def print_two_again(argv1, argv2):
    print "arg1: %r, argv2: %r" % (argv1, argv2)
    
# this just takes one argument
def print_one(argv):
    print "arg1: %r" % argv
    
# this one takes no arguments
def print_none():
    print "I got nothing."
    
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()