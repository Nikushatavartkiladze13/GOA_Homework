# 7) შექმენით ახალი სია მხოლოდ ლუწი რიცხვების ერთი დიდი სიიდან


number =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
num = []
for i in range(len(number)):
    if i % 2 == 0:
        i += 2
        num.append(i)
    else:
        continue

print(num)