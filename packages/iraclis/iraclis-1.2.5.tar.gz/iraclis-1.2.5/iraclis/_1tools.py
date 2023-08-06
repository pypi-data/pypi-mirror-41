from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ._0errors import *
from ._0imports import *


class Tools:

    def __init__(self):
        pass

    @staticmethod
    def central_crop(original_array, destination_fits):

        crop1 = len(original_array) / 2 - len(destination_fits[1].data) / 2
        crop2 = len(original_array) / 2 + len(destination_fits[1].data) / 2

        return original_array[crop1:crop2, crop1:crop2]

    def fit_2d_gauss(self, dataxy):

        model = self.gauss(np.arange(len(dataxy)), len(dataxy) / 2, np.max(dataxy), 1.0)
        dx = np.argmax(np.convolve(np.sum(dataxy, 0), model)) - np.argmax(np.convolve(model, model))
        dy = np.argmax(np.convolve(np.sum(dataxy, 1), model)) - np.argmax(np.convolve(model, model))

        x00 = int(dx + len(dataxy) / 2)
        y00 = int(dy + len(dataxy) / 2)

        min_y = int(max(y00 - 50, 0))
        max_y = int(min(y00 + 50, len(dataxy)))
        min_x = int(max(x00 - 50, 0))
        max_x = int(min(x00 + 50, len(dataxy[0])))
        dataxy = dataxy[min_y:max_y, min_x:max_x]

        # fit the 2D gaussian

        def twod_gauss(dataxy, h, mean_x, mean_y, width_x, width_y, c):
            datax, datay = dataxy
            z = h * np.exp(
                -(((mean_x - datax) ** 2) / (width_x ** 2) + ((mean_y - datay) ** 2) / (width_y ** 2)) / 2) + c
            return z.flatten()

        x = np.arange(min_x, max_x)
        y = np.arange(min_y, max_y)
        x, y = np.meshgrid(x, y)
        pp0 = [np.max(dataxy) - np.median(dataxy), x00, y00, 1.0, 1.0, np.median(dataxy)]
        popt, pcov = curve_fit(twod_gauss, (x.flatten() + 0.5, y.flatten() + 0.5), dataxy.flatten(),
                               p0=pp0, maxfev=10000)

        center_x = popt[1]
        center_y = popt[2]

        return center_x, center_y, popt

    @staticmethod
    def gauss(x_arr, x0, aa, bb):
        return aa * np.exp(-np.power(x0 - x_arr, 2) / (2 * (bb ** 2)))

    def fit_gauss(self, datax, datay):

        for expand in range(10, 30):
            datax = np.append(datax, max(datax) + expand)
            datay = np.append(datay, 0)
            datax = np.append(datax, min(datax) - expand)
            datay = np.append(datay, 0)

        popt, pcov = curve_fit(self.gauss, datax, datay, p0=[datax[np.argmax(datay)], max(datay), 1.0])

        center = popt[0]

        center_err = np.sqrt(pcov[0][0])

        return center, center_err, popt

    def box(self, x_arr, x0, aa, bb, cc):
        return aa * np.exp(-np.power(np.power(x0 - x_arr, 2) / (2 * (bb ** 2)), cc))

    def fit_box(self, datax, datay):

        minlim = datax[np.argmax(datay[5:] - datay[:-5])]
        maxlim = datax[np.argmin(datay[5:] - datay[:-5])]

        for expand in range(10, 30):
            datax = np.append(datax, max(datax) + expand)
            datay = np.append(datay, 0)
            datax = np.append(datax, min(datax) - expand)
            datay = np.append(datay, 0)

        popt, pcov = curve_fit(self.box, datax, datay,
                               p0=[0.5 * (maxlim + minlim), max(datay), 0.5 * (maxlim - minlim), 1.0])

        center = popt[0]

        center_err = np.sqrt(pcov[0][0])

        fwhm = popt[2] * 2.0 * np.sqrt(2.0 * (np.log(2) ** (1.0 / popt[3])))

        s, c = popt[2], popt[3]
        ss, cs = np.sqrt(pcov[2][2]), np.sqrt(pcov[3][3])
        fwhm_err = np.sqrt(8.0 * (ss ** 2) * (np.log(2.0) ** (1.0 / c))
                           + (2.0 * (cs ** 2) * (s ** 2) * (np.log(2.0) ** (1.0 / c))
                              * (np.log(np.log(2.0)) ** 2)) / (c ** 4))

        return center, center_err, fwhm, fwhm_err, popt

    def fit_line(self, datax, datay):

        mx = np.mean(datax)
        my = np.mean(datay)

        ssxx = np.sum((datax - mx) ** 2)
        ssyy = np.sum((datay - my) ** 2)
        ssxy = np.sum((datax - mx) * (datay - my))

        bb = ssxy / ssxx
        aa = my - bb * mx

        n = len(datax)
        sss = np.sqrt((ssyy - bb * ssxy) / (n - 2))

        aerr = sss * np.sqrt(1.0 / n + (mx ** 2) / ssxx)
        berr = sss / np.sqrt(ssxx)

        return aa, bb, aerr, berr

    @staticmethod
    def distribution(data_i, xstep=5.0):

        def gauss(x, aa, x0, bb):
            return aa * np.exp(-(x - x0) ** 2 / (2 * bb ** 2))

        data = np.array(data_i)
        xstep = np.sqrt(np.median((data - np.median(data)) ** 2)) / xstep
        xmin = min(data)
        xmax = max(data)
        x_size = round((xmax - xmin) / xstep) + 1

        distrx = xmin + np.arange(x_size) * xstep
        data = np.int_((data - xmin) / xstep)
        distr = np.bincount(data)
        distr = np.insert(distr, len(distr), np.zeros(int(x_size) - len(distr)))

        pick = np.max(distr)
        mean = distrx[np.argmax(distr)]
        sigma = np.abs(distrx[np.argmin(np.abs(distr - pick / 2))] - mean)
        try:
            popt, pcov = curve_fit(gauss, distrx, distr, p0=[pick, mean, sigma])
        except RuntimeError:
            popt = [0, np.mean(data_i), np.std(data_i)]
        return distrx, distr, popt

    @staticmethod
    def posterior_analysis(data_i):

        data = np.array(data_i)
        xstep = np.sqrt(np.median((data - np.median(data)) ** 2)) / 5.0
        bin_width = xstep
        xmin = min(data)
        xmax = max(data)
        x_size = round((xmax - xmin) / xstep) + 1

        distrx = xmin + np.arange(x_size) * xstep
        data = np.int_((data - xmin) / xstep)
        distr = np.bincount(data)
        distr = np.insert(distr, len(distr), np.zeros(int(x_size) - len(distr)))

        confidence_interval = 68. / 100.
        # corresponds to the 1-sigma level propability

        pleft = 0.0
        centroid = np.argmax(distr)
        exp_val = distrx[centroid]

        total_propability_left = np.sum(bin_width * distr[:centroid]) * confidence_interval
        total_propability_right = np.sum(bin_width * distr[centroid:]) * confidence_interval

        num = centroid
        leftci = 0
        while pleft <= total_propability_left:
            if num == centroid:
                pleft += (bin_width / 2.0) * distr[num]
            else:
                pleft += bin_width * distr[num]
            leftci = distrx[num]
            num -= 1
            if num < 0:
                print('ERROR : confidence level can not be reached from left')
                break
        pright = 0.0
        num = centroid
        rightci = 0
        while pright <= total_propability_right:
            if num == centroid:
                pright += (bin_width / 2.0) * distr[num]
            else:
                pright += bin_width * distr[num]
            rightci = distrx[num]
            num += 1
            if num > len(distr) - 1:
                print('ERROR : confidence level can not be reached from right')
                break

        error_plus, error_minus = rightci - exp_val, exp_val - leftci

        return exp_val, error_minus, error_plus

    @staticmethod
    def correlation(x, y):
        n = len(x)
        mx = np.mean(x)
        sx = np.std(x)
        my = np.mean(y)
        sy = np.std(y)
        return np.round(np.sum((x - mx) * (y - my)) / ((n - 1) * sx * sy), 2)


tools = Tools()
