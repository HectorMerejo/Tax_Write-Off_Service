def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def clean_up(data):
    is_trillion = data.endswith("T")
    is_billion = data.endswith("B")
    is_million = data.endswith("M")
    value = 0
    if is_trillion:
        value = float(data.replace("T", "")) * 1_000
    elif is_billion:
        value = float(data.replace("B", "")) * 1
    elif is_million:
        value = float(data.replace("M", "")) / 1_000

    return value


def fixNumber(data):
    value = 0
    data = data.strip()
    if data.endswith("%"):
        value = float(data.replace("%", "")) / 100
    elif not is_number(data):
        value = 0
    else:
        value = float(data)

    return value


def original_price(current_value, _5YearGrowth):
    price = 0
    if _5YearGrowth > 0:
        price = current_value / _5YearGrowth
    else:
        price = current_value - (current_value * _5YearGrowth)
    return price


    #  for v in ['2.3T', '5B', '250M']:
    #  value = clean_up(v)
    #  data_type = type(value)
    #  print(f"value in the billions: {value} the data type is {data_type}")

    for x in ['-17%', '300', '100', '100', '142.33', '0.80%', 'N/A']:
        result = fixNumber(x)
        the_type = type(result)
        print(f"result is {result}, the data type is {the_type}")
