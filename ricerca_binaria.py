lst = [1,3,7,11,13,14,18]
x = 7
low , high= lst[0], lst[len(lst) - 1]

def binary_search(x, low, high, lst):
    for j in range(0, len(lst)):
        if x != low and x != high:
            mid = (low + high) / 2
        
        if x == mid:
            return True
        if x < mid: 
            high = mid
        elif x > mid:
            low = mid
        else: 
            return True

app = binary_search(x,low,high, lst)
print(app)