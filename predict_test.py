from bi_lstm_crf.app import WordsTagger

if __name__=='__main__':
    model = WordsTagger(model_dir="model_xxx")
    tags, sequences = model(["市领导到成都..."])  # CHAR-based model
    print(tags)
    # [["B", "B", "I", "B", "B-LOC", "I-LOC", "I-LOC", "I-LOC", "I-LOC", "B", "I", "B", "I"]]
    print(sequences)
    # [['市', '领导', '到', ('成都', 'LOC'), ...]]

    model([["市", "领导", "到", "成都", ...]])  # WORD-based model