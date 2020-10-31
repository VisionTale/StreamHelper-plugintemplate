from flask import render_template
from . import bp


@bp.route('/', methods=['GET'])
@bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('templates_dashboard.html')
