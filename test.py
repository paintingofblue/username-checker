import datetime

time1 = str(datetime.datetime.now()).split('.')[0].replace(":", "-")
print(time1)