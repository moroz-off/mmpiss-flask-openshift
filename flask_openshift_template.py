# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, request, url_for
from models import mm1, mminf, mmv, mmvk, mmvkn

__authors__ = "Морозов Денис - morozoff.py@gmail.com и Павшева Мария"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/models/")
@app.route("/models/<model>", methods=["POST"])
def models(model=None):
    if not model:
        return redirect(url_for('index'))
    base_args = (request.form['lambd'], request.form['miu'], request.form['to'])
    if model == 'mm1':
        return mm1.MM1(*base_args).get_json()
    if model == 'mminf':
        return mminf.MMinf(*base_args).get_json()
    if model == 'mmv':
        return mmv.MMV(request.form['v'], *base_args).get_json()
    if model == 'mmvk':
        return mmvk.MMVK(request.form['v'], *base_args).get_json()
    if model == 'mmvkn':
        return mmvkn.MMVKN(request.form['v'], request.form['lambd'], request.form['miu'],
                           request.form['to'], request.form['n']).get_json()


if __name__ == '__main__':
    from logging.handlers import RotatingFileHandler
    import logging
    handler = RotatingFileHandler('sys.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run(
        debug=True
    )
