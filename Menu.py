class Menu:
    def __init__(self, menu_list):
        self.__menu_list = menu_list
        self.__menu_dicc = {0: ""}
        self.__actual_position = 1

        # Populate dictionary with 1-based index
        for index, item in enumerate(self.__menu_list, start=1):
            self.__menu_dicc[index] = item
            
        self.__menu_dicc[len(self.__menu_list) + 1] = ""

    # Change the first nun used value of the dict
    def set_first_non_used_value(self, value):
        self.__menu_dicc[0] = value

    # Change the value of the last non used space of the dict
    def set_last_non_used_value(self, value):
        self.__menu_dicc[self.length() + 1] = value

    # Returns the length of the list
    def length(self):
        return len(self.__menu_list)

    # Iterate to the next element in the menu
    def next(self):
        if self.__actual_position < self.length():
            self.__actual_position += 1
        else:
            self.__actual_position = 1

    def __show_next(self):
        if self.__actual_position < self.length():
            return self.__actual_position + 1
        else:
            return 1

    # Iterate to the previous element in the menu
    def previous(self):
        if self.__actual_position > 1:
            self.__actual_position -= 1
        else:
            self.__actual_position = self.length()

    def __show_previous(self):
        if self.__actual_position > 1:
            return self.__actual_position - 1
        else:
            return self.length()

    # Returns the actual value of the menu
    def get_value(self):
        return self.__menu_dicc.get(self.__actual_position)

    # Returns the key related to the actual value
    def get_key(self):
        return list(self.__menu_dicc.keys())[self.__actual_position]

    # Return a list with the previous value, the actual value, and the next value
    def get_triplet_value(self):
        triplet_list = []
        triplet_list.append(self.__menu_dicc.get(self.__show_previous()))
        triplet_list.append(self.__menu_dicc.get(self.__actual_position))
        triplet_list.append(self.__menu_dicc.get(self.__show_next()))

        return triplet_list

    # Return a list with the previous key, the actual key, and the next key
    def get_triplet_key(self):
        triplet_list = []
        triplet_list.append(list(self.__menu_dicc.keys())[self.__show_previous()])
        triplet_list.append(list(self.__menu_dicc.keys())[self.__actual_position])
        triplet_list.append(list(self.__menu_dicc.keys())[self.__show_next()])

        return triplet_list