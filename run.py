from app import create_app, db
from app.seed import load_colors_from_json
app = create_app()

with app.app_context():
    db.create_all()
    added = load_colors_from_json("colors.json")
    print(f"added {added} colors")

if __name__ == "__main__":
    app.run(debug=True)

