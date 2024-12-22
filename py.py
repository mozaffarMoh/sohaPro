import streamlit as st
from googletrans import Translator
import speech_recognition as sr
import os

# إعداد المترجم
translator = Translator()

# إعداد الصفحة
st.set_page_config(page_title="المترجم الذكي للأطفال", layout="wide")

# تطبيق التنسيقات باستخدام CSS
css = """
<style>
   
    /* تنسيق العناوين */
    h1 {
        color: #007bff;
        text-align: center; /* توسيط العنوان */
        margin-top: 0; /* تقليل المسافة من الأعلى */
    }
    /* تنسيق زر الترجمة */
    .stButton>button {
        width: 100%;
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        height: 50px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    /* توسيط الرسائل */
    .st-alert {
        text-align: center;
    }
</style>
"""

# تطبيق التنسيقات
st.markdown(css, unsafe_allow_html=True)

# إنشاء الصندوق ليبدأ من الأعلى
st.markdown('<div class="main">', unsafe_allow_html=True)

with st.container():
   
    st.title("المترجم الذكي للأطفال")
   
    st.markdown("#### اضغط على الزر لتسجيل صوتك:")
    if st.button("تسجيل الصوت"):
        try:
       
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                st.info("يرجى التحدث الآن...")
                audio = recognizer.listen(source)

         
                st.info("جاري تحويل الصوت إلى نص...")
                text_input = recognizer.recognize_google(audio, language="ar")
                st.success(f"النص المكتشف: {text_input}")

          
                translation = translator.translate(text_input, src="ar", dest="fr")
                st.success(f"الترجمة: {translation.text}")
        except sr.UnknownValueError:
            st.error("لم يتم التعرف على الصوت، يرجى المحاولة مرة أخرى.")
        except sr.RequestError:
            st.error("حدث خطأ أثناء الاتصال بخدمة التعرف على الصوت.")

# إنهاء التصميم الرئيسي
st.markdown('</div>', unsafe_allow_html=True)
from flask import Flask, request, jsonify
from googletrans import Translator

# إنشاء التطبيق باستخدام Flask
app = Flask(__name__)

# تهيئة المترجم
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        # الحصول على النص المُرسل من الواجهة الأمامية
        data = request.json
        text = data.get('text', '')
        
        # الترجمة من العربية إلى الفرنسية
        if text:
            translation = translator.translate(text, src='ar', dest='fr').text
            return jsonify({'translation': translation})
        else:
            return jsonify({'error': 'No text provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == 'main':
    app.run(host='127.0.0.1', port=5000, debug=True)                