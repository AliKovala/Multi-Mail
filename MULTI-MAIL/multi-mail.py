import smtplib, ssl
from email.message import EmailMessage
from colorama import Fore, Back, Style, init
import os
os.system('color 0')
os.system("cls")
print(Fore.GREEN, """
 █████╗ ██╗     ██╗██╗  ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗      █████╗ 
██╔══██╗██║     ██║██║ ██╔╝██╔═══██╗██║   ██║██╔══██╗██║     ██╔══██╗
███████║██║     ██║█████╔╝ ██║   ██║██║   ██║███████║██║     ███████║
██╔══██║██║     ██║██╔═██╗ ██║   ██║╚██╗ ██╔╝██╔══██║██║     ██╔══██║
██║  ██║███████╗██║██║  ██╗╚██████╔╝ ╚████╔╝ ██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                     
""")
try:
	soru = int(input('[1] NASIL KULLANILIR ? / How to use ?\n[2] ÇOKLU MAİL GÖNDER / SEND MULTI MAIL: '))
except ValueError:
	print(" 1 yada 2 | 1 or 2")

if(soru == 1):
	try:
		dil = int(input("DİL / LANG\n [1] TR [2] EN: "))
	except ValueError:
			print(" 1 yada 2 | 1 or 2")
	if(dil == 1):
		print(
			"""
			1 > Öncelikle mail göndermek istediğin kişileri >> persons.txt << dosyasına yazın.
				Örn.: 
				a@asd.com
				b@asd.com
				c@asd.com
				d@asd.com
			2 > Mesajınızı >> message.txt << dosyasına yazın.
			3 > Mailiniz SMTP ayarlarını kontrol etmeniz gerek.
			4 > Mail bilgilerinizi hatasız girin.
			5 > Ardndan Mail işlemi başlamak üzere
			"""
		)
	elif(dil == 2):
		print(
			"""
			1 > First of all, write the people you want to send mail to >> persons.txt << file.
				eg:
					a@asd.com
					b@asd.com
					c@asd.com
					d@asd.com
			2	> Write your message to >> message.txt <<
			3 > You need to check your mail SMTP settings.
			4 > Enter your mail information without error.
			5 > Then Mail process is about to start
			"""
		)
elif(soru == 2):
	try:
		dil = int(input("DİL / LANG\n [1] TR [2] EN: "))
	except ValueError:
			print(" 1 yada 2 | 1 or 2")
	if(dil == 1):
		mail_adresi = input("Mail adresi : ")
		password = input("Şifre : ")
		smtp_mail = input("SMTP SUNUCUSU örn(smtp.gmail.com): ")
		port = int(input("PORT (465 / 587) : "))
		konu = input("KONU: ")
	elif(dil == 2):
		mail_adresi = input("Mail Address : ")
		password = input("Password : ")
		smtp_mail = input("SMTP SERVER example(smtp.gmail.com): ")
		port = int(input("PORT (465 / 587) : "))
		konu = input("SUBJECT: ")

	EMAIL_ADDRESS = mail_adresi
	EMAIL_PASSWORD = password

	mail = EmailMessage()

	mail['Subject'] = konu
	mail['From'] = EMAIL_ADDRESS
	fr = open("persons.txt","r")
	kisiler = fr.readlines()
	icerik = open("message.txt","r")
	icerik_oku = icerik.readlines()

	mesaj = " ".join(icerik_oku)

	mail.set_content(mesaj)

with smtplib.SMTP_SSL(smtp_mail, port) as smtp:
	for i in kisiler:
		del mail['To']
		mail["To"] = i
		try:
			smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		except:
			print(Back.RED+'    > BAŞARISIZ GİRİŞ KULLANICI ADI YADA ŞİFRE HATALI')
			print(Back.RED+'    > FAILED LOGIN INCORRECT USERNAME OR PASSWORD')
		print(i+' Kişisine Gönderildi')
		if(smtp.send_message(mail)):
			print('MAİL BAŞARIYLA GÖNDERİLDİ\nMAIL SUCCESSFULLY SENT')