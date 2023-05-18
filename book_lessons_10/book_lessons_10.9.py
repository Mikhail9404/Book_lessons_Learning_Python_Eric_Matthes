filename_cats = 'names_cats.txt'
filename_dogs = 'names_dogs.txt'
filename_not_exist = 'names_not_exist.txt'


def open_file(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            names = f.read()
    except FileNotFoundError:
        pass
#        print(f"\nИзвините! Файл с именем {filename} не найден! Проверьте правильность указанного названия файла!")
    else:
        print(f"\nКлички животных из файла {filename}: \n{names}")


open_file(filename_dogs)
open_file(filename_cats)
open_file(filename_not_exist)