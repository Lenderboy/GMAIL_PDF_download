#v1.01

import sys
import os
import credentials
import gmail_client
import re
# print help(gmail_client)
g = gmail_client.login(credentials.email_account, credentials.password)

count = 0
email = g.inbox().mail(unread = True)

# print email[1].fetch()

# for email in g.inbox().mail(unread = True):
#     email.fetch


for mail in email:
    print (mail)
    print (type(mail))
    count += 1
    mail.fetch() # if you want a screen print of what is being downloaded
    # mark the mail as read
    # mail.mark_read()
    # print mail.attachments()

    for pdf in mail.attachments:

        if re.search('.pdf', pdf.name) is not None:
            print ('Saving attachment: ' + pdf.name)
            print 'Size: ' + str(pdf.size) + ' KB'
            pdf.save('PDFdownload/' + pdf.name)
            print 'PDF attachment present'
            print re.search('.pdf', pdf.name)
            result = re.search('.pdf', pdf.name)
            print 'Real Expression result: ', result.group(0)
            print 'Real Expression result #2: ', re.search('.pdf',pdf.name).group(0)


print (count)

print 'This is pdf: ', pdf
print 'this is pdf.name: ', pdf.name

