class students:
  def _init_(self,name,rn,cgpa):
    self.name=name
    self.rn=rn
    self.cgpa=cgpa
def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students
students=[
  students("Sam","A111",7.8),
  students("Jam","A112",8.9),
  students("Ram","A113",9.1),
  students("Cam","A114",9.9)
]
sorted_students=sort_students(students)
for student in sorted_students:
  print("Name: {},RollNO: {},CGPA: {}".format(student.name,student.rn,student.cgpa))