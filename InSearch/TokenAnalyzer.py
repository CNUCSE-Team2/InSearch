from eunjeon import Mecab

def token_analyzer(text):
    morphs_analyzer = Mecab()
    token_list = morphs_analyzer.morphs(text)
    return token_list