from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
import logging
from keyboards.reply.choice_buttons import markup
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.callback_data import courses_callback
from keyboards.inline.choice_buttons import courses, python_keyboard, math_keyboard
from loader import dp
from states import Registration


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer("Привет, я бот-журнал!)\nДля списка команд нажми /help")


@dp.message_handler(Command('help'))
async def start(message: types.Message):
    await message.answer("*Команды для студентов:\n/reg - Начать регистрацию пользователя\n/infoaboutme - получить "
                         "информацию о себе\n/getgrades получить оценки и средний "
                         "балл\n/leavethecours - покинуть курс\n*Команды для "
                         "преподавателя:\n/regadmin - стать администратором курса\n/torate - "
                         "выставить оценки студентам\n/listofstudents - получить список студентов на курсе")


@dp.message_handler(Command("reg"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Введите свое имя")
    await Registration.Q1.set()


@dp.message_handler(state=Registration.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Введите свою фамилию")
    await Registration.next()


@dp.message_handler(state=Registration.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer("Введите номер своего студенческого билета")
    await Registration.next()


@dp.message_handler(state=Registration.Q3)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer3=answer)
    # await message.answer("Выбери курс", reply_markup=courses)
    await message.reply("Выберете курс", reply_markup=markup)
    await Registration.next()


@dp.message_handler(state=Registration.Q4)
async def answer_q2(message: types.Message, state: FSMContext):
    # await message.reply("Убираем шаблоны сообщений", reply_markup=ReplyKeyboardRemove())
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4 = message.text
    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)
    await message.answer("Спасибо за ваши ответы!", reply_markup=ReplyKeyboardRemove())

    # Вариант 1
    await state.finish()

    # Вариант завершения 2
    # await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    # await state.reset_state(with_data=False)
