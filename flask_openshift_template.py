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


def json_mm1(*args):
    ms = mm1.MM1(*args)
    return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(ms.pk)),
                    'check': ms.check_stable(),
                    'valcal': {'km': round(ms.k_mean(), 5),
                               'lq': round(ms.lq(), 5),
                               'ws': round(ms.ws(), 5),
                               'wq': round(ms.wq(), 5),
                               'ro': round(ms.ro, 5)
                               }
                    })


def json_mminf(*args):
    ms = mminf.MMinf(*args)
    return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(ms.pk)),
                    'check': ms.check_stable(),
                    'valcal': {'km': round(ms.k_mean(), 5),
                               'wp': round(ms.w_ro(), 5),
                               'ro': round(ms.ro, 5)
                               }
                    })


def json_mmv(*args):
    ms = mmv.MMV(*args)
    pk = sorted(set(ms.pk), reverse=True)
    return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(pk)),
                    'check': ms.check_stable(),
                    'valcal': {'gm': round(ms.gamma_mean(), 5),
                               'jm': round(ms.j_mean(), 5),
                               'pt': round(ms.pt(), 5),
                               'ro': round(ms.ro, 5)
                               }
                    })


def json_mmvk(*args):
    ms = mmvk.MMVK(*args)
    return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(ms.pk)),
                    'check': ms.check_stable(),
                    'valcal': {'pt': round(ms.pt(), 5),
                               'ro': round(ms.ro, 5)
                               }
                    })


def json_mmvkn(*args):
    ms = mmvkn.MMVKN(*args)
    return jsonify({'data': tuple({'x': x, 'y': round(y, 12)} for x, y in enumerate(ms.pk)),
                    'check': ms.check_stable(),
                    'valcal': {'km': round(ms.k_mean(), 5),
                               'tm': round(ms.t_mean(), 5),
                               'pt': round(ms.pt(), 5),
                               'pv': round(ms.pv(), 5),
                               }
                    })


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
        return json_mm1(*base_args)
    if model == 'mminf':
        return json_mminf(*base_args)
    if model == 'mmv':
        return json_mmv(int(data['v']), *base_args)
    if model == 'mmvk':
        return json_mmvk(int(data['v']), *base_args)
    if model == 'mmvkn':
        return json_mmvkn(int(data['v']), float(data['a']),
                          float(data['miu']), int(data['to']), int(data['n']))


if __name__ == '__main__':
    from logging.handlers import RotatingFileHandler
    import logging
    handler = RotatingFileHandler('sys.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run(
        debug=True
    )
