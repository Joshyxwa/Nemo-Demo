# Nemo-Demo
 Demostration of Nvidia Nemo Application. This demo contains the use of the following models
 
 1) stt_en_citrinet_1024
 - To transcribe English audio files to english text
 2) stt_zh_citrinet_512
- To transcribe Chinese audio files to chinese text
 3) punctuation_en_bert
- To add capitalisation and punctuations to english transcribed text

This project does not consist of fine tuning therefore models might not produce accurate results for certain accents. This project does not support good punctutation of chinese transcribed text as model is not punctuation_en_bert is not fine tuned to chinese dataset.

If you would want to see how to apply trained Nemo models with flask template and see it in action, this project is for you.

# Setup

1) Clone this repository in your computer
2) Run docker file and build docker image
    docker build -t nemo_demo .
    docker run -it -d -rm nemo_demo bash
3) Run notebook.ipynb to download the different models from Nvidia Nemo
4) Run flask and open the url to start translating audio files to text.
    FLASK_APP=\app.py python -m flask run

Note: Current Nemo models only accept wav files and not mp3. Convert mp3 file to wav file before uploading

# Important Resource Links
https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/intro.html
https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/nlp/punctuation_and_capitalization.html
