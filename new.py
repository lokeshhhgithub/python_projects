from time import *

def mistake(paratest , usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest:
                error = error + 1
        except:
            error = error + 1
    return error

def time_taken(ftime, ltime, test_time):
    real_time = ltime - ftime
    time_r = round(real_time,2)
    speed = len(test_time) / time_r
    return round(speed)



test = ['Hello this is lokesh dhakal. I am from kailali']

print('******  Typing Speed  *****')
print(test)
print('\n\n')
time1= time()
testinput = input('Enter : ') 
time2 = time()
print('Your Time is: ', time_taken(time2, time1,testinput))





