from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Services")],
            [KeyboardButton(text="Booking to service")],
            [KeyboardButton(text="My bookings")]
        ],
        resize_keyboard=True,
    )
