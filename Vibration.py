import schedule
import time
from datetime import datetime
import pygame
import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "rpi652781@gmail.com"
receiver_email = "pimonitor7@gmail.com"
password = "pi187256"
context2 = ssl.create_default_context()

ExecutionTime1 = "7:00"  # time of the day for signal to be played
ExecutionTime2 = "18:00"  # a second time for the signal to be played


def output_signal():
    # output vibration start
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    print ("starting vibration...")
    message = """\
        Subject: Vibration

        Started at """ + dt_string
    
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context2) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    finally:
        # play increasing signal
        pygame.mixer.init(frequency=1000)
        pygame.mixer.music.load("/home/pi/Desktop/wav_inc.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

    
        pygame.mixer.music.load("/home/pi/Desktop/wav_const.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)


        # output vibration end
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        print ("im done")
        message = """\
            Subject: Vibration
            
            Ended at """ + dt_string
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context2) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        finally:
            return


# startup
time.sleep(10)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
print ("starting up")
message = """\
    Subject: Vibration
    
    Script startup at """ + dt_string

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context2) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
finally:
    schedule.every().day.at(ExecutionTime1).do(output_signal)
    schedule.every().day.at(ExecutionTime2).do(output_signal)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
