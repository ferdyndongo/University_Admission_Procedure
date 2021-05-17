#!/usr/bin/env python3

def print_admission(first_exam, second_exam, third_exam):
    """Print the result of enrollment process given 3 exam scores and fixed the threshold GPA to 60."""
    scores = [first_exam, second_exam, third_exam]
    gpa = sum(scores) / len(scores)
    print(gpa)
    if gpa >= 60:
        print("Congratulations, you are accepted!")
    else:
        print("We regret to inform you that we will not be able to offer you admission.")


def mean_score(score):
    return sum(score) / len(score)


def best_score(mean_exams, final_exam):
    if mean_exams >= final_exam:
        return mean_exams
    else:
        return final_exam


def admitted_by_gpa(n, m):
    """Print the admitted applicants by GPA."""
    applicants = []
    for _ in range(n):
        applicant = input().split()
        applicant[2] = float(applicant[2])
        applicants.append(applicant)
    sorted_applicants = sorted(applicants, key=lambda x: (-x[2], x[0], x[1]))
    print("Successful applicants:")
    for accepted in range(m):
        print(sorted_applicants[accepted][0], sorted_applicants[accepted][1])


def admitted_by_gpa_priorities(applications, n):
    """Return the dictionary of admitted applicants by GPA and priorities given the list of applicants."""
    admission = {}
    for priority in (3, 4, 5):
        sorted_applications = sorted(applications, key=lambda x: (-x[2], x[0], x[1]))
        for applicant in sorted_applications:
            admission.setdefault(applicant[priority], [])
            if len(admission[applicant[priority]]) < n:
                admission[applicant[priority]].append(applicant[:3])
                applications.remove(applicant)
    return admission


def print_admitted_by_gpa_priorities(admission):
    """Print the admitted applicants by GPA and priorities given the dictionary of admitted in input."""
    for keys in sorted(admission):
        print(keys)
        admission[keys] = sorted(admission[keys], key=lambda x: -x[2])
        for admitted in admission[keys]:
            print(admitted[0], admitted[1], admitted[2])
        print()


def admitted_by_exam_priorities(applications, n, algo, priorities):
    """Return the dictionary of admitted applicants by relevant exam score and priorities given the list of applicants."""
    admission = {}
    for priority in priorities:
        tmp = applications
        chosen = {}
        for applicant in tmp:
            chosen.setdefault(applicant[priority], [])
            chosen[applicant[priority]].append(applicant)

        for keys in sorted(chosen):
            if keys == 'Physics':
                if algo == 'S':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-x[2], x[0], x[1]))
                elif algo == 'G':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-((x[2] + x[4])/2), x[0], x[1]))
                elif algo == 'B':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-best_score(((x[2] + x[4])/2), x[6]), x[0], x[1]))
            if keys == 'Chemistry':
                if algo == 'B':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-best_score(x[3], x[6]), x[0], x[1]))
                else:
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-x[3], x[0], x[1]))
            if keys == 'Mathematics':
                if algo == 'B':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-best_score(x[4], x[6]), x[0], x[1]))
                else:
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-x[4], x[0], x[1]))
            if keys == 'Engineering':
                if algo == 'S':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-x[5], x[0], x[1]))
                elif algo == 'G':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-((x[5] + x[4])/2), x[0], x[1]))
                elif algo == 'B':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-best_score(((x[5] + x[4])/2), x[6]), x[0], x[0], x[1]))
            if keys == 'Biotech':
                if algo == 'S':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-x[3], x[0], x[1]))
                elif algo == 'G':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-((x[3] + x[2])/2), x[0], x[1]))
                elif algo == 'B':
                    chosen[keys] = sorted(chosen[keys], key=lambda x: (-best_score(((x[3] + x[2])/2), x[6]), x[0], x[1]))

        for key in chosen:
            admission.setdefault(key, [])
            for index, value in enumerate(chosen[key]):
                if len(admission[key]) < n:
                    admission[key].append(value)
                    # chosen.get(dep).remove(value)
                    applications.remove(value)
    return admission


def print_admitted_by_exam_priorities(admission, algo):
    """Print the admitted applicants by highest score at relevant exam and priorities given the dictionary of admitted in input."""
    for keys in sorted(admission):
        if keys == 'Physics':
            if algo == 'S':
                admission[keys] = sorted(admission[keys], key=lambda x: (-x[2], x[0], x[1]))
            elif algo == 'G':
                admission[keys] = sorted(admission[keys], key=lambda x: (-((x[2] + x[4])/2), x[0], x[1]))
            elif algo == 'B':
                admission[keys] = sorted(admission[keys], key=lambda x: (-best_score(((x[2] + x[4])/2), x[6]), x[0], x[1]))
        if keys == 'Chemistry':
            if algo == 'B':
                admission[keys] = sorted(admission[keys], key=lambda x: (-best_score(x[3], x[6]), x[0], x[1]))
            else:
                admission[keys] = sorted(admission[keys], key=lambda x: (-x[3], x[0], x[1]))
        if keys == 'Mathematics':
            if algo == 'B':
                admission[keys] = sorted(admission[keys], key=lambda x: (-best_score(x[4], x[6]), x[0], x[1]))
            else:
                admission[keys] = sorted(admission[keys], key=lambda x: (-x[4], x[0], x[1]))
        if keys == 'Engineering':
            if algo == 'S':
                admission[keys] = sorted(admission[keys], key=lambda x: (-x[5], x[0], x[1]))
            elif algo == 'G':
                admission[keys] = sorted(admission[keys], key=lambda x: (-((x[5] + x[4])/2), x[0], x[1]))
            elif algo == 'B':
                admission[keys] = sorted(admission[keys], key=lambda x: (-best_score(((x[5] + x[4])/2), x[6]), x[0], x[1]))
        if keys == 'Biotech':
            if algo == 'S':
                admission[keys] = sorted(admission[keys], key=lambda x: (-x[3], x[0], x[1]))
            elif algo == 'G':
                admission[keys] = sorted(admission[keys], key=lambda x: (-((x[3] + x[2])/2), x[0], x[1]))
            elif algo == 'B':
                admission[keys] = sorted(admission[keys], key=lambda x: (-best_score(((x[3] + x[2])/2), x[6]), x[0], x[1]))

        if algo == 'S':
            print(keys)
            for admitted in admission[keys]:
                if keys == 'Physics':
                    print(admitted[0], admitted[1], admitted[2])
                if keys == 'Chemistry':
                    print(admitted[0], admitted[1], admitted[3])
                if keys == 'Mathematics':
                    print(admitted[0], admitted[1], admitted[4])
                if keys == 'Engineering':
                    print(admitted[0], admitted[1], admitted[5])
                if keys == 'Biotech':
                    print(admitted[0], admitted[1], admitted[3])
                print()
        elif algo == 'G':
            path = keys.lower() + '.txt'
            with open(file=path, mode='w', encoding='utf-8') as output_file:
                for admitted in admission[keys]:
                    if keys == 'Physics':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str((admitted[2] + admitted[4]) / 2) + '\n')
                    if keys == 'Chemistry':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str(admitted[3]) + '\n')
                    if keys == 'Mathematics':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str(admitted[4]) + '\n')
                    if keys == 'Engineering':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str((admitted[5] + admitted[4]) / 2) + '\n')
                    if keys == 'Biotech':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str((admitted[3] + admitted[2]) / 2) + '\n')
        elif algo == 'B':
            path = keys.lower() + '.txt'
            with open(file=path, mode='w', encoding='utf-8') as output_file:
                for admitted in admission[keys]:
                    if keys == 'Physics':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str(best_score(((admitted[2] + admitted[4])/2), admitted[6])) + '\n')
                    if keys == 'Chemistry':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str(best_score(admitted[3], admitted[6])) + '\n')
                    if keys == 'Mathematics':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str(best_score(admitted[4], admitted[6])) + '\n')
                    if keys == 'Engineering':
                        output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str(best_score(((admitted[5] + admitted[4])/2), admitted[6])) + '\n')
                    if keys == 'Biotech':
                        pass
                output_file.write(admitted[0] + ' ' + admitted[1] + ' ' + str(best_score(((admitted[3] + admitted[2])/2), admitted[6])) + '\n')
