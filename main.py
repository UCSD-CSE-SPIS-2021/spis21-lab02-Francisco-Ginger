

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


# Step 4
# created a list of int values called wagelist
# wagelist[0] is the wage gap for the US, wagelist[1] is the wage gap for Mexico, and wagelist[2] is the wage gap for Canada
wagelist = [.182, .161 , .096];
# The function below takes two arguments of value int and string below
def convertWageMtoW(mWage, country):
  wageGap = 0;
  # I used an if elif elif statement and .lower() prewritten method to compare what the user types
  if country.lower() == "usa":
     wageGap = wagelist[0]
  elif country.lower() == "mexico":
     wageGap = wagelist[1]
  elif country.lower() == "canada":
     wageGap = wagelist[2]
   
  # Calculates the ratio
  ratio = 1 - wageGap

  # Calculates the wage of the Women
  return mWage * ratio

print(convertWageMtoW(100, "USA"))

print(convertWageMtoW(100, "Mexico"))

print(convertWageMtoW(100, "Canada"))
