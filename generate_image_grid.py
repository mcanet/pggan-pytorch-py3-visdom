# generate interpolated images.


import os,sys
import torch
from config import config
from torch.autograd import Variable
import utils as utils
from torchvision.utils import save_image

use_cuda = True
checkpoint_path = 'repo/model/gen_R8_T4200.pth.tar'
n_row = 1
n_col = 1
n_image  = n_col * n_col
trials = 50


# load trained model.
import network as net
test_model = net.Generator(config)
if use_cuda:
    torch.set_default_tensor_type('torch.cuda.FloatTensor')
    test_model = torch.nn.DataParallel(test_model).cuda(device=0)
else:
    torch.set_default_tensor_type('torch.FloatTensor')

for resl in range(3, config.max_resl+1):
    test_model.module.grow_network(resl)
    test_model.module.flush_network()
print(test_model)


print('load checkpoint form ... {}'.format(checkpoint_path))
checkpoint = torch.load(checkpoint_path)
test_model.module.load_state_dict(checkpoint['state_dict'])


# create folder.
for i in range(1000):
    name = 'repo/grid/{}'.format(i)
    if not os.path.exists(name):
        os.system('mkdir -p {}'.format(name))
        break

# interpolate between twe noise(z1, z2).
for i in range(trials):
    z1 = torch.FloatTensor(1, config.nz).normal_(0.0, 1.0)
    if use_cuda:
        z1 = z1.cuda()
        test_model = test_model.cuda()

    z = Variable(z1)
    fake_im = test_model.module(z)
    fname = os.path.join(name, '{}.jpg'.format(i))
    utils.save_image_single(fake_im.data, fname, imsize=pow(2,config.max_resl))




