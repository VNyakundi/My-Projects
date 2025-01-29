# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# M-Pesa API credentials
MPESA_CONSUMER_KEY = 'your_consumer_key'
MPESA_CONSUMER_SECRET = 'your_consumer_secret'
MPESA_SHORTCODE = 'your_shortcode'
MPESA_PASSKEY = 'your_passkey'

def generate_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET))
    response_data = response.json()
    return response_data['access_token']

@app.route('/api/mpesa/payment', methods=['POST'])
def process_payment():
    data = request.json
    phone = data.get('phone')
    amount = data.get('amount')

    if not phone or not amount:
        return jsonify({'success': False, 'message': 'Phone number and amount are required'}), 400

    access_token = generate_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payment_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": generate_password(),
        "Timestamp": generate_timestamp(),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": "https://your-backend-url/api/mpesa/callback",
        "AccountReference": "POS Payment",
        "TransactionDesc": "Payment for goods",
    }

    response = requests.post(payment_url, json=payload, headers=headers)
    response_data = response.json()

    if response.status_code == 200 and response_data.get('ResponseCode') == '0':
        return jsonify({'success': True, 'message': 'Payment request sent successfully'})
    else:
        return jsonify({'success': False, 'message': 'Failed to process payment'}), 500

def generate_password():
    from base64 import b64encode
    import time
    timestamp = generate_timestamp()
    raw_password = f"{MPESA_SHORTCODE}{MPESA_PASSKEY}{timestamp}"
    return b64encode(raw_password.encode()).decode('utf-8')

def generate_timestamp():
    from datetime import datetime
    return datetime.now().strftime('%Y%m%d%H%M%S')

@app.route('/api/mpesa/callback', methods=['POST'])
def mpesa_callback():
    data = request.json
    # Process the callback here (e.g., update payment status in the database)
    print("Callback data:", data)
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)
