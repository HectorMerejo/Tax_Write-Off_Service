import pprint


def getResults():
    mylist = []
    beginningBalance = 1500
    for n in range(1, 37 + 1):
        currentRow = {"age": 23 + n,
                      "numOfYears": n,
                      "beginningBalance": beginningBalance,
                      "currentSalary": 72_000,
                      "dividendsAndGrowth": n,
                      "yearlyDeposit": 8_640,
                      "yearlyTotal": n}

        currentRow["dividendsAndGrowth"] = currentRow["beginningBalance"] * 0.02
        currentRow["yearlyTotal"] = currentRow["dividendsAndGrowth"] + currentRow["yearlyDeposit"] + currentRow[
            "beginningBalance"]

        beginningBalance = currentRow["yearlyTotal"]
        mylist.append(currentRow)

    return mylist


if __name__ == "__main__":
    z = getResults()
    pprint.pprint(z)
