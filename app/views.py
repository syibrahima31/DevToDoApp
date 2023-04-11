from flask import Blueprint, render_template, redirect, url_for, request
from .models import Task
from . import db

bp = Blueprint("bp", __name__)


@bp.route("/")
def index():
    taches = Task.query.order_by(Task.id).all()
    print(taches)
    return render_template('index.html', taches=taches)


@bp.route("/update/<int:id>")
def update(id):
    task = Task.query.get(id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('bp.index'))


@bp.route("/traitement", methods=["GET", "POST"])
def traitement():
    form = request.form
    action = form.get('action')
    if action == 'save':
        title = form.get('title')
        tache = Task(title=title)
        db.session.add(tache)
        db.session.commit()
        return redirect(url_for('bp.index'))

    else:
        title = form.get('title').strip().lower()
        taches = Task.query.filter_by(title=title).all()
        return render_template('index.html', taches=taches)


@bp.route("/delete/<int:id>")
def delete(id):
    tache = db.get_or_404(Task, id)
    db.session.delete(tache)
    db.session.commit()
    return redirect(url_for('bp.index'))
