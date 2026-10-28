import re
from telethon import TelegramClient, events

api_id = 38602507
api_hash = '40deef564220768c39b63594aee03e18'

source_channel = 'etjmir'
target_channel = 'Azarakhshgoldgallery'

client = TelegramClient('gold_bot_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def my_event_handler(event):
    text = event.raw_text
    
    if "گرم‌طلای18عیار" in text or "نرخ‌روزطــلانقــره‌وسکــه‌مشـهدمقــدس" in text:
        date_match = re.search(r'([آ-ی]+\s+\d{2}\s+[آ-ی]+\s+\d{4})', text)
        date_str = date_match.group(1) if date_match else "اعلام نشده"

        time_match = re.search(r'(\d{2}:\d{2})', text)
        time_str = time_match.group(1) if time_match else "اعلام نشده"

        price_match = re.search(r'گرم‌طلای18عیار\s*:\s*([\d,]+)', text)
        price_str = price_match.group(1) if price_match else "اعلام نشده"

        custom_message = f"""💎 AZARAKH GALLERY

✨ گالری آذرخش

━━━━━━━━━━━━━━━━━━

📊 گزارش نرخ روز طلا و سکه

📅 تاریخ: {date_str}
🕰 ساعت: {time_str}

━━━━━━━━━━━━━━━━━━

🟡 طلای ۱۸ عیار
💰 هر گرم: {price_str} تومان

━━━━━━━━━━━━━━━━━━

⚜️ گالری آذرخش
زیباییِ ماندگار، انتخابی ارزشمند

📌 نرخ اعلامی مربوط به زمان انتشار است.

#نرخ_روز_طلا_نقره_و_سکه_مشهد_مقدس"""

        await client.send_message(target_channel, custom_message)

print("ربات فیلتر و قالب‌بندی نرخ طلا فعال شد...")
client.start()
client.run_until_disconnected()
