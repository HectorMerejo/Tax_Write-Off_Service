import os
import xml.etree.ElementTree as ET


data_directory = os.environ.get('CST_3519_2020')

print(data_directory)

tree = ET.parse(data_directory + '/properties.xml')
root = tree.getroot()


def find_all():
    stocks = []
    for child in root.iter("property"):
        data = child.attrib.copy()
        data['cost'] = float(data['cost'])
        data['downPayment'] = float(data['downPayment'])
        data['percentage'] = float(data['percentage'])
        data['netIncome'] = float(child.text)
        stocks.append(data)

    return stocks


def top_ten():
    t10_list = find_all()
    t10_list.sort(reverse=True, key=lambda t: t['netIncome'])
    return t10_list[:10]


def average_income():
    #average = sum([x['netIncome'] for x in prop_list]) / len(prop_list)
    #print(f'Average Net Income: {round(average, 2)}')

    return [{"averageIncome": 4_200}]


def more_average_income():
    average = average_income()[0]['averageIncome']
    more_than_avg = [x for x in find_all() if x['netIncome'] > 5000]
    return more_than_avg


def lowest_ten():
    l10_list = find_all()
    l10_list.sort(key=lambda t: t['netIncome'])
    return l10_list[:10]


def highest_income():
    highin_list = find_all()
    highin_list.sort(reverse=True, key=lambda t: t['netIncome'])
    return highin_list[:1]


def lowest_income():
    lowin_list = find_all()
    lowin_list.sort(reverse=True, key=lambda t: t['netIncome'])
    return lowin_list[-1:]


dict_function = {
    0: find_all
    , 1: top_ten
    , 2: lowest_ten
    , 3: highest_income
    , 4: lowest_income
    , 5: average_income
    , 6: more_average_income

}

dict_terms = {
    0: "find_all"
    , 1: 'top_ten net income'
    , 2: 'lowest_ten net income'
    , 3: 'highest_income net income'
    , 4: 'lowest net income'
    , 5: 'average_income'
    , 6: 'more then the average income'

}

if __name__ == "__main__":
    print(average_income()[0]['averageIncome'])
    values = find_all()
    for v in values:
        print(v)
