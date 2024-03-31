from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from document_processor import DocumentProcessor

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/process', methods = ['POST', 'OPTION'])
@cross_origin()
def process_word():
    try:
        data = request.json
        word_processor = DocumentProcessor(data)
        word_processor.process_document()

        return jsonify({'message': 'Cover Letter processed successfullly'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(port = 5000)