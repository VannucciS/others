gpa = float(input('What was your grade point average'))
lowest_grade = float(input('what was your lowest grade'))


if gpa >= .85 and lowest_grade >= .7:
    honour = True
else:
    honour = False


if honour:
    print('congrats')
