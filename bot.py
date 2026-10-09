from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import random
from datetime import datetime

TOKEN = "8875844712:AAGQFl56SwFEjpL_hN_pfvLgyfMOFisLdZw"
DEVELOPER_LINK = "https://t.me/Owner_official_pk"
CHAT_GROUP_LINK = "https://t.me/+DAQ4w6oJKfRiYjE0"
WELCOME_PHOTO = "https://i.imgur.com/8Km9tLL.jpg"

WELCOME_TEXT = """
HEY 👋 MAIN AMINA HUN 💖

Tumhari pyari dost - Har sawal ka jawab dungi 😘
Mujhe admin banao, group ko aur pyara bana dungi ✨

POWERED BY Rajput_ 👨‍💻
"""

# --- PYARI AI LOGIC ---
def get_sweet_reply(user_text, user_name):
    text = user_text.lower()
    name = user_name

    # Gali / Group ke khilaf - Pyar se mana karegi
    bad_words = ["lund", "chut", "gand", "fuck", "bc", "mc"]
    if any(w in text for w in bad_words):
        return f"{name} jaan aise gande lafz nahi bolte 🥺 chalo pyar se baat karte hain 💖"

    # Greetings
    if any(w in text for w in ["hi", "hello", "hy", "salam", "aslam", "aoa"]):
        return random.choice([
            f"Heyy {name} 😘 kaisi ho jaan? Tumhara hi intezar kar rahi thi!",
            f"Hello meri jaan {name} 💋 bolo kya haal hai?",
            f"As-salamu Alaikum {name} 🌸 bolo kya madad karun?"
        ])

    # Kaisi ho
    if any(w in text for w in ["kesi ho", "kya karti", "kya haal", "how are you"]):
        return f"Mai bilkul theek hun {name} jaan 😍 bas tum logon se baat karke khush hun! Tum sunao? 🥰"

    # Koi bhi sawal - AI jaisa helpful jawab
    if "?" in text or any(w in text for w in ["kya", "kaise", "kyu", "kab", "kahan", "what", "how", "why", "when", "where", "batao", "explain"]):
        return random.choice([
            f"Acha {name} suno 💖 is bare me mera khayal ye hai ke... {user_text} ka best hal ye hai ke pyar aur samajh se kaam lo 😘 agar detail chahiye to bolo mai aur bata dungi!",
            f"{name} jaan ye sawal to bohot pyara hai 😚 Dekho, iska simple jawab ye hai ke har cheez me niyat saaf honi chahiye, baaki mai hun na tumhare saath 💋",
            f"Uff {name} tum kitne intelligent ho 😍 {user_text} ke liye mai ye kahungi ke... dil se socho aur pyar se jawab do, sab theek ho jayega ✨"
        ])

    # Default pyar bhara reply - Har bande ke liye
    return random.choice([
        f"Hayee {name} 😏 tumhari baatein to dil ko chu jati hain 💖",
        f"{name} jaan bolo na aur kya baat hai? 🥺 Mai sun rahi hun",
        f"Hihi {name} 😚 mujhe tumse baat karke bohot acha lagta hai",
        f"{name} baby tum group ki jaan ho 😘 aise hi pyari baatein karte raho",
        f"Aww {name} 💋 tumhara message dekh ke mera din ban gaya",
        f"Bolo {name} meri jaan, kya chahiye tumhe? Mai hazir hun 😍"
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ADD ME BABY 👶💋", url=f"https://t.me/{context.bot.username}?startgroup=true")],
        [InlineKeyboardButton("DEVELOPER 🧑‍💻", url=DEVELOPER_LINK), InlineKeyboardButton("JOIN CHANNEL 📢", url="https://t.me/pubgcardingtopups")],
        [InlineKeyboardButton("CHAT GROUP 🔥", url=CHAT_GROUP_LINK)]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo(photo=WELCOME_PHOTO, caption=WELCOME_TEXT, reply_markup=markup)

async def chat_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    
    user_name = update.message.from_user.first_name
    reply_text = get_sweet_reply(update.message.text, user_name)

    keyboard = [
        [InlineKeyboardButton("ADD ME IN YOUR GROUP 💖", url=f"https://t.me/{context.bot.username}?startgroup=true")],
        [InlineKeyboardButton("JOIN CHAT GROUP 🔥", url=CHAT_GROUP_LINK)]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(reply_text, reply_markup=markup)

async def game_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Game Starting... 🎮\n/new4 - 4 Letter Game\n/new5 - 5 Letter Game\n/leaderboard - Top Players")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(["new", "new4", "new5", "new6", "leaderboard", "wordseek"], game_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_reply))
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()