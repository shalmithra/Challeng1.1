class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the student list in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Test the sort_students function with a list of student objects
if __name__ == "__main":
  # Create a list of student objects
  students = [
      Student("Alice", "001", 3.7),
      Student("Bob", "002", 3.5),
      Student("Charlie", "003", 4.0),
      Student("David", "004", 3.9),
      Student("Eve", "005", 3.8),
  ]

  # Sort the students based on CGPA
  sorted_students = sort_students(students)

  # Print the sorted list
  for student in sorted_students:
      print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")