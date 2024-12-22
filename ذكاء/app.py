from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

# تهيئة مترجم
translator = Translator()

# تعريف المسار لترجمة النص
@app.route('/translate', methods=['POST'])
def translate():
    # الحصول على النص المرسل من الواجهة
    data = request.get_json()
    arabic_text = data.get('text', '')

    # ترجمة النص إلى الفرنسية
    translated = translator.translate(arabic_text, src='ar', dest='fr')

    # إرسال النص المترجم كاستجابة
    return jsonify({
        'translated_text': translated.text
    })

if __name__ == '__main__':
    app.run(debug=True)
