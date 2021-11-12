from .TokenAnalyzer import token_analyzer


class InSearch:
    def __init__(self):
        # key : value = string token : {dictionary document_id : frequency}
        # id_n_len_in_table, table에 들어있는 doc id와 len의 딕셔너리
        self.table = {}
        self.id_n_len_in_table = {}
        self.average_of_document_len = 0

    # table에 document의 token과 id를 추가
    # parameter : int document_id, string document
    # return : boolean
    def add_document(self, document_id, document):
        # 해당 id가 없는지 확인
        if document_id in self.id_in_table:
            return False
        # id_in_table에 해당 id 추가
        self.id_in_table.append(document_id)
        # document 형태소 분석
        token_list = ta.token_analyzer(document)
        # table에 { token : document id }를 추가
        #   token이 없으면, 새로이 추가
        #   token이 있으면, 원래의 id list에 해당 id값만 추가
        for token in token_list:
            if token in self.table.keys():
                self.table[token].insert(document_id)
            else:
                self.table[token] = [document_id]
        return True

    # table에 document의 token과 id를 삭제
    # parameter : int document_id, string document
    # return : boolean
    def delete_document(self, document_id):
        # 해당 id가 있는지 확인
        if document_id not in self.id_in_table:
            return False

        # table의 모든 token에서 document_id를 삭제
        # token에 해당하는 id가 없다면 token도 table에서 삭제

        for token in self.table.keys():
            if document_id in self.table[token]:
                self.table[token].remove(document_id)
                if len(self.table[token]) == 0:
                    self.table.pop(token)
        # id_in_table에 해당 id 삭제
        self.id_in_table.pop(document_id)
        return True

    # table의 해당 document의 기록을 new_document로 변경
    # parameter : int document_id, string old_document, string new_document
    # return : boolean
    def update_document(self, document_id, new_document):
        self.delete_document(document_id)
        self.add_document(document_id, new_document)
        return True

    # 전체 table을 딕셔너리로 반환
    # parameter : int document_id
    # return : Dictionary table
    def return_table(self):
        return self.table

    # 검색어와 가장 부합한 document의 id를 table에서 찾아 반환
    # parameter : string query
    # return : list rank_of_document_id
    def search(self, query):
        return list()

    # table 초기화
    # return : boolean
    def delete_all(self):
        return True
