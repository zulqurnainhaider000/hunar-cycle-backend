from flask import Flask
from .routes.onboarding import onboarding_bp
from .routes.auth import auth_bp
from .routes.lessons import lessons_bp, courses_bp
from .routes.users import users_bp, user_bp
from .routes.gigs import gigs_bp
from .routes.dojos import dojos_bp
from .routes.hub import hub_bp
from .routes.zen import zen_bp

def create_app():
    app = Flask(__name__)
    
    # Register Core API Blueprints
    app.register_blueprint(onboarding_bp) # From previous step
    app.register_blueprint(auth_bp)
    app.register_blueprint(lessons_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(gigs_bp)
    app.register_blueprint(dojos_bp)
    app.register_blueprint(hub_bp)
    app.register_blueprint(zen_bp)
    
    @app.route('/api/health')
    def health_check():
        return {"status": "healthy", "service": "HunarCircle API"}

    return app
