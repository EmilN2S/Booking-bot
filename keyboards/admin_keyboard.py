from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Manage my services"), KeyboardButton(text="Schedule")],
            [KeyboardButton(text="Services")],
            [KeyboardButton(text="Booking to service"), KeyboardButton(text="My bookings")]
        ],
        resize_keyboard=True,
    )
