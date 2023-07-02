
# install

The compatibility of tensorflow is actually becomre worser. [A note about different operating system packages](https://github.com/tensorflow/text#a-note-about-different-operating-system-packages). Which means windows tensorflow is dying at the same time. 

## amd
for amd gpu, I will say good luck for you.  

[GPU and OS Support (Linux)](https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html)

You have to check several thing. GPU, distro version, kernel version... Make sure you have really carfully checked. Even docker will not work if you have not supported gpu, and current supported gpu is limited. E.g. (2023/6/23) my gpu is 5700xt which is gfx1010 instruction. This is not support by rocm, even your are able to install rocm.

After make rocm work, tensorflow is another story. You have to choose a tensorflow version build with rocm. Your tensorflow, rocm, bazel, numpy... version is limited.

