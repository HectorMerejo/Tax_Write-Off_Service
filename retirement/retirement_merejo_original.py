import os
import xml.etree.cElementTree as ET

data_directory = os.environ.get('CST_3519_2020')

print(data_directory)

tree = ET.parse(data_directory + '/s01.retirement.xml')
root = tree.getroot()


def retirement_element():
    retirement = []
    for child in root.iter("retirement"):
        data = child.attrib.copy()
        data['years'] = float(data['years'])
        data['age'] = float(data['age'])
        data['raise'] = float(data['raise'])
        retirement.append(data)
    return retirement


def yearly_element():
    retirement = []
    for child in root.iter("yearlyIncome"):
        data = child.attrib.copy()
        data['year'] = int(data['year'])
        data['contribution'] = float(data['contribution'])
        data['yearlyIncome'] = float(child.text)
        retirement.append(data)
    return retirement


def retirement_data(y):
    retirement = sorted(y, key=lambda x: -x['years'], reverse=True)
    for x in retirement[:1]:
        print(x)


def yearly_data(y):
    retirement = sorted(y, key=lambda x: -x['year'], reverse=True)
    for x in retirement[:6]:
        print(x)


def average_income(i):
    retirement = sorted(i, key=lambda x: -x["yearlyIncome"])
    average = sum([x['yearlyIncome'] for x in retirement]) / len(retirement)
    print(round(average, 2))


if __name__ == '__main__':
    my_func = {
        "Retirement Attributes": retirement_data
    }

    for key, funct in my_func.items():
        print(f"{key}")
        data = retirement_element()
        funct(data)

    my_func = {
        "Yearly Attributes & Income": yearly_data
        , "Average Yearly Income": average_income
    }

    for key, funct in my_func.items():
        print(f"{key}")
        data = yearly_element()
        funct(data)
