# 基于CRNN+CTC架构的OCR模型
> 更详细信息的记录在该篇文章中：[深度学习实战--快递单手机号识别（训练篇）](<https://mp.weixin.qq.com/s?__biz=MzU2Njg4MTMzNA==&mid=2247483891&idx=1&sn=b43573e8c10b36070811387f7edd7cca&chksm=fca4fcaacbd375bcf507ffe1e5bb5f2568ff214b58d3bfa1a83ed703d2248805fcdbb678e652&token=563582328&lang=zh_CN#rd>)

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

