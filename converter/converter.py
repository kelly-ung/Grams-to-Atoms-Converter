from flask import Flask, render_template, request, url_for, Blueprint

bp = Blueprint('converter', '__name__')

def do_calculation(grams, molar_mass):
    answer = (grams * (6.022 * (10**23))) / molar_mass
    answer = '{:.3e}'.format(answer)
    return answer

@bp.route('/', methods=["GET", "POST"])
def start():
    errors = []
    if request.method == "POST":
        grams = None
        molar_mass = None
        try:
            grams = float(request.form["grams"])
        except:
            errors.append("ⓘ Please enter a numerical value for grams.\n".format(request.form["grams"]))
        try:
            molar_mass = float(request.form["molar_mass"])
        except:
            errors.append("ⓘ Please enter a numerical value for molar mass.\n".format(request.form["molar_mass"]))

        if grams is not None and molar_mass is not None:
            result = do_calculation(grams, molar_mass)
            return render_template("calculation.html", grams=grams, molar_mass=molar_mass, result=result)
    return render_template("index.html", errors=errors)


