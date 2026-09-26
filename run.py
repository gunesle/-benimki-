from flask_cors import CORS
from app import create_app

app = create_app()
CORS(app, origins=["https://gunesdamla.wixstudio.com", "https://benimki-qr6m.onrender.com"])
if __name__ == "__main__":
    app.run(debug=True, port=5000)
