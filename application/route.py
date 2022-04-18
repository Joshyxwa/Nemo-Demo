import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
from crypt import methods
from application import app
from flask import redirect, render_template, request, flash
import onnx
import librosa
import soundfile as sf
import os
import json

app.config["AUDIO_UPLOADS"] = "application/static/audio"
app.config["JSON_DATA"] = "application/static/json"
app.config["MODEL_FILES"] = "notebook"
app.jinja_env.globals.update(config=app.config)

# Model Functions
def eng_asr_model(filename):

    #load audio file
    resampled_audio, sample_rate = librosa.load(os.path.join(app.config["AUDIO_UPLOADS"], filename), sr=22050)

    # delete audio file
    os.remove(os.path.join(app.config["AUDIO_UPLOADS"], filename))

    # transcribe english audio to english text
    citrinet_model = nemo_asr.models.EncDecCTCModelBPE.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "eng_citrinet.nemo"))
    sf.write(os.path.join(app.config["AUDIO_UPLOADS"], "preprocessed_audio.wav"), resampled_audio, sample_rate)
    transcribed_text = citrinet_model.transcribe(paths2audio_files=[os.path.join(app.config["AUDIO_UPLOADS"], "preprocessed_audio.wav")], batch_size=4)
    
    # remove processed audio file
    os.remove(os.path.join(app.config["AUDIO_UPLOADS"], "preprocessed_audio.wav"))

    return transcribed_text

def chi_asr_model(filename):

    #load audio file
    resampled_audio, sample_rate = librosa.load(os.path.join(app.config["AUDIO_UPLOADS"], filename), sr=22050)

    # delete audio file
    os.remove(os.path.join(app.config["AUDIO_UPLOADS"], filename))

    # transcribe chinese audio to chinese text
    citrinet_model = nemo_asr.models.EncDecCTCModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "chi_citrinet.nemo"))
    sf.write(os.path.join(app.config["AUDIO_UPLOADS"], "preprocessed_audio.wav"), resampled_audio, sample_rate)
    transcribed_text = citrinet_model.transcribe(paths2audio_files=[os.path.join(app.config["AUDIO_UPLOADS"], "preprocessed_audio.wav")], batch_size=4)
    
    # remove processed audio file
    os.remove(os.path.join(app.config["AUDIO_UPLOADS"], "preprocessed_audio.wav"))

    return transcribed_text

def punc_model(text):
    puncbert_model = nemo_nlp.models.PunctuationCapitalizationModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "punc_bert.nemo"))
    transformed_text = puncbert_model.add_punctuation_capitalization([i for i in text])
    dict_texts = [ {"transcribed_text": text[0],
                    "punc_text": transformed_text[0]}
    ]
    # json_texts = json.loads(str(dict_texts))
    with open(os.path.join(app.config["JSON_DATA"], 'punc_text.json'), 'w') as f:
        json.dump(dict_texts, f, ensure_ascii=False)
    return transformed_text

#Handles http://127.0.0.1:5000/
@app.route('/') 
@app.route('/index') 
@app.route('/home') 
def index_page(): 
    return render_template("index.html")

@app.route('/stop_record', methods=["POST", "GET"])
def applyNemo_audio():
    print('Hi')
    if request.method == "POST":
        print('Hi')
        wav_file = request.data()
        transcribed_text = eng_asr_model(wav_file)
        print(transcribed_text)
        punc_text = punc_model(transcribed_text)
        print(punc_text)
        flash(punc_text)

    elif request.method == 'GET':
        print('Hii')
    return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def upload_audiofile():
    if request.method == "POST":
        if request.files:
            audio_file = request.files["audiofile"]
            audio_file.save(os.path.join(app.config["AUDIO_UPLOADS"], audio_file.filename))
            model_lang = request.form['selectlanguage']
            print(model_lang)
            if model_lang =='english':

                transcribed_text = eng_asr_model(audio_file.filename)
                print(transcribed_text)
                punc_text = punc_model(transcribed_text)
                print(punc_text)
                flash(punc_text)

            else:
                transcribed_text = chi_asr_model(audio_file.filename)
                print(transcribed_text)
                punc_text = punc_model(transcribed_text)
                print(punc_text)
                flash(transcribed_text)

            return redirect(request.url)
    return render_template('result.html')
