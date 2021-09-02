from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"✨ **Halo, Saya Adalah telegram video streaming bot.**\n\n💭 **Saya Dibuat Untuk Memutar Video di group voice chats dengan mudah.**\n\n❔ **Cara Menggunakan Saya, Tolong Tekan Tombol Dibawah inj** 👇🏻",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "👑Developer", url="https://t.me/riio00")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             " Cara Menggunakan Saya❓", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "📣 Group", url="https://t.me/VeezSupportGroup"),
                          InlineKeyboardButton(
                             "📣 Channel", url="https://t.me/riobotsupport")
                       ]]
                    ))
   else:
      await m.reply("**✨ Bot Online ✨**")
