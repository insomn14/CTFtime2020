#!/usr/bin/env python3

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/secret", methods=['POST'])
def secret():

        if request.method == 'POST':
                var1 = request.form.get('FLAG')
                if var1 != '' or 'flag' in var1:
                    return 'POST : HOREE!!'
                print(f'[+] FLAG {var1}')

if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=80)

