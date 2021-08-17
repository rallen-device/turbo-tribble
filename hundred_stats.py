import csv

def import_csv_to_dict(file_path: str) -> list:
    """Convert a csv to a list of dictionaries, the first dictionary is the
    headers

    Args:
        file (str): file path

    Returns:
        list(dict): list of dictionaries, each row is a dict
    """
    raw_data_list = []
    with open(file_path, 'r') as file:
        file_reader = csv.reader(file, delimiter=',')
        for row in file_reader:
            raw_data_list.append(row)

    headers = raw_data_list.pop(0)
    data_list = []
    for row in raw_data_list:
        row_data = dict()
        for index, header in enumerate(headers):
            row_data[header] = row[index]
        row_data['match'] = False
        data_list.append(row_data)

    return data_list

def add_none_match_to_list(combined_list: list, other_list: list) -> list:
    """Adds the none matched lists to the combined list

    Args:
        combined_list (list): combined list
        other_list (list): [description]

    Returns:
        list: combined list of dictionaries
    """
    headers = list(combined_list[0].keys())
    for other_list_row in other_list:
        if other_list_row['match'] == False:
            row_data = other_list_row
            for header in headers:
                if header not in row_data:
                    row_data[header] = 0
            combined_list.append(row_data)
    return combined_list



def combine_lists(list1: list, list2: list, key: str) -> list:
    """Combines two lists of dictionary based on the dictionary key

    Args:
        list1 (list): list number 1
        list2 (list]): list number 2
        key (str): key which the lists will be combined

    Returns:
        list: combined list of dictionaries
    """
    combined_list = []
    for list1_row in list1:
        row_data = dict()
        for list2_row in list2:
            if list1_row[key] == list2_row[key]:
                list1_row['match'] = True
                list2_row['match'] = True
                row_data = {**list1_row, **list2_row}
                combined_list.append(row_data)
    
    combined_list = add_none_match_to_list(combined_list, list1)
    combined_list = add_none_match_to_list(combined_list, list2)

    return combined_list

def improve_data(data_list: list) -> list:
    """Takes a list of dictionaries containting the data, make sure all
    dictionaries have the correct data, 0's all missing entries

    Args:
        data_list (list): list of dictionaries containing the data

    Returns:
        list: improved list of data
    """
    headers = list(data_list[0].keys())
    for data in data_list:
        print (data)
        for header in headers:
            if data[header] == '':
                data[header] = '0'

    return data_list



batting_data = import_csv_to_dict('batting.csv')
bowling_data = import_csv_to_dict('bowling.csv')
combined_data = combine_lists(batting_data, bowling_data, 'Name')
combined_data = improve_data(combined_data)

print ((combined_data))
