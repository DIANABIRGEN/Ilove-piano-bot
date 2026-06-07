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
        [InlineKeyboardButton("😰 Я сомневаюсь", callback_data="menu_doubts")],
        [InlineKeyboardButton("📊 Как выглядит прогресс", callback_data="menu_progress")],
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

def menu_doubts():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("😟 Я уже слишком взрослый", callback_data="doubt_age")],
        [InlineKeyboardButton("⏰ У меня нет времени", callback_data="doubt_time")],
        [InlineKeyboardButton("🎹 У меня нет инструмента", callback_data="doubt_instrument")],
        [InlineKeyboardButton("🤔 Я не уверен в себе", callback_data="doubt_confidence")],
        [InlineKeyboardButton("📺 Я учусь по YouTube", callback_data="doubt_youtube")],
        [InlineKeyboardButton("← Главное меню", callback_data="menu")],
    ])

def menu_progress():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⏱ 30 мин в день", callback_data="calc_30")],
        [InlineKeyboardButton("⏱ 1 час в день", callback_data="calc_60")],
        [InlineKeyboardButton("⏱ 2 часа в день", callback_data="calc_120")],
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

    "doubt_age": """😟 *"Я уже слишком взрослый"*

Это самый распространённый страх — и самый необоснованный.

Нейропластичность работает в любом возрасте. Взрослые ученики имеют огромное преимущество: эмоциональный опыт. Вы понимаете музыку так, как ребёнок никогда не поймёт.

_Диана начала в 30. Через 5 лет играет серьёзную классику._""",

    "doubt_time": """⏰ *"У меня нет времени"*

30 минут в день. Это всё что нужно.

Регулярные короткие занятия эффективнее редких длинных. 30 минут каждый день лучше, чем 3 часа по выходным.

30 минут — это одна серия сериала. Один скролл ленты.

_Время есть. Вопрос в приоритетах._""",

    "doubt_instrument": """🎹 *"У меня нет инструмента"*

Для начала достаточно цифрового фортепиано с 61 клавишей — от $150-200.

Главное — взвешенные клавиши, которые дают правильное ощущение.

В сообществе поможем выбрать инструмент под твой бюджет.""",

    "doubt_confidence": """🤔 *"Я не уверен в себе"*

Именно поэтому существует это сообщество.

Обучение в одиночку — путь, где легко бросить. Сообщество — это люди, которые проходят тот же путь рядом.

Плюс — индивидуальная консультация с Дианой, где разберём именно твою ситуацию.

_Уверенность приходит через действие, не наоборот._""",

    "doubt_youtube": """📺 *"Я учусь по YouTube, мне хватает"*

YouTube показывает как нажать клавиши в определённом порядке. Но не учит музыке.

Разница как между выучить фразу на иностранном языке и выучить сам язык.

Никто ещё не научился играть качественно с обучающих видео.

_Ты заслуживаешь настоящего обучения._""",

    "calc_30": """📊 *Твой прогресс при 30 минутах в день*

*Шаг первый — фундамент:*
Нотная грамота, ритм, координация двух рук.

*Шаг второй — слух:*
Сольфеджио, интервалы, аккорды. Музыка становится текстом.

*Шаг третий — гармония:*
Понимаешь почему музыка звучит именно так.

*Шаг четвёртый — свобода:*
Берёшь любые ноты и разбираешь самостоятельно.

_Это не про три песни. Это навык на всю жизнь._""",

    "calc_60": """📊 *Твой прогресс при 1 часе в день*

*Шаг первый — фундамент:*
Быстрее осваиваешь ноты, ритм и координацию.

*Шаг второй — слух:*
Сольфеджио на хорошем уровне за несколько месяцев.

*Шаг третий — гармония:*
Серьёзное понимание теории. Разбираешь сложные произведения.

*Шаг четвёртый — свобода:*
Музыка — твой второй язык.

_Час в день меняет всё._""",

    "calc_120": """📊 *Твой прогресс при 2 часах в день*

*Шаг первый — фундамент:*
Быстрый старт. За несколько месяцев — то, чего другие достигают за год.

*Шаг второй и третий — слух и гармония:*
Серьёзная теоретическая база. Продвинутый уровень реален за год.

*Шаг четвёртый — свобода:*
Профессиональный подход к музыке.

_2 часа в день — это выбор тех, кто серьёзно._""",

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
    elif data == "menu_doubts":
        await query.edit_message_text(
            "😰 *Я сомневаюсь...*\n\nЧто тебя останавливает? Выбери — разберём честно:",
            parse_mode="Markdown",
            reply_markup=menu_doubts()
        )
    elif data == "menu_progress":
        await query.edit_message_text(
            "📊 *Как выглядит прогресс*\n\nСколько времени ты готов уделять фортепиано каждый день?",
            parse_mode="Markdown",
            reply_markup=menu_progress()
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
        elif data.startswith("doubt_"):
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("← Назад", callback_data="menu_doubts")],
                [InlineKeyboardButton("← Главное меню", callback_data="menu")],
            ])
        elif data.startswith("calc_"):
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton("← Назад", callback_data="menu_progress")],
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
