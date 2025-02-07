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
        case "6":
            task6()
        case "7":
            task7()
        case "8":
            task8()
        case "9":
            task9()
        case "10":
            task10()
        case "11":
            task11()
        case "12":
            task12()
        case "13":
            task13()
        case "14":
            task14()
        case "15":
            task15()
        case "16":
            task16()
        case "17":
            task17()
        case "18":
            task18()
        case "19":
            task19()
        case "20":
            task20()
        case _:
            print("Incorrect value. Try again.")
            init()


def exit():
    print("Have a good day!.")


def inputNumList():
    print("Please, enter list of values, one by one.")
    print("To end list press 0.")
    valuesList = []
    while True:
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
        return sum


def strReverse(str):
    return str[::-1]


def multiplyValues(a, b):
    return a * b


def maxNum(list):
    return max(list)


def isPalindrome(str):
    charsFromStr = "".join(e for e in str if e.isalnum())
    return charsFromStr.lower() == strReverse(charsFromStr.lower())


def formatDict(dict):
    for key, value in dict.items():
        print(str(key) + ":")
        print("    " + str(value))


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
    print("Time complexity: O(1)")
    print("/--------------------------------------/")
    init()


def task2():
    print("/--------------------------------------/")
    print("Task 2:")
    userStr = input("Please, enter some string: ")
    print("String length: " + str(len(userStr)))
    print("/--------------------------------------/")
    print("Time complexity: O(1)")
    print("/--------------------------------------/")
    init()


def task3():
    print("/--------------------------------------/")
    print("Task 3:")
    studentInfo = {"name": "Dmitriy", "age": 29, "course": 1}
    print("Student Info:")
    print("Name: " + studentInfo["name"])
    print("Age: " + str(studentInfo["age"]))
    print("Course: " + str(studentInfo["course"]))
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task4():
    print("/--------------------------------------/")
    print("Task 4:")
    numList = []
    number = 1
    while number <= 10:
        numList.append(number)
        number += 1
    print("Our generated list: [" + (", ".join(str(num) for num in numList)) + "]")
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task5():
    print("/--------------------------------------/")
    print("Task 5:")
    userList = inputNumList()
    print("List summary: " + str(listSum(userList)))
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task6():
    print("/--------------------------------------/")
    print("Task 6:")
    numbersSet = set()
    while len(numbersSet) < 5:
        numbersSet.add(random.randint(1, 100))
    print("Your set: " + str(numbersSet))

    while len(numbersSet) < 6:
        value = input("Enter value to add to set: ")
        if value.isdigit():
            value = int(value)
        else:
            print("Incorect value. Try again.")
            continue
        if value in numbersSet:
            print("This value is already in the set. Try again.")
            continue
        else:
            numbersSet.add(value)
            print("This value was added to the set.")

    print("Done! Your current set: " + str(numbersSet))
    print("/--------------------------------------/")
    print("Time complexity: O(n2)")
    print("/--------------------------------------/")
    init()


def task7():
    print("/--------------------------------------/")
    print("Task 7:")
    while True:
        value = input("Please, enter integer value: ")
        if value.isdigit():
            value = int(value)
            break
        else:
            print("Incorect value. Try again.")
            continue
    print("Good job! Your value: " + str(value))
    print("/--------------------------------------/")
    print("Time complexity: O(1)")
    print("/--------------------------------------/")
    init()


def task8():
    print("/--------------------------------------/")
    print("Task 8:")
    fruitsDict = {
        "Apple": "Red",
        "Mandarin": "Orange",
        "Pear": "Yellow",
        "Plum": "Purple",
        "Grape": "Green",
    }
    print("Fruts:")
    for key, value in fruitsDict.items():
        print(str(key) + "'s color is " + str(value))
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task9():
    print("/--------------------------------------/")
    print("Task 9:")
    usersStr = input("Please, enter some string: ")
    print("It's reversed version:")
    print(strReverse(usersStr))
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task10():
    print("/--------------------------------------/")
    print("Task 10:")
    strList = ["Vladislav", "Dmitriy", "Igor", "Maria", "Tatyana"]
    print("Our list of names: [" + (", ".join(str for str in strList)) + "]")

    while True:
        newStr = input(
            "Please, enter new name for the list, to replace " + strList[2] + ": "
        )
        if len(newStr) > 0:
            strList[2] = newStr
            break
        else:
            print("Incorect value, try again")
            continue

    print("Current list of names: [" + (", ".join(str for str in strList)) + "]")
    print("/--------------------------------------/")
    print("Time complexity: O(1)")
    print("/--------------------------------------/")
    init()


def task11():
    print("/--------------------------------------/")
    print("Task 11:")
    userTuple = ("Dmitriy", 29, True, -1.5, None, bytes(1))
    print("Current tuple:")
    print(str(userTuple))

    print("This tuple contains next items:")
    for item in userTuple:
        print(str(item) + "'s type is " + str(type(item)))

    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task12():
    print("/--------------------------------------/")
    print("Task 12:")
    while True:
        firstValue = input("Please, enter first integer value: ")
        if firstValue.isdigit():
            firstValue = int(firstValue)
            break
        else:
            print("Incorect value. Try again.")
            continue
    while True:
        secondValue = input("Please, enter second integer value: ")
        if secondValue.isdigit():
            secondValue = int(secondValue)
            break
        else:
            print("Incorect value. Try again.")
            continue
    print(
        "The result of multiplying your numbers: "
        + str(multiplyValues(firstValue, secondValue))
    )
    print("/--------------------------------------/")
    print("Time complexity: O(1)")
    print("/--------------------------------------/")
    init()


def task13():
    print("/--------------------------------------/")
    print("Task 13:")
    bookInfo = {
        "author": "Douglas Adams",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "year": 1979,
    }
    print("Book Info:")
    print("Author: " + bookInfo["author"])
    print("Title: " + str(bookInfo["title"]))
    print("Year of publication: " + str(bookInfo["year"]))
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task14():
    print("/--------------------------------------/")
    print("Task 14:")

    citiesSet = set()
    citiesSet.add("London")
    citiesSet.add("Tokio")
    citiesSet.add("Moscow")
    citiesSet.add("Minsk")
    citiesSet.add("Berlin")
    print("Your set: " + str(citiesSet))
    while True:
        value = input("Please, enter city to remove from this set: ")
        if value in citiesSet:
            citiesSet.remove(value)
            break
        else:
            print("Incorect value. Try again.")
            continue
    print("Done! Your current set: " + str(citiesSet))
    print("/--------------------------------------/")
    print("Time complexity: O(1)")
    print("/--------------------------------------/")
    init()


def task15():
    print("/--------------------------------------/")
    print("Task 15:")
    userList = inputNumList()
    print("The biggest number in your list is: " + str(maxNum(userList)))
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task16():
    print("/--------------------------------------/")
    print("Task 16:")
    numList = []
    number = 1
    while number <= 20:
        numList.append(number)
        number += 1
    evenNumList = []
    for num in numList:
        if (num % 2) == 0:
            evenNumList.append(num)
    print("Our list of numbers: [" + (", ".join(str(num) for num in numList)) + "]")
    print(
        "Even numbers of that list: ["
        + (", ".join(str(num) for num in evenNumList))
        + "]"
    )
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task17():
    print("/--------------------------------------/")
    print("Task 17:")
    usersStr = input("Please, enter some string: ")
    if isPalindrome(usersStr):
        print("This string is a palindrome")
    else:
        print("This string isn't a palindrome")
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task18():
    print("/--------------------------------------/")
    print("Task 18:")
    userTuple = ("Dmitriy", 29, True)
    print("Current tuple:")
    print(str(userTuple))
    first, second, third = userTuple
    print("Elements of this tuple: ")
    print(first)
    print(second)
    print(third)
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task19():
    print("/--------------------------------------/")
    print("Task 19:")
    studentInfo = {"Name": "Dmitriy", "Age": 29, "Course": 1}
    print("Student Info:")
    formatDict(studentInfo)
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


def task20():
    print("/--------------------------------------/")
    print("Task 20:")
    userList = []
    while len(userList) < 4:
        value = input("Please, enter some value to add to your list: ")
        if len(value) > 0:
            userList.append(value)
        else:
            print("Incorrect value. Try again.")

    print("Your list of items: [" + (", ".join(str(item) for item in userList)) + "]")
    print("/--------------------------------------/")
    print("Time complexity: O(n)")
    print("/--------------------------------------/")
    init()


init()
