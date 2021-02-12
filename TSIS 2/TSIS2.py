# 1 defanging an ip-address
def defangIPaddr(self, address):
    address=address.replace('.', '[.]')
    return address


# 2  goal parser
def interpret(self, command):
    command=command.replace('()', 'o')
    command=command.replace('(al)', 'al')
    return command

# 3 number of good pairs
def numIdenticalPairs(self, nums):
    sum=0
    for i in nums:
        sum+=nums.count(i)-1
        nums=nums[1:]
    return sum

# 4 largest altitude
def largestAltitude(self, gain):
    max, x = 0, 0
    for i in gain:
        x += i
        if x > max:
            max = x
    return max

# 5 product and sum
def subtractProductAndSum(self, n):
    n = str(n)
    sum, product = 0, 1
    for i in n:
        sum += int(i)
        product *= int(i)
    return product - sum

