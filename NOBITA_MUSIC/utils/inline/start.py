from pyrogram.types import InlineKeyboardButton

import config
from NOBITA_MUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_7"], callback_data="gib_source"),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
    ]
    return buttons
