from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__, template_folder=os.getcwd())

with open(r'C:\Users\OM yadav\OneDrive\Desktop\ML Project\news.pkl', 'rb') as f:
    model = pickle.load(f)


with open(r'C:\Users\OM yadav\OneDrive\Desktop\ML Project\tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        data = request.form
        text = str(data.get("text"))
        
        user_input = [text] 
        
        user_input_transformed = tfidf_vectorizer.transform(user_input)
        
        model_output = model.predict(user_input_transformed)
        
        output_user = "News is Fake" if model_output == 0 else "News is Real"
        return render_template('index.html', News=output_user)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
