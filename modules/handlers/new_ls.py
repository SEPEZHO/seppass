import os

def ls_main(root_folder):
	# root_folder = 'Users_folder/user_'+str(message.from_user.id)
	response_arr = []
	for root, dirs, files in os.walk(root_folder):
		for dir_ in dirs:
			response_arr.append(root+ '/' +dir_)
		for file in files:
			if file.find(".") != -1:
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
		if file_name.find(".") != -1:
			response_arr[index_file] =  line(file, root_folder)+last_symbol+file_name
		else:
			response_arr[index_file] =  line(file, root_folder)+last_symbol+'📂 '+file_name
	response_text = '╠══════════════════════════════════╣\n\n'+'  📂 '+''.join(root_folder.split('/')[-1])+'\n  ╔══════════════\n'
	for response_arr_text in response_arr:
		response_text +='  '+response_arr_text+'\n'
	response_text +='\n╠══════════════════════════════════╣'
	# bot.send_message(message.chat.id, response_text)
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
		print(listdir)
		num = listdir.index(folder)
		if len(listdir) == num+1:
			line = '       '+line
		else:
			line = '║      '+line
	return line

# a = ls_main('/home/sepezho/Documents/Portfolio/src/Components/')
a = ls_main('/home/sepezho/Documents/Portfolio/src')
print(a)