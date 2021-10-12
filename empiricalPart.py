# @. Shamsulhaq Basir

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def load_data(data):
	vector = np.loadtxt(data, delimiter="\n")
	return vector 

def plotFigures(raw_return, tile_return):
	raw_return  = load_data(raw_return) 
	tile_return = load_data(tile_return)

	raw = pd.DataFrame({"raw_return":raw_return})
	raw['rolling_mean'] = raw['raw_return'].rolling(window=25).mean()
	print(raw)
	raw.plot(title = "raw_mode")
	plt.savefig('raw_mode.png')

	tile = pd.DataFrame({"tile_return": tile_return})
	tile['rolling_mean'] = tile['tile_return'].rolling(window=25).mean()
	print(tile)
	tile.plot(title = "Tile_mode")
	plt.savefig('tile_mode.png')

	plt.show()



def main(args):
	raw_return   = args[1]
	tile_return  = args[2]
	plotFigures(raw_return, tile_return)



if __name__ == "__main__":
        main(sys.argv)

