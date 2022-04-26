# 找出一个五位数，满足 算法描述题*算 = 题题题题题题
for i in range(10000, 99999):
    for j in range(0, 10):
        if i * j % 111111 == 0:
            if len(set(str(i))) == 5:
                if str(j) == str(i)[0]:
                    print("该五位数为{}".format(i))
