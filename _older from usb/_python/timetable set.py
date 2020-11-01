Days = {'Monday': [], 'Tuesday': [], 'Wednesday': [], \
        'Thursday': [], 'Friday': []}

for Day in Days:
    for i in range(5):
        Days[str(Day)].append(input(str(Day) + ' ' + str(i + 1) + '\n'))

with open('timetable.txt', 'w+') as File:
    File.write(str(Days))
