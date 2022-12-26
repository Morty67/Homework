
class ErrorLimitGroup(BaseException):
    def __init__(self, limit_group):
        self.limit_group = limit_group

    def __str__(self):
        return f'Sorry, group is full {self.limit_group}'
class Group:

    def __init__(self, title: str, max_group:int=10):
        self.title = title
        self.max_group = max_group
        self.students_list = []


    def add_to_group(self, student: str):

        if student not in self.students_list and len(self.students_list) < self.max_group:
            self.students_list.append(student)

        if len(self.students_list) >= self.max_group:
            raise ErrorLimitGroup('')


    def remove_student(self, student: str):
        if student in self.students_list:
            self.students_list.remove(student)

    def search_student(self, surname: str):
        search = []
        for student in self.students_list:
            if student.surname == surname:
                search.append(student)
        return search

    def __str__(self):
        return f"{'Group:'} {self.title} \n{'-' * 30}\n" + \
           '\n'.join(map(str, self.students_list)) + '\n'

