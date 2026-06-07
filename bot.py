import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8720872052:AAHqWZw3mExe5HyER3cJNYjY5Jzm5Ao-a6A")
PATREON = "https://www.patreon.com/cw/dianabirgen/membership"
YOUTUBE = "https://youtu.be/P-B-B6dBZUQ"
PDF = "https://drive.google.com/file/d/1cqYP_NObft_ri-xYkOVH1vVIv79rZnAD/view?usp=sharing"
DIANA = "https://t.me/Diana_Birgen"

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎹 Мой путь обучения 30+ лет", callback_data="menu_about")],
        [InlineKeyboardButton("🎼 Почему именно фортепиано?", callback_data="menu_why")],
        [InlineKeyboardButton("👥 Что даст тебе сообщество?", callback_data="menu_community")],
        [InlineKeyboardButton("🎁 Подарок — гайд DoFaMi·n", url=PDF)],
        [InlineKeyboardButton("💳 Community — $1.99/месяц", url=PATREON)],
        [InlineKeyboardButton("⭐ Mentorship — $12.99/месяц", url=PATREON)],
    ])

def menu_about():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎹 Мой путь — с нуля в 30 лет", callback_data="about")],
        [InlineKeyboardButton("🎬 Посмотри как это выглядит", callback_data="video")],
        [InlineKeyboardButton("💪 Истории тех, кто начал в 30+", callback_data="stories")],
        [InlineKeyboardButton("← Главное меню", callback_data="menu")],
    ])

def menu_why():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🧠 Почему фортепиано развивает мозг?", callback_data="brain")],
        [InlineKeyboardButton("🎼 Как развить музыкальный вкус?", callback_data="taste")],
        [InlineKeyboardButton("📱 Детокс от соцсетей", callback_data="detox")],
        [InlineKeyboardButton("⚠️ Важно понять до вступления", callback_data="truth")],
        [InlineKeyboardButton("← Главное меню", callback_data="menu")],
    ])

def menu_community():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👥 О сообществе", callback_data="community")],
        [InlineKeyboardButton("📖 Книга DoFaMi·n", callback_data="book")],
        [InlineKeyboardButton("📥 Скачать гайд DoFaMi·n", url=PDF)],
        [InlineKeyboardButton("💬 Написать Диане", url=DIANA)],
        [InlineKeyboardButton("💳 Community — $1.99/месяц", url=PATREON)],
        [InlineKeyboardButton("⭐ Mentorship — $12.99/месяц", url=PATREON)],
        [InlineKeyboardButton("← Главное меню", callback_data="menu")],
    ])

