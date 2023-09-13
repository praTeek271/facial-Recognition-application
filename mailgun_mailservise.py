import requests
import threading as th
import os

def send_complex_message(reciever_email, path_to_file, name_of_file,text_msg="",html_msg=""):
    file=os.path.join(path_to_file,name_of_file)
    return (requests.post("https://api.mailgun.net/v3/codebusters.codes/messages",
        auth=("api", "4e05c4f4e6224165c75974b388fa2b94-30344472-05226e85"),
        files=[("attachment", ("sample.png", open(file,"rb").read())),
               ],
        data={"from": "Admin",
              "to": f"{reciever_email}",
              "subject": "Security FIGHT Alert from : TEAM\t''>.<''\t'",
              "text": "{0}".format(text_msg),
              "html": "<html>{0}</html>".format(html_msg)}))


if __name__=="__main__":
    send_complex_message("prateekasme@outlook.com","","img.png",'yeah dekh','<a href="https://github.com/praTeek271">click me to test me</a>')