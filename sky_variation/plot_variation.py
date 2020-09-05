#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 05:57:42 2020

@author: bikram
"""


try:
    import pyfits as fits
except:
    from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

image_1, header_1 = fits.getdata('../19970514_1310_B.fits', header=True)

print(image_1.shape)

def mean_with_sigmaclip(x, y, sigma = 1.5, iter_ = 3):
    y_ = np.copy(y)
    x_ = np.copy(x)
    for i in range(iter_):
        mean = np.mean(y_)
        std = np.std(y_)*sigma
        z = np.polyfit(x_, y_, 3); p = np.poly1d(z)
        y_0 = y_-p(x_)
        x_ = x_[np.abs(y_0)<=std]
        y_ = y_[np.abs(y_0)<=std]
    return x_, y_


def plot_xy(x, y, x_label='x', y_label='y', title='plot', f_name='test_plot.pdf', sigmaclip=False):
    if sigmaclip:
        x, y = mean_with_sigmaclip(x, y)
    fig = plt.figure(figsize=[12,7])
    ax = fig.add_subplot(111)
    ax.plot(x,y,'o')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.tight_layout()
    plt.savefig(f_name)
    plt.show()

x = np.arange(image_1.shape[0])
y = np.arange(image_1.shape[1])

med_x = np.mean(image_1, axis=1)
med_y = np.mean(image_1, axis=0)

plot_xy(x, med_x, x_label='CCD rows', y_label='median(CCD rows)',
        f_name='temporal_variation.png', sigmaclip=True)
plot_xy(y, med_y, x_label='CCD columns', y_label='median(CCD columns)', 
        f_name='spatial_variation.png', sigmaclip=True)
