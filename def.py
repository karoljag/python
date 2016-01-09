#!/usr/bin/env python

# def test(*args):
# 	return args

# print test('a', 'abc', 1, 2, 3)

# def test():
# 	return 'abc'

# test.a = 1
# test.lol = 'omg'

# # print test()
# # print test.__dict__
# tupla = (1,2,3,4,"bocian")
# tup1 = (7,8)+(9,0)*4
# # print tupla


# print tupla[4]
# print tup1




# def test():
# 	return 'abc'

# test.a = 1
# test.lol = 'omg'

# print test()
# print test.__dict__

# a = lambda : 'a'
# print a()

# b = lambda x,y : x+y
# print b(1,2)
#----------------------------------------------
# liczby = [1,2,3,4,5]
# def dwa(x):
# 	return x*2+1

# print map(dwa, liczby)
#----------------------------------------------
liczby = [2,2,2,2,2]
def suma(x,y):
	return x+y
print reduce(suma, liczby)