salary = 250_000

if salary > 523_600:
    taxesOwed = (((salary - 523_600) * .37) + 109_961.25 + 14_240 + 18_852.00 + 10_087.00 + 3_669.00 + 995.50)
    print("They owe $" + str(taxesOwed) + " in taxes")

elif salary > 209_425:
    taxesOwed = (((salary - 209_425) * .35) + 14_240 + 18_852.00 + 10_087.00 + 3_669.00 + 995.50)
    print("They owe $" + str(taxesOwed) + " in taxes")

elif salary > 164_925:
    taxesOwed = (((salary - 164_925) * .32) + 18_852.00 + 10_087.00 + 3_669.00 + 995.50)
    print("They owe $" + str(taxesOwed) + " in taxes")

elif salary > 86_375:
    taxesOwed = (((salary - 86_375) * .24) + 10_087.00 + 3_669.00 + 995.50)
    print("They owe $" + str(taxesOwed) + " in taxes")

elif salary > 40_525:
    taxesOwed = (((salary - 40_525) * .22) + 3_669.00 + 995.50)
    print("They owe $" + str(taxesOwed) + " in taxes")

elif salary > 9950:
    taxesOwed = (((salary - 9_950) * .12) + 995.50)
    print("They owe $" + str(taxesOwed) + " in taxes")

elif salary > 0:
    taxesOwed = salary * .10
    print("They owe $" + str(taxesOwed) + " in taxes")
