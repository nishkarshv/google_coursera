#!/usr/bin/env python3
import shutil
import psutil
import emails
import socket

def health():
    healthstr =""
    #print(socket.gethostbyname("localhost"))
    mem = psutil.virtual_memory()
    total, used, free = shutil.disk_usage("/")
    THRESHOLD = 500*1024*1024
    if psutil.cpu_percent()> 80:
        healthstr = "Error - CPU usage is over 80%"
    elif free//1024**2 < 0.2*total//1024**2:
        healthstr = "Error - Available disk space is less than 20%"
    elif mem.available < THRESHOLD:
        healthstr = "Error - Available memory is less than 500MB"
    elif socket.gethostbyname("localhost") != "127.0.0.1":
      healthstr = "Error - localhost cannot be resolved to 127.0.0.1"
    else:
        healthstr ="Good Health"
    return healthstr
def main():
    subject = health()
    body = "Please check your system and resolve the issue as soon as possible."
    email = emails.generate_email("automation@example.com",
"student-04-d994d532c433@example.com", subject,body, None)
    emails.send_email(email)

if __name__ == "__main__":
    main()

