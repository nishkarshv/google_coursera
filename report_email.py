#!/usr/bin/env python3
import os 
import datetime 
import reports 
import emails 
path = os.path.normpath(os.path.join(os.getcwd(), "supplier-data", 
"descriptions")) 
fruit = {} 
def get_data():
    the_text = ""
    for item in os.listdir(path):
        fruit.clear()
        filename=os.path.join(path,item)
        with open(filename) as f:
            line=f.readlines()
            for i in range(2,len(line)):
                fruit["weight"]=line[1]
                fruit["name"]=line[0]
        if the_text == "":
            the_text = "<br />".join([str("name: " + fruit["name"]), 
str("weight: " + fruit["weight"])])
        else:
            the_text = "<br />".join([the_text, "", str("name: " + 
fruit["name"]), str("weight: " + fruit["weight"])])
    #print(the_text)
    return the_text 

def main():
    paragraph = get_data()
    today = datetime.date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(today)
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)
    email = emails.generate_email("automation@example.com", 
"student-04-d994d532c433@example.com", "Upload Completed - Online Fruit Store","All fruits are uploaded to our website successfully. A detailed list is attached to this email.", attachment)
    emails.send_email(email) 

if __name__ == "__main__":
    main()
