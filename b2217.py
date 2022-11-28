n = int(input())
weight = []
for i in range(n):
    w = int(input())
    weight.append(w)

weight.sort(reverse=True)

value = []
for i in range(n):
    value.append(weight[i]*(i+1))

print(max(value))