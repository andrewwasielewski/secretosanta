import random
import sys
import smtplib, ssl
from email.message import EmailMessage

SEND_EMAIL = False
DEBUG_MODE = True

all_people = {'name1': 'email1', 'name2': 'email2', 'name3': 'email3', 'name4': 'email4', 'name5': 'email5', 'name6': 'email6', 'name7': 'email7', 'name8': 'email8', 'name9': 'email9'}
not_allowed = {'name1': ['name2', 'name3'], 'name2': ['name1', 'name3'], 'name3': ['name1', 'name2'], 'name4': ['name5'], 'name5': ['name4'], 'name8': [], 'name9': [], 'name6': ['name7'], 'name7': ['name6']}
secret_santas = dict()

remaining_people = list(all_people.keys())
for cur_person in all_people.keys():

	# make a list of the remaining people (and remove self)
	selection_list = remaining_people.copy()
	if cur_person in selection_list:
		selection_list.remove(cur_person)

	# filter out people the current person is not allowed to pick
	if not_allowed.get(cur_person) != None:
		for not_allowed_person in not_allowed.get(cur_person):
			if not_allowed_person in selection_list:
				selection_list.remove(not_allowed_person)

	# exit if no possible options left
	if not selection_list:
		print('Failure! No people left to pick for ', cur_person, '\n')
		sys.exit(0)

	# pick a person at random from the allowed people
	picked_person = random.choice(selection_list)
	remaining_people.remove(picked_person)

	if DEBUG_MODE:
		print(cur_person, ' picked ', picked_person, ' from ', selection_list)
	secret_santas[cur_person] = picked_person

print('\nAll people have been assigned a secret santa\n')

if not SEND_EMAIL:
	sys.exit(0)

# email settings
port = 465
smtp_server = 'smtp.gmail.com'
sender_email = 'youremail@gmail.com'
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	for k, v in secret_santas.items():
		receiver_email = all_people[k]

		content = """Greetings {},\n\nYou\'ve been picked as the secret santa for \"{}\" !\n\nDon't tell anyone or you'll be on the naughty list,\nSanta Claus""".format(k, v)
		msg = EmailMessage()
		msg.set_content(content)
		msg['Subject'] = 'Merry Christmas!'
		msg['From'] = sender_email
		msg['To'] = receiver_email

		print('sending email to ', receiver_email)
		server.send_message(msg)
