import sys
from typing import List
import numpy as np
import networkx as nx



def fetch_brec_dataset(
	ds_name:str,
	base_path:str="../data/BREC"
	)->List[nx.Graph]:
	

	ds_strings = np.load(f"{base_path}/{ds_name}.npy")
	print(ds_strings)
	if ds_name=='basic':
		print(ds_strings.reshape(-1,2))
	print(ds_strings.shape)
	sys.exit(1)
	graph_list = [nx.from_graph6_bytes(str.encode(g6_string)) for g6_string in ds_strings]

	return graph_list


def fetch_strongly_regular_family(
	family_name:str,
	base_path:str="../data/McKay/SR"
	)->List[nx.Graph]:
	

	graph_list = nx.read_graph6(f"{base_path}/{family_name}.g6")

	return graph_list

