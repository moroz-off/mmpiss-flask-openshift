# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, request, url_for
from models import mm1, mminf, mmv, mmvk, mmvkn
import settings
from core.jinja_func import static_css, static_js

if settings.SETTINGS['lang'] == 'ru':
    from lang.ru import index as lang_index
else:
    from lang.en import index as lang_index

__authors__ = "Морозов Денис - morozoff.py@gmail.com и Павшева Мария"

app = Flask(__name__)
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'


@app.route("/")
def index():
    return render_template('index.html', settings=settings.SETTINGS, lang=lang_index, author=__authors__,
                           static_css=static_css, static_js=static_js)


@app.route("/models/")
@app.route("/models/<model>", methods=["POST"])
def models(model=None):
    if not model:
        return redirect(url_for('index'))
    base_args = (float(request.form['lambd']), float(request.form['miu']), int(request.form['to']))
    if model == 'mm1':
        return mm1.MM1(*base_args).get_json()
    if model == 'mminf':
        return mminf.MMinf(*base_args).get_json()
    if model == 'mmv':
        return mmv.MMV(int(request.form['v']), *base_args).get_json()
    if model == 'mmvk':
        return mmvk.MMVK(int(request.form['v']), *base_args).get_json()
    if model == 'mmvkn':
        return mmvkn.MMVKN(int(request.form['v']), float(request.form['lambd']),
                           float(request.form['miu']), int(request.form['to']), float(request.form['n'])).get_json()


if __name__ == '__main__':
    from logging.handlers import RotatingFileHandler
    import logging
    handler = RotatingFileHandler('sys.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run(
        debug=True
    )
