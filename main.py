# import time
# fire =   ["⭐","💥","🔔"]
# for i in range(5,0,-1):
#     print(f"{i} 🎄")
#     time.sleep(0.5)

# for f in fire:
#     print(f * 10)
#     time.sleep(0.3)

# print("MERRY CHRISTMAS")



# ---------------------------------------------------------------------------- #
#                                     LIST                                     #
# ---------------------------------------------------------------------------- #

l1 = [1,2,'art',1.23]
l2 = []



# append(add a value at the end of the list)
# l1.append('kavya')
# print(l1)

# insert(add a value at specific location or index)
# l1.insert(1,'kusum')
# print(l1)

# remove(to remove a particular element)
# l1.remove(2)
# print(l1)

# pop(to remove a particular element of specific location)
# l1.pop(0)
# print(l1)

# copying a list(changes made in any list after copying it changes will be done in both the list)
# myl = [23,12,45.8,'gini']
# myl2 = myl
# # print(myl2)
# myl2.append('kavya')
# print(myl2)
# print(myl)

# myl.append('hen')
# print(myl)
# print(myl2)

# To made a actual copy of the list we have to use .copy() method [In this changes made in copied list will not affect original list]
# lis1 = [1,2,'k','kite']
# lis2 = lis1.copy()
# lis2.insert(1,'red')

# print(lis1)
# print(lis2)

a = [1,2,3,4]
b = [i*i for i in a]
print(b)