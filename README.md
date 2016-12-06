# Математические методы построения инфокоммуникационных сетей и систем

This is a template to host in [OpenShift](https://openshift.redhat.com) a Python 3.x app using [Flask](http://flask.pocoo.org/). If you want to learn the process, you can read the [step by step](https://github.com/moroz-off/mmpiss-flask-openshift/blob/master/Step-by-step.md) guide.

### Используемые технологии

**Back end:**
    &nbsp;&nbsp;&nbsp;&nbsp;- [Python](https://www.python.org/) 3.3,<br> 
    &nbsp;&nbsp;&nbsp;&nbsp;- [Flask](http://flask.pocoo.org/) microframework

**Front end:**
    &nbsp;&nbsp;&nbsp;&nbsp;- [AngularJS](https://angularjs.org/)  1.5.3,<br> 
    &nbsp;&nbsp;&nbsp;&nbsp;- Foundation for Sites ([Foundation 6](https://github.com/zurb/foundation-sites)),<br> 
    &nbsp;&nbsp;&nbsp;&nbsp;- [Material Design](https://github.com/eucalyptuss/material-foundation) version of Foudation for Sites by Zurb,<br> 
    &nbsp;&nbsp;&nbsp;&nbsp;- [Foundation 6 directives for Angular](https://github.com/circlingthesun/angular-foundation-6) 1.5+,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;- [n3-line-chart](https://github.com/n3-charts/line-chart) is an easy-to-use JavaScript library for creating beautiful charts in [AngularJS](https://angularjs.org/) applications and it is built on top of [D3.js](https://d3js.org/)

[Sass](http://sass-lang.com/) (SCSS) - Syntactically Awesome Style Sheets,
[Docker](https://github.com/docker/docker) - the open-source application container engine

### Running on OpenShift

Create a Python application with this command

```bash
rhc app-create <project> python-3.3 --from-code https://github.com/moroz-off/mmpiss-flask-openshift.git
```

Checkout the "Web app" at

```
https://<project>-<namespace>.rhcloud.com
```

### Running on Docker

Run a Python application with this command

```bash
docker-compose up -d --no-recreate web
```

Checkout the "Web app" at

```
http://127.0.0.1:8051
```

# License

Code licensed under [GNU General Public License v3](http://opensource.org/licenses/GPL-3.0).
