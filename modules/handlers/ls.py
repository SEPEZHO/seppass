import os
from del_mess import del_mess

def ls_main(message, bot):
	command = message.text.split()
	way = '/home/sepezho/Documents/seppass/Users_folder/user_' + str(message.from_user.id)

	if (len(command) == 2):
		if (message.text.find('//') == -1) and (message.text.find('.') == -1):
			way = way + '/' + command[1]
			if command[1][-1] == '/':
				way = way[:-1]
			if os.path.isdir(way):
				text = ls(way)
				msg = bot.send_message(message.chat.id, text)
			else:
				msg = bot.send_message(message.chat.id,'Такой папки не существует.')
		else: 
			msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /ls папка/папка (или просто /ls)')
	elif len(command) == 1:
		text = ls(way)
		msg = bot.send_message(message.chat.id, text)
	else: 
		msg = bot.send_message(message.chat.id,'Используйте правильный синтаксис: /ls папка/папка (или просто /ls)')
	del_mess(msg, bot, 2)

def ls(root_folder):
	if root_folder[-1] == '/':
		root_folder = root_folder[:-1]
	response_arr = []
	for root, dirs, files in os.walk(root_folder):
		for dir_ in dirs:
			response_arr.append(root+ '/' +dir_)
		for file in files:
			if file.find(".gpg") != -1:
				response_arr.append(root + '/' +file)
	
	response_arr = sorted(response_arr)
	for file in response_arr:
		ls = sorted(os.listdir('/'.join(file.split('/')[:-1])))
		index = ls.index(''.join(file.split('/')[-1]))
		index_file = response_arr.index(file)
		last_symbol = '╠══ '
		if len(ls) == index + 1:
			last_symbol = '╚══ '
		file_name = ''.join(file.split('/')[-1])
		if file_name.find(".gpg") != -1:
			response_arr[index_file] =  line(file, root_folder)+last_symbol+file_name[:-4]
		else:
			response_arr[index_file] =  line(file, root_folder)+last_symbol+'📂 '+file_name
	response_text = '╠══════════════════════════════════╣\n\n'+'  📂 '+''.join(root_folder.split('/')[-1])+'\n  ╔══════════════\n'
	for response_arr_text in response_arr:
		response_text +='  '+response_arr_text+'\n'
	response_text +='\n╠══════════════════════════════════╣'
	return response_text

def line(way, root_folder):
	way = way.split('/')
	deepth = len((root_folder).split('/'))
	way = way[deepth:][:-1][::-1]
	line = ''
	i=0
	for folder in way:
		i = i+1
		depth_path = root_folder+'/'+'/'.join(way[::-1][:-i])
		listdir = sorted(os.listdir(depth_path))
		num = listdir.index(folder)
		if len(listdir) == num+1:
			line = '       '+line
		else:
			line = '║      '+line
	return line