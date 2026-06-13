from pathlib import Path
from faker import Faker
import random

def get_sign_up_data():
    
    fake_en = Faker('en_US') 
    fake_ru = Faker('ru_RU')
    name = fake_ru.first_name()
    surname = fake_ru.last_name()
    login = fake_en.user_name()
    email = fake_en.email()
    password = fake_en.password()
    return name, surname, login, email, password

def get_recipe_data():
    
    fake_ru = Faker('ru_RU')

    food_words = ['суп', 'борщ', 'пирог', 'салат', 'плов', 'кекс', 'омлет', 'блин', 'соус', 'рагу']
    name = random.choice(food_words)
    ingredient_one = 'вод'
    ingredient_two = 'мук'
    amount = random.randint(1, 999)
    time = random.randint(1, 120)
    description = fake_ru.text(max_nb_chars=150)

    BASE_DIR = Path(__file__).resolve().parent.parent 
    image = str(BASE_DIR / 'assets' / 'recipe_image.jpg')
    
    return name, ingredient_one, amount, ingredient_two, time, description, image

