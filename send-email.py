import email.message

# Part I: Create and set an email object and related information
msg=email.message.EmailMessage()
msg["From"]="llm234@ha.org.hk"
msg["To"]="llm234@ha.org.hk"
msg["Subject"]="Hello Python send email"

# Text Message
# msg.set_content("Python Program Text Message")

# Alternative Content
msg.add_alternative("<h3>Test HTML Tilte</h3>", subtype="html")

# Part II: Connect to SMTP server
import smtplib

#########################################################################################
# # Set Proxy for Urllib
# proxy="https://llm234:85167787887Ss!@proxy.ha.org.hk:8080"
# proxy_support=req.ProxyHandler({'https':proxy}) # Build ProxyHandler object by given proxy
# opener = req.build_opener(proxy_support) # Build opener with ProxyHandler object
# req.install_opener(opener) # Install opener to request
# r = urllib.request.urlopen('http://icanhazip.com',timeout = 1000) # Open url
##########################################################################################

# SMTP can be found on google
# server=smtplib.SMTP_SSL("smtp.ha.org.hk") #Gmail SMTP 
server=smtplib.SMTP_SSL("MAILDEVSMTP.server.ha.org.hk") #Gmail SMTP 
# server=smtplib.SMTP_SSL("MAILCORPHTS.server.ha.org.hk",25) #Gmail SMTP 
# server.login("dsonlamatwork@gmail.com","85167787887Ss") # Verification of Username and Password
# server.send_message(msg)
# server.close()

# print("Email Sent from: "+ msg["From"]+" to "+msg["To"])



