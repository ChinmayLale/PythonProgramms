# Program to check the status of student pass or fail
print('Enter Your 5 subject marks out of 100')
s1 = int(input('1.Science : '))
s2 = int(input('2.Maths : '))
s3 = int(input('3.Sanskrit : '))
s4 = int(input('4.History : '))
s5 = int(input('5.Geography : '))
tot  = s1+s2+s3+s4+s5
per = (tot/500.0)*100
print('Percentage required for passing - 37 % \nYou got : ' +str(per)+'%')
if per >= 37:
    print('Congrats You are passed in exams ')
else:
    print('Better Luck next time ')
