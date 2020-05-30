import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("thakur2suyash@gmail.com", "*************")


    # message
message1 = "accuracy is less than 90%.Try again"
    

    # sending the mail 
s.sendmail("thakur2suyash@gmail.com", "1706277@kiit.ac.in", message1)
    

    # terminating the session 
s.quit()
