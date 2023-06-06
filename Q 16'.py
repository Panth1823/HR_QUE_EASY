
start = int(input())
end = int(input())
step = int(input())

currentFahrenhietValue = start

while currentFahrenhietValue <= end :
    celsiusValue = (5 / 9) * (currentFahrenhietValue - 32)
    print(str(currentFahrenhietValue) + "\t" + str(int(celsiusValue)))
    currentFahrenhietValue += step