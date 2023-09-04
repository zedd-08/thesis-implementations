import pydot
import sys

if len(sys.argv)!=3:
	sys.exit(f'Usage: python write_graph_to_png.py $inp_dot $out_png')
	

inp_file = sys.argv[1]
out_file = sys.argv[2]

graphs = pydot.graph_from_dot_file(inp_file)
graph = graphs[0]
graph.write_png(out_file)