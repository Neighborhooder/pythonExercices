class MyClass:
    def __init__(self):
        self._my_dict = {"a":123, "b": True}

    def set_c(self, value):
        self._my_dict["c"] = value

    def get_c(self):
        return self._my_dict["c"]

    # I slightly change this function in order to duplicate the 'a' entry inside dictionary
    # I called it 'a2' because a dictionary can only have one key of each value
    def get_dict_with_twice_a(self):
        buffer = self._my_dict
        buffer['a2'] = buffer['a']
        return buffer

# iniciate and object of class MyClass
p1 = MyClass()
# duplicate a entrance in dictionary
p1.get_dict_with_twice_a()
# set 'c' to 72
p1.set_c(72)
# print dictionary
print(p1._my_dict)
