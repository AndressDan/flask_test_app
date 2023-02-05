from flask import render_template, request, flash, redirect
from app import app
from app.db_control import *


@app.route("/")
def main():
    return render_template("base.html")


@app.route("/add_test", methods=["GET", "POST"])
def add_test():
    if request.method == "POST":
        question = request.form["question"]
        ans1 = request.form["ans1"]
        ans2 = request.form["ans2"]
        correct = request.form["correct"]

        msg = add_new_question(question, ans1, ans2, correct)

        flash(msg)

        return redirect("add_test")
    return render_template("add_test.html")


@app.route("/pass_test", methods=["GET", "POST"])
def pass_test():
    all_tests = get_all_tests()
    return render_template("pass_test.html", all_tests=all_tests)
