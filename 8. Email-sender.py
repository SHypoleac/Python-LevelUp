import yagmail

my_email=input("Type your email address")
password=input("and password")
me=yagmail.SMTP(my_email, password)
print("FAILED! Now you can use normal email service providers, good luck ;)")
onmail="MichalWolonciej@interia.pl"
topic="Hello Python!"
msg="I was send by Python program"
me.send(to=onmail, subject=topic, contents=msg)
