from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
champions_list = convert_to_dict("ncaa.csv")

# create a list of tuples in which the first item is the number
# (Presidency) and the second item is the name (President)
pairs_list = []
for p in champions_list:
    pairs_list.append( (p['Champion'], p['Year ']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Champions Index")

# second route

@app.route('/champion/<num>')
def detail(num):
    try:
        champion_dict = champions_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Champion: {num}</h1>"
    # a little bonus function, imported on line 2 above
    return render_template('champions.html', champion=champion_dict, ord=ord, the_title=champion_dict['Champion'])

# keep this as is
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999, debug=True)
