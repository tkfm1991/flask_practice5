from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/output', methods=['POST'])
def output():
    u_name = request.form['name']
    # 選択していないときにエラーになる
    # res_over18 = request.form['over18']
    # sex = request.form['sex']
    res_over18 = request.form.get('over18', '')
    sex = request.form.get('sex', '不明')
    other = request.form['other']
    belong = request.form['belong']

    if res_over18:
        over18 = '18歳以上'
    else:
        over18 = '18歳未満'

    return render_template('output.html', name=u_name, over18=over18, sex=sex, other=other, belong=belong)


if __name__ == '__main__':
    app.run(debug=True)
