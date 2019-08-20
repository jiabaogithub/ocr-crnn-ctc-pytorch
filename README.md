# 基于CRNN+CTC架构的OCR模型

## Dependence

- Python3.6.4
- torch==1.1.0
- torchvision==0.3.0
- lmdb==0.95
- RTX 2070 - Nvidia

## Run demo

- Run demo

  ```sh
  python demo.py -m trained_models/netCRNN_mobiles_26w_0.99acc.pth -i imgs/227_292_cut.jpg
  ```

## Feature

- 增加了数据样本生成功能

- 解决了使用IntTensor在面对长整型字符串的时候会导致不能在GPU上运算的问题

  具体报错：“RuntimeError: Expected tensor to have CPU Backend, but got tensor with CUDA Backend (while checking arguments for cudnn_ctc_loss)”

- torch升级到1.1.0，torchvision升级到0.3.0


### Train

Run `train.py` by

```sh
python train.py --trainroot train_mobiles_lmdb --valroot val_mobiles_lmdb
```



## Reference

[Holmeyoung/crnn.pytorch](<https://github.com/Holmeyoung/crnn-pytorch>)

[Sierkinhane/crnn_chinese_characters_rec](<https://github.com/Sierkinhane/crnn_chinese_characters_rec>)

