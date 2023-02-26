import random
import os
import openai
from flask import Flask, render_template, request
import checkocc
import PyPDF2

app = Flask(  # Create a flask app
  __name__,
  template_folder='import',  # Name of html file folder
  static_folder='import/static'  # Name of directory for static files
)

@app.route('/')
def home():
  print(os.getcwd())
  return render_template('mainpage.html')
@app.route('/upload', methods = ['POST'])
def upload():
    app.config['UPLOAD_FOLDER'] ='/home/runner/Mainhackathon' 
    file = request.files['pdf_file']
    filename = file.filename

    #uploads the file into uploads folder from the webpage.
    file.save(os.path.join(app.config ['UPLOAD_FOLDER'], filename))
    # Process the uploaded file
    with open(filename, 'rb') as f:
      reader = PyPDF2.PdfReader(f)
      text = ''
      for i in range(len(reader.pages)):
          page = reader.pages[i]
          text += page.extract_text()

        # Split text into lines and append a full stop to each line
      lines = [line.strip() for line in text.split('.') if line.strip()]
        #return lines
      L=[]
      for l in lines:
        line=checkocc.checkocc(l)
        if len(line) > 1:
          L.append(line)
      impPts_str= "\n".join(L)
      
    openai.api_key = "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"

    model_engine= "text-davinci-003"
    prompt=f"Simplify the legal jargon in these lines {impPts_str} and give me relevant market information related to it in 10 sentences."

    completion =  openai.Completion.create( engine= model_engine, prompt= prompt, max_tokens=250, n=1, stop= None,           temperature = 0.5)

    response= completion.choices[0].text
    

    
    return render_template('upload.html', filename=filename, file_response= response, imp_list=L)

  
if __name__ == "__main__":  # Makes sure this is the main process
  app.run( debug=True,host='0.0.0.0', port=random.randint(2000, 9000))

