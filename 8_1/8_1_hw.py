# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# with open('Phonebook.txt', '+w', encoding='utf-8') as file:
#      print(file)

def writing_txt():  #get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
         data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\n\n')
    return

def choice():
    flag = input(
        'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    while (flag.lower() == 'да'):
        choice_action = input(
            'Введите \'да\', если хотите записать новые данные, или любой другой символ, если хотите осуществить поиск в консоли: ')
        if choice_action.lower() == 'да':
             writing_txt()
        else:
             view()
        flag = input(
            'Для продолжения работы нажмите \'да\', или любой символ для завершения работы... ')
    print('Программа завершена.')


def view():
    user_sign = input("Введите фамилию для поиска: ")
    with open('Phonebook.txt', 'r', encoding='utf-8') as file:
       find_sign = file.read().count(user_sign)
       if  find_sign == True:
           print("Такой абонент есть")
       else:
           print("Такого абонента нет")


def from_file(file):
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary

if __name__ == '__main__':
    choice()