n = int(input())
arr = list(map(int, input().split()))

max_value = max(arr)

item_occurences = {}

for item in arr:
    if(item != max_value):
        item_occurences[item] = max_value - item

runner_up = min(item_occurences, key=lambda x: item_occurences[x])

print()