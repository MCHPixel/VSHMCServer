from flask import Flask, render_template, request, redirect, session, url_for
from translations.strings import translations

app = Flask(__name__)
app.secret_key = '68034459u'  # Replace with a strong secret key in production

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['lang'] = request.form.get('lang', 'en')
        return redirect(url_for('index'))

    lang = session.get('lang', 'en')
    texts = translations.get(lang, translations['en'])
    return render_template('landing_page.html', texts=texts, lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
