# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""CIFAR datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import random

import numpy as np
import six
from six.moves import cPickle
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# Shared constants
_CIFAR_IMAGE_SIZE = 32
_CIFAR_IMAGE_SHAPE = (_CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE, 3)


_CITATION = """\
@TECHREPORT{Krizhevsky09learningmultiple,
    author = {Alex Krizhevsky},
    title = {Learning multiple layers of features from tiny images},
    institution = {},
    year = {2009}
}
"""


class Cifar10(tfds.core.GeneratorBasedBuilder):
  """CIFAR-10."""

  VERSION = tfds.core.Version("1.0.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("The CIFAR-10 dataset consists of 60000 32x32 colour "
                     "images in 10 classes, with 6000 images per class. There "
                     "are 50000 training images and 10000 test images."),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_CIFAR_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        urls=["https://www.cs.toronto.edu/~kriz/cifar.html"],
        citation=_CITATION,
    )

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url="https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz",
        train_files=[
            "data_batch_1", "data_batch_2", "data_batch_3", "data_batch_4",
            "data_batch_5"
        ],
        test_files=["test_batch"],
        meta_file="batches.meta",
        prefix="cifar-10-batches-py/",
        label_keys=["labels"],
    )

  def _split_generators(self, dl_manager):
    cifar_path = dl_manager.download_and_extract(self._cifar_info.url)
    cifar_info = self._cifar_info

    cifar_path = os.path.join(cifar_path, cifar_info.prefix)

    # Load the label names
    metadata = _load_pickle(os.path.join(cifar_path, cifar_info.meta_file))
    for label_key in cifar_info.label_keys:
      label_key = _strip_s(label_key)  # labels => label
      label_names = metadata["{}_names".format(label_key)]

      self.info.features[_label_to_feature_key(label_key)].names = label_names

    # Define the splits
    def gen_filenames(filenames):
      for f in filenames:
        yield os.path.join(cifar_path, f)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={"filepaths": gen_filenames(cifar_info.train_files)}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={"filepaths": gen_filenames(cifar_info.test_files)}),
    ]

  def _generate_examples(self, filepaths):
    """Generate CIFAR examples as dicts.

    Shared across CIFAR-{10, 100}. Uses self._cifar_info as
    configuration.

    Args:
      filepaths (list[str]): The files to use to generate the data.

    Yields:
      The cifar examples, as defined in the dataset info features.
    """
    images, labels = [], []
    for path in filepaths:
      data = _load_pickle(path)

      batch_images = data["data"]
      num_images = batch_images.shape[0]
      batch_images = batch_images.reshape(
          (num_images, 3, _CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE))
      # Get images into [height, width, channels] format
      images.extend([
          np.squeeze(batch_images[j]).transpose((1, 2, 0))
          for j in range(num_images)
      ])

      # Extract the list[dict[label_key, example_label]]
      labels.extend([
          {
              _label_to_feature_key(_strip_s(k)): data[k][j]
              for k in self._cifar_info.label_keys
          } for j in range(num_images)
      ])

    # Shuffle the data to make sure classes are well distributed.
    data = list(zip(images, labels))
    random.shuffle(data)

    for image, label in data:
      features = {"image": image}
      features.update(label)
      yield features


class Cifar100(Cifar10):
  """CIFAR-100 dataset."""

  VERSION = tfds.core.Version("1.3.0")

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url="https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz",
        train_files=["train"],
        test_files=["test"],
        meta_file="meta",
        prefix="cifar-100-python/",
        label_keys=["fine_labels", "coarse_labels"],
    )

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("This dataset is just like the CIFAR-10, except it has "
                     "100 classes containing 600 images each. There are 500 "
                     "training images and 100 testing images per class. The "
                     "100 classes in the CIFAR-100 are grouped into 20 "
                     "superclasses. Each image comes with a \"fine\" label "
                     "(the class to which it belongs) and a \"coarse\" label "
                     "(the superclass to which it belongs)."),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_CIFAR_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=100),
            "coarse_label": tfds.features.ClassLabel(num_classes=20),
        }),
        supervised_keys=("image", "label"),
        urls=["https://www.cs.toronto.edu/~kriz/cifar.html"],
        citation=_CITATION,
    )


class CifarInfo(collections.namedtuple("_CifarInfo", [
    "name",
    "url",
    "prefix",
    "train_files",
    "test_files",
    "meta_file",
    "label_keys",
])):
  """Contains the information necessary to generate a CIFAR dataset.

  Args:
    name (str): name of dataset.
    url (str): data URL.
    prefix (str): path prefix within the downloaded and extracted file to look
      for `train_files` and `test_files`.
    train_files (list<str>): name of training files within `prefix`.
    test_files (list<str>): name of test files within `prefix`.
    meta_file (str): name of metadata file (labels) within `prefix`.
    label_keys (list<str>): names of the label keys in the data. If longer than
      1, provide `out_label_keys` to specify output names in feature
      dictionaries.  Otherwise will use "label".
  """


def _load_pickle(path):
  with tf.io.gfile.GFile(path, "rb") as f:
    if six.PY2:
      data = cPickle.load(f)
    else:
      data = cPickle.load(f, encoding="latin1")
  return data


def _strip_s(s):
  """Remove the 's': labels => label."""
  if not s.endswith("s"):
    raise AssertionError("{} should ends with 's'".format(s))
  return s[:-1]


def _label_to_feature_key(key):
  if key == "fine_label":
    return "label"
  return key
