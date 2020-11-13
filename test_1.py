"""

The Program is trying to determine which payment option makes more money therefore more beneficial.
Option 1 offers $100 a day for ten days.
Option 2 offers $1 a the first day, $2 the second, as every consecutive day the pay doubles to the tenth day. 
Two functions will be needed to calculate the first and second option.
As function1 will calculate option 1 and function2 will calculate option 2.

Function1 will output $100 * 10 days
Function2 will loop 10 times with each time doubling the dollar amount and then adding it to the total. 

if the amount is equal we ouput to the user that "option1 and2 are the same".

if option1 is better (makes more money) than option2, we will output "option1 is better".

if option2 is better (makes more money) than option2, we will output "option2 is better".


"""

"""

#option1
 return 100 * 10


#option2
 amount = 1 
 list1 = []
 loop 10 times
   add amount to list1
   amount *=2
sum = sum of all items in loop
return sum
#main
if  var1 = var2
    "Option 1 and Option 2 pay the same"
if var < var2 
  "Option 2 is better"
else 
  "Option 1 is better"

main


"""

def option1():
  return 100*10

def option2():
    amount = 1
    list1 = []
    for i in range(0,10):
      list1.append(amount)
      amount *= 2
    total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option1() #1000
    var2 = option2() #1023
    if var1 == var2:
      answer = "Option1 and Option 2 pays the same"
    elif var1 < var2:
      answer =  "Option 2 is better"
    else:
      answer =    "Option 1 is better"
    print(answer)


main()
