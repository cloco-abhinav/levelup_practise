class Chair:
    def sit_on(self):
        return 'Chair'

class Table:
    def place_items_on(self):
        raise 'Table'

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair"

class ModernTable(Table):
    def place_items_on(self):
        return "Placing items on a modern table"

class ClassicChair(Chair):
    def sit_on(self):
        return "Sitting on a classic chair"

class ClassicTable(Table):
    def place_items_on(self):
        return "Placing items on a classic table"

class FurnitureFactory:
    def create_chair(self):
        raise NotImplementedError

    def create_table(self):
        raise NotImplementedError

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()

class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_table(self):
        return ClassicTable()

class FurnitureStore:
    def __init__(self, factory: FurnitureFactory):
        self.factory = factory
        self.chair = self.factory.create_chair()
        self.table = self.factory.create_table()

    def display_furniture(self):
        print(self.chair.sit_on())
        print(self.table.place_items_on())

def client_code(factory: FurnitureFactory):
    store = FurnitureStore(factory)
    store.display_furniture()

print("Using Modern Furniture Factory:")
client_code(ModernFurnitureFactory())

print("\nUsing Classic Furniture Factory:")
client_code(ClassicFurnitureFactory())
