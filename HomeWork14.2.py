import module_group
import module_student


my_group = module_group.Group('Python-It-Generation')


my_group.add_to_group(module_student.Student('Heorhii', 'Karabetskyi', 'male'))
my_group.add_to_group(module_student.Student('Hanna', 'Karabetska', 'female'))
my_group.add_to_group(module_student.Student('Oleksandr', 'Fedorov', 'male'))
my_group.add_to_group(module_student.Student('Ivan', 'Stoianov', 'male'))
my_group.add_to_group(module_student.Student('Inna', 'Stoianova', 'female'))
my_group.add_to_group(module_student.Student('Marian', 'Stoianov', 'male'))
my_group.add_to_group(module_student.Student('Oleksii', 'Leemon', 'male'))
my_group.add_to_group(module_student.Student('Maria', 'Cheban', 'female'))
my_group.add_to_group(module_student.Student('Viktor', 'Dadisha', 'male'))
#my_group.add_to_group(module_student.Student('Mark', 'Karabetskyi', 'male'))
#my_group.add_to_group(module_student.Student('Oleksii', 'Fevrov', 'male'))
#my_group.add_to_group(module_student.Student('Dmitro', 'Sezonov', 'male'))
#my_group.add_to_group(module_student.Student('Vitalyina', 'Zelenska', 'female'))
print(my_group)
print('-' * 30)
for student in my_group.search_student('Stoianov'):
    print(student.name, student.surname, '-', student.gender)
