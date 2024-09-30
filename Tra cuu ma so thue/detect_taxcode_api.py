from flask import Flask, request, jsonify
import requests
import json
import logging

app = Flask(__name__)

# Create logger
logger = logging.getLogger('taxcode_logger')
logger.setLevel(logging.INFO)

# Create file to handle log
file_handler = logging.FileHandler('taxcode_requests.log')
file_handler.setLevel(logging.INFO)

# Formatting log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handle file to logger
logger.addHandler(file_handler)

# Validate taxcode value

def validate_taxcode(taxcode):
            if taxcode.isdigit() and len(taxcode) == 13 or len(taxcode) == 10:
               return True
            return False  


#---------API actions--------

@app.route('/input-taxcode', methods=['GET'])
def input_taxcode():

#---------GET method---------

    if request.method == 'GET':
        taxcode = request.args.get('taxcode') # Get taxcode value
         
        # Kiểm tra độ dài của taxcode
        if taxcode is None or not validate_taxcode(taxcode):
            return jsonify({"Error": "Nhập sai. Vui lòng kiểm tra lại MST"}), 400
        logger.info(f'New taxcode request received: {taxcode}') # Define message with taxcode value
        return jsonify({"taxcode": taxcode, "Status": "Thành công"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
