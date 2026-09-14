from flask import Blueprint, jsonify, request, render_template
from services import ai_service
from app.database import lead_ekle, tum_leadler

views = Blueprint('views', __name__)
api = Blueprint('api', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@api.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.json
    mesaj = data.get('mesaj')
    cevap = ai_service.ai_service.yanit_uret(mesaj, [])
    return jsonify({'cevap': cevap})

@api.route('/leads', methods=['POST'])
def lead_kaydet():
    data = request.json
    lead_ekle(data['isim'], data['telefon'], data.get('mesaj'))
    return jsonify({'mesaj': 'Lead kaydedildi'}), 201

@api.route('/leads', methods=['GET'])
def lead_listele():
    leads = tum_leadler()
    return jsonify([dict(lead) for lead in leads])