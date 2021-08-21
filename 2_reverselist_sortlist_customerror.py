lst=['C++','Python','Java','SQL','PHP','.NET']
print('Main List= ',lst)
#Reverse a List:
print('After Reverse= ',lst[::-1])
######################

#Sort a list:
for i in range(len(lst)):
    for j in range(i , len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print('After Sorting= ',lst)
#####################

#Create a CustomError:
class CustomError(Exception):
    def __init__(self, msg):
        self.msg=msg
    def show(self):
        return self.msg

#Check Eligibility:
print('Check Eligibility:')
marks=int(input("Enter your total marks out of 800: "))
try:
    if (marks>=480 ):
        print('You are eligible in this course')
    else:
        raise(CustomError('Your are not eligible in this course'))
except CustomError as error:
    print('CustomError: ',error.msg)
