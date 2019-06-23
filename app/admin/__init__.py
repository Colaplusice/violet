from flask.blueprints import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')
# 导入view 中的url
from . import view
