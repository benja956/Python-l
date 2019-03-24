
import itertools
import math

# 全部
a = range(2,100)
# # 质数
# b = list(filter(lambda x: not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i ==0], range(2,100+1)))

# 所有可能组合
c = [i for i in itertools.combinations(a, 2)]
print('所有可能的两个数字组合，共%d项'%len(c),c)


# 庞涓：我肯定你不知道
times = [i[0]*i[1] for i in c]
temp = []
for i in range(len(times)):
    if times.count(times[i])==1:
        temp.append(c[i])
print('先求出项目相乘得到的乘数唯一的可能，共%d项'%len(temp),temp)

temp2 = set([sum(i) for i in temp])
print('计算这些唯一项的和，得到和数共有%d种'%len(temp2),temp2)

temp3 = []
for i in c:
    if sum(i) not in temp2:
        temp3.append(i)
c = temp3
print('因为肯定不唯一，所以和数一定不在上述和数当中，剔除后剩余项%d项'%len(c),c)


# 庞涓：我不知道（和数不唯一）
plus = [i[0]+i[1] for i in c]
temp = []
for i in range(len(c)):
    if plus.count(plus[i])!=1:
        temp.append(c[i])
c = temp
print('项目相加得到的和数不唯一，剩余项%d项'%len(c),c)

# 孙膑：听你一说所现在知道了（乘数唯一）
times = [i[0]*i[1] for i in c]
temp = []
for i in range(len(c)):
    if times.count(times[i])==1:
        temp.append(c[i])
c = temp
print('两数相乘答案唯一，剩余项%d项'%len(c),c)

# 庞涓：我也知道了（和数唯一）
plus = [i[0]+i[1] for i in c]
temp = []
for i in range(len(c)):
    if plus.count(plus[i])==1:
        temp.append(c[i])
c = temp
print('两数相加答案唯一，剩余项%d项'%len(c),c)

print(c)

