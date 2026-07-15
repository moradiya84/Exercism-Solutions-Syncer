def append(list1, list2):
    return list1+list2

def concat(lists):
    l=[]
    for item in lists:
        l = l+item
    return l


def filter(function, list):
    l = []
    for item in list:
        if function(item):
            l.append(item)
    return l

def length(list):
    return len(list)

def map(function, list):
    l=[]
    for item in list:
        l.append(function(item))
    return l


def foldl(function, list, initial):
    for item in list:
        initial = function (initial,item)
    return initial

def foldr(function, list, initial):
    list=reverse(list)
    for item in list:
        initial = function (initial,item)
    return initial

def reverse(list):
    for i in range(len(list)//2):
        list[i],list[-1-i]=list[-1-i],list[i]
    return list
