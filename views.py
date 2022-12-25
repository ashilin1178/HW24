from flask import Blueprint, request, jsonify

from builder import build_query

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    # TODO: Принять запрос от пользователя

    data = request.json

    # TODO: Обработать запрос, валидировать значения


    # TODO: Выполнить запрос

    return jsonify(build_query(cmd='', value='POST', file_name='data/apache_logs.txt'))