TEXTS = {
    "about": """🎹 *Мой путь — с нуля в 30 лет*

Меня зовут Диана. Я выросла в семье музыкантов — но сама начала серьёзно учиться фортепиано только в 30 лет. Без чьих-либо советов, в осознанном возрасте.

Пять лет назад я не могла сыграть ни одной ноты. Сегодня я изучаю сольфеджио, теорию, гармонию и играю серьёзные классические произведения.

*Моя миссия* — показать, как в реальности выглядит профессиональное обучение фортепиано во взрослом возрасте. Без прикрас. Честные результаты, настоящий прогресс.

Это сложно. Это долго. И это одно из лучших решений в моей жизни.""",

    "video": f"""🎬 *Посмотри как это выглядит*

Реальный пример — взрослый человек, который начал с нуля в 30 лет.

Никакого монтажа. Никаких чудес. Настоящий процесс и настоящий результат.

👇 [Смотреть видео]({YOUTUBE})""",

    "stories": """💪 *Истории тех, кто начал в 30+*

Диана, 30 лет: "Я начала, вдохновившись классической музыкой. Казалось невозможным. Пять лет спустя — играю серьёзные произведения и понимаю музыку так, как никогда раньше."

Взрослые ученики часто превосходят детей в глубине понимания музыки — потому что у них есть эмоциональный опыт, которого у детей ещё нет.

_Поздно начать невозможно. Можно только не начать._""",

    "brain": """🧠 *Почему фортепиано развивает мозг?*

Когда ты играешь, одновременно работают четыре области мозга: моторная кора, слуховая кора, префронтальная кора и эмоциональный центр.

Научный факт: взрослые, занимающиеся музыкой 6 месяцев, улучшают рабочую память на 30% и снижают уровень кортизола — гормона стресса.

Нейропластичность работает в любом возрасте. Мозг меняется — просто нужен правильный инструмент.""",

    "taste": """🎼 *Как развить музыкальный вкус?*

Когда ты учишься играть, ты начинаешь слышать музыку иначе — не просто фон, а архитектуру и эмоцию.

Ты понимаешь почему одна последовательность аккордов вызывает тревогу, а другая — покой. Почему музыка трёхсотлетней давности до сих пор вызывает мурашки.

Развитый вкус переносится на всё: ты тоньше чувствуешь мир вокруг.""",

    "detox": """📱 *Детокс от соцсетей через музыку*

Маятник истерии по соцсетям и успешному успеху скоро качнётся в другую сторону. Люди будут искать человеческого — не идеального, сложного, с глубиной.

30 минут за инструментом — состояние потока, которое не заменит никакая лента.

По данным исследования профессора Глории Марк, средняя концентрация внимания упала с 2,5 минут в 2004 году до 47 секунд в 2023-м. Фортепиано буквально восстанавливает то, что цифровая среда разрушает.""",

    "truth": """⚠️ *Важно понять до вступления*

Фортепиано — это не три песни на праздник.

Настоящее обучение — это изучение языка музыки. Сольфеджио, теория, гармония — это алфавит и грамматика. Когда ты его освоишь, ты сможешь сыграть что угодно.

Никто ещё не научился играть качественно с обучающих видео на ютуб. YouTube даёт иллюзию обучения, а не сам навык.

Здесь — настоящее обучение. Сложное, долгое и невероятно вознаграждающее.""",

    "community": """👥 *Adult Piano Learners*

Закрытое сообщество взрослых, которые учатся играть на фортепиано осознанно.

✅ Закрытый Telegram-канал с видео и материалами
✅ Онлайн-встреча раз в месяц
✅ Оффлайн-встреча раз в год в Бодруме

*Community — $1.99/месяц*
Доступ к каналу, встречам и гайду DoFaMi·n в подарок.

*Mentorship — $12.99/месяц*
Всё из Community + индивидуальная консультация с Дианой 1,5 часа.""",

    "book": """📖 *Книга DoFaMi·n*

До-Фа-Ми — три ноты. И немного дофамина.

Книга о том, как взрослый человек меняется, когда решается на сложное и красивое.

Как преодолеть страх "я уже слишком взрослый". Как найти время. Как не бросить.

Входит в подарок при вступлении в сообщество 🎁""",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎹 *Добро пожаловать в Adult Piano Learners!*\n\nМы — взрослые, которые решились на то, о чём давно мечтали: начать играть на фортепиано.\n\nНе три песни на праздник. Настоящий музыкальный язык.\n\nВыбери, что тебя интересует 👇",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "menu":
        await query.edit_message_text(
            "🎹 *Adult Piano Learners*\n\nВыбери, что тебя интересует 👇",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
    elif data == "menu_about":
        await query.edit_message_text(
            "🎹 *Мой путь обучения 30+ лет*\n\nВыбери раздел:",
            parse_mode="Markdown",
            reply_markup=menu_about()
        )
    elif data == "menu_why":
        await query.edit_message_text(
            "🎼 *Почему именно фортепиано?*\n\nВыбери раздел:",
            parse_mode="Markdown",
            reply_markup=menu_why()
        )
    elif data == "menu_community":
        await query.edit_message_text(
            "👥 *Что даст тебе сообщество?*\n\nВыбери раздел:",
            parse_mode="Markdown",
            reply_markup=menu_community()
        )
    elif data in TEXTS and TEXTS[data]:
        if data in ["about", "video", "stories"]:
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("← Назад", callback_data="menu_about")],
                [InlineKeyboardButton("← Главное меню", callback_data="menu")],
            ])
        elif data in ["brain", "taste", "detox", "truth"]:
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("← Назад", callback_data="menu_why")],
                [InlineKeyboardButton("← Главное меню", callback_data="menu")],
            ])
        else:
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("💳 Community — $1.99/месяц", url=PATREON)],
                [InlineKeyboardButton("⭐ Mentorship — $12.99/месяц", url=PATREON)],
                [InlineKeyboardButton("← Назад", callback_data="menu_community")],
                [InlineKeyboardButton("← Главное меню", callback_data="menu")],
            ])
        await query.edit_message_text(
            TEXTS[data],
            parse_mode="Markdown",
            reply_markup=kb
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
