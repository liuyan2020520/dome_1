###列表推导式1.要有for循环；2.要有append；
#给你一个整数数组nums，请你返回其中位数为偶数的数字的个数
nums = [12,345,2,6,7896]
# nums1=[]
# for i in nums:
#     if len(str(i))%2==0:
#         nums1.append(i)
# print(len(nums1))
print(len([i for i in nums if len(str(i)) % 2 == 0]))
