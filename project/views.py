from flask import render_template

from app import app, pages


@app.route('/')
def home():
    d = {}
    for page in pages:
        sec = page.meta['section']
        d[sec] = d.get(sec, page.meta['content'])
    
    return render_template('index.html', 
        education = d['education'],
        professional = d['professional'],
        extracurricular = d['extracurricular'],
        publications = d['publications'],
        honors = d['honors'])


