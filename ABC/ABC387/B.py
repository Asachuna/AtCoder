X = int(input())

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

for i in nums:
  for j in nums:
    if i*j != X:
      sum += i*j

print(sum)
