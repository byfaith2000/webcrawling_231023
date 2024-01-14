ivalue = 102323222
fvalue = 423234223.42325

str1 =  '정수값 : %d, 실수값 : %f' % (ivalue, fvalue)
print(str1)

str2 = '정수값 : {}, 실수값 : {}'.format(ivalue, fvalue)
print(str2)


str3 =  '정수값 : %-15d, 실수값 : %.3f' % (ivalue, fvalue)
print(str3)

str4 = '정수값 : {:<15}, 실수값 : {:,.3f}'.format(ivalue, fvalue)
print(str4)

str5 = f'정수값 : {ivalue}, 실수값 : {fvalue}'
print(str5)

str5 = f'정수값 : {ivalue:<15}, 실수값 : {fvalue:,.3f}'
print(str5)