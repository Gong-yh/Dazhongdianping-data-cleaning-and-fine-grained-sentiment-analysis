mkdir -p D:/Programfile/py-object/fsauor2018-master/scripts/

echo 'training  ...'

python D:/Programfile/py-object/fsauor2018-master/main.py \
    --mode=train \
    --data_files=D:/Programfile/py-object/fsauor2018-master/scripts/data/train.json \
    --eval_files=D:/Programfile/py-object/fsauor2018-master/scripts/data/validation.json \
    --label_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/labels.txt \
    --vocab_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/vocab.txt \
    --embed_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/embedding.txt \
    --num_layers=3 \
    --batch_size=64 \
    --num_train_epoch=50 \
    --encoder=elmo \
    --rnn_cell_name=lstm \
    --feature_num=20 \
    --steps_per_eval=2000 \
    --learning_rate=0.001 \
    --focal_loss=0.0 \
    --checkpoint_dir=D:/Programfile/py-object/fsauor2018-master/scripts/data/elmo_adma_B64_0902_001
