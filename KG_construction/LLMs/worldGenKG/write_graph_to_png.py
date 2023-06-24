import pydot
import sys

inp_file = sys.argv[1]
out_file = sys.argv[2]

graphs = pydot.graph_from_dot_file(inp_file)
graph = graphs[0]
graph.write_png(out_file)