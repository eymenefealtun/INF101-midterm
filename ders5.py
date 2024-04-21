# Write a recursive function to find the sum of first n natural numbers.
# Q1

def Sum(a):
  if a==1:
    return 1
  return a+Sum(a-1)

print(Sum(3))

# Q2
def power(a,b):
  if b==0:
    return 1
  return a*power(a,b-1) # 5,2 5,1 5,0
###### Main Code ####
x=5
y=2
print(power(x,y))


#Q7 Write a recursive function for reversing a list
def reverse(list):
  if len(list) <=1:
    return list
  else:
    temp=reverse(list[1:])
    temp.append(list[0])

    return temp
########## Main Code ###########
L=[2,3,5,6,7,8,4]
print(reverse(L))


#Q8 Write a recusrive function for reversing a string
def str_rev(s):
  if len(s)==1:
    return s
  return str_rev(s[1:])+s[0]
####### Mani Code ############
x='ab123'
print(str_rev(x))
