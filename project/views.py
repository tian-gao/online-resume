from flask import render_template

from app import app, pages


@app.route('/')
def home():
    posts = [page for page in pages if 'section' in page.meta]
    print posts[0].path
    print posts[0].meta['content'][0]['company']
    # for key in posts[1].meta.keys():
    #     print key, posts[1].meta['key']
    # print type(posts[0])
    # Sort pages by date
    # sorted_posts = sorted(posts, reverse=True,
    #     key=lambda page: page.meta['date'])
    return render_template('index.html', pages=posts)


@app.route('/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
