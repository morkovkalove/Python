class Barbershop:
	__name = None  #Инкапсуляция
	__subway = None

	def __init__(self, name, subway): #Конструктор
		self.name = name
		self.subway = subway

	def print_info(self):
		print("Barber organization name:", self.name, ".Position:", self.subway)

class Barbers(Barbershop):   #Наследование
	staff = 0

	def __init__(self, staff, name, subway):   
		super(Barbers, self).__init__(name, subway) #Полиморфизм
		self.staff = staff

	def print_info(self):
		super().print_info()
		print("Sraff:", self.staff, "people")

barbers = Barbers(15, "Brutal", "Voykovskaya") #Передача параметров: 15 барберов, Название Барбершопа "Brutal", Месторасположение : метро "Voykovskaya".
barbers.print_info() #Вывод информации
