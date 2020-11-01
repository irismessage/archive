from datetime import datetime
from calendar import day_name

with open('timetable.txt', 'r') as TimetableFile:
    TimetableText = TimetableFile.read()
    Timetable = eval(TimetableText)

DayName = day_name[datetime.today().weekday()]
DayLessons = Timetable[DayName]

Time = str(datetime.now())
Hour = int(Time[Time.index(' ') + 1:Time.index(' ') + 3])
Minute = int(Time[Time.index(':') + 1:Time.index(':') + 3])
Minutes = (Hour * 60) + Minute

Times = [[540, 600], [600, 660] ,[680, 740], [740, 800], [850,910]]

i = 0
for Bracket in Times:
    if Minutes > Bracket[0] and Minutes < Bracket[1]:
        LessonNum = i
        break
    i += 1

Lesson = DayLessons[LessonNum]

with open('lesson.txt', 'w+') as LessonFile:
    LessonFile.write(Lesson)
        
