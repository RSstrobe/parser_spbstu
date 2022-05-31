def prepare_list_for_dataframe(list_after_clean):
    """
    Функция для приведения списка к необходимому виду.
    :param list_after_clean: list after data_cleaning() function
    :return: list ready for convert to dataframe
    """
    final_list = []
    for string in list_after_clean:
        if 'DATES' in string and len(string) == 2:
            final_list.append([string[1]] + [None] * 15)
        if any(element in string for element in ['COMPDAT', 'COMPDATL']):
            if 'DATES' in string:
                indices = [i for i, x in enumerate(string) if x in ["COMPDAT", "COMPDATL"]]
                for ind in indices:
                    i = 1
                    while ind + i not in indices and (ind + i) <= (len(string) - 1):
                        l = string[ind + i].split()
                        if string[ind] == "COMPDAT":
                            l.insert(0, string[1])
                            l.insert(2, None)
                            final_list.append(l)
                        elif string[ind] == "COMPDATL":
                            l.insert(0, string[1])
                            final_list.append(l)
                        i += 1
            if 'DATES' not in string:
                indices = [i for i, x in enumerate(string) if x in ["COMPDAT", "COMPDATL"]]
                for ind in indices:
                    i = 1
                    while ind + i not in indices and (ind + i) <= (len(string) - 1):
                        l = string[ind + i].split()
                        if string[ind] == "COMPDAT":
                            l.insert(0, None)
                            l.insert(2, None)
                            final_list.append(l)
                        elif string[ind] == "COMPDATL":
                            l.insert(0, None)
                            final_list.append(l)
                        i += 1
    return final_list
