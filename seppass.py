import telebot
import sys
from telebot import types

sys.path.append('./modules')
from auth import auth_main

telebot.apihelper.proxy = {
	'http': 'socks5://sockduser:f2%kElHW0SEC@46.101.118.222:1080',
	'https': 'socks5://sockduser:f2%kElHW0SEC@46.101.118.222:1080'
}

bot = telebot.TeleBot("1028700604:AAGYy9m51_TGRUCUzGagAQKnKZfTiR0tFk8")

@bot.message_handler(commands=['start'])
def message_handler_start_main(message):
	bot.send_message(message.chat.id,
		'Привет!\nЯ - бот, предназначенный для хранения паролей. Хранение оных очень надежно, т.к. каждый шифруется вашим собственный'+
		' GPG ключем, пароль от которого знаете только вы (конечно если выбрали пункт "хранить пароль у себя" в настройках).'+
		'\n\nИспользуйте /auth, чтобы войти в акк, или создать его. Используйте команду /help, если растерялись.\n\nУдачи.'
		)

@bot.message_handler(commands=['auth'])
def message_handler_auth_main(message):
	auth_main(message, bot)

@bot.message_handler(commands=['help'])
def message_handler_auth_main(message):
	bot.send_message(message.chat.id,
	'Команды и их описание, которые может выполнять этот бот.\n\n'+
	'---------------------------------------------------------------\n'+
	'Команды, доступные без авторизации:\n'+
	'---------------------------------------------------------------\n\n'+
	'/start - Приветствие, и небольшое описание возможностей бота.\n\n'+
	'/auth - Авторизация пользователя, для дальнейшей работы.\n\n'+
	'/about - О разработчике.\n\n'+
	'/help - Очень трудно догадаться (выводит это сообщение).\n\n'+
	'---------------------------------------------------------------\n'+
	'Команды, доступные после авторизации:\n'+
	'---------------------------------------------------------------\n\n'+
	'/ls - Просмотр списка шифрованых записей.\n\n'+
	'/cat - Просмотр записи, но нужно ввести пароль, чтоб ее расшифровать.\nИспользуется так: /cat name (после ввода пароля (если надо) вам вернется запись, которую вы шифровали с именем "name")\n\n'+
	'/insert - Создать новую запись, ввести ее сообщением.\nИспользуется так: /insert name. После введите запись.\n\n'+
	'/generate - Сгенерирует запись, используя случайные буквы, цифры и спец. символы.\nИспользуйте так: /generate name -12 (Сгенерирует случаную запись с названием "name", длиной в 12 символов)\n\n'+
	'/edit - Изменяет запись.\nИспользуется так: /edit name. Затем вводите новое сообщение, которое будет записанно в запись, под названием "name".\n\n'+
	'/rm - Удаляет запись.\nИспользуется так: /rm name.\n\n'+
	'/mv - Перемещает запись.\n\n'+
	'/settings - Настройки.'
	)

@bot.message_handler(commands=['about'])
def message_handler_auth_main(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text= 'Сайт разработчика.', url='https://sepezho.ru'))

	bot.send_message(message.chat.id,
		'-----------------Created by SEPEZHO-----------------\n'+
		'Btw by this guy: Vladislav Bliznyuk\n'+
		'Start creating: 23.01.2020\n'+
		'End creating: __.__.____\n'+
		'Version: 0.0.1\n'+
		'Have a nice day\n'+
		'-----------------Created by SEPEZHO-----------------\n',
		reply_markup=markup)

bot.polling()