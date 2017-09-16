import smtplib

# GMAIL     | smpt.gmail.com
# Outlook   | smtp-mail.outlook.com
# Hotmail   | smtp-mail.outlook.com
# Yahoo     | smpt.mail.yahoo.com
# AT&T      | smtp.mail.att.net (port 465)
# Comcast   | smtp.comcast.net
# Verizon   | smtp.verizon.net (port 465)
# Typically use Port 587 or 465

smpt_server = 'smpt.gmail.com'
smpt_port = 587
smtpObj = smtplib.SMTP(smpt_server, smpt_port)

