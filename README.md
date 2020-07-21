# LockdownAnalysis

## Impact of C19-induced Lockdown on Air Quality
With the spirit of reproducible research, this repository contains codes required to produce the results in the manuscript:
    
    
    
    
    
Please cite the above paper if you intent to use whole/part of the code. This code is only for academic and research purposes.

![timeseries](https://user-images.githubusercontent.com/62281372/87881577-da13a300-ca17-11ea-8785-1cc321c4cffd.jpg)


 ## Code Organization
 The codes are written in Jupyter Notebook and python3.
 
 ## Dependencies
 
 1) Xarray: pip install xarray
 2) numpy: pip install numpy
 3) pandas 1.0.5: pip install pandas
 4) matplotlib: pip install matplotlib
 5) netCDF4 1.5.3: pip install netCDF4
 6) cartopy 0.18.0: pip instal Cartopy
 7) termcolor 1.1.0: pip install termcolor
 8) ipywidgets 7.5.1: pip install ipywidgets
 9) glob2 0.7: pip install glob2
 10) functools 0.5: pip install functools
 11) scikit-image 0.17.2: pip install scikit-image
 12) opencv-python 4.3.0.36: pip install opencv-python



1. CombiningNetCDFfiles.ipynb : Run this script to combine netCDF files. This comes under preprocessing of data to obtain a publication quality dataset.(http://nco.sourceforge.net/)  

2. DailyAverageConcPlots.ipynb : Run this script to obtain the distribution plots used in the paper. Contains time series line plot of daily average Nitrogen Dioxide concentration, bar plots of satellite data obtained from Sentinel-5p for average concentration of 15 days for year 2019 and 2020 and line plots of ground based monitoring station(ITO,Delhi station). It saves the plots as .png and .pdf format for future use in the same folder as the script.

3. ImageDifferenceofTwoPlots.py : Run this script to obtain the difference of two NO2 Concentration plots made using Cartopy or Panoply(https://www.giss.nasa.gov/tools/panoply/) to infer and analyze the decrease in daily average concentration.

4. MapsfromNetCDFfiles.ipynb : Run this script to retrieve,read,edit,store and plot netCDF files obtained from Sentinel-5P.
