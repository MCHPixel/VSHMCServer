from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def load_translation(lang_code):
    filepath = os.path.join('translations', f'{lang_code}.json')
    if not os.path.exists(filepath):
        filepath = os.path.join('translations', 'en.json')  # fallback
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def landing_page():
    lang = request.args.get('lang', 'en')
    translations = load_translation(lang)
    return render_template('landing_page.html', t=translations, current_lang=lang)

if __name__ == '__main__':
    app.run(debug=True)