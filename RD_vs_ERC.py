#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 22:30:07 2016

@author: bentkowski.piotr@gmail.com
Dla Ruchu Społecznego Obywatele Nauki
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Arial')

dt = np.dtype([('Country', 'S30'), ('Abrv', 'S3'), ("isEU", 'S5'),
               ('RD', np.float), ('Staff', np.float), ('SciPerMln', np.float),
               ('Granted', np.float), ('Eval', np.float),
               ('SucRate', np.float)])
MS = 10
FS = 19
TFS = 15
CLR = (0.25, 0.25, 0.85, 0.65)
FIGSZ = (10, 10)
low = 1.0
high = 2.0
figFormat = "png"
legend_toupl = (u'> 2%', '1% - 2%', '< 1%', 'Polska', 'średnia')
legTitle = '% PKB na BiR'


def main():
    """ """
    data = np.genfromtxt("GDB_for_RD.csv", skip_header=1, dtype=dt,
                         delimiter=',')
    pol = data[data['Abrv'] == "PL".encode()]
    jeden = data[data["RD"] <= low]
    dwa = data[np.logical_and(data["RD"] > low, data["RD"] <= high)]
    richBoys = data[data["RD"] > high]
    EU_mean_Staff = data[~np.isnan(data["Staff"])]["Staff"].mean()

    # How many application were evaluated depending on number of research staff
    plt.figure(1, figsize=FIGSZ)
    rb, = plt.loglog(richBoys["Staff"], richBoys["Eval"]+1, 'go', ms=MS)
    dw, = plt.loglog(dwa["Staff"], dwa["Eval"]+1, 'o', ms=MS, color=CLR)
    jj, = plt.loglog(jeden["Staff"], jeden["Eval"]+1, 'yo', ms=MS)
    pl, = plt.loglog(pol["Staff"], pol["Eval"]+1, 'ro', ms=MS)
    eu, = plt.loglog(EU_mean_Staff, np.mean(data["Eval"]+1), 'cD', ms=MS-2)
    plt.xlabel(u"Liczba badaczy na etatach w tys. [dane na 2014 r.]",
               fontsize=FS)
    plt.ylabel(u"Liczba wszystkich rozpatrzonych wniosków o granty ERC w 2015",
               fontsize=FS)
    for i, xy in enumerate(zip(data["Staff"], data["Eval"]+1)):
        plt.annotate(data['Abrv'][i].decode(), xy=xy, textcoords='data')
    plt.annotate("mean", xy=(EU_mean_Staff, np.mean(data["Eval"]+1)),
                 textcoords='data')
    markers_toupl = (rb, dw, jj, pl, eu)
    plt.legend(markers_toupl, legend_toupl, loc='lower right',
               framealpha=0, numpoints=1, title=legTitle)
    plt.xticks(fontsize=TFS)
    plt.yticks(fontsize=TFS)
    plt.xlim(xmin=1)
    plt.grid(True)
    plt.savefig("EvalERC_Staff." + figFormat)

    # How many projects got approved depending on number of research staff
    plt.figure(2, figsize=FIGSZ)
    plt.loglog(richBoys["Staff"], richBoys["Granted"]+1, 'go', ms=MS)
    plt.loglog(jeden["Staff"], jeden["Granted"]+1, 'yo', ms=MS)
    plt.loglog(dwa["Staff"], dwa["Granted"]+1, 'o', ms=MS, color=CLR)
    plt.loglog(pol["Staff"], pol["Granted"]+1, 'ro', ms=MS)
    plt.loglog(EU_mean_Staff, np.mean(data["Granted"]+1), 'cD', ms=MS-2)
    plt.xlabel(u"Liczba badaczy na etatach w tys. [dane na 2014 r.]",
               fontsize=FS)
    plt.ylabel(u"Liczba pozytywnie rozpatrzonych wniosków o granty" +
               " ERC w 2015", fontsize=FS)
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
    plt.savefig("GrantedERC_Staff." + figFormat)

    # Success rate vs fraction of GDP spend on R&D
    plt.figure(3, figsize=FIGSZ)
    plt.plot(richBoys['RD'], richBoys['SucRate'], 'go', ms=MS)
    plt.plot(jeden['RD'], jeden['SucRate'], 'yo', ms=MS)
    plt.plot(dwa['RD'], dwa['SucRate'], 'o', ms=MS, color=CLR)
    plt.plot(pol['RD'], pol['SucRate'], 'ro', ms=MS)
    plt.plot(np.mean(data["RD"]), np.mean(data["SucRate"]), 'cD', ms=MS-2)
    plt.xlabel(u"Proc. PKB na badania i rozwój [dane na 2014 r.]",
               fontsize=FS)
    plt.ylabel("Wskaźnik sukcesu wliczajacy wszytkie konkursy ERC w 2015",
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
    plt.savefig("SucRate_GDP." + figFormat)

    # Number of scientist per million people vs R&D spending
    plt.figure(4, figsize=FIGSZ)
    plt.plot(richBoys['RD'], richBoys['SciPerMln'], 'go', ms=MS)
    plt.plot(jeden['RD'], jeden['SciPerMln'], 'yo', ms=MS)
    plt.plot(dwa['RD'], dwa['SciPerMln'], 'o', ms=MS, color=CLR)
    plt.plot(pol['RD'], pol['SciPerMln'], 'ro', ms=MS)
    plt.plot(np.mean(data["RD"]), np.mean(data["SciPerMln"]), 'cD', ms=MS-2)
    plt.xlabel(u"Proc. PKB na badania i rozwój [dane na 2014 r.]",
               fontsize=FS)
    plt.ylabel("Liczba badaczy przypadająca na million mieszkanców" +
               " [dane na 2014 r.]", fontsize=FS)
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
    plt.savefig("GDP_SciPerMln." + figFormat)

    print("Done!")
    plt.show()


if __name__ == "__main__":
    main()
