#Общий класс конфета
class Candy:
	name = None #Название
	properties = [None] #Свойства
	taste = None #Вкус
	isDelicious = None #Съедобно или нет

	def __init__(self, name, properties, taste, isDelicious):
		self.set_param(name, properties, taste, isDelicious)
		self.print_param()


#Принимаем параметры
	def set_param(self, name = None, properties = [None], taste = None, isDelicious = None):
		self.name = name
		self.properties = [properties]
		self.taste = taste
		self.isDelicious = isDelicious
    
#Выводим параметры
	def print_param(self):
		print('Name:', self.name, ',', 'properties:', self.properties, 'taste:', self.taste, 'is delicious?', self.isDelicious)

#Наши конфеты : Сникерс и Твикс
snikers = Candy('Snikers', ['sweet', 'chocolate', 'nut'], '7/10', True)
twix = Candy('Twix', ['sweet', 'caramel', 'cookie'], '9/10', True)
