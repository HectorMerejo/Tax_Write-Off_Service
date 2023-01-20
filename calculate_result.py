import pprint


def getResults(age=24, numberOfYears=37, beginningBalance=1_500, currentSalary=72_000, interestRate=.02,
               contribution=.12):  # numberOfYears makes it dynamic
    mylist = []
    for n in range(1, numberOfYears + 1):
        dividendAndGrowth = beginningBalance * interestRate
        yearlyDeposit = currentSalary * contribution
        yearlyTotal = beginningBalance + dividendAndGrowth + yearlyDeposit

        currentRow = {"age": age,
                      "numberOfYears": n,
                      "beginningBalance": beginningBalance,
                      "currentSalary": currentSalary,
                      "dividendsAndGrowth": dividendAndGrowth,
                      "yearlyDeposit": yearlyDeposit,
                      "yearlyTotal": yearlyTotal}

        mylist.append(currentRow)

        beginningBalance = yearlyTotal
        age = age + 1

    return mylist


if __name__ == "__main__":
    z = getResults()  # can change any variables from here in the () i.e. age=35, numberOfYears=22
    pprint.pprint(z)
