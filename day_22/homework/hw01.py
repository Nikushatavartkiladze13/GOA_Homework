# 2 ) გააკეთეთ სია სადაც იქნება 10 ინტეჯერი , ინტეჯერები რომელიბ იქნება 10 ზე ნაკლები append ის დახმარებით შეიყვანეთ ახალ ცხრილში

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
second_list = []
for i in my_list:
    if i < 10:
        second_list.append(i)
print(second_list)