# 6) დაწერეთ პროგრამა რომელიც სიაში მყოფი ელემენტების ჯამს გამოითვლის 

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


num = 0
for i in range(len(my_list)):
    num += i

print(num)