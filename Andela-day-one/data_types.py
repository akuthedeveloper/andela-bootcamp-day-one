def data_types(a):
    # checks if the value of a is isinstance of string nand returns length
    if isinstance(a, str):
        return len(a)
    # checks if the value of a is empty string and returns no value
    elif a==None:
        return 'no value'
    # checks if the value is Boolean
    elif isinstance(a, bool):
        return a
    # checks if the value is integer
    elif isinstance(a, int):
    # checks if the int is equal to 100
        if a==100:
            return 'equal to 100'
        else:
            return 'more than 100'
    # checks if the value a is a string
    elif isinstance(a, list):
        if len(a)<3:
            return None
        else:
            return a[2]
    # print statement
print data_types(2)
print data_types('my value')
print data_types(None)
print data_types(False)
print data_types([1,2])
print data_types([1,2,3,4])
