import os
import datetime

result = dir(os)
result = os.name
result = os.getcwd()

result = os.listdir("/home/kaang")


# result = os.listdir("/home/") # listing all the files under the home section

# for d in os.listdir("/home/kaang"):
#     if d.endswith('.tmp'):
#         print(d)

result = os.stat("dmodule.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # getting information(date) about when this file is created
# result = datetime.datetime.fromtimestamp(result.st_atime) # last access date  a stands for access
# result = datetime.datetime.fromtimestamp(result.st_mtime) # last modufied date  m stands for modufied

# result = os.system("file name") # opening an system file

result = os.path.abspath("_os.py") # get the detail file path

result = os.path.exists("_os.py") # there is a file called .... or not

print(result)