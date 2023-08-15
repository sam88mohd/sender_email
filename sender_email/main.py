from email_sender.smemail import SMEmail

email = SMEmail("hello@gmail.com", "hello world")
email.send_email()
