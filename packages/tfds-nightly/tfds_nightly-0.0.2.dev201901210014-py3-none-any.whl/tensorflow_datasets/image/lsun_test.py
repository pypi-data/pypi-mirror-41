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

"""Tests for tensorflow_datasets.image.lsun."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.image import lsun
from tensorflow_datasets.testing import dataset_builder_testing


class LsunTest(dataset_builder_testing.TestCase):
  DATASET_CLASS = lsun.Lsun
  BUILDER_CONFIG_NAMES_TO_TEST = ["classroom"]

  SPLITS = {
      "train": 3,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {"train": "", "val": ""}


if __name__ == "__main__":
  dataset_builder_testing.main()
