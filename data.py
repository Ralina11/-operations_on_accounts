from utils import *


def main ():
    URL_OPERATIONS = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679010338980&signature=rK6z51QR_6FxbPj9wJJnlFJEm4jjKMELRYPlhb-0bGk&downloadName=operations.json"
    data, info = get_data(URL_OPERATIONS)
    if not data:
        exit(info)
    print(info)

    data = get_filtered_data(data)
    data = format_date(data)
    data = refactoring_to(data)
    data = refactoring_from(data)
    data = sort_date(data)
    data = summary(data)
    print_data(data)


if __name__ == '__main__':
    main()