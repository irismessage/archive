from time import time, localtime, struct_time, mktime

epoch = time()
date = localtime(epoch)

if date[1] == 12 and date[3] == 25:
    print("It's christmas!")
else:
    christmas = struct_time(tm_year=date[0], tm_mon=12, tm_mday=25)
    c_epoch = mktime(christmas)
    difference_seconds = c_epoch - epoch
    difference = timedelta(seconds=difference_seconds)
    eves = difference.days
    print("It's christmas{}!".format(" eve"*eves))
    
    

