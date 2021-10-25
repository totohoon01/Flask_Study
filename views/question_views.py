import re
from flask import Blueprint, render_template
from models import Question
from forms import QuestionForm

bp = Blueprint("question", __name__, url_prefix="/question")


@bp.route("/list/")
def qlist():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template("question/question_list.html", question_list=question_list)


@bp.route("/list/detail/<int:question_id>/")
def detail(question_id):
    # question = Question.query.get(question_id)
    question = Question.query.get_or_404(question_id)
    return render_template("question/question_detail.html", question=question)


@bp.route("/create")
def create():
    form = QuestionForm()
    return render_template("question/question_form.html", form=form)
