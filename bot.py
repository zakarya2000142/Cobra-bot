
import urllib.request
import urllib.parse
import json
import random
import time

TOKEN = "8964806662:AAGz61wrTw7mllDH9Z1UG9wnyKGeqf7p0uw"
BASE = "https://api.telegram.org/bot" + TOKEN

love_texts = [
    "تولدت مبارک کبری ❤️",
    "کبری... هر وقت اسمت میاد قلبم یه جور دیگه می‌زنه 🌙",
    "چشمات... نمی‌دونم چی دارن که آدم رو خلع سلاح می‌کنه 💘",
    "فقط می‌خوام بدونی که هستی، دنیا یه جور دیگه‌ست ❤️",
    "کبری، کاشکی همین الان جلوم بودی و می‌دیدی چقدر دلم برات تنگ شده...",
    "بعضی آدما خاصن، ولی تو از اون خاص‌تری ✨",
    "تولدت مبارک عزیزم. امیدوارم همیشه بخندی 🌙",
    "دوست دارم امروز کنارت باشم و تولدت رو یه جور دیگه تبریک بگم...",
    "کبری، دلم می‌خواد بدونی که چقدر برام مهمی ❤️",
    "تو از اون رویاهایی هستی که نمی‌خوام ازش بیدار شم 💘",
]

hot_texts = [
    "چشات... فقط یه نگاه کافیه 💋",
    "کبری... بعضی وقتا دلم نمی‌خواد مودب باشم 🖤",
    "دلم یه بغل می‌خواد که تا صبح تموم نشه 🌙",
    "دلم می‌خواد صداتو بشنوم، نه از پشت گوشی... از نزدیک 💋",
]

def send_message(chat_id, text, keyboard=None):
    data = {"chat_id": chat_id, "text": text}
    if keyboard:
        data["reply_markup"] = json.dumps(keyboard)
    url = BASE + "/sendMessage?" + urllib.parse.urlencode(data)
    urllib.request.urlopen(url, timeout=30)

def get_updates():
    req = urllib.request.urlopen(BASE + "/getUpdates", timeout=30)
    return json.loads(req.read())

last_update_id = 0

while True:
    try:
        data = get_updates()
        for update in data.get("result", []):
            if update["update_id"] > last_update_id:
                last_update_id = update["update_id"]
                message = update.get("message")
                if message:
                    chat_id = message["chat"]["id"]
                    text = message.get("text", "")

                    keyboard = {
                        "keyboard": [
                            ["💌 متن عاشقانه", "🔥 چیزای داغ"],
                            ["🌙 دلتنگی"]
                        ],
                        "resize_keyboard": True
                    }

                    if text == "/start":
                        send_message(chat_id, "سلام کبری ❤️\nتولدت مبارک! چی می‌خوای؟", keyboard)
                    elif text == "💌 متن عاشقانه":
                        send_message(chat_id, random.choice(love_texts), keyboard)
                    elif text == "🔥 چیزای داغ":
                        send_message(chat_id, random.choice(hot_texts), keyboard)
                    elif text == "🌙 دلتنگی":
                        send_message(chat_id, "دلم برات یه جوری تنگ شده که با هیچ زبونی نمی‌شه گفت 🌙", keyboard)
                    else:
                        send_message(chat_id, "از دکمه‌ها استفاده کن عزیزم ❤️", keyboard)
    except Exception as e:
        print("Error:", e)
    time.sleep(2)
