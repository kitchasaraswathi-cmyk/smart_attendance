from flask import Blueprint, render_template, session, redirect

parent_bp = Blueprint(
    "parent",
    __name__
)


def parent_required():

    if "user_id" not in session:
        return False

    if session.get("user_role") != "parent":
        return False

    return True


@parent_bp.route("/parent-dashboard")
def parent_dashboard():

    if not parent_required():
        return redirect("/login")

    return render_template("parent/dashboard.html")