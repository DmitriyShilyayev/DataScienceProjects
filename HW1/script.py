import random


def init():
    print("Choose task number to run (1-20).")
    print("To exit press 0.")
    task = input("Task number: ")
    match task:
        case "0":
            exit()
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case _:
            print("Incorrect value. Try again.")
            init()


def exit():
    print("Have a good day!.")


def task1():
    print("/--------------------------------------/")
    print("Task 1:")
    numbers = (
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
    )
    print("Our random tuple: (" + (", ".join(str(num) for num in numbers)) + ")")
    print("Second item: " + str(numbers[1]))
    print("/--------------------------------------/")
    init()


def task2():
    print("/--------------------------------------/")
    print("Task 2:")
    userStr = input("Please, enter some string: ")
    print("String length: " + str(len(userStr)))
    print("/--------------------------------------/")
    init()


def task3():
    print("/--------------------------------------/")
    print("Task 3:")
    studentInfo = {"name": "Dmitriy", "age": 29, "course": 1}
    print("Studen Info:")
    print("Name: " + studentInfo["name"])
    print("Age: " + str(studentInfo["age"]))
    print("Course: " + str(studentInfo["course"]))
    print("/--------------------------------------/")
    init()


def task4():
    print("/--------------------------------------/")
    print("Task 4:")
    numList = []
    number = 1
    while number < 10:
        numList.append(number)
        number += 1
    print("Our generated list: [" + (", ".join(str(num) for num in numList)) + "]")
    print("/--------------------------------------/")
    init()


def task5():
    print("/--------------------------------------/")
    print("Task 5:")
    userList = inputNumList()
    listSum(userList)
    print("/--------------------------------------/")
    init()


def inputNumList():
    print("Please, enter list of values, one by one.")
    print("To end list press 0.")
    valuesList = []
    value = 1
    while value != 0:
        value = input("Enter value: ")
        if value.isdigit():
            value = int(value)
        else:
            print("Incorect value. Try again.")
            continue
        if value == 0:
            break
        valuesList.append(value)
    print("Done! Your list: [" + (", ".join(str(num) for num in valuesList)) + "]")
    return valuesList


def listSum(list):
    sum = 0
    for num in list:
        sum += num
    else:
        print("List summary: " + str(sum))


init()
