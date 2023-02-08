import time

time.time()

import time

print(time.time())

print('---------------------------')
print('Calculating Time')
print('---------------------------')


# This can be found by subtracting the finish time from the start time

def calcProd():
    product = 1
    for i in range(1, 100000):
        print(f'Multiplying {i} with {product}')
        product = product * i
    return product


starTime = time.time()
prod = calcProd()
endTime = time.time()
print(f'The result is {len(str(prod))} digits long')
print(f'Took {str(endTime - starTime)} to calculate')


print('---------------------------')
print('Human Readable Time with time.ctime()')
print('---------------------------')
import time

print(time.ctime())

print('---------------------------')
print('Time.sleep Function')
print('---------------------------')

import time
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

print('---------------------------')
print('Date Time')
print('---------------------------')

import datetime

print(datetime.datetime.now())

dt = datetime.datetime(2019, 2, 27, 11, 10, 49, 55)  # Setting Specific TimeLines
print(dt.year, dt.month, dt.day)

print(dt.hour, dt.minute, dt.second)

print('---------------------------')
print('Time Delta')
print('---------------------------')

import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(str(delta.total_seconds()))

print('---------------------------')
print('Time Delta')
print('---------------------------')
# Time delta allows us to calculate time and dates
import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(str(delta.total_seconds()))

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print(str(dt + thousandDays))

aboutThiryYears = datetime.timedelta(days=365 * 30)
print(str(dt - aboutThiryYears))

print('---------------------------')
print('Pausing Until a specific date')
print('---------------------------')

import datetime, time

print('---------------------------')
print('Converting Date Time Objects Into Strings')
print('---------------------------')
import datetime, time

oct21st = datetime.datetime(2022, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y%m%d %H:%M:%S'))

print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime('%B of %ynd'))

print('-----------------------------------------')
print('Converting Strings Into Date Time Objects')
print('-----------------------------------------')

converted = datetime.datetime.strptime('October 21, 2022', '%B %d, %Y')
print(converted)

converted = datetime.datetime.strptime('2022/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(converted)

converted = datetime.datetime.strptime('October of 22', '%B of %y')
print(converted)