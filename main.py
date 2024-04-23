from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
import smtplib
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
app.secret_key = os.environ.get('APP_KEY')
bootstrap = Bootstrap5(app)

class ContactForm(FlaskForm):
    email = StringField(label='Email',  validators=[DataRequired(), Length(min=6), Email(message=('That\'s not a valid email address.'))])
    name = StringField(label="Your name", validators=[DataRequired()])
    subject = StringField(label="Subject", validators=[DataRequired()])
    message = TextAreaField(label="Message", validators=[DataRequired()], render_kw={'rows': 5})
    submit = SubmitField(label='Send Message')


@app.route('/', methods=['GET', 'POST'])
def home(): 
    form = ContactForm()   
    if form.validate_on_submit():
        name_submit = form.name.data 
        email_submit = form.email.data
        subject_submimt = form.subject.data
        message_submit = form.message.data
        my_email = 'jaimevillalbaoyola@gmail.com'
        password = 'sjgwizpxcgmesaps' 
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls() #make the conection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=email_submit, 
                                msg=f"Subject:{subject_submimt}\n\n{name_submit}\n{message_submit}"
                                )
        flash('Successfully sent your message', 'success')  # Agregar mensaje flash
        pass
        # return render_template('submit_form.html', form=form)  # Renderizar la misma
        
    return render_template("index.html", form=form, contact= True)


if __name__ == "__main__":
    app.run(debug=True)