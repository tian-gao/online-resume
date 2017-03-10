from flask import render_template, redirect, url_for
from flask import request

from app import app, pages
from forms import ContactForm

@app.route('/', methods = ['GET','POST'])
def home():
    d = {}
    for page in pages:
        sec = page.meta['section']
        d[sec] = d.get(sec, page.meta['content'])
    form = ContactForm()
    err_string = []
    show_success = False
    
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            print 'Please fill in all fields'
            for field, errors in form.errors.items():
                for error in errors:
                    err_string += ["Error in the %s field - %s" % (getattr(form, field).label.text, error)]
            print err_string
            show_success = False
            return render_template('index.html', 
                education = d['education'],
                professional = d['professional'],
                extracurricular = d['extracurricular'],
                publications = d['publications'],
                honors = d['honors'],
                skills = d['skills'],
                form = form,
                err_string = err_string,
                show_success = show_success)

        else:
            # msg = Message("Message from your visitor" + form.name.data,
            #               sender='YourUser@NameHere',
            #               recipients=['yourRecieve@mail.com', 'someOther@mail.com'])
            # msg.body = """
            # From: %s <%s>,
            # %s
            # """ % (form.name.data, form.email.data, form.message.data)
            # mail.send(msg)
            # return "Successfully  sent message!"
            show_success = True
            print '\nSuccessfully  sent message!\n'
            print request.form['name']
            print request.form['email']
            print request.form['message']
            return render_template('index.html', 
                education = d['education'],
                professional = d['professional'],
                extracurricular = d['extracurricular'],
                publications = d['publications'],
                honors = d['honors'],
                skills = d['skills'],
                form = form,
                err_string = err_string,
                show_success = show_success)
            # return redirect(url_for('home'), )

    else:
        return render_template('index.html', 
            education = d['education'],
            professional = d['professional'],
            extracurricular = d['extracurricular'],
            publications = d['publications'],
            honors = d['honors'],
            skills = d['skills'],
            form = form,
            err_string = err_string,
            show_success = show_success)
