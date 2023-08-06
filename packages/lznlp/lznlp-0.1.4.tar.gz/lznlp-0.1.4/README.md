# LiangZhiNLP Python SDK

LiangZhi HTTP API 封装库（SDK）

## 开发模式安装

修改代码之后不用重新安装，立即可用最新的代码，在 `setup.py` 的同级目录下运行以下命令

```bash
$ python setup.py develop
```

## 打包

现在在 `setup.py` 的同级目录下运行以下命令，`dist` 目录下会生成相应文件

```bash
$ python setup.py sdist bdist_wheel
```

## 依赖

根据 `requirements.txt` 安装依赖包

```bash
$ pip install -r requirements.txt
```

## 测试

进行单元测试的命令如下，`-v -s` 参数是为了在控制台输出更多的打印信息

```bash
$ nosetests -v -s lznlp/tests/test_lznlp.py
```

## 文档

- [fasttext - pypi](https://pypi.org/project/fasttext/)
- [pyahocorasick - readthedocs](https://pyahocorasick.readthedocs.io/en/latest/)
- [jieba - github](https://github.com/fxsjy/jieba)
- [pytorch](https://pytorch.org/docs/stable/index.html)
- [torchtext - github](https://github.com/pytorch/text)

## 参考

- [如何打包 Python 代码](http://192.168.1.26:8099/liangzhi.ai/lznlp-platform/blob/master/docs/%E5%A6%82%E4%BD%95%E6%89%93%E5%8C%85%20Python%20%E4%BB%A3%E7%A0%81.md)
- [BosonNLP](https://github.com/bosondata/bosonnlp.py)
- [Print Messages With Nosetests](http://www.otsukare.info/2017/03/29/nosetests-print)