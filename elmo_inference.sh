python main.py \
--mode=inference \
--data_files=D:/Programfile/py-object/fsauor2018-master/scripts/data/testa.json \
--label_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/labels.txt \
--vocab_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/vocab.txt \
--out_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/elmo_adma_B64_0902_001/out.testa.json \
--embed_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/embedding.txt \
--prob=False \
--batch_size=300 \
--feature_num=20 \
--checkpoint_dir=D:/Programfile/py-object/fsauor2018-master/scripts/data/elmo_adma_B32_0902_001