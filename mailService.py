# send mail using outlook mail service

def mail_service(email,metadata):

    import smtplib
    import getpass

    # body to mail
    subject,email_body=metadata['subject'],metadata['email_body']
    
    
    mail_body = f'Subject:{subject} \n\n' + f'{email_body}'

    try:
        smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)

    except Exception as e:
        print(e)

        smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)

    smtpObj.ehlo()

    smtpObj.starttls()

    print("--------------Login---------------")

    try:
        password=getpass.getpass(prompt='',stream=None)
        smtpObj.login('0201csai099@niet.co.in',password) 

    except Exception as error:
        print(error)

        print("Login Failed")


    smtpObj.sendmail('0201csai099@niet.co.in', email,mail_body)

    load_gif()

    print(f"Mail Succesfully Sent to {email}")

    smtpObj.quit()
    del getpass,smtplib




#check if the email recieved is from gmail or outlook


def load_gif():
    import time

    from tqdm import tqdm

    for _ in tqdm(range(10),desc="Sending your Mail.....",ascii=False):

        time.sleep(0.01)

    time.sleep(2)


def sendmail(email,metadata):

    extension=email.lower().split('@')[1]
    if extension:
        mail_service(email,metadata)
    else:
        print("Other Mail Services are not Supported Yet..")



if __name__=='__main__':
    # sendmail(email,metadata)
    sendmail('prateekasme@gmail.com',{'subject':'Hoooooooooo & Hiiiiiiiii','email_body':'aur kaisa hai bro'})

