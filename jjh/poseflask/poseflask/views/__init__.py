from flask import Flask


def create_app():
    app = Flask(__name__)

    
    # 블루프린트
    from .views import main_views, cam_views, storage_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(cam_views.bp)
    app.register_blueprint(storage_views.bp)

    return app