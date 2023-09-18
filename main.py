from flask import Flask, render_template, request, jsonify
from image_processing import preprocess_image
from text_extraction import extract_text
from text_parsing import parse_aadhaar_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file and allowed_file(file.filename):
            # Process the image
            image_data = preprocess_image(file)
            extracted_text = extract_text(image_data)
            aadhaar_info = parse_aadhaar_info(extracted_text)

            if aadhaar_info:
                return jsonify(aadhaar_info)
            else:
                return jsonify({'error': 'Aadhaar information not found'})

    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg'}

if __name__ == '__main__':
    app.run(debug=True)
