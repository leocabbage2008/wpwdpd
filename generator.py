import pandas as pd
from ecmwfapi import ECMWFDataServer
from tqdm import tqdm
import contextlib
import os

os.makedirs("data", exist_ok=True)
os.chdir("./data")
server = ECMWFDataServer()
daterange = pd.period_range(start='01/01/1984',end='12/31/2017', freq='D')

with contextlib.redirect_stdout(None):
	for i in tqdm(daterange): 
		server.retrieve({
			"class": "ei",
			"dataset": "interim",
			"date": f"{i}",
			"expver": "1",
			"grid": "0.75/0.75",
			"levtype": "sfc",
			"param": "228.128",
			"step": "3/6/9/12",
			"stream": "oper",
			"time": "00:00:00/12:00:00",
			"type": "fc",
			"format": "netcdf",
			"target": f"{i}.nc",
		})
