import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
dollar=50
GROUP_ID = ['#']
token = '625524568a3M'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber =1084525687
@bot.message_handler(commands=["start"])
def start(message):
	found='unpr'
	chat_id = message.chat.id
	with open("premium.txt", "r") as file:
		for line in file:
			if str(chat_id) in line.strip():
				found='pro'
	if not 'pro' in found:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
		return
	bot.reply_to(message,"Send the file now \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	found='unpr'
	chat_id = message.chat.id
	with open("premium.txt", "r") as file:
		for line in file:
			if str(chat_id) in line.strip():
				found='pro'
	if not 'pro' in found:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @MNOW4")
		return
	current_dir = os.getcwd()
	for filename in os.listdir(current_dir):
		if filename.endswith(".start"):
			bot.reply_to(message, "هناك شخص اخر يستخدم البوت")
			return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			if total > 100000:
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='الحد الاقصي للفحص 100 بطاقه لكل ملف ')
				return
			with open("start.start", "w") as yu:
				pass
			for cc in lino:
				time.sleep(15)
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @MNOW4')
						os.remove('start.start')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @MNOW4 ''', reply_markup=mes)
				
				print(last)
				if "live" in last or 'Funds' in last:
					msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑖𝑛𝑠𝑢𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑡 𝑓𝑢𝑛𝑑𝑠 ✅
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 
◆ 𝑻𝑹𝒀 𝑰𝑵 ➜ 𝚃𝙶 𝙿𝚁𝙴𝙼𝙸𝙺𝙼 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg)
					live += 1
				elif 'success' in last:
					msg1=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑼𝑪𝑪𝑬𝑺𝑺
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg1)
					live += 1
				else:
					dd += 1
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @MNOW4')
	os.remove('start.start')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
@bot.message_handler(commands=["chk"])
def start(message):
	found='unpr'
	chat_id = message.chat.id
	with open("premium.txt", "r") as file:
		for line in file:
			if str(chat_id) in line.strip():
				found='pro'
	if not 'pro' in found:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url="https://t.me/PEGASTS")
		keyboard.add(contact_button)
		
		bot.send_message(chat_id=message.chat.id, text='''
		→ لا يمكنك استخدام البوت مجانا الا في الجروب الخاص بنا 
		→ You can only use the bot for free in our group 
		''', reply_markup=keyboard)
		return
	cc = message.text.replace('/chk ', '')
	try:
		data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
	except:
		pass
	try:
		bank=(data['bank']['name'])
	except:
		bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		emj=(data['country']['emoji'])
	except:
		emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		cn=(data['country']['name'])
	except:
		cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		dicr=(data['scheme'])
	except:
		dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		typ=(data['type'])
	except:
		typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
	try:
		url=(data['bank']['url'])
	except:
		url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑼𝑪𝑪𝑬𝑺𝑺
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
	msgu = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑖𝑛𝑠𝑢𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑡 𝑓𝑢𝑛𝑑𝑠 ✅
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 
◆ 𝑻𝑹𝒀 𝑰𝑵 ➜ 𝚃𝙶 𝙿𝚁𝙴𝙼𝙸𝙺𝙼 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
	time.sleep(15)
	try:
		last = str(Tele(cc))
	except Exception as e:
		print(e)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='An error occurred while checking your card ⚠️')
		return
	if "live" in last or 'Funds' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgu)
	elif 'success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		msg2=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝐷𝐸𝐶𝐿𝐼𝑁𝐸𝐷 ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙱𝚁𝙰𝙸𝙽𝚃𝚁𝙴𝙴 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @MNOW4
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg2)
@bot.message_handler(commands=["restart"])
def start(message):
	try:
		os.remove('start.start')
		bot.reply_to(message, "The Bot Has Been Restarted")
	except:
		bot.reply_to(message, "error")
@bot.message_handler(commands=["add"])
def start(message):
	chat_id = message.from_user.id
	if chat_id == 5267630441:
		id=message.text.replace("/add ", "")
		with open("premium.txt", "a+") as file:
			file.writelines('\n'+id)
		bot.reply_to(message,"It has been added to the premium list  ✅")
print("تم تشغيل البوت")
bot.polling()