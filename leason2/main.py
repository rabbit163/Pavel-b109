#Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.
name = input("Введите ваше имя:")
age = int(input("Введите ваш возраст:"))
a = age - 18
print(name,"тебе больше на", a, "от 18 лет!")