from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b>👋🏻 Merhaba {message.from_user.mention()}!</b>\n\n'
       'Ben SR Müzik botuyum,'
        'Grup görüşmelerinde müzik çalmana izin verdim.'
        '\n\nŞu anda desteklediğim komutlar:\n\n'
        '/oynat - yanıtlanan ses dosyasını veya YouTube videosunu oynat\n'
        '/dur - ses akışını duraklat\n'
        '/devam - ses akışını devam ettir\n'
        '/ileri - mevcut ses akışını atla\n'
        '/sus - kullanıcı robotunu sessize alır\n'
        '/sesac - kullanıcı robotunun sesini aç\n'
        '/bitir - kuyruğu temizle ve kullanıcı robotunu aramadan kaldır',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '🔈 Channel', url='https://t.me/DamageExe',
                    ),
                    InlineKeyboardButton(
                        'Group 💬', url='https://t.me/DmageExe',
                    ),
                ],
            ],
        ),
    )
