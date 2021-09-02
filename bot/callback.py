from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ Cara menggunakan bot ini:
1.) pertama, tambahkan saya ke groupmu.
2.) lalu promote saya menjadi admin , dan berikan semua izin kecuali admin anonim.
3.) tambahkan @riostreamingbot ke groupmu.
4.) nyalakan voice chat terlebih dahulu sebelum memulai stream video.
5.) tulis /stream (reply ke video) untuk memulai streaming.
6.) tulis /stop untuk menghentikan video streaming.
⚡ __Maintained by Rio Project__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🔙 Kembali", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Halo, Saya adalah telegram video streaming bot.**\n\n💭 **Saya dibuat untuk memutar video di voice chat dengan mudah.**\n\n❔ **Cara menggunakan saya, tolong tekan tombol help dibawah** 👇🏻",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❓ Cara Menggunakan Saya", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "👑 Developer", url="https://t.me/riio00")
                       ],[
                          InlineKeyboardButton(
                             "📣 Group", url="https://t.me/siiniaja"),
                          InlineKeyboardButton(
                             "📣 Channel", url="https://t.me/riobotsupport")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **Bot Informasi**
🤖 __Bot ini dibuat untuk stream video di telegram group video chat menggunakan several methods dari WebRTC.__
💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots.__
👨🏻‍💻 __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__
👩🏻‍✈️ » [Levina](https://github.com/levina-lab)
🤵🏻 » [Rio](https://github.com/RioProjectX)
__This bot licensed under GNU-GPL 3.0 License__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🔙 Kembali", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
