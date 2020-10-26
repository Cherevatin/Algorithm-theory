import sys
def to_decimal(binary):
    i = 1
    result = 0
    for char in binary:
        result += int(char)*2**(len(binary)-i)
        i+=1
    return result
    
while(True):
    binary = input("Enter a binary number:")
    if binary.count('0') + binary.count('1') == len(binary):
        break
    else:
        print("Input error! Try again")

min = binary.count('1')*str(1)
max = binary.count('1')*str(1)
while(to_decimal(max) < sys.maxsize):
    max +="0"
    if(to_decimal(max + "0") >=sys.maxsize):
        break

print("\n_____INPUT DATA_____")
print("Binary:" + binary + "\nDecimal:" + str(to_decimal(binary)))

print("\n_____OUTPUT DATA_____")

print("\nMin number:")
print("Binary:" + min + "\nDecimal:" + str(to_decimal(min)))

print("\nMax number:")
print("Binary:" + max + "\nDecimal:" + str(to_decimal(max)) + "\n")
