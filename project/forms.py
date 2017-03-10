from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired()], render_kw={"placeholder": "Name"})
    email = StringField("Email", [validators.DataRequired(), validators.Email('your@email.com')], render_kw={"placeholder": "E-Mail"})
    message = TextAreaField("Message", [validators.DataRequired()], 
    	render_kw={"placeholder": "Message (banned for Flask frozen pages)", "rows": 4})
    submit = SubmitField("Send Message")