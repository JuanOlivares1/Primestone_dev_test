from flask import Flask, request, abort, jsonify
from db import db, app, Data
import json


@app.route('/')
def index():
    return ''


@app.route('/get-prime-numbers', methods=['GET'])
def get_prime_numbers():
    limit = request.args.get('limit')
    if not limit:
        return abort(400, 'No range specified, send limit to see reults')
    lim = int(limit)
    prime = []
    for num in range(1, lim + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    return jsonify(prime)


@app.route('/convert-height', methods=['POST'])
def convert_height():
    json = request.json
    if json:
        height_str = json['height']
        if not height_str:
            return abort(400, 'Wrong data')

        height = height_str.split(' ')
        if len(height) == 2:
            if height[0].isnumeric():
                inch = int(height[0])
                height[0] = round(((inch * 2.54) / 100), 2)
            else:
                return abort(400, 'Wrong data recieved')

            height[1] = 'metros'
            json['height'] = ' '.join([str(x) for x in height])
            return json
        else:
            return abort(400, 'Wrong data recieved')
    return abort(400, 'No information recieved')


@app.route('/set-data', methods=['PUT'])
def set_data():
    json_ = request.json
    if json_:
        json_ = json.dumps(json_)
        data = Data(json=json_)
        db.session.add(data)
        db.session.commit()
        if data.id:
            return 'Created'
        return 'Failed'
    return abort(400, 'No information recieved')


if __name__ == '__main__':
    app.run(debug=True)
