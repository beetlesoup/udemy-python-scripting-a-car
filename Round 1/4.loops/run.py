from browser import document, window, alert
from browser import timer
window.indexedDB.deleteDatabase('brython_stdlib')
print("hello world!")
env = window.env

######################
# Start Learning Here
######################

def sleepTime(time):
    timeLock = False
    def someFunction():
        timeLock = True

    timer.set_timeout(sleepTime, 3000)    
    while timeLock == False:
        continue
    
    print("Finished after 3 seconds")

def Move100StepsForward():
    numberOfTimes = range(100)
    for everySingleNumberInTheRange in numberOfTimes:
        print(everySingleNumberInTheRange)
        sleepTime(1)
        env.step(0)

Move100StepsForward()


#######################
# End Learning Here
#######################
