from asyncio import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from .. import queues
from ..callsmusic import callsmusic
from ..helpers.chat_id import get_chat_id
from ..helpers.decorators import authorized_users_only
from ..helpers.decorators import errors
from ..helpers.filters import command
from ..helpers.filters import other_filters


@Client.on_message(command('durdur') & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    (
        await message.reply_text('<b>⏸ duraklatıldı</b>', False)
    ) if (
        callsmusic.pause(get_chat_id(message.chat))
    ) else (
        await message.reply_text('<b>❌ hiçbir şey çalmıyor</b>', False)
    )


@Client.on_message(command('devam') & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    (
        await message.reply_text('<b>▶️ devam etti</b>', False)
    ) if (
        callsmusic.resume(get_chat_id(message.chat))
    ) else (
        await message.reply_text('<b>❌ Hiçbir şey duraklatılmadı</b>', False)
    )


@Client.on_message(command('dur') & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text('<b>❌ hiçbir şey çalmıyor</b>', False)
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await callsmusic.stop(chat_id)
        await message.reply_text('<b>⏹ Durdurulan şarkı</b>', False)


@Client.on_message(command('ileri') & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text('<b>❌ hiç birşey çalmıyor</b>', False)
    else:
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            await callsmusic.stop(chat_id)
        else:
            await callsmusic.set_stream(
                chat_id,
                queues.get(chat_id)['dosya'],
            )
        await message.reply_text('<b>✅ ilerletildi</b>', False)


@Client.on_message(command('sus') & other_filters)
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(get_chat_id(message.chat))
    (
        await message.reply_text('<b>✅ sustu</b>', False)
    ) if (
        result == 0
    ) else (
        await message.reply_text('<b>❌ zaten susmuştu</b>', False)
    ) if (
        result == 1
    ) else (
        await message.reply_text('<b>❌ sesli sohbette değilim.</b>', False)
    )


@Client.on_message(command('sesac') & other_filters)
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(get_chat_id(message.chat))
    (
        await message.reply_text('<b>✅ ses açtı</b>', False)
    ) if (
        result == 0
    ) else (
        await message.reply_text('<b>❌ susturulmadı</b>', False)
    ) if (
        result == 1
    ) else (
        await message.reply_text('<b>❌ sesliye geçmedi</b>', False)
    )
