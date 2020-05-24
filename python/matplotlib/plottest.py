#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
import sys

def main(args):
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.title('日本語タイトル')
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro']
    plt.show()

if __name__ == "__main__":
    main(sys.argv)
