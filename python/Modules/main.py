#import module
# different ways to import modules
from module import student # only import student section
from module import student,sum 
from module import *
import module as m

result = m.student["exam_notes"]

result = m.sum(10,20)
print(result)