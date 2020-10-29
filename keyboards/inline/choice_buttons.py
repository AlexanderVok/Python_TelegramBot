from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import courses_callback

courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python', callback_data=courses_callback.new(
                course='Python'
            )),
            InlineKeyboardButton(text='Math', callback_data=courses_callback.new(
                course='Math'
            )),
            InlineKeyboardButton(text='English', callback_data=courses_callback.new(
                course='English'
            )),
            InlineKeyboardButton(text='Probability Theory', callback_data=courses_callback.new(
                course='Probability Theory'
            )),
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)


python_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Купи тут', url='vk.com')
        ]
    ]
)


math_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Купи тут', url='google.com')
        ]
    ]
)
