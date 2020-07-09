class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"ITEM: {self.name} \nINFO: {self.description}"

if __name__ == "__main__":
    my_item = Item("Key", "Seems to unlock something ...")
    print(my_item)