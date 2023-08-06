from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
   inputText = request.json.get("text")
    
   if not inputText:
      
        # Response to send if the input_text is undefined
        response = {
           "status":"error",
           "message":"Please enter some text to predict emotion"
        }
        return jsonify(response)
   
   else:
       predicted_emo, predicted_emo_img_url = predict(inputText)
       
        
        # Response to send if the input_text is not undefined
       response = {
           "status":"success",
           "data":{
               "predicted_emo":predicted_emo,
               "predicted_emo_img_url":predicted_emo_img_url
           }
        }
        
        # Send Response 
       return jsonify(response)        
        
       
app.run(debug=True)



    