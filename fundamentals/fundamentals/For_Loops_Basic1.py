#-------1.Basic - Print all integers from 0 to 150.-------------------
"""
for i in range (0,151):
    print(i)
"""
#-------2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000--------
"""
for x in range (5,1001,5):
    print(x)
"""
#------3.Counting, the Dojo Way - Print integers 1 to 100---------------
"""for i in range (0,101):
    if (i%10==0):
        print("Coding Dojo")
    elif (i%5==0):
        print("Coding")
    else:
        print(i)
"""
#------4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.---
"""
x=0
for i in range(0,500001):
    x=x+i
print(x)
"""
#-----5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.---
"""
for i in range(2018, 0, -4):
    print(i)
"""
#----6.Flexible Counter - ---------------
lowNum=2
HighNum=9
mult=3
for i in range(lowNum,HighNum+1):
    if(i%mult==0):
        print(i)
