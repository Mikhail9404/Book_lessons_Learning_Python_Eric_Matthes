book_1 = 'book_1.txt'
book_2 = 'book_2.txt'
book_3 = 'book_4.txt'


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"\nИзвините! Файл с именем {filename} не найден! Проверьте правильность указанного названия файла!")
    else:
        word_find = input('Введите искомое слово: ')
        count = content.lower().count(word_find)
        print(f"\nКоличество повторяющихся вхождений слова '{word_find}' равно: {count}")


count_words(book_3)