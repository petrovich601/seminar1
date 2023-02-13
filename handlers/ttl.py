
from loader import dp
from aiogram.types import Message
global max
max = 130

@dp.message_handler(commands=['total'])
async def max_ttl(message: Message):
    global max
    await message.answer(f'Какое количество конфет на столе? ')
    print(message.from_user.id)
    max = int(message.from_user)
