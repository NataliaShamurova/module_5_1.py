class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors  # кол-во этажей
        #self.new_floor = new_floor    # номер этажа

    def go_to(self, new_floor):

            if new_floor > self.number_of_floors:
               print("Такого этажа не существует")
            else:
                l = list(range(1, new_floor + 1))
                for i in l:
                    print(f'{i}')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 5)
h1.go_to(5)
h2.go_to(10)

