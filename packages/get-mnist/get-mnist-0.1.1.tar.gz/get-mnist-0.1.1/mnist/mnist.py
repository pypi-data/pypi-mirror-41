from six.moves.urllib.request import urlretrieve

import os
import argparse
from hashlib import sha1
from gzip import GzipFile
from struct import unpack_from
import numpy as np


LABEL_MAGIC = 2049
IMAGE_MAGIC = 2051


class MNIST:
    TRAIN=u"http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
    TRAIN_LABELS=u"http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
    TEST=u"http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"
    TEST_LABELS=u"http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"


class FashionMNIST:
    TRAIN=u"http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz"
    TRAIN_LABELS=u"http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz"
    TEST=u"http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz"
    TEST_LABELS=u"http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz"


def read_labels(data):
    magic, examples = unpack_from(">2i", data)
    assert magic == LABEL_MAGIC, "Magic number in file {} doesn't match".format(file_name)
    labels = unpack_from(">{}B".format(examples), data[8:])
    return np.frombuffer(data[8:], dtype=np.uint8).astype(np.int32)


def read_images(data):
    magic, number, rows, cols = unpack_from(">4i", data)
    assert magic == IMAGE_MAGIC, "Magic number in file {} doesn't match".format(file_name)
    images = np.frombuffer(data[16:], dtype=np.uint8).astype(np.float32)
    images = np.reshape(images, (number, rows, cols))
    return images


def download_hook():
    last = 0
    def step(count, block, total):
        precent = count * block * 100 // total
        if last != percent:
            if percent % 5 == 0:
                sys.stdout.write("{}%".format(percent))
            else:
                sys.stdout.write(".")
            sys.stdout.flush()
        last = percent
    return step


def get_data(url, cache=None):
    path = None
    if cache is not None:
        if not os.path.exists(cache):
            os.makedirs(cache)
        h = sha1(url.encode("utf-8")).hexdigest()
        path = os.path.join(cache, h)
        if os.path.exists(path):
            with GzipFile(path, "rb") as f:
                return f.read()
    file_name, _  = urlretrieve(url, path)
    with GzipFile(file_name) as f:
        return f.read()


def get_mnist(
        cache=None,
        train_url=MNIST.TRAIN,
        train_label_url=MNIST.TRAIN_LABELS,
        test_url=MNIST.TEST,
        test_label_url=MNIST.TEST_LABELS,
):
    x_train = read_images(get_data(train_url, cache))
    x_test = read_images(get_data(test_url, cache))
    y_train = read_labels(get_data(train_label_url, cache))
    y_test = read_labels(get_data(test_label_url, cache))
    return x_train, y_train, x_test, y_test


def get_fashion_mnist(
        cache=None,
        train_url=FashionMNIST.TRAIN,
        train_label_url=FashionMNIST.TRAIN_LABELS,
        test_url=FashionMNIST.TEST,
        test_label_url=FashionMNIST.TEST_LABELS,
):
    return get_mnist(
        cache,
        train_url, train_label_url,
        test_url, test_label_url
    )


def main():
    parser = argparse.ArgumentParser(description="Download MNIST dataset")
    parser.add_argument(
        "--data", default="mnist",
        choices=["mnist", "fashion"],
        help="Which dataset to download."
    )
    parser.add_argument(
        "--cache", default="MNIST",
        help="Directory to save data in"
    )
    args = parser.parse_args()

    if args.data.lower() == "mnist":
        get_mnist(args.cache)
    else:
        get_fashion_mnist(args.cache)


if __name__ == "__main__":
    main()
