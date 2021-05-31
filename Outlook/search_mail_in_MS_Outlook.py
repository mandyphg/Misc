import win32com.cient

outlook = win32com.client.Dispatch("OutlookApplication").GetNamespace("MAPI")
inbox = outlook.Folders[0].Folders["Inbox"]
messages = inbox.Items

mail_subject = "Email Subject to be searched"

# Get email matched the mail_subject
message = messages[mail_subject]

# Get attachments
message_attachments = message.attachments

# Get sender
message_sender = message.Sender.GetExchangeUser().PrimarySmtpAddress


