 # tax2vec

Semantic space vectorization algorithm

## Short description

Tax2vec is a simple data enrichment approach. Its main goal is to extract corpus-relevant information in form of new features, which can be used for learning.

![](workflow.png)

## Getting Started
Below you shall find instructions for installation of tax2vec library.

### Prerequisites

What things you need to install the software and how to install them

```
pip install -r requirements.txt
```
And also:
```
conda install --yes --file requirements.txt
```

### Installing

Installing is simple!

```
pip3 install tax2vec
```
And that's it. You can also install the library directly:

```
python3 setup.py install
```

Note that some of the tf-idf constructors use nltk addons. Tax2vec informs you when an addon is needed and how to install it. For example, to install punctuation, one does:

```
import nltk
nltk.download('punct')
```

## Basic use

First, import the library and some of the preprocessing methods..

```python
import tax2vec as t2v
from tax2vec.preprocessing import *
```

Next, we load the corpus using in-build methods. Note that any tokenizer can be used for this!

```python
# load corpus
labels, d_corpus,class_names = generate_corpus("./datasets/PAN_2016_age_srna_en.csv.gz",100000000000)

# Tokenize -> this is just to get the splits and class names.
sequence_word_matrix, _, _ = data_docs_to_matrix(d_corpus, mode="index_word")

# Split generator
split_gen = split_generator(sequence_word_matrix, d_corpus, labels, num_splits=1, test=0.1)

# Get splits
(train_x,test_x,train_y,test_y) = split_gen.next()

# Tokenize corpus
train_sequences,tokenizer,mlen = data_docs_to_matrix(train_x, mode="index_word")
test_sequences = tokenizer.texts_to_sequences(test_x)

# Important! Store the index-word mappings.
dmap = tokenizer.__dict__['word_index']

## tax2vec part
tax2vec_instance = t2v.tax2vec(max_features=30, targets=train_y,num_cpu=8,heuristic="closeness_centrality",class_names=class_names)

## fit and transform
semantic_features_train = tax2vec_instance.fit_transform(train_sequences, dmap)

## just transform
semantic_features_test = tax2vec_instance.transform(test_sequences)

## And that's it!

```


## Example uses

To reproduce SOTA results on the classification task, you can run:
```
python3 demo_classification.py
```

To use custom feature constructor by Martinc et al. (2017)
```
python3 demo_classification_custom_features.py
```

To reproduce the explainability features:

```
python3 demo_explain_corpus.py
```

And to use it in an unsupervised setting:

```
python3 demo_explain_unsupervised.py
```

## Contributing

To contribute, simply open an issue or a pull request!

## Authors

tax2vec was created by Blaž Škrlj, Jan Kralj, Matej Martinc, Nada Lavrač and Senja Pollak.

## License

See LICENSE.md for more details.

## Citation