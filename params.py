import alphabets

# about data and net
alphabet = alphabets.alphabet
keep_ratio = False # whether to keep ratio for image resize
manualSeed = 1234 # reproduce experiement
random_sample = True # whether to sample the dataset with random sampler
imgH = 32 # the height of the input image to network
imgW = 100 # the width of the input image to network
nh = 256 # size of the lstm hidden state
nc = 1
pretrained = 'trained_models/mixed_second_finetune_acc97p7.pth' # path to pretrained model (to continue training)
expr_dir = 'expr' # where to store samples and models
dealwith_lossnone = True # whether to replace all nan/inf in gradients to zero

# hardware
cuda = True # enables cuda
multi_gpu = False # whether to use multi gpu
ngpu = 0 # number of GPUs to use. Do remember to set multi_gpu to True!
workers = 0 # number of data loading workers

# training process
displayInterval = 4096 # interval to be print the train loss
valInterval = 4096 # interval to val the model loss and accuray
saveInterval = 5 # interval to save model
n_test_disp = 10 # number of samples to display when val the model

# finetune
nepoch = 500 # number of epochs to train for
batchSize = 64 # input batch size
lr = 0.001 # learning rate for Critic, not used by adadealta 手机号训练
# lr = 0.0001 # learning rate for Critic, not used by adadealta all训练
beta1 = 0.5 # beta1 for adam. default=0.5
adam = False # whether to use adam (default is rmsprop)
adadelta = False # whether to use adadelta (default is rmsprop)
