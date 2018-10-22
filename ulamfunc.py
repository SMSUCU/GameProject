# def ulam(number):
# 	ulam = [1, 2]
# 	for suma in range(number):
#  		for i in ulam:
#  			for j in ulam:
#  				if j != i:
#                     suma = i + j
#                     for a in range(1, i):
#                         for b in range(i + 1, j):
#                             newsum = a + b
#                             if newsum != suma:
#                                 ulam.append(suma)

#     return ulam
# print(ulam(1))


# def ulam_generator(chyslo):
#     ulam = [1, 2]
#     for i in range(chyslo):
#         lst = []
#         for each in ulam:
#             for every in ulam:
#                 if each != every:
#                     lst.append(each + every)
#                     print(lst)
#     while True:
#         a = min(lst)
# 		if lst.count(a) == 1 and not in ulam:
# 			ulam.append(a)
#             break
#         else:
#             lst.remove(a)
#     return ulam
# print(ulam_generator(5))

