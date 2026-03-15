from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/location', methods=['GET'])
def location():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    if latitude and longitude:
        data = {
            "classroom": "Cloud Lab",
            "latitude": latitude,
            "longitude": longitude
        }
    else:
        data = {
            "error": "Please provide latitude and longitude"
        }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)