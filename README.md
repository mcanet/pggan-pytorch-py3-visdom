## Pytorch Implementation of "Progressive growing GAN (PGGAN)"
PyTorch implementation of [PROGRESSIVE GROWING OF GANS FOR IMPROVED QUALITY, STABILITY, AND VARIATION](http://research.nvidia.com/sites/default/files/pubs/2017-10_Progressive-Growing-of//karras2017gan-paper.pdf)   

Check the original repository for detail description.
This repository introduces 2 major changes.
1. python3 compatability   
the original repository crash for some reason when used with python3
2. use visdom instead of tensorboard   
which is lightweight, doesn't require tensorflow and IMO a better visualization framework overall.
