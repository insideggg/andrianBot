import telebot
import time

# Initialize bot with your token
API_TOKEN = '7445735950:AAE1z05ln_b7b4hZ-z31ABjRXJpxX0hWQZQ'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Send the first message
    bot.send_message(message.chat.id, "11.08.24 Неділя, ти збираєшся і їдеш в Жмеренку!")

    # 3-second delay
    time.sleep(3)

    # Send the second message
    bot.send_message(message.chat.id, "Добре, це жарт. Поїдеш іншим разом")

    # Send a Google Maps link
    bot.send_message(message.chat.id,
                     "https://www.google.com.ua/maps/place/Peyntbol%CA%B9nyy+Klub+B3+L%CA%B9viv/@49.8840672,23.9281586,14z/data=!4m7!3m6!1s0x473adf74dcbfc7dd:0x6fd6d5439a8d3523!8m2!3d49.8840672!4d23.9477561!15sCgvQutC70YPQsSBiM5IBEHBhaW50YmFsbF9jZW50ZXLgAQA!16s%2Fg%2F11vdmzvtp3?hl=ru&entry=ttu")

    # Path to your video file
    video_path = 'video_introduction.mp4'
    video = open(video_path, 'rb')

    # Send the video
    try:
        bot.send_video(message.chat.id, video)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        video.close()
    # video = open(video_path, 'rb')
    # bot.send_video(message.chat.id, video)
    # video.close()


# Start polling (waiting for messages)
bot.polling()

