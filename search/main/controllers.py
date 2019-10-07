from flask import Blueprint, render_template, redirect, request


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('search/index.html')


@main.route('/search', methods=['GET'])
def search():
    if 'q' in request.args:
        q = request.args.get("q")
        query = q.split()
        url = ""
        # get_result = requests.get(url).content
        # result = json.loads(get_result)
        # if user_detail['code'] == 200:
        return render_template('search/search.html', q=q, query=query)
    else:
        return redirect('index')