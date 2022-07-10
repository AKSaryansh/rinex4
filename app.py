import streanlit as st
import joblib
model = joblib.load('spam-ham')
st.title('Spam-Ham Classifier')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
