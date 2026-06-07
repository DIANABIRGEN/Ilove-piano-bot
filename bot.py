import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8720872052:AAHqWZw3mExe5HyER3cJNYjY5Jzm5Ao-a6A")

PATREON = "https://www.patreon.com/c/dianabirgen/membership"

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🧠 Почему пианино развивает мозг?", callback_data="brain")],
        [InlineKeyboardButton("🎼 Как развить музыкальный вкус?", callback_data="taste")],
        [InlineKeyboardButton("📱 Детокс от соцсетей через музыку", callback_data="detox")],
        [InlineKeyboardButton("💪 Истории тех, кто начал в 30+", callback_data="stories")],
        [InlineKeyboardButton("👥 О сообществе", callback_data="community")],
        [InlineKeyboardButton("📖 Книга DoFaMin", callback_data="book")],
        [InlineKeyboardButton("💳 Вступить за $1.99/месяц", url=PATREON)],
    ])

def back_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💳 Вступить за $1.99/месяц", url=PATREON)],
        [InlineKeyboardButton("← Назад", callback_data="menu")],
    ])

TEXTS = {
    "brain": """🧠 *Почему пианино развивает мозг?*

Когда ты играешь, одновременно работают четыре области мозга: моторная кора, слуховая кора, префронтальная кора и эмоциональный центр.

Научный факт: взрослые, занимающиеся музыкой 6 месяцев, улучшают рабочую память и концентрацию на 30%.

Нейропластичность работает в любом возрасте. Мозг меняется — просто нужен правильный инструмент.""",

    "taste": """🎼 *Как развить музыкальный вкус?*

Когда ты учишься играть, ты начинаешь слышать музыку иначе — не просто фон, а архитектуру и эмоцию.

Ты понимаешь почему Шопен — это про нежность и боль, Бах — математика с мурашками, Лист — сила без слов.

Развитый вкус переносится на всё: ты тоньше чувствуешь мир вокруг.""",

    "detox": """📱 *Детокс от соцсетей через музыку*

Соцсети не дают остановиться. Пианино работает наоборот — требует полного присутствия.

Через 10-15 минут игры мозг входит в состояние потока: стресс уходит, время останавливается.

30 минут за пианино = настоящий отдых. Не прокрутка ленты, которая мозг перегружает.""",

    "stories": """💪 *Истории тех, кто начал в 30+*

Диана, 35 лет: "Я начала в 30, вдохновившись Листом. Казалось невозможным. Пять лет спустя — играю классику и понимаю музыку так, как никогда раньше."

Взрослые ученики часто превосходят детей в глубине понимания музыки — потому что у них есть эмоциональный опыт.

Поздно начать невозможно. Можно только не начать.""",

    "community": """👥 *Adult Piano Learners*

Закрытое сообщество взрослых, которые учатся играть на пианино.

✅ Закрытый Telegram-канал с видео
✅ Индивидуальная консультация с Дианой
✅ Онлайн-встреча раз в месяц
✅ Оффлайн-встреча раз в год
🎁 Книга DoFaMin в подарок

💰 Всего $1.99 в месяц""",

    "book": """📖 *Книга DoFaMin*

До-Фа-Мин — три ноты и формула внутренней трансформации через музыку.

Книга о том, как взрослый человек меняется, когда решается на сложное и красивое.

Как преодолеть страх "я уже слишком взрослый". Как найти время. Как не бросить.

Входит в подарок при вступлении в сообщество 🎁""",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎹 *Добро пожаловать в Adult Piano Learners!*\n\nМы — взрослые, которые решились на то, о чём давно мечтали: начать играть на пианино.\n\nВыбери, что тебя интересует:",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "menu":
        await query.edit_message_text(
            "🎹 *Добро пожаловать в Adult Piano Learners!*\n\nВыбери, что тебя интересует:",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
    elif query.data in TEXTS:
        await query.edit_message_text(
            TEXTS[query.data],
            parse_mode="Markdown",
            reply_markup=back_menu()
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
