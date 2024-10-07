from flask import Flask, request, jsonify
import logging
import os
from auto_detect_taxcode import check_text_appearance
from datetime import datetime

app = Flask(__name__)

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'taxcode_requests.log')

# Create logger
logger = logging.getLogger('taxcode_logger')
logger.setLevel(logging.INFO)

# Create file to handle log
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)

# Formatting log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handle file to logger
logger.addHandler(file_handler)

# Validate taxcode value

def validate_taxcode(taxcode):
            if taxcode.isdigit() and len(taxcode) == 14 or len(taxcode) == 10: # Value must be xxxxxxxxxx-xxx (14) or xxxxxxxxxx (10)
               return True
            return False  


#---------API actions--------

@app.route('/input-taxcode', methods=['GET'])
def input_taxcode():

#---------GET method---------

    if request.method == 'GET':
        taxcode = request.args.get('taxcode') # Get taxcode value
        
        if taxcode is None or not validate_taxcode(taxcode): #Verify lenght of taxcode value
            return jsonify({"error": "Nhập sai. Vui lòng kiểm tra lại MST"}), 400 # Return when it falses
        
        logger.info(f'New taxcode request received: {taxcode}') # Define message with taxcode value
        
        xpath = "/html/body/div/section/main/section/div/div/div/div/div[3]/div[2]/div[2]/div[2]/section/p"
        text1 = "đã đăng ký"
        result = check_text_appearance(xpath, text1)# Gọi hàm check_text_appearance từ file Selenium

        # Tạo file taxcode_results.log
        
        log_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'taxcode_results.log')
        
        def log_result(taxcode, result):
            with open(log_file_path, 'a', encoding='utf-8') as log_file:
              log_file.write(f"Thời gian tra cứu: {datetime.now()} | Mã số thuế: {taxcode} | Kết quả: {result}\n")

        log_result(taxcode, result)
       
        return jsonify({"taxcode": taxcode, "status": "Thành công", "result": result}), 200 # Return when it trues

if __name__ == '__main__':
    app.run(debug=True, port=5000)
