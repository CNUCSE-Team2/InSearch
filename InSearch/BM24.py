import numpy as np
from . import TokenAnalyzer as ta


def IDF(document_count, fq_document):
    return np.log(1 + ((document_count - fq_document + 0.5)/fq_document + 0.5))


def bm24(table, document_id, document_len_id, query, avgdl):
    score_list = []
    k1 = 1.2
    b = 0.75
    document_count = len(document_id)
    # query문을 형태소 분석
    query_token = ta.token_analyzer(query)
    # 각 document마다 반복
    for id in document_id:
        score = 0
        # query문의 각 형태소마다 반복
        for token in query_token:
            if table.get(token) == None:
                # 해당 token을 포함하는 document개수
                fq_document = 0
                # document에서 token의 개수(빈도)
                fq_count = 0
            else:
                fq_document = len(table[token].keys())      
                fq_count = table[token].get(id, 0)
            # IDF
            token_idf = IDF(document_count, fq_document)
            # TF
            token_tf = (fq_count * (k1 + 1))/(fq_count + k1 * (1 - b + b * (len(document_id)/avgdl)))
            score += token_idf * token_tf
        # score(D,Q) = sigma(IDF*TF)
        score_list.append((score, id))

    return score_list
