from flask import Flask, request, jsonify
from app.word_processor import WordProcessor

app = Flask(__name__)

@app.route('/process_cover_letter', method = ['POST'])
def process_word():
    file_path = request.form.get() # TODO: file_path
    target_word = request.form.get() # TODO: target_word
    replacement_word = request.form.get() # TODO: replacement_word

    if not file_path or not target_word or not replacement_word:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    try:
        word_processor = WordProcessor(file_path)
        word_processor.find_replace(target_word, replacement_word)
        word_processor.save_document() # TODO: Target_Path
        return jsonify({'message': 'Cover Letter processed successfullly'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug = True)