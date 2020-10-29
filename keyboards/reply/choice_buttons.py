from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('Python')
button2 = KeyboardButton('Mathematical Analysis')
button3 = KeyboardButton('Probability Theory')
button4 = KeyboardButton('Database Management')


markup = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button1, button2, button3, button4
)





