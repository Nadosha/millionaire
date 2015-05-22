# coding: utf-8
from sys import argv, exit
script = argv[0]
print "=" * 20 + script + "=" * 20 + "\n"
print "\t\tМИЛЛИОНЕР" + "\n" + "-" * 50

print """
  Привет.
  Это аналог игры 'Кто хочет стать миллионером' \n
"""
print """
ПРАВИЛА ИГРЫ:	
  Отвечайте на вопросы, зарабатывайте балы. Гордитесь своей эрудированностью 
  или стыдитесь своей глупости. Вместо 3-х подсказок (как в оригинальной игре) 
  вам дается право сделать 3 ошибки. Если вы допустили ошибку вы перейдете
  к следующему вопросу и баллы за ваш ответ не будут засчитаны. После третей
  ошибки игра прекратиться.
"""


points = 0
lifes = 3
quest = "." * 50 + "\nНапишите букву вашего варианта 'A' 'B' 'C' 'D' > "
right = "\n||" + "\tОтлично! Это првильный ответ\t+5 баллов"
wrong = "\n||" + "\tК сожалению это не верный ответ!\t-1 жизнь"
score = "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50

# out_a = answer == "b" or answer == "c" or answer == "d" 
# out_b = answer == "a" or answer == "c" or answer == "d"
# out_c = answer == "a" or answer == "b" or answer == "d"
# out_d = answer == "a" or answer == "b" or answer == "c"

not_correct = "-" * 50 + "\nНе ту нажали кнопку! Бывает. Попробуйте еще раз:"

def greating():
	print "=" * 50 + "\n\t\tУРА! ТЫ МИЛЛИОНЕР!\n" + "-" * 50
	print "\t\t Твой счет: %d балов" % points
	print "\t\t Ты сохранил %d жизни" % lifes
	print "-" * 50
	exit(0)

def q_ten():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Какой цветок держала в руке булгаковская Маргарита, когда 
	её впервые увидел Мастер?\n
	"""
		print """
	\t A)	Тюльпан
	\t B)	Мимоза
	\t C)	Нарцис
	\t D)	Роза
	"""
		answer = raw_input(quest)
		if answer == "b":
			print right
			count(True)
			greating()
		elif answer == "a" or answer == "c" or answer == "d":
			print wrong
			count(False)
			greating()
		else:
			print not_correct

def q_nine():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Какое из этих государств ранее называлось Берегом Слоновой Кости?\n
	"""
		print """
	\t A)	Кот-д'Ивуар
	\t B)	Буркина-Фасо
	\t C)	Мьянма 
	\t D)	Бенин
	"""
		answer = raw_input(quest)
		if answer == "a":
			print right
			count(True)
			q_ten()
		elif answer == "b" or answer == "c" or answer == "d":
			print wrong
			count(False)
			q_ten()
		else:
			print not_correct

def q_eight():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Сколько лошадей впряжено в колесницу на фронтоне Большого театра?\n
	"""
		print """
	\t A)	Три
	\t B)	Четыре
	\t C)	Пять
	\t D)	Шесть
	"""
		answer = raw_input(quest)
		if answer == "b":
			print right
			count(True)
			q_nine()
		elif answer == "a" or answer == "c" or answer == "d":
			print wrong
			count(False)
			q_nine()
		else:
			print not_correct

def q_seven():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Кто из персонажей Ильфа и Петрова считал большинство 
	окружающих 'жалкими, ничтожными людьми'?\n
	"""
		print """
	\t A)	Бендер
	\t B)	Паниковский
	\t C)	Корейко
	\t D)	Балаганов
	"""
		answer = raw_input(quest)
		if answer == "b":
			print right
			count(True)
			q_eight()
		elif answer == "a" or answer == "c" or answer == "d":
			print wrong
			count(False)
			q_eight()
		else:
			print not_correct

def q_six():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Чему равны 5400 секунд?\n
	"""
		print """
	\t A)	Двум часам
	\t B)	Полутора часам
	\t C)	Часу
	\t D)	Получасу
	"""
		answer = raw_input(quest)
		if answer == "b":
			print right
			count(True)
			q_seven()
		elif answer == "a" or answer == "c" or answer == "d":
			print wrong
			count(False)
			q_seven()
		else:
			print not_correct

def q_five():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Какой тип растительности можно наблюдать в североамериканской прерии?\n
	"""
		print """
	\t A)	Пустыня
	\t B)	Болото
	\t C)	Степь
	\t D)	Лес
	"""
		answer = raw_input(quest)
		if answer == "c" :
			print right
			count(True)
			q_six()
		elif answer == "a" or answer == "b" or answer == "d":
			print wrong
			count(False)
			q_six()
		else:
			print not_correct

def q_four():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Как называется группа центральной Африки, отличающихся очень низким ростом?\n
	"""
		print """
	\t A)	Берберы
	\t B)	Папуасы
	\t C)	Зулусы
	\t D)	Пигмеи
	"""
		answer = raw_input(quest)
		if answer == "d":
			print right
			count(True)
			q_five()
		elif answer == "a" or answer == "b" or answer == "c":
			print wrong
			count(False)
			q_five()
		else:
			print not_correct

def q_three():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Как называется детская болезнь, похожая на корь?\n
	"""
		print """
	\t A)	Чернуха
	\t B)	Синюха
	\t C)	Желтуха
	\t D)	Краснуха
	"""
		answer = raw_input(quest)
		if answer == "d":
			print right
			count(True)
			q_four()
		elif answer == "a" or answer == "b" or answer == "c":
			print wrong
			count(False)
			q_four()
		else:
			print not_correct

def q_two():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Магнитный носитель информации, это?\n
	"""
		print """
	\t A)	Гранит
	\t B)	Монета
	\t C)	Магнит
	\t D)	Дискета
	"""
		answer = raw_input(quest)
		if answer == "d":
			print right
			count(True)
			q_three()
		elif answer == "a" or answer == "b" or answer == "c":
			print wrong
			count(False)
			q_three()
		else:
			print not_correct

def q_one():
	while True:
		print "\nScore: %d  Lifes: %d\n" % (points, lifes) + "-" * 50
		print """
	Как звали лидера гайдаровской команды, 
	оказывавший бескорыстную помощь пожилым людям?\n
	"""
		print """
	\t A)	Тимур
	\t B)	Егор
	\t C)	Аркадий
	\t D)	Борис
	"""
		answer = raw_input(quest)
		if answer == "a":
			print right
			count(True)
			q_two()
		elif answer == "b" or answer == "c" or answer == "d":
			print wrong
			count(False)
			q_two()
		else:
			print not_correct

def count(answer):
	global points
	global lifes
	if answer:
		points += 5
		return points
	elif not answer:
		lifes -=1
		if lifes <= 0:
			print "\n" * 3
			print "-" * 50 + "\n\tGAME OVER \tВаш счет: %d\n" % points + "-" * 50 + "\n" * 3
			exit(0)
		else:
			return lifes
	else:
		"ERROR!"

def start():
	print "-" * 50
	print "\t Ну что, готовы начать игру? \n"

	while True:
		answer = raw_input("Нажмите клавишу Y(yes - да) или N(no - нет) > ").lower()

		if answer == "y" or answer == "н":
			print "\nОтлично! Тогда не теряя времени переходим к игре"
			q_one()
		elif answer == "n" or answer == "т":
		    print "." * 50 + "\nОчень жаль. Может поиграем в следующий раз!\n" + "." * 50
		    exit(0)
		else:
			print not_correct

start()

