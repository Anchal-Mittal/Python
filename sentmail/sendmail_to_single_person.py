import smtplib
def fun():
    
    s=smtplib.SMTP("smtp.gmail.com",587)
    #for encrypt
    s.starttls()

    # create login
    s.login("anchal.mcs17.du@gmail.com","qwerttyy")

    #for message 
    message="first mail send using python"

    #sendmail
    s.sendmail("anchalmittal3010.gmail.com","anchal.mcs17.du@gmail.com",message)
    s.quit()

fun();
    
