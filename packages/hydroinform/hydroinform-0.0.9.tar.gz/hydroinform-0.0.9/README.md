# hydroinform
This package contains a steady-state stream model and some tools to access .dfs-files from DHI

#Usage
Write a pump extraction file to be used with MikeZero:
```sh
#Import DFS from HydroInform
from hydroinform import DFS

#Set the path to your MikeZero bin directory. (Where ufs.dll is located)
DFS.MikeZeroBinDIR=r'C:\Program Files (x86)\DHI\2017\bin\x64'

#The number of Items (In this case number of pumping wells)
numberofitems = 5;

#Now create the file.
_tso = DFS.DFS0.NewFile(r'c:\temp\extraction.dfs0'), numberofitems);

#Loop the items and set the units etc.
for itemCount in range (0, numberofitems):
    _tso.Items[itemCount].ValueType = DFS.DataValueType.MeanStepBackward
    _tso.Items[itemCount].EumItem = DFS.EumItem.eumIPumpingRate
    _tso.Items[itemCount].EumUnit = DFS.EumUnit.eumUm3PerYear
    _tso.Items[itemCount].Name = "Item number: " + str(itemCount)
      
#Loop the years where you have pumping data
tscount = 0;
for year in range(2010, 2016):
    #For every year append a new timestep
    _tso.AppendTimeStep(datetime.datetime(year, 12, 31, 12))
    #Loop the items and set a value for this timestep
    for itemCount in range (0, numberofitems):
        #Sets the data. Note that timesteps count from 0 and Items count from 1
        _tso.SetData(tscount, itemCount+1, year * itemCount)
    tscount+=1
#Call dispose which will save and close the file.
_tso.Dispose();
```