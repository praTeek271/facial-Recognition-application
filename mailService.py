 # send mail using outlook mail service
import threading as th
import requests
import smtplib
import getpass
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
        print("--------------Login**SUCESS---------------")

    except Exception as error:
        print(error)

        print("Login Failed")


    smtpObj.sendmail('0201csai099@niet.co.in', email,mail_body)

    load_gif()

    print(f"Mail Succesfully Sent to {email}")

    smtpObj.quit()
    del getpass,smtplib



def send_complex_message(messages,resv_email):
    return (requests.post(
        "https://api.mailgun.net/v3/sandbox05976aef3a874496b7b0d3e7619795c9.mailgun.org/messages",
        auth=("api", "4e05c4f4e6224165c75974b388fa2b94-30344472-05226e85"),
        files=[("attachment", ("test.jpg", open("files/test.jpg","rb").read())),
               ("attachment", ("test.txt", open("files/test.txt","rb").read()))],
        data={"from": "Excited User <prateekasme@gmail>",
              "to": f"{resv_email}",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!",
              "html": "<html>HTML version of the body</html>"}))
# def send_simple_message(messages,resv_email):
#     print("sending mail to ",resv_email)
#     return (requests.post("https://api.mailgun.net/v3/sandbox05976aef3a874496b7b0d3e7619795c9.mailgun.org/messages",
# 		auth=("api", "4e05c4f4e6224165c75974b388fa2b94-30344472-05226e85"),
# 		data={"from": "Excited User prateekasme@gmail.com",
# 			"to": [f"{resv_email}", "prateekasme@gmail.com"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"}))

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/codebusters.codes/messages",
		auth=("api", "4e05c4f4e6224165c75974b388fa2b94-30344472-05226e85"),
		data={"from": "Excited User <mailgun@codebusters.codes>",
			"to": ["antonystarkasme@outlook.com", "YOU@codebusters.codes"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})

# API base URL:https://api.mailgun.net/v3/sandbox05976aef3a874496b7b0d3e7619795c9.mailgun.org

# API key:
# 4e05c4f4e6224165c75974b388fa2b94-30344472-05226e85

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

    sendmail('antonystarkasme@outlook.com',{'subject':'Hoooooooooo & Hiiiiiiiii','email_body':'aur kaisa hai bro\nthis is a test mail'})
    # thrd1=th.Thread(target=send_simple_message,args=('hello who are you dude', '0201csai099@niet.co.in'))
    # thrd2=th.Thread(target=load_gif)
    # thrd1.start()
    # thrd2.start()
    

    # send_simple_message()
