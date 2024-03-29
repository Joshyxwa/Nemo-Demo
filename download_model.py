import nemo
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp

eng_citrinet = nemo_asr.models.EncDecCTCModelBPE.from_pretrained(model_name="stt_en_citrinet_1024")
eng_citrinet.save_to('models/eng_citrinet.nemo')

chi_citrinet = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="stt_zh_citrinet_512")
chi_citrinet.save_to('models/chi_citrinet.nemo')

punc_bert = nemo_nlp.models.PunctuationCapitalizationModel.from_pretrained(model_name="punctuation_en_distilbert")
punc_bert.save_to('models/punc_bert.nemo')