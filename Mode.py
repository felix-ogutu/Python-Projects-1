from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
marks = [45, 78, 56, 78, 89, 45, 89, 89, 67, 90]
Entry = [100, 102, 102, 103, 563, 670, 102, 102, 102]

x = stats.mode(speed)
y = stats.mode(marks)
z = stats.mode(Entry)

print(x)
print(y)
print(z)
