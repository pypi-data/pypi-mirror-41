"""This is the nester.py"""
def print_lol(the_list):
    #This is a function
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

