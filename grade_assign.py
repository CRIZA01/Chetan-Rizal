#chetanrizal

math = float(input('what is your grade in math?'))
chemistry = float(input('what is your grade in chemistry?'))
art = float(input('what is your grade in art?'))
english = float(input('what is your grade in english?'))
jrotc = float(input('what is your grade in jrotc?'))


grade = [math,chemistry,art,english,jrotc]

grade_average = (math+chemistry+art+english+jrotc)

grade.append ('grade average:'+ str(grade_average))
print grade

if grade_average >= 60:
        print('you get an U')
elif grade_average >= 90 and grade <=100:
    print('you get an A')
elif grade_average >= 80 and grade <=90:
    print('you get an B')
elif grade_average >= 70 and grade <=80:
    print('you get an C')
elif grade_average >=60 and grade <= 70:
     print('you get an D')
else:
    print str (grade_average)+ ' is not a valid average'
