# pirveli davaleba
# class MyList(object):
#     def __init__(self, data):
#         self.data = data
#
#     def __add__(self, other):
#         return self.data+other
#
#     def __mul__(self, other):
#         result = []
#         for i in range(1,other):
#             result+= self.data
#
#         return result
#
#     def __str__(self):
#         return f"{self.data}"
#
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1+l2
# l4 = l1*3
# print(str(l3))
#
#
# meore davaleba


class TestPaper:
    def __init__(self, subject, mark_scheme, pass_mark):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken."

    def take_test(self, paper, results):
        if isinstance(paper, TestPaper):
            score = 0
            count = len(paper.mark_scheme)
            per = float(paper.pass_mark.strip("%"))

            for i in range(count):
                if paper.mark_scheme[i] == results[i]:
                    score += 1
            current_per = (score * 100) / count

            if isinstance(self.tests_taken, str):
                self.tests_taken = {}

            if current_per >= per:
                self.tests_taken[paper.subject] = f"Passed! ({int(current_per)}%)"
            else:
                self.tests_taken[paper.subject] = f"Failed! ({int(current_per)}%)"


paper1 = TestPaper("Maths", ["1A", "2D", "3C", "4B"], "56%")
paper2 = TestPaper("Computing", ["1D", "2C", "3A", "4B"], "15%")

student1 = Student()

print(student1.tests_taken)

student1.take_test(paper1, ["1A", "2D", "3B", "4A"])
student1.take_test(paper2, ["1D", "2B", "3A", "4B"])

print(student1.tests_taken)