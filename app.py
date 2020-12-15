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

        email=request.form['e1']
        phone=request.form['p1']
        course=request.form['c1']

        
        
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login('faketestcodeheroku@gmail.com','balram5525')
        TEXT='Hello {0},\nThank you for register in our  college Ims ghaziabad\nour faculty will call you for the {1} course you enrolled soon\nThank you '.format(Name,course)
        SUBJECT = "Acknowledgement"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        server.sendmail("faketestcodeheroku@gmail.com", email, message)
        server.quit()
        
        return render_template("registeration.html")

if __name__=="__main__":
    app.run()
