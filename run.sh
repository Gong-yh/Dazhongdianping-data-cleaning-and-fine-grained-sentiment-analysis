cd /d/Programfile/py-object/fsauor2018-master

nvidia-smi
#数据处理
cd scripts
echo 'activate process envir  ...'

ENV_NAME = process
echo "You are in the virtualvenv '$ENV_NAME'"
source activate $ENV_NAME


#train/val/test
echo 'activate tensorflow envir  ...'

sh scripts/data/preprocess.sh

# train  val
ENV_NAME = tensorflow
echo "You are in the virtualvenv '$ENV_NAME'"
source activate $ENV_NAME


source activate tensorflow

sh bash/elmo_train.sh
sh bash/elmo_inference.sh

python D:/Programfile/py-object/fsauor2018-master/main.py \
    --mode=train \
    --data_files=D:/Programfile/py-object/fsauor2018-master/scripts/data/train.json \
    --eval_files=D:/Programfile/py-object/fsauor2018-master/scripts/data/validation.json \
    --label_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/labels.txt \
    --vocab_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/vocab.txt \
    --embed_file=D:/Programfile/py-object/fsauor2018-master/scripts/data/embedding.txt \
    --num_layers=3 \
    --batch_size=16 \
    --num_train_epoch=50 \
    --encoder=elmo \
    --rnn_cell_name=lstm \
    --feature_num=20 \
    --steps_per_eval=2000 \
    --learning_rate=0.001 \
    --focal_loss=0.0 \
    --checkpoint_dir=D:/Programfile/py-object/fsauor2018-master/scripts/data/elmo_adma_001

2021-09-02 15:37:37.196944: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1325] Created TensorFlow device (/job:localhost/replica:0/task:0/devic
e:GPU:0 with 2867 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1650, pci bus id: 0000:01:00.0, compute capability: 7.5)
2021-09-02 15:38:11.926387: E tensorflow/stream_executor/cuda/cuda_blas.cc:428] failed to run cuBLAS routine: CUBLAS_STATUS_INTERNAL_ERROR
2021-09-02 15:38:11.926904: F tensorflow/core/kernels/rnn/lstm_ops_gpu.cu.cc:282] Non-OK-status: GpuLaunchKernel( lstm_gates<T, false, gate_layout>,
grid_dim_2d, block_dim_2d, 0, cu_stream, gates.data(), b.data(), cs_prev.data(), wci.data(), wcf.data(), wco.data(), o.data(), h.data(), ci.data(), c
s.data(), co.data(), i.data(), f.data(), forget_bias, cell_clip, batch_size, cell_size) status: Internal: unspecified launch failure
2021-09-02 15:38:12.593696: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_100.dll
WARNING:tensorflow:From D:\Programfile\py-object\fsauor2018-master\thrid_utils.py:142: The name tf.layers.Dense is deprecated. Please use tf.compat.v
1.layers.Dense instead.

