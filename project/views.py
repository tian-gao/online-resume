from flask import render_template, redirect, url_for, flash
from flask import request

from app import app, pages
from forms import ContactForm

@app.route('/', methods = ['GET','POST'])
def home():
    d = {}
    for page in pages:
        sec = page.meta['section']
        d[sec] = d.get(sec, page.meta['content'])
    form = ContactForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit() == False:
            for field, errors in form.errors.items():
                for error in errors:
                    if error == "your@email.com":
                        flash("Wrong format of email address!", 'error')
                    else:
                        flash("%s cannot be empty!" % getattr(form, field).label.text, 'error')
            return redirect(url_for('home', _anchor='contact'))

        else:
            flash('Successfully send message!', 'success')
            print '\nSuccessfully send message!\n'
            print request.form['name']
            print request.form['email']
            print request.form['message']
            return redirect(url_for('home', _anchor='contact'))

    return render_template('index.html', 
        education = d['education'],
        professional = d['professional'],
        extracurricular = d['extracurricular'],
        publications = d['publications'],
        honors = d['honors'],
        skills = d['skills'],
        form = form)
