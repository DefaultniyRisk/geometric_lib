import circle
import square
'''Вызов функций из 2х других файлов - circle.py, square.py'''

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}
'''Создаем 2 списка и словарь'''

def calc(fig, func, size):
    '''Функция принимает 3 переменных (2 списка и словарь), проверяет наличие fig в figs и func в funcs с помощью булевских выражений (проверяет их на допустимость)'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	'''Функция eval принимает 3 аргумента: fig, где содержится необходимая для вызова функция, func - имя функции в fig, size - список аргументов, переданных в функцию. f' превращает это в строку. Eval динамически выполняет вышеперечисленные функции и выводит результат'''
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    '''Создаем 2 пустых элемента и список size, а также выполняем все действия ниже при выполнении условия в if'''
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	    '''Считываем значение fig до тех пор, пока оно некорректно'''
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	'''Считываем значение func до тех пор, пока оно некорректно'''
	while len(size) != sizes.get(f"{func}-{fig}", 1):
	    '''Сравнивает длину size с количеством подходящих элементов size'''
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
		'''Создает список size до тех пор, пока он не станет корректным'''
	
	calc(fig, func, size)
	'''Вызывает вышеописанную функцию calc для аргументов fig, func и size'''



