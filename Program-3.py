a = int(input("Enter a number: "))
if a % 2 == 0:
    length = a - 1
else:
    length = a

result = []
for i in range(length):
    num = 2*i + 1
    result.append(num)
print(result)
