# Currency Converter

import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")


url = "https://www.iban.com/currency-codes"
website = requests.get(url)
website_soup = BeautifulSoup(website.text, "html.parser")

country_and_code = []
informations = website_soup.find("tbody").find_all("tr")
for information in informations:
    data = information.find_all("td")
    country = data[0].text
    alpha3_code = data[2].text
    currency = data[1].text
    if currency != 'No universal currency':
        country_and_code.append([country, alpha3_code])
    else:
        pass


def first_ask():
    try:
        choice = int(input("#: "))
        if choice in dictionary.keys():
            first_result = (dictionary[choice])
            print(f"{first_result[0]}\n")
            code.append(first_result[1])
        else:
            print("Choose a number from the list.")
            first_ask()
    except ValueError:
        print("That wasn't a number.")
        first_ask()


def second_ask():
    try:
        choice = int(input("#: "))
        if choice in dictionary.keys():
            second_result = (dictionary[choice])
            print(f"{second_result[0]}\n")
            code.append(second_result[1])
        else:
            print("Choose a number from the list.")
            second_ask()
    except ValueError:
        print("That wasn't a number.")
        second_ask()


def convert_ask():
    try:
        convert_input = int(
            input(
                f"How many {code[0]} do you want to convert to {code[1]}?\n"))
        convert_input = str(convert_input)
        url = "https://transferwise.com/gb/currency-converter/" + code[0].lower(
        ) + "-to-" + code[1].lower() + "-rate?amount=" + convert_input
        transferwise = requests.get(url)
        transferwise_soup = BeautifulSoup(transferwise.text, "html.parser")
        information = transferwise_soup.find("tbody").find(
            "td", {
                "value": "1"
            }).text
        information = information.replace(f"{code[1]}", "")
        information = float(convert_input) * float(information)
        converted_money = (format_currency(information,
                                           code[1],
                                           locale="ko_KR"))
        print(f"{code[0]} {float(convert_input)} is {converted_money}")
    except ValueError:
        print("That wasn't a number.")
        convert_ask()


print("Welcome to CurrencyConvert PRO 2000\n")
dictionary = {}
code = []
for index, item in enumerate(country_and_code, start=0):
    dictionary[index] = item
    print('#', index, item[0])
first_ask()
print("Now choose another country\n")
second_ask()
convert_ask()