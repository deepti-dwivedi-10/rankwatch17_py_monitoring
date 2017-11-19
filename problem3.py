import psutil #cross-platform python library for retrieving information on running processes & system utilization
import time #provides various time related functions
import threading #for multithreading

def find_usage():
    threading.Timer(5.0, find_usage).start() #creating the timer
    print "Current Usage"
    print psutil.cpu_percent() #to get CPU usage
    print psutil.virtual_memory() #to check virtual memory usage
    print psutil.disk_usage('/') #for disk usage

def find_usage_30sec(): #function for checking the usage in last 30 seconds
    threading.Timer(30.0, find_usage_30sec).start() 
    print "Usage in last 30 seconds"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

def find_usage_1min(): #function for checking the usage in last 1 minute
    threading.Timer(60.0, find_usage_1min).start()
    print "Usage in last 1 minute"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

def find_usage_5min(): #function for checking the usage in last 5 minutes
    threading.Timer(300.0, find_usage_5min).start()
    print "Usage in last 5 minutes"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

#function calls
find_usage() 
find_usage_30sec()
find_usage_1min()
find_usage_5min()

#creating threads
thread.start_new_thread(find_usage,())
thread.start_new_thread(find_usage_30sec,())
thread.start_new_thread(find_usage_1min,())
thread.start_new_thread(find_usage_5min,())