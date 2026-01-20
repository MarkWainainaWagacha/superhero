from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from server.models import Hero, Power, HeroPower
from server.config import db


def register_routes(app):

    # -------------------------
    # ROOT (debug helper)
    # -------------------------
    @app.route("/")
    def home():
        return {"status": "Superheroes API is running"}, 200


    # -------------------------
    # GET /heroes
    # -------------------------
    @app.route("/heroes", methods=["GET"])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([
            {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            }
            for hero in heroes
        ]), 200


    # -------------------------
    # GET /heroes/<id>
    # -------------------------
    @app.route("/heroes/<int:id>", methods=["GET"])
    def get_hero(id):
        hero = Hero.query.get(id)

        if not hero:
            return {"error": "Hero not found"}, 404

        return {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [
                {
                    "id": hp.id,
                    "hero_id": hp.hero_id,
                    "power_id": hp.power_id,
                    "strength": hp.strength,
                    "power": {
                        "id": hp.power.id,
                        "name": hp.power.name,
                        "description": hp.power.description
                    }
                }
                for hp in hero.hero_powers
            ]
        }, 200


    # -------------------------
    # GET /powers
    # -------------------------
    @app.route("/powers", methods=["GET"])
    def get_powers():
        powers = Power.query.all()
        return jsonify([
            {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            for power in powers
        ]), 200


    # -------------------------
    # GET /powers/<id>
    # -------------------------
    @app.route("/powers/<int:id>", methods=["GET"])
    def get_power(id):
        power = Power.query.get(id)

        if not power:
            return {"error": "Power not found"}, 404

        return {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }, 200


    # -------------------------
    # PATCH /powers/<id>
    # -------------------------
    @app.route("/powers/<int:id>", methods=["PATCH"])
    def update_power(id):
        power = Power.query.get(id)

        if not power:
            return {"error": "Power not found"}, 404

        data = request.get_json()
        description = data.get("description")

        if not description or len(description) < 20:
            return {
                "errors": ["Description must be at least 20 characters long"]
            }, 400

        power.description = description
        db.session.commit()

        return {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }, 200


    # -------------------------
    # POST /hero_powers
    # -------------------------
    @app.route("/hero_powers", methods=["POST"])
    def create_hero_power():
        data = request.get_json()

        try:
            hero_power = HeroPower(
                strength=data["strength"],
                hero_id=data["hero_id"],
                power_id=data["power_id"]
            )

            db.session.add(hero_power)
            db.session.commit()

            return {
                "id": hero_power.id,
                "hero_id": hero_power.hero_id,
                "power_id": hero_power.power_id,
                "strength": hero_power.strength,
                "hero": {
                    "id": hero_power.hero.id,
                    "name": hero_power.hero.name,
                    "super_name": hero_power.hero.super_name
                },
                "power": {
                    "id": hero_power.power.id,
                    "name": hero_power.power.name,
                    "description": hero_power.power.description
                }
            }, 201

        except (KeyError, IntegrityError, ValueError):
            db.session.rollback()
            return {
                "errors": ["validation errors"]
            }, 400
