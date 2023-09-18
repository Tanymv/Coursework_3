import json
from utils import get_date_formatting, getting_an_invoice, getting_an_map

filename = "operations.json"


def main():
    def get_operations(filename_):
        """
        функция открывает файл json.
        """
        with open(filename_, 'r', encoding='utf-8') as f:
            operations = json.load(f)
            return operations

    all_operations = get_operations(filename)

    def get_executed_operations(all_operations_):
        """
        функция фильтрует список по EXECUTED.
        """
        list_executed = []
        for item in all_operations_:
            if item == {}:
                continue
            elif item["state"] == "EXECUTED":
                list_executed.append(item)
        return list_executed

    filtered_operations = get_executed_operations(all_operations)

    def sort_by_date(filtered_operations_):
        """
        функция сортирует список по дате.
        """
        return sorted(filtered_operations_, key=lambda operations: operations["date"])[-5:]

    sorted_operations = sort_by_date(filtered_operations)
    sorted_operations.reverse()
    date_formatting = get_date_formatting(sorted_operations)
    map_ = getting_an_map(sorted_operations)
    invoice = getting_an_invoice(sorted_operations)
    for i in range(len(date_formatting)):
        operations_description = sorted_operations[i]["description"]
        separating_the_cards = " ".join(map_[i])
        separating_account = " ".join(invoice[i])
        operations_amount = sorted_operations[i]["operationAmount"]["amount"]
        operations_name = sorted_operations[i]["operationAmount"]["currency"]["name"]
        print(f"{date_formatting[i]} {operations_description}")
        print(f"{separating_the_cards} -> {separating_account}")
        print(f"{operations_amount} {operations_name}\n")


main()
