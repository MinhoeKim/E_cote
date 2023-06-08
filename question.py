n = int(input())

num = [int(x) for x in str(n)]

half = int(len(num)/2)


if sum(num[:half]) == sum(num[half:]):
    print("LUCKY")
else:
    print("READY")
