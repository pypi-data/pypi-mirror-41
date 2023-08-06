# Bert Embeddings

[![Build Status](https://travis-ci.org/imgarylai/bert_embedding.svg?branch=master)](https://travis-ci.org/imgarylai/bert_embedding) [![PyPI version](https://badge.fury.io/py/bert-embedding.svg)](https://badge.fury.io/py/bert-embedding)

[BERT](https://arxiv.org/abs/1810.04805), published by [Google](https://github.com/google-research/bert), is new way to obtain pre-trained language model word representation. Many NLP tasks are benefit from BERT to get the SOTA.

The goal of this project is to obtain the sentence and token embedding from BERT's pre-trained model. In this way, instead of building and do fine-tuning for an end-to-end NLP model, you can build your model by just utilizing the sentence or token embedding.

This project is implemented with [@MXNet](https://github.com/apache/incubator-mxnet). Special thanks to [@gluon-nlp](https://github.com/dmlc/gluon-nlp) team.

## Install

```
pip install bert-embedding
pip install https://github.com/dmlc/gluon-nlp/tarball/master
# If you want to run on GPU machine, please install `mxnet-cu92`.
pip install mxnet-cu92
```

> This project use API from gluonnlp==0.5.1, which hasn't been released yet. Once 0.5.1 is release, it is not necessary to install gluonnlp from source. 

## Usage

```python
from bert_embedding import BertEmbedding

bert_abstract = """We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
 Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations by jointly conditioning on both left and right context in all layers.
 As a result, the pre-trained BERT representations can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. 
BERT is conceptually simple and empirically powerful. 
It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE benchmark to 80.4% (7.6% absolute improvement), MultiNLI accuracy to 86.7 (5.6% absolute improvement) and the SQuAD v1.1 question answering Test F1 to 93.2 (1.5% absolute improvement), outperforming human performance by 2.0%."""
sentences = bert_abstract.split('\n')
bert = BertEmbedding()
result = bert.embedding(sentences)
```

## 