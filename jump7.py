# jump int with 7 between 1 and 100
# program language : python3
# author : vic
# date : 2020 Feb 20
# email : capricorn90@foxmail

__author__ = 'vic'

for i in range(1,101):
    if i%7 == 0:
        continue
    elif i//10 ==7:
        continue
    elif i%10 == 7:
        continue
    else:
        print(i)
