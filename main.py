import time 


def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    
    print('Timers up') 



t = 10 #ammount of time, t = number of seconds :)


countdown(int(t))
