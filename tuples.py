#Given tuple k of length n, find the minimum and maximum elements of tuple k and 
# return the result as a new tuple(min, max)

m = (9,214,8,19,90,4)
print(m)
  
K = 1

new_tuple = []
m = list(m)
sortedm = sorted(m)
  
for i, y in enumerate(sortedm):
    if i < K or i >= len(sortedm) - K:
        new_tuple.append(y)
res = tuple(new_tuple)
print(new_tuple) 






