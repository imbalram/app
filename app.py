#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#!/usr/bin/env python
# coding: utf-8

# In[8]:

subject="acknowledgement of college regeisteration"
from flask import Flask,render_template,request
import smtplib
app=Flask(__name__)
@app.route("/")
def xyz():
  return render_template("registeration.html")
@app.route("/basicdetails",methods=['GET','POST'])
def hjfhjfhjf():
  if(request.method=='POST'):
      
      Name=request.form['n1']
      Sur_Name=request.form['n2']
      email=request.form['e1']
      phone=request.form['p1']
      course=request.form['c1']
      
      
      server=smtplib.SMTP_SSL('smtp.gmail.com',465)
      server.login('faketestcodeheroku@gmail.com','balram5525')
      TEXT='Hello {0},\nthank you for register in our  college Ims ghaziabad\n our faculty will call you for the {2} course\n Thank you '.format(Name,course)
      SUBJECT = "Acknowledgement"
      message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

      server.sendmail("faketestcodeheroku@gmail.com", email, message)
      server.quit()
      
      return render_template("registeration.html")
if __name__=="__main__":
  app.run()

