# University Admission Procedure
## About
This project is about university applications. It's the implementation of an
algorithm to determine which applicants are going to be enrolled.  
The university has five departments, and the potential students 
can apply to the Mathematics, Physics, Biotech, Chemistry, or the Engineering Department.
Each applicant needs to choose three departments and rank them. First, the department with
the highest priority; second, the department in case the first option doesn't work out. 
The third department is Plan C.  
The program will need to rank the potential students and determine who's going 
to get admitted according to their *GPA*, and their priorities. The *Grade Point Average (GPA)
is the mean grade of all high school courses.  
But taking only student's GPAs into consideration may not be very conclusive. It would be better
if we could take the results of the finals depending on the Department.
## Objectives
1. Read an **N** integer from the input. This integer represents the maximum number of students
   for each department.
2. Read a file named applicants.txt. It can be of 2 types: with GPA or with a set of scores for relevant exams:
   * For the first type, each line equals one applicant, their first name, last name, GPA, first priority department, second priority
     department, and third priority department. Columns with values are separated by whitespace characters. 
     For example, `Laura Spungen 3.71 Physics Engineering Mathematics`.
   * For the second type instead of the GPA column, each line contains four columns with scores for particular exams: physics, chemistry,
     math, computer science (in this order). For example `John Ritchie 89 45 83 75 Physics Engineering Mathematics`.
3. a. If the file has the GPA score, sort applicants according to their GPA and priorities (and names, if their GPA score is the same). 
   As in the previous stage, if two applicants to the same department have the same GPA, sort them by
   their full names in alphabetical order.  
   b. If the file has a set of score, we can:
      * Take into account the following exam results for the departments: physics for the Physics department, chemistry
        for the Chemistry department, math for the Mathematics department, computer science for the Engineering, and 
        chemistry (again) for the Biotech department. 
      * Take into account the following exam results for the departments: both math and physics exams for Physics
         Department, only math exam for Mathematics Department, chemistry for the Chemistry department, computer science
        and math for the Engineering Department, chemistry and physics for the Biotech department. For the departments 
        that need several exams, calculate the mean score and use it to rank the applicants.
4. Now the applicants pass an additional exam for their department: the `admission exam`, and the best score will be chosen to determine the
applicant's ranking: either the mean score or the score of the special exam
5. For each department, choose the N best candidates according to different algorithms.
5. Create a file for each department, name it %department_name%.txt, for example, `physics.txt`. Write the names of the 
   students accepted to the department, and their mean finals score to the corresponding file (one student per line).
