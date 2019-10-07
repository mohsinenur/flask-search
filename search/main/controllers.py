from flask import Blueprint, render_template, redirect, request


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('search/index.html')


@main.route('/search', methods=['GET'])
def search():
    if 'q' in request.args:
        query = request.args.get("q")
        return render_template('search/search.html', query=query)
    else:
        return redirect('index')