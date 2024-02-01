class Menu:
    def __init__(self, menu_list):
        self.list = menu_list
        self.__menu_dicc = {0:None}
        self.__actual_position = 1
        self.__submenu_dicc = {}

        for i in self.list:
            
            if i != 0 or i <= self.list:
                self.__menu_dicc[self.__actual_position] = self.list[self.__actual_position-1]
                self.__submenu_dicc[self.__actual_position] = None
                self.__actual_position += 1

        self.__menu_dicc[self.__actual_position + 1] = None
        self.__actual_position = 1

    # Change the first nun used value of the dict
    def set_first_non_used_value(self, value):
        self.__menu_dicc[0] = value

    # Change the value of the last non used space of the dict
    def set_last_non_used_value(self, value):
        self.__menu_dicc[self.length() + 1] = value

    # Returns the length of the list
    def length(self):
        return len(self.list)

    # Iterate to the next element in the menu
    def next(self):
        if self.__actual_position < self.length():
            self.__actual_position += 1

    # Iterate to the previous element in the menu
    def previous(self):
        if self.__actual_position > 1:
            self.__actual_position -= 1

    # Returns the actual value of the menu
    def get_value(self):
        return self.__menu_dicc.get(self.__actual_position)
    
    # Returs the key related to the actual value
    def get_key(self):
        return list(self.__menu_dicc.keys())[self.__actual_position]
        
    # Return a list whith the previous value, the actual value, and the next value
    def get_triplet_value(self):
        triplet_list = []
        triplet_list.append(self.__menu_dicc.get(self.__actual_position - 1))
        triplet_list.append(self.__menu_dicc.get(self.__actual_position))
        triplet_list.append(self.__menu_dicc.get(self.__actual_position + 1))

        return triplet_list

    # Return a list whith the previous key, the actual key, and the next key
    def get_triplet_key(self):
        triplet_list = []
        triplet_list.append(list(self.__menu_dicc.keys())[self.__actual_position - 1])
        triplet_list.append(list(self.__menu_dicc.keys())[self.__actual_position])
        triplet_list.append(list(self.__menu_dicc.keys())[self.__actual_position + 1])

        return triplet_list
    
    # Create a submenu for a key whith a menu
    def set_submenu(self, key, menu_list):
        self.__submenu_dicc[key] = Menu(menu_list)

    # Returns the menu releted whit a key
    def get_submenu(self, key):
        return self.__submenu_dicc.get(key)

