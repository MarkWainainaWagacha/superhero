from server.app import app
from server.config import db
from server.models import Hero, Power, HeroPower

def seed_database():
    with app.app_context():
        db.drop_all()      # Only if you want to reset
        db.create_all()

        # Add Heroes
        h1 = Hero(name="Peter Parker", super_name="Spider-Man")
        h2 = Hero(name="Tony Stark", super_name="Iron Man")

        # Add Powers
        p1 = Power(name="Strength", description="Super strong")
        p2 = Power(name="Flying", description="Can fly")

        db.session.add_all([h1, h2, p1, p2])
        db.session.commit()

        # Add Hero Powers
        hp1 = HeroPower(hero_id=h1.id, power_id=p1.id, strength="High")
        hp2 = HeroPower(hero_id=h2.id, power_id=p2.id, strength="Medium")

        db.session.add_all([hp1, hp2])
        db.session.commit()

        print("Database created and seeded")

if __name__ == "__main__":
    seed_database()
