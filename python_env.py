pytorch_env


"""安装依赖包遇到的问题

anaconda-client==1.6.3 需要改成anaconda-client==1.2.2  pip导出requirements.txt的时候就是1.6.3，但是安装的时候报错说只有1.1.1和1.2.2，未能找到1.6.3
keras-contrib==2.0.8 需要通过 pip install git+https://www.github.com/keras-team/keras-contrib.git来安装，具体参考https://github.com/keras-team/keras-contrib

"""

