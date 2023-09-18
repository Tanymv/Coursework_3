import datetime


def get_date_formatting(list_):
    a = []
    """
    функция форматирует дату.
    """
    for i in list_:

        date_time_date = datetime.datetime.fromisoformat(i["date"])
        a.append(date_time_date.strftime("%d.%m.%Y"))
    return a


def getting_an_map(list_):
    a = []
    """
    функция выводит зашифрованную карту.
    """
    for i in list_:
        if len(i) == 6:
            a.extend([["Данных о карте нет"]])
        else:
            split_account = i['from'].split()
            if len(split_account[1]) == 20:
                score = split_account[1]
                char = score[0:6] + '*' * (len(score) - 10) + score[-4:]
                split_account_ = [char[i:i + 4] for i in range(0, len(char), 4)]
                split_account_ = ' '.join(split_account_)
                a.extend([[split_account[0], split_account_]])

            elif len(split_account[1]) == 16:
                score = split_account[1]
                char = score[0:6] + '*' * (len(score) - 10) + score[-4:]
                split_account_ = [char[i:i + 4] for i in range(0, len(char), 4)]
                split_account_ = ' '.join(split_account_)
                a.extend([[split_account[0], split_account_]])

            elif len(split_account[1]) != 16:
                score = split_account[2]
                char = score[0:6] + '*' * (len(score) - 10) + score[-4:]
                split_account_ = [char[i:i + 4] for i in range(0, len(char), 4)]
                split_account_ = ' '.join(split_account_)
                a.extend([[split_account[0], split_account[1], split_account_]])
    return a


def getting_an_invoice(list_):
    a = []
    """
    функция выводит зашифрованный счет.
    """
    for i in list_:

        if i['to']:
            split_account = i['to'].split()
            score = split_account[1]
            char = '*' * (len(score) - 18) + score[-4:]
            a.extend([[split_account[0], char]])
        else:
            continue
    return a
