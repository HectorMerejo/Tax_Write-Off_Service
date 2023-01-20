import os
import xml.etree.cElementTree as ET

data_directory = os.environ.get('CST_3519_2020')

fileName = '/taxRules.xml'
tree = ET.parse(data_directory + fileName)
root = tree.getroot()


def taxRules():
    data_list = []
    for child in root.iter("taxRule"):
        data = child.attrib.copy()
        data['status'] = str(data['status'])
        data['rate'] = float(data['rate'])
        data['range1'] = float(data['range1'])

        if data['range2'] == 'max':
            data['range2'] = float('inf')
        else:
            data['range2'] = float(data['range2'])
        data_list.append(data)

    return data_list


if __name__ == '__main__':
    values = taxRules()
    for v in values:
        print(v)
