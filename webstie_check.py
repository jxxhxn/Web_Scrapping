# Website Checker


import requests
import os

while True:
    print("Welcome to IsItDown.py!")
    input_url = input(
        "Please write a URL or URLs you want to check. (separated by comma)\n")
    converted_url = []
    input_url = input_url.split(',')

    for url in input_url:
        converted_url.append(url.strip())

    for i in range(len(converted_url)):
        converted_url[i] = converted_url[i].lower()
        if ("." not in converted_url[i]):
            print(f"{converted_url[i]} is not a valid URL.")
            break
        elif converted_url[i].startswith("https://"):
            pass
        else:
            converted_url[i] = "https://" + converted_url[i]
        try:
            r = requests.get(converted_url[i])
            r.raise_for_status()
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout):
            print(f"{converted_url[i]} is down!")
        else:
            print(f"{converted_url[i]} is up!")
    run = True
    while (run == True):
        answer = input("Do you want to start over? y/n ")
        if answer == 'y':
            os.system('clear')
            break
        elif answer == 'n':
            print("k, bye!")
            run = False
        else:
            print("That's not a valid answer.")
    if run == False:
        break