__author__ = 'chaotism'
import random
from time import time

def timed(fn):
    def decorated(*x):
        start = time()
        result = fn(*x)
        print "Executing %s took %d ms" % (fn.__name__, (time()-start)*1000)
        return result
    return decorated

random_list1 = [random.randint(0, 10000) for i in xrange(10000)]
print "random_list1"
#print random_list1


@timed
def gnome_sort(sorting_list):
    n = 0
    for index in xrange(len(sorting_list) - 1):
        i = index
        while True:
            n += 1
            if sorting_list[i] < sorting_list[i + 1]:
                sorting_list[i], sorting_list[i + 1] = sorting_list[i + 1], sorting_list[i]
                i -= 1
                if i < 0:
                    break
            else:
                break
    print n
    return sorting_list


print "gnome sort"
gnome_sort(random_list1)

print "random_list2"
random_list2 = [random.randint(0, 10000) for i in xrange(10000)]
#print random_list2


@timed
def bubble_sort(sorting_list):
    n = 0
    while True:
        errors = 0
        for index in xrange(len(sorting_list) - 1):
            n +=1
            i = index
            if sorting_list[i] < sorting_list[i + 1]:
                sorting_list[i], sorting_list[i + 1] = sorting_list[i + 1], sorting_list[i]
                errors += 1
        if not errors:
            break
    print n
    return sorting_list


print "bubble_sort"
bubble_sort(random_list2)
