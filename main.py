
# Step 1

def sumTwo(a,b):

   c = a + b

   return c

x = sumTwo(3,5)

print(x)

# Step 2

def getNumber():
  answer = ""  
  symbols = input("Enter a digit: ")
  number = int(symbols)
  while number >= 0:
    answer += symbols
    symbols = input("Enter a digit: ")
    number = int(symbols)
  return answer

print (getNumber())


# Step 3
# Return the sum of the digits of a number
def sumDigits(x):
    far_right = x % 10 #get furthest right digit
    left_number = x // 10 #left most digits
    answer = 0
    while left_number > 0: #runs through each digit
      answer += far_right
      far_right = left_number % 10 
      left_number = left_number // 10
    answer += far_right #for last digit won't run
    #loop so need to add that digit outside loop
    return answer

print(sumDigits(588))



# Step 3 (Recursion)
def sumDigits(x):
  if x < 10:
    return x
  else:
    return x % 10 + sumDigits(x  //10)
x = 236
print(sumDigits(x))

