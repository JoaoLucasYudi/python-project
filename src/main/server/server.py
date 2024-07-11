from flask import Flask

from src.main.routers.trips_routes import trips_route_bp
from src.main.routers.links_routes import links_routes_bp

app = Flask(__name__)

app.register_blueprint(trips_route_bp, links_routes_bp)