from flask import Blueprint
from ..models import Permission, ReleaseType

main =Blueprint('main', __name__)

from . import views, errors


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

@main.app_context_processor
def inject_releasetype():
    return dict(ReleaseType=ReleaseType)
