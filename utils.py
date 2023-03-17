import requests
import json
from _datetime import datetime

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), "INFO: GOOD"
    return None, f"ERROR: BAD {response.status_code}"

def get_filtered_data(data):
    filtered_data = []
    for i in data:
        if i.keys().__contains__("state"):
            if i["state"] == "EXECUTED":
                filtered_data.append(i)
            else:
                continue
        else:
            continue
    return filtered_data

def format_date(data):
    for i in data:
        if i.keys().__contains__("date"):
            some_date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f")
            formatted_date = some_date.strftime("%d.%m.%Y")
            i["date"] = formatted_date
        else:
            continue
    return data


def refactoring_to(data):
    for i in data:
        x = 0
        if i.keys().__contains__("to"):
            for k,v in i.items():
                if k == "to":
                    for item in v:
                        if item.isalpha() or item == " ":
                            x += 1
        else:
            continue
        text = i["to"][0:x]
        start = i["to"][x+2:x+6]
        done = f'{text} **{start}'
        i["to"] = done
    return data


def refactoring_from(data):
    for i in data:
        x = 0
        if i.keys().__contains__("from"):
            for k,v in i.items():
                if k == "from":
                    for item in v:
                        if item.isalpha() or item == " ":
                            x += 1
        else:
            continue
        text = i["from"][0:x]
        start = i["from"][x:x + 6]
        finish = i["from"][-4:]
        done = f'{text} {start[:4]} {start[4:6]}** **** {finish}'
        i["from"] = done
    return data

def sort_date(data):
    delu = {}
    for i in data:
        if i.keys().__contains__("date"):
            continue
        else:
            delu = i
            data.remove(i)
    data.sort(key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"))
    data.append(delu)
    return data

def summary(data):
    for i in data:
        if i.keys().__contains__("operationAmount"):
            sum = i["operationAmount"]["amount"]
            currency = i["operationAmount"]["currency"]["name"]
            done = f"{sum} {currency}"
            i["operationAmount"] = done
        else:
            continue
    return data


def print_data(data):
    for i in range(5):
        str = f'{data[i]["date"]} {data[i]["description"]}\n{data[i]["from"]} -> {data[i]["to"]}\n{data[i]["operationAmount"]}'
        print(str)
        print("")