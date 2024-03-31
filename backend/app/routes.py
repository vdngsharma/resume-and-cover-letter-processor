from flask import Flask, request, jsonify
from document_processor import DocumentProcessor

app = Flask(__name__)

@app.route('/process_document', methods = ['POST'])
def process_word():
    try:
        data = request.json
        word_processor = DocumentProcessor(data)
        word_processor.process_document()

        return jsonify({'message': 'Cover Letter processed successfullly'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug = True, port = 5001)