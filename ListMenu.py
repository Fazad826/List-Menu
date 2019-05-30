from random import randint
import math
print("Hello this is a List menu")
print("you can create a list and change it however you want")
ans = str(input("Do you want this to be a list with numbers or strings? (n for numbers, s for string)"))
list = []
size = 0
def create_list(p):
    if ans == "n":
        j = int(input("would you like to chose the values or do you want them randomized ?(1 to chose, 2 for random)"))
        if j == 2:
            for i in range (p):
                list.append( randint(1,99))
        elif j == 1:
            for i in range(p):
                nums = int(input ("Type a value "))
                list.append(nums)
        else:
            print("Wrong choice")
    elif ans == "s":
        for i in range(p):
                nums = str(input ("Type a value "))
                list.append(nums)

    print(list)
    return list
      
    
def log(list1, p):
    high = list1[0]
    low = list1[0]
    sum1 = 0
    dis= 0
    a = 0
    for i in range (p):
        if list1[i] >= high:
            high = list1[i]
    for i in range (p):
        if list1[i] < low:
            low = list1[i]
    for i in range (p):
        sum1 = sum1 + list[i]
    average = sum1/ p
    for i in range(p):
        dis = (list1[i] - average) * (list1[i] - average)
        a = a+ dis
    std = math.sqrt(a/p)
    list1.sort()
    if p%2 ==0:
        median = (list1[int(p/2)] + list[int(p/2) -1])/2
    else:
        median  = list1[int(p/2)]
    print("High " + str(high))
    print("Low " + str(low))
    print("Sum " + str(sum1))
    print("Average " + str(average))
    print("Median " + str(median))
    print("Standard Deviation " + str(std))
def find_ind(list1, p):
    k = False
    if ans == "n":
        num = int(input("what number you need ? "))
    elif ans == "s":
        num = str(input("what word you need ? "))
    for i in range (p):
        if num == list1[i]:
              k = True
              print (str(num) +" is at index "+str(i))
    if k == False:
              print(str(num) +" is not in this list ")
def inser_ind(list1, p):
    if ans == "n":
        numi = int(input("Add a item "))
    elif ans == "s":
        numi = str(input("Add a item "))
    ini = int(input("What index? "))
    while ini < 0 or ini >p-1:
        print("invaild index")
        ini = int(input("What index? "))
    i = p-1
    while i > ini:
        list1[i] = list1[i-1]
        i = i-1
    list1[ini] = numi
    print(list)
    return list
def findn(list1, p, num1):
    k = False
    for i in range (p):
        if num1 == list1[i]:
              k = True
    return k
def remove_ind(list1,p):
    ini = int(input("What index? "))
    while ini < 0 or ini >p-1:
        print("invaild index")
        ini = int(input("What index? "))
    i = ini 
    while i <= p-2:
        list1[i] = list[i+1]
        i = i+1
def same_element(list1, p, n):
    v = False
    for i in range (p-1):
        if list1[i] == n:
            v = True
    return v
def shuffle_lis(p):
    alist = []
    i = 0
    while i < p:
        k = randint(0, p-1)
        alist.append( list[k])
        if i > 0:
            while same_element(alist,i+1, alist[i]) == True:
                alist.pop()
                k = randint(0, p-1)
                alist.append(list[k])
        i = i + 1
    for c in range (p):
        list[c] = alist[c]
    print(list)
    return list
def menu():
    print("0. Create List")
    print("1. Find high, low, sum, average, median, and standard deviation")
    print("2. Add a number to the end")
    print("3. Find the index of a number")
    print("4. Insert number at index")
    print("5. Remove number")
    print("6. Remove number at index")
    print("7. Sort list") 
    print("8. Shuffle list")
    print("9. Quit")
def smenu():
    print("0. Create List")
    print("1. Add a word to the end")
    print("2. Find the index of a word")
    print("3. Insert word at index")
    print("4. Remove word")
    print("5. Remove word at index")
    print("6. Sort list") 
    print("7. Shuffle list")
    print("8. Quit")
def num_list():
    choice = -1
    while choice != 9:
        menu()
        choice = int(input("which one you want? "))
        if choice == 0:
            list.clear()
            size= int(input("how many elements? "))
            create_list(size)
        elif choice == 1:
            log(list, size)
        elif choice == 2:
            numi = int(input("Add a number "))
            list.append(numi)
            size = size + 1
            print(list)
        elif choice == 3:
            find_ind(list, size)
        elif choice == 4:
            size= size+1
            list.append(0)
            inser_ind(list, size)
        elif choice == 5:
            numi = int(input("remove a number "))
            if (findn(list, size, numi) == False):
                print(str(numi) +" is not in this list ")
            else:
                list.remove(numi)
                size = size - 1
                print(list)
        elif choice == 6:
            remove_ind(list,size)
            size = size - 1
            list.pop()
            print(list)
        elif choice == 7:
            list.sort()
            print(list)
        elif choice == 8:
            shuffle_lis(size)
    print("Goodbye")
def str_list():
    choice = -1
    while choice != 8:
        smenu()
        choice = int(input("which one you want? "))
        if choice == 0:
            list.clear()
            size= int(input("how many elements? "))
            create_list(size)
        elif choice == 1:
            numi = str(input("Add a Word "))
            list.append(numi)
            size = size + 1
            print(list)
        elif choice == 2:
            find_ind(list, size)
        elif choice == 3:
            size= size+1
            list.append(0)
            inser_ind(list, size)
        elif choice == 4:
            numi = str(input("remove a word "))
            if (findn(list, size, numi) == False):
                print(str(numi) +" is not in this list ")
            else:
                list.remove(numi)
                size = size - 1
                print(list)
        elif choice == 5:
            remove_ind(list,size)
            size = size - 1
            list.pop()
            print(list)
        elif choice == 6:
            list.sort()
            print(list)
        elif choice == 7:
            shuffle_lis(size)
    print("Goodbye")
if ans == "n":
    num_list()
elif ans == "s":
    str_list()