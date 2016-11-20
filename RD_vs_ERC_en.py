#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 22:30:07 2016

@author: bentkowski.piotr@gmail.com
for 'Citizens of Acamedia' social movement
"""
import numpy as np
import matplotlib.pyplot as plt


dt = np.dtype([('Country', 'S30'), ('Abrv', 'S3'), ("isEU", 'S5'),
               ('RD', np.float), ('Staff', np.float), ('SciPerMln', np.float),
               ('Granted', np.float), ('Eval', np.float),
               ('SucRate', np.float)])
MS = 10
FS = 17
TFS = 14
FIGSZ = (10, 10)
low = 1.0
high = 2.0
figFormat = "png"
legend_toupl = (u'> 2%', '1% - 2%', '< 1%', 'mean')
legTitle = '% of GDP for R&D'


def main():
    """ """
    data = np.genfromtxt("GDB_for_RD.csv", skip_header=1, dtype=dt,
                         delimiter=',')
    ones = data[data["RD"] <= low]
    twos = data[np.logical_and(data["RD"] > low, data["RD"] <= high)]
    richBoys = data[data["RD"] > high]
    EU_mean_Staff = data[~np.isnan(data["Staff"])]["Staff"].mean()

    # How many application were evaluated depending on number of research staff
    plt.figure(1, figsize=FIGSZ)
    rb, = plt.loglog(richBoys["Staff"], richBoys["Eval"]+1, 'go', ms=MS)
    dw, = plt.loglog(twos["Staff"], twos["Eval"]+1, 'yo', ms=MS)
    jj, = plt.loglog(ones["Staff"], ones["Eval"]+1, 'ro', ms=MS)
    eu, = plt.loglog(EU_mean_Staff, np.mean(data["Eval"]+1), 'cD', ms=MS-2)
    plt.xlabel(u"Researchers in full-time equivalents x1000 [data from 2014]",
               fontsize=FS)
    plt.ylabel(u"Number of evaluated ERC grants in all three schemes in 2015",
               fontsize=FS)
    for i, xy in enumerate(zip(data["Staff"], data["Eval"]+1)):
        plt.annotate(data['Abrv'][i].decode(), xy=xy, textcoords='data')
    plt.annotate("mean", xy=(EU_mean_Staff, np.mean(data["Eval"]+1)),
                 textcoords='data')
    markers_toupl = (rb, dw, jj, eu)
    plt.legend(markers_toupl, legend_toupl, loc='lower right',
               framealpha=0, numpoints=1, title=legTitle)
    plt.xticks(fontsize=TFS)
    plt.yticks(fontsize=TFS)
    plt.xlim(xmin=1)
    plt.grid(True)
    plt.savefig("EvalERC_Staff_EN." + figFormat)

    # How many projects got approved depending on number of research staff
    plt.figure(2, figsize=FIGSZ)
    plt.loglog(richBoys["Staff"], richBoys["Granted"]+1, 'go', ms=MS)
    plt.loglog(ones["Staff"], ones["Granted"]+1, 'ro', ms=MS)
    plt.loglog(twos["Staff"], twos["Granted"]+1, 'yo', ms=MS)
    plt.loglog(EU_mean_Staff, np.mean(data["Granted"]+1), 'cD', ms=MS-2)
    plt.xlabel(u"Researchers in full-time equivalents x1000 [data from 2014]",
               fontsize=FS)
    plt.ylabel(u"Number of awarded ERC grants in all three schemes in 2015",
               fontsize=FS)
    for i, xy in enumerate(zip(data["Staff"], data["Granted"]+1)):
        plt.annotate(data['Abrv'][i].decode(), xy=xy, textcoords='data')
    plt.annotate("mean", xy=(EU_mean_Staff, np.mean(data["Granted"]+1)),
                 textcoords='data')
    plt.legend(markers_toupl, legend_toupl, loc='lower right', framealpha=0,
               numpoints=1, title=legTitle)
    plt.xticks(fontsize=TFS)
    plt.yticks(fontsize=TFS)
    plt.xlim(xmin=1)
    plt.grid(True)
    plt.savefig("GrantedERC_Staff_EN." + figFormat)

    # Success rate vs fraction of GDP spend on R&D
    plt.figure(3, figsize=FIGSZ)
    plt.plot(richBoys['RD'], richBoys['SucRate'], 'go', ms=MS)
    plt.plot(ones['RD'], ones['SucRate'], 'ro', ms=MS)
    plt.plot(twos['RD'], twos['SucRate'], 'yo', ms=MS)
    plt.plot(np.mean(data["RD"]), np.mean(data["SucRate"]), 'cD', ms=MS-2)
    plt.xlabel(u"Research & development expenditure (% of GDP)" +
               " [data from 2014]", fontsize=FS)
    plt.ylabel("Success rate in all three ERC grants schemes in 2015",
               fontsize=FS)
    for i, xy in enumerate(zip(data['RD'], data['SucRate'])):
        plt.annotate(data['Abrv'][i].decode(), xy=xy, textcoords='data')
    plt.annotate("mean", xy=(np.mean(data["RD"]), np.mean(data["SucRate"])),
                 textcoords='data')
    plt.legend(markers_toupl, legend_toupl, loc='lower right', framealpha=0,
               numpoints=1, title=legTitle)
    plt.xticks(fontsize=TFS)
    plt.yticks(fontsize=TFS)
    plt.ylim(ymax=0.30001)
    plt.grid(True)
    plt.savefig("SucRate_GDP_EN." + figFormat)

    # Number of scientist per million people vs R&D spending
    plt.figure(4, figsize=FIGSZ)
    plt.plot(richBoys['RD'], richBoys['SciPerMln'], 'go', ms=MS)
    plt.plot(ones['RD'], ones['SciPerMln'], 'ro', ms=MS)
    plt.plot(twos['RD'], twos['SciPerMln'], 'yo', ms=MS)
    plt.plot(np.mean(data["RD"]), np.mean(data["SciPerMln"]), 'cD', ms=MS-2)
    plt.xlabel(u"Research & development expenditure (% of GDP)" +
               " [data from 2014]", fontsize=FS)
    plt.ylabel("Researchers in R&D per million people [data from 2014]",
               fontsize=FS)
    for i, xy in enumerate(zip(data['RD'], data['SciPerMln'])):
        plt.annotate(data['Abrv'][i].decode(), xy=xy, textcoords='data')
    plt.annotate("mean", xy=(np.mean(data["RD"]), np.mean(data["SciPerMln"])),
                 textcoords='data')
    plt.legend(markers_toupl, legend_toupl, loc='lower right', framealpha=0,
               numpoints=1, title=legTitle)
    plt.xticks(fontsize=TFS)
    plt.yticks(fontsize=TFS)
    plt.grid(True)
#    plt.tight_layout()
    plt.savefig("GDP_SciPerMln_EN." + figFormat)

    print("Done!")
    plt.show()


if __name__ == "__main__":
    main()
