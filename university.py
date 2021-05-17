#!/usr/bin/env python3

from print import admitted_by_exam_priorities, print_admitted_by_exam_priorities

Departments = ['Physics', 'Chemistry', 'Mathematics', 'Engineering', 'Biotech']
max_n = int(input())
# for _ in range(len(departments)):
#    max_n.append(int(input()))

applications = []

# admitted by gpa and priorities
# with open('./applicants.txt', 'r') as file:
#     for line in file:
#         applicant = line.split()
#         applicant[2] = float(applicant[2])
#         applications.append(applicant)
# admission = admitted_by_gpa_priorities(applications, max_n, algo='S')
# print_admitted_by_gpa_priorities(admission='S')

# admitted by score at relevant exam (or some gpa) and priorities
# with open('./applicants.txt', 'r') as file:
#     for line in file:
#         applicant = line.split()
#         applicant[2] = float(applicant[2])
#         applicant[3] = float(applicant[3])
#         applicant[4] = float(applicant[4])
#         applicant[5] = float(applicant[5])
#         applications.append(applicant)

# admission = admitted_by_exam_priorities(applications, max_n, algo='G', priorities=[6, 7, 8])
# print_admitted_by_exam_priorities(admission, algo='G')

# admitted by priorities and best mean score or best score at final admission exam
n_exam = 5  # number of exams to take into consideration: 1 for single exam; 4 for relevant and gpa; 5 for final admission exam
with open('./applicants.txt', 'r') as file:
    for line in file:
        applicant = line.split()
        for n in range(2, 2 + n_exam):
            applicant[n] = float(applicant[n])
        applications.append(applicant)

admission = admitted_by_exam_priorities(applications, max_n, 'B', [7, 8, 9])
print_admitted_by_exam_priorities(admission, 'B')
