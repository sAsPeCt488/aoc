increased = 0

with open("input.txt", "r") as input:
    measurements = [int(num) for num in input.read().splitlines()]

for i in range(1, len(measurements)):
    if measurements[i-1] < measurements[i]:
        increased += 1
print("[+] Result: ", increased)
