a = 234
b = 45
if a > a:
    print("a is greater is b")

# Collect input from the user
kilometers = float(input('How many kilometers?: '))
# conversion factor
conv_fac = 0.621371
# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' % (kilometers, miles))

# python programme to display the calender
import calendar

# enter the month and the year
yy = int(input("Enter year :"))
mm = int(input("Enter month :"))

# display the calender
print(calendar.month(yy, mm))

# python programme to print all calender for a year

