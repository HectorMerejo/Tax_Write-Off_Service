import os
import xml.etree.cElementTree as ET
import pprint

from statistics import mean
from calculate_result import getResults

data_directory = os.environ.get('CST_3519_2020')

# Printing attribute of the retirement tag
def retirement_tag(mode="s01"):
    fileName = mode + '.retirement.xml'
    tree = ET.parse(data_directory + '/_retirement/' + fileName)
    root = tree.getroot()

    retirement = next(root.iter("retirement"))
    data = retirement.attrib.copy()
    data['years'] = int(data['years'])
    data['fileName'] = fileName
    data['age'] = int(data['age'])
    data["increasedContribution"] = float(data["increasedContribution"])
    data["interestRate"] = float(data["interestRate"])
    data["maxSalary"] = float(data["maxSalary"])
    data['raise'] = float(data['raise'])
    data["startingBalance"] = float(data["startingBalance"])
    return data


# Printing attribute of the incomeSalary attribute
def yearly_tag(mode="s01"):
    tree = ET.parse(data_directory + '/_retirement/' + mode + '.retirement.xml')
    root = tree.getroot()

    data_list = []

    for child in root.iter("yearlyIncome"):
        data = child.attrib.copy()
        data['year'] = int(data['year'])
        data['contribution'] = float(data['contribution'])
        data['Salary'] = float(child.text)
        data_list.append(data)

    return data_list


def average_income(mode="s01"):
    tree = ET.parse(data_directory + '/_retirement/' + mode + '.retirement.xml')
    root = tree.getroot()
    salaries = mean([float(x.text) for x in root.iter("yearlyIncome")])
    return salaries


def getAllRetirementSettings(mode="s01"):
    retirement = retirement_tag(mode)
    yearlyIncome = yearly_tag(mode)[-1]  # last or current yearlyIncome
    averageIncome = average_income(mode)

    print(retirement)

    age = retirement["age"]
    numberOfYears = retirement["years"]
    beginningBalance = retirement["startingBalance"]
    currentSalary = yearlyIncome["Salary"]
    interestRate = retirement['interestRate']
    contribution = yearlyIncome['contribution']

    userSettings = {
        "retirement": retirement,
        "yearlyIncome": yearlyIncome,
        "averageIncome": averageIncome,
    }

    calculatedUserSettings = {
        "fileSettings": userSettings,
        "results": getResults(age=age, numberOfYears=numberOfYears, beginningBalance=beginningBalance,
                              interestRate=interestRate, currentSalary=currentSalary, contribution=contribution)
    }

    return calculatedUserSettings


if __name__ == '__main__':
    modeSelection = "s03"
    results = getAllRetirementSettings(mode=modeSelection)
    pprint.pprint(results)
