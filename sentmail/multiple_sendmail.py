import smtplib
def sentmail():
    #list of the people who receive the mail    
    listt=["anchalmittal3010@gmail.com","mayank.mcs17.du@gmail.com","mayankgangwar44@gmail.com","anchal.mcs17.du@gmail.com"]
  
    # list to the people who receive the msg  
    message=["msg1 ","msg2 ","msg3 ","msg4"]
    
    for i in range (len(listt)):
        s=smtplib.SMTP("smtp.gmail.com",587)
        # for encrypt at transport layer
        s.starttls()

        #create login
        s.login("anchal.mcs17.du@gmail.com","password")
        
        # sendmail from sender anchal.mcs17.du@gmail.com
        
        s.sendmail("anchal.mcs17.du@gmail.com",listt[i],message[i])
        
        # quit the seesion
        s.quit()
sentmail();        
        
    
