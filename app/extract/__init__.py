
from flask import Blueprint

extract = Blueprint('extract', __name__)

from . import views
