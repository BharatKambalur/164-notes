# Large header  
## Smaller header  
  
Some text. **Some bold text**. *Some italic text*. Here is a bullet list:  
  
* Item 1  
* Item 2  
  
<table>  
  <tr>  
    <td>This is a table...</td>  
    <td>...created with HTML</td>  
  </tr>  
</table>  
  
And this is a LaTeX equation: $L=4\pi\sigma R^{2} T^{4}$.


####################################################################


print "Hello world!"


####################################################################


2                       # Outputs 2  
2 + 2                   # Outputs 4  
2 * 3                   # Outputs 6  
4 / 2                   # Outputs 2  
5 / 2                   # Outputs 2 (!!)  
float(5) / float(2)     # Outputs 2.5  
5.0 / 2                 # Outputs 2.5  
'Hello'                 # Outputs 'Hello'  
'Hello' + 'World'       # Outputs 'HelloWorld'  
'Hello' * 3             # Outputs 'HelloHelloHello'  


####################################################################


2 + 2                    # Outputs 4  
str(2) + str(2)          # Outputs 22  
'2' + '2'                # Outputs 22  
int(2.6) + float('3.5')  # Outputs 5.5  
3 ** (2 + 2)             # Outputs 81  
str(int(1e20 + 2))       # Outputs '100000000000000000000'  
str(int(1e20) + 2)       # Outputs '100000000000000000002'  
1+5j * 3                 # Outputs (1+15j)  
(1+5j).imag              # Outputs 5.0



####################################################################


a = 2  
b = 6  
c = a * b + a  
print c, float(c), complex(c)  


####################################################################


def square_root(x):  
    result = x ** 0.5  
    return result  
  
print square_root(1), square_root(2), square_root(3)  


####################################################################


def solve_quadratic(a, b, c):  
    """Solves a*x**2 + b*x + c = 0 and returns both roots"""  
    d = b**2.0 - 4 * a * c  
    d = complex(d)  
    x1 = (-b + d**0.5) / (2*a)  
    x2 = (-b - d**0.5) / (2*a)  
    return x1, x2  
  
print solve_quadratic(1, 1, 0), solve_quadratic(1, 0, 2)  


#####################################################################


a = -2+1j  
  
# Check if a is purely real  
a = complex(a)  
if a.imag == 0:  
    print "a is purely real"  
a = a.real  
  
# Check if a is between 5 (inclusive) and 10 (exclusive)  
if a >= 5 and a < 10:  
    print "a is between 5 and 10"  
else:  
    print "a is not between 5 and 10"  
  
# Check if a is positive, negative or 0  
if a > 0:  
    print "a is positive"  
elif a < 0:  
    print "a is negative"  
else:  
    print "a is neither positive nor negative"  
    print "So it is probably zero"  



#####################################################################



1 == 2                        # False  
1 != 2                        # True  
not (1 == 2)                  # True  
(1 != 2) and (1 != 3)         # True  
(1 == 2) and (1 != 3)         # False  
(1 == 2) or  (1 != 3)         # True  
(not (1 == 2)) and (1 != 3)   # True  



#####################################################################


if 42:  
    print "Python thinks that 42 is True"  
  
if 'Area 51':  
    print "Python thinks that Area 51 is True"  
      
if not 0:  
    print "Python thinks that 0 is False"  
  
if not "":  
    print "Python thinks that an empty string is False"  



#####################################################################


i = 1  
while i <= 10:  
    print i  
    i += 1


#####################################################################


i = 1  
while i <= 10:  
    print "Iteration started"  
    print "i =", i  
    i += 1  
      
    if i == 5:  
        continue  
          
    if i == 7:  
        break  
      
    print "Iteration finished"  
  
print "End of loop"


#####################################################################


my_first_list = [1, 2.5, "Area 51", 1+5j]  
my_second_list = [1 == 3, 2 != 4]  
  
print my_first_list                   #  [1, 2.5, 'Area 51', (1+5j)]  
print my_first_list + my_second_list  #  [1, 2.5, 'Area 51', (1+5j), False, True]  
print my_first_list[2]                #  Area 51  
  
i = 0  
while i < len(my_first_list):  
    print i, ':', my_first_list[i]  
    i += 1


#####################################################################


my_first_list = [1, 2.5, "Area 51", 1+5j]  
  
for element in my_first_list:  
    print element  


#####################################################################


my_first_list = [1, 2.5, "Area 51", 1+5j]  
  
for i, element in enumerate(my_first_list):  
    print i, ':', element  


#####################################################################


my_first_list = [1, 2.5, "Area 51", 1+5j]  
  
for i, element in enumerate(my_first_list):  
    if element == "Area 51":  
        my_first_list[i] = "Aliens"  
      
print my_first_list


#####################################################################


to_sort = [5, 9, 1, -4, 12, 0.5]  
  
for i, element_1 in enumerate(to_sort):  
    for j, element_2 in enumerate(to_sort):  
        if i >= j:  
            continue     # Avoid checking the same elements twice  
        if element_1 > element_2:  
            to_sort[i] = element_2  
            to_sort[j] = element_1  
            element_1 = to_sort[i]  
            element_2 = to_sort[j]  
          
print to_sort            # Prints [-4, 0.5, 1, 5, 9, 12]


#####################################################################


import numpy as np  
  
print np.pi          # The circle constant  
print np.e           # Euler's constant  
  
# Trigonometric functions  
x = 5  
print np.sin(5), np.cos(5), np.tan(5)  
  
# Statistics  
my_list = [1, 5, 25, 50]  
print np.mean(my_list), np.std(my_list)


#####################################################################


print np.ones(5)                     # Create an array of five "ones"  
print np.zeros(6)                    # Create an array of six "zeros"  
print np.random.uniform(0, 1, 10)    # Create an array of ten random numbers between 0 and 1  
print np.array([1, 3, 6])            # Create an array from a list
print np.linspace(1, 10, 19)         # Create an array of 19 evenly spaced numbers between 1 and 10
  
# Arrays can be saved in files for future use and loaded from them  
a = np.random.uniform(0, 1, 10)      # Generate some random numbers  
np.savetxt('random.dat', a)          # Save them in the file random.dat  
b = np.loadtxt('random.dat')         # Load them back from the file into b  
print b                              # Print them



#####################################################################


x = np.linspace(0, np.pi, 1000)        # Array of 1000 evenly spaced numbers between 0 and pi  
                                       # sin(x) will be "sampled" at these points  
y = np.sin(x)                          # Compute sin(x) for all 1000 numbers (no loops necessary)  
dx = x[1] - x[0]                       # Difference between adjacent x values  
print "Integral:", np.sum(dx * y)



#####################################################################


import matplotlib.pyplot as plt  
%matplotlib inline  
  
x = np.linspace(2, 5, 1000)  
y = np.log(x)  
plt.plot(x, y, 'k-', label = 'Plot', lw = 4)  
plt.xlabel('$x$', size = 20)  
plt.ylabel('$\ln(x)$', size = 20)  
plt.title('My first MatPlotLib plot')  
plt.grid()  
plt.legend(loc = 'upper left')
