#6
def driver(speed):
    if speed <= 70:
        print("OK")
    elif speed > 70:
        local = speed - 70
        x =local//5
        print("points ",x)
        if x>=12:
            print("License suspended")

print(driver(70))

#7
def showNumbers(limit):
    for i in range(0,limit+1):
        if(i%2==0):
            print(i,"EVEN")
        else:
            print(i,"ODD")

print(showNumbers(3))

#8
def function(limit):
    sum =0
    for i in range(1,limit+1):
        if(i%3==0 or i%5==0):
            sum =sum+i

    print(sum)

print(function(20))

#9
def show_stars(rows):
   for i in range(0,rows):
       for j in range(0,i+1):
           print("*",end ="")
           
        print("\r")
print(show_stars(5))

#10
def isPrime(limit):
    if(limit==1 or limit==0):
        return False
    for i in range(2,limit):
        
        if(limit%i==0):
            return False
        return True

limit = 100
for i in range(1,limit+1):
  if(isPrime(i)):
    print(i,end=" ")










