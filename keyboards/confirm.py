from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def confirm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Confirm", callback_data="confirm")]
        ]
    )
