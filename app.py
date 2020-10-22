from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json
from flask_mail import Mail,Message


app=Flask(__name__)

app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'priyankamahakud15@gmail.com'
app.config['MAIL_PASSWORD'] = 'intelcore@31'
#app.config['MAIL_DEFAULT_SENDER'] = ('Priyanka from Keonjhar','priyankamahakud15@gmail.com')
app.config['MAIL_MAX_EMAILS'] = 5
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

#mail = Mail()
mail.init_app(app)

@app.route('/')
def index():
	msg=Message('Hello there',sender=('Priyanka from Keonjhar','priyankamahakud15@gmail.com'), recipients=['priyankamahakud23@gmail.com'])#subject, you can add the sender here as well
	#Smsg.add_recipient('priyankamahaku31@gmail.com')
	msg.body = 'This a test email sent from Priyanka and you don\'t have to reply.'# You cannot use both body and html. only one can be used.
	#msg.html = '<b>This a  bold  email sent from Priyanka and you don\'t have to reply.<b>'
	#to attach attachments.

	"""
	with app.open_resource('music.jpg') as guitars:
		msg.attach('music.jpg', 'image/jpg',guitars.read())
	mail.send(msg)"""

	with app.open_resource('memo.pdf') as memomanual:
		msg.attach('memo.pdf', 'document/pdf',memomanual.read())
	mail.send(msg)

	return' I hope the Message has been sent again  !'

#required fields
	"""
	msg = Message(
		subject='',
		recipients='',
		body='',
		html='',
		sender='',
		cc = '',
		bcc = '',
		attachments = [],
		reply_to = [],
		date = 'date',
		charset = '', #will give you ascii or utf-8
		extra_headers = {'':''}, #will send extra headers if you want to send along with the email,header name and header value
		mail_options = [],
		rcpt_options = []

		)
	"""

"""

#for multiple recipients
@app.route('/bulk')
def bulk():
	users = [{'name':'Priyanka', 'email':'priyankamahaku31@gmail.com'}]
#for multiple users nd data will be carried down from database
	with mail.connect() as conn:
		for user in users:
			msg = Message('Bulk!', recipients[user['email']])
			msg.body = 'Lets try!'
			conn.send(msg)
"""




if __name__ == '__main__':
	app.run(debug=True)