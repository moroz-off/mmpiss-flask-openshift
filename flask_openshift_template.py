# -*- coding: utf-8 -*-
from __future__ import division
from flask import Flask, redirect, render_template, request, url_for, jsonify
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
                           static_css=static_css, static_js=static_js, url_for=url_for)


@app.route("/models/")
@app.route("/models/<model>", methods=["PUT", "POST"])
def models(model=None):
    if not model:
        return redirect(url_for('index'))
    if request.json:
        data = request.json
    else:
        data = request.form
    base_args = (float(data['lambd']), float(data['miu']), int(data['to']))
    if model == 'mm1':
        return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(mm1.MM1(*base_args).pk))})
        # return jsonify({'data': []})
        # return mm1.MM1(*base_args).get_json()
    if model == 'mminf':
        return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(mminf.MMinf(*base_args).pk))})
        # return mminf.MMinf(*base_args).get_json()
    if model == 'mmv':
        return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(mmv.MMV(int(data['v']), *base_args).pk))})
        # return mmv.MMV(int(request.form['v']), *base_args).get_json()
    if model == 'mmvk':
        return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(mmvk.MMVK(int(data['v']), *base_args).pk))})
        # return mmvk.MMVK(int(request.form['v']), *base_args).get_json()
    if model == 'mmvkn':
        # return mmvkn.MMVKN(int(request.form['v']), float(request.form['lambd']),
        #                    float(request.form['miu']), int(request.form['to']),
        #                    float(request.form['n'])).get_json()
        init_mmvkn = mmvkn.MMVKN(int(data['v']), float(data['lambd']),
                                 float(data['miu']), int(data['to']), int(data['n']))
        return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(init_mmvkn.pk))})


if __name__ == '__main__':
    from logging.handlers import RotatingFileHandler
    import logging
    handler = RotatingFileHandler('sys.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run(
        debug=True
    )
