sname=input('enter student name')
srno=int(input('enter student roll number'))
sub1=int(input('enter first sub marks'))
sub2=int(input('enter second sub marks'))
sub3=int(input('enter third sub marks'))
total=sub1+sub2+sub3
avg=total/3
print('------------STUDENT INFORMAION-------------')
print('student name is',sname)
print('student roll numb is',srno)
print('student total marks',total)
print('student average marks',avg)