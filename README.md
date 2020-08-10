# Impact of C19-induced Lockdown on Air Quality

With the spirit of reproducible research, this repository contains codes required to produce the results in the manuscript:
    
> D. Kaloni, Y. H. Lee, S. Dev, Impact of C19-induced Lockdown on Air Quality, *under review*.
    
Please cite the above paper if you intent to use whole/part of the code. This code is only for academic and research purposes.

![gif11](https://user-images.githubusercontent.com/62281372/89396679-79c97480-d72c-11ea-9ac2-424ee965f33b.gif)

*Time lapse of spatial distribution of nitrogen dioxide concentration for the case study of New Delhi.*

![timeseries](https://user-images.githubusercontent.com/62281372/87881577-da13a300-ca17-11ea-8785-1cc321c4cffd.jpg)
*Impact of lockdown in the nitrogen dioxide concentration for the case study of New Delhi.*

 ## Code Organization
 All codes are written in `python3`.
 
 ### Dependencies
 The following libraries should be installed before the execution of the codes.
 + Xarray: `pip install xarray`
 + numpy: `pip install numpy`
 + pandas 1.0.5: `pip install pandas`
 + matplotlib: `pip install matplotlib`
 + netCDF4 1.5.3: `pip install netCDF4`
 + cartopy 0.18.0: `pip instal Cartopy`
 + termcolor 1.1.0: `pip install termcolor`
 + ipywidgets 7.5.1: `pip install ipywidgets`
 + glob2 0.7: `pip install glob2`
 + functools 0.5: `pip install functools`
 + scikit-image 0.17.2: `pip install scikit-image`
 + opencv-python 4.3.0.36: `pip install opencv-python`
 
### Data
The data source in this work is NASA's Goddard Earth Sciences Data and Information Services Center ([GES DISC](https://disc.gsfc.nasa.gov/)). We are releasing the processed data that we used in this work. You may download the processed data from [this Google Drive link](https://drive.google.com/drive/folders/1mo6IYjHD1XFzmsdIrhZira2YxTLBOfSy?usp=sharing). 

### Scripts

 + `CombiningNetCDFfiles.ipynb`: Run this script to [combine netCDF files](http://nco.sourceforge.net/). This comes under preprocessing of data to obtain a publication quality dataset.  

+ `DailyAverageConcPlots.ipynb`: Run this script to obtain the distribution plots used in the paper. Contains time series line plot of daily average nitrogen dioxide concentration, bar plots of satellite data obtained from Sentinel-5P for average concentration of 15 days for year 2019 and 2020 and line plots of ground based monitoring station (ITO, Delhi station). It saves the plots as `.png` and `.pdf` format for future use in the same folder as the script.

+ `python3 ImageDifferenceofTwoPlots.py`: Run this script to obtain the difference of two NO<sub>2</sub> Concentration plots made using Cartopy or [Panoply](https://www.giss.nasa.gov/tools/panoply/) to infer and analyze the decrease in daily average concentration.

+ `MapsfromNetCDFfiles.ipynb`: Run this script to retrieve, read, edit, store and plot netCDF files obtained from Sentinel-5P.


To explore Sentinel-5P in detail, follow Research and User Support of Copernicus at https://rus-training.eu/
