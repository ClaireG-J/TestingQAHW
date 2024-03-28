from flask import Flask, request
from bmi import BMI_Calc

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=["GET","POST"])
def page():
    errors = ""
    if request.method == "POST":
        f = None
        i = None
        w = None
        try:
            f = float(request.form["f"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["f"])
        try:
            i = float(request.form["i"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["i"])
        try:
            w= float(request.form["w"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["w"])
        if f is not None and i is not None and w is not None:
            result, category = BMI_Calc(f, i, w)
            return '''
                <html>
                    <body>
                        <p>\nThis person's BMI is {result:.1f}, which is {category}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result, category=category)
    return '''
        <html>
            <body>
                {errors}
                <p>Welcome to the BMI Calculator</p>
                <p>Please enter your numbers in the boxes below:</p>
                <form method="post" action=".">
                    <p>Feet: <input name="f" /></p>
                    <p>Inches: <input name="i" /></p>
                    <p>Weight(lbs): <input name="w" /></p>
                    <p><input type="submit" value="BMI_Calc" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
