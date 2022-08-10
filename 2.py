# arr=[]
# for i in range(0,2):
#     col = []
#     for j in range(0,5):
#         if j == 0:
#             col.append(i)
#         elif j > 0:
#             value = input()
#             col.append(value)  
#     arr.append(col)
# print(arr)

raw_d = input()
u = raw_d[1:]
uInput = int(u)
uInput = int(589)

DATA = [[0 ,'$1' ,'$400', '5%'],
       [1, '$401', '$800' ,'4%'],
       [2 ,'$801', '$1200', '3%'],
       [3 ,'$1201' ,'$9000', '2%'],
       [4, '$9001', '$15000',' 1%']]

for i in range(0,len(DATA)):
    a = DATA[i][1]
    b = DATA[i][2]
    x = a[1:]
    y = b[1:]
    c = int(x)
    d = int(y)
    if(uInput>=c and uInput<=d):
        per = DATA[i][3]
        per = int(per[:-1])
        print(type(per))
        print("Your commission rate is {}% you will get ${} and remaining amount is ${}".format(per,uInput*per/100,uInput -uInput*per/100 ))
        break
