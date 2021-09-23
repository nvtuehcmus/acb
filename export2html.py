import dominate
from dominate.tags import *
from statistics import mean
from copy import deepcopy


def max_index(data):
    result = []
    max_avg = max(data, key=lambda r: r[1])
    for i in range(len(data)):
        if(data[i][1] == max_avg[1]):
            result.append(i)

    return result


def get_data(path):
    f = open(path, "r")
    result = []
    ls_data_element = f.read().split("\n")
    [result.append(e.split(";")) for e in ls_data_element]
    return result


def solve_data(data, sort=0):
    result = []
    for e in data:
        number_array = [int(numeric_string) for numeric_string in e[1:]]
        result.append([e[0], mean(number_array), min(
            number_array), max(number_array)])
    if(sort):
        result.sort(key=lambda r: r[0])
    return result


student_data = solve_data(get_data("testdata.csv"), 1)
max_avg_students = max_index(student_data)
s = [student_data[max_avg_students[0]][0] for s in max_avg_students]

test_data = [["Max", "Min", "Mean"], [97, 2, 54, 6], [100, 1, 48, 97],
             [99, 1, 48, 81], [100, 1, 53, 6], [100, 5, 52, 8]]
doc = dominate.document(title='export doc demo')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(cls="container"):
        h1("test data")
        with table(id="tb-data-test", cls="table table-striped"):
            with thead():
                with tr():
                    for i in range(len(test_data)):
                        if(i == 0):
                            th("")
                        else:
                            th("test ", i)
            with tbody():

                for i in range(len(test_data[0])):
                    with tr():
                        td(test_data[0][i])
                        for d in test_data[1:]:
                            td(d[i])
        h1("Hightest mean")
        p("the hightest avg score is ",
          str(student_data[max_avg_students[0]][1]), ". The student(s)", ", ".join([student_data[max_avg_students[0]][0] for s in max_avg_students]))

        with table(id="tb-data-student", cls="table table-striped"):
            with thead():
                with tr():
                    th("Student")
                    th("Mean")
                    th("Min")
                    th("Max")
            with tbody():

                for i in range(len(student_data)):
                    with tr():
                        for e in student_data[i]:
                            td(e)

print(doc)
