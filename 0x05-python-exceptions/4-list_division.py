#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    newlist = []
    while (i < list_length):
        try:
            j = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except TypeError:
            print("wrong type")
            j = 0
        except IndexError:
            print("out of range")
            j = 0
        finally:
            newlist.append(j)
            i += 1
    return newlist
