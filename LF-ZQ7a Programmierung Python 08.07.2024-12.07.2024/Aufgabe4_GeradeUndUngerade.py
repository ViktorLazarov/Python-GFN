def is_even(zahl):
    return True if zahl % 2 else False

numbersList = [4,7,12,56,33,59]

for i in numbersList:
    print("ungerade" if is_even(i) else "gerade")
