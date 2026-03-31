students = {
    "Иванов": {"китайский", "английский"},
    "Петров": {"английский", "немецкий"},
    "Сидоров": {"китайский", "французский"},
    "Кузнецов": {"испанский"},
    "Смирнов": {"китайский", "японский"}
}
all_languages = set()
chinese_students = []
for student, langs in students.items():
    all_languages.update(langs)
    if "китайский" in langs:
        chinese_students.append(student)
print("Все языки:", sorted(all_languages))
print("Студенты, знающие китайский:", chinese_students)