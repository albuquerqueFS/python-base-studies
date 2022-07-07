from datetime import date

name = input('What\'s your name? ')
age = int(input('How old are you? '))
height = float(input('What\'s your height? '))
weight = int(input('If you don\'t mind, what\'s your weight? '))

imc = (weight / (height * height)) / 2
current_year = date.today().year
year_birth = current_year - age
formatted_height = "{:.2f}".format(height)

print(f'{name} tem {age} anos, {formatted_height} de altura e pesa {weight}kg.'
      f'O IMC de {name} é {imc}.'
      f'{name} nasceu em {year_birth}.')