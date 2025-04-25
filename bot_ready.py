
import telebot
import openai

# ВСТАВЬ СВОЙ TELEGRAM BOT TOKEN и OpenAI API KEY
BOT_TOKEN = "7681369408:AAFroVEoMovrf5rNey_yKYf2lusuQ2E_JdE"
OPENAI_API_KEY ="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"

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

scenarios = {
    "1": "Придумай отмазку, почему я не пришёл на учёбу.",
    "2": "Придумай остроумный ответ на критику.",
    "3": "Придумай слоган для бизнеса по продаже носков.",
    "4": "Сделай смешной ответ девушке в Тиндере.",
    "5": "Дай совет, как не выгореть на работе."
}

def generate_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты — ироничный помощник, отвечай кратко, с юмором и креативно."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "Привет! Я бот, который решает твои мини-проблемы за копейки. Вот что я умею:\n\n"
        "1. Отмазка для учёбы\n"
        "2. Ответ на критику\n"
        "3. Слоган для бизнеса\n"
        "4. Ответ в Тиндере\n"
        "5. Советы от выгорания\n\n"
        "✏️ Напиши номер пункта, и я сгенерирую ответ!"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: True)
def handle_query(message):
    choice = message.text.strip()
    if choice in scenarios:
        prompt = scenarios[choice]
        bot.send_message(message.chat.id, "Генерирую ответ... 🤖")
        reply = generate_reply(prompt)
        bot.send_message(message.chat.id, f"✅ Готово:\n\n{reply}")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выбери номер от 1 до 5.")

bot.polling()
