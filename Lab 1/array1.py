def student_grades():
    grades = [85, 90, 78, 92, 88] 
    print("Original Grades:", grades)
    
    
    average = sum(grades) / len(grades)
    print("Average Grade:", average)
    
    
    grades.append(95)
    print("Updated Grades:", grades)
    
    
    grades.sort()
    print("Sorted Grades:", grades)

student_grades()