import time

def getTime(fxn):
    def timeThing(*arg):
        start = time.time()
        runFunc = fxn(*arg)
        end = time.time()
        print "Time: %s" % (str(end-start))
        return runFunc
    return timeThing

def getName(fxn):
    def nameThing(*arg):
        print "Function: %s" % (fxn.func_name)
        print "Args: %s" % (str(arg))
        return fxn(*arg)
    return nameThing

@getTime
@getName
def adder(x,y):
    return str(x + y) + " -- Daniel wuz here"

print adder(4,5)
