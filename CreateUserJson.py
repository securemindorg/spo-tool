#!/bin/python
#
# Written by: Joshua White
#
#

import simplejson as json
import networkx as nx
import matplotlib.pyplot as plt

# this is not a displayed graph, it's just used for calculations
g = nx.DiGraph()
#g = nx.Graph()

input_csv = "./data/spo-tool-data.csv"
output_csv = "./static/data.csv"

def overall_network_stats(g):
	'''
	The intention of this function it to provide a return of every graph calculation we can
	squeeze out of the graph. In most cases this function simply calls multiple other functions
	and assigns them to variables which it returns as a result. Not all of these can be derived
	from the same library or the same source/target edge graph format so we do transforms here
	as necessary.
	'''

	# these are empty until they are not

	# basic counters
	number_of_nodes = g.number_of_nodes()
	number_of_edges = g.number_of_edges()

	# measures of centrality
	degree_centrality = nx.degree_centrality(g)
	in_degree_centrality = nx.in_degree_centrality(g)								# this only works for digraphs
        out_degree_centrality = nx.out_degree_centrality(g)								# this only works for digraphs
        closeness_centrality = nx.closeness_centrality(g)
	betweenness_centrality = nx.betweenness_centrality(g)
	edge_betweenness_centrality = nx.edge_betweenness_centrality(g)
	#betweenness_centrality_subset = nx.betweenness_centrality_subset(g)
	#edge_betweenness_centrality_subset = nx.edge_betweenness_centrality_subset(g)
	#current_flow_closeness_centrality = nx.current_flow_closeness_centrality(g) 					# this only works on non digraphs
	#current_flow_betweenness_centrality = nx.current_flow_betweenness_centrality 					# this only works on non digraphs
	#edge_current_flow_betweenness_centrality = nx.edge_current_flow_betweenness_centrality(g)			# this only works on non digraphs
	#approximate_current_flow_betweenness_centrality =  nx.approximate_current_flow_betweenness_centrality(g)	# this only works on non digrphs
	#current_flow_betweenness_centrality_subset = nx.current_flow_betweenness_centrality_subset(g)			# this only works on non digraphs
	#edge_current_flow_betweenness_centrality_subset = nx.edge_current_flow_betweenness_centrality_subset(g)
	eigenvector_centrality = nx.eigenvector_centrality(g)
	hits_centralities = nx.hits(g)
	katz_centrality = nx.katz_centrality(g)
	load_centrality = nx.load_centrality(g)
	in_degree = g.in_degree()
	out_degree = g.out_degree()

	# measures of ranking
	pagerank = nx.pagerank(g)


	# <><><><><><><><><><><><><><><><><><><><><>
	# lets create a data table csv for d3 to use
        # <><><><><><><><><><><><><><><><><><><><><>

	nametemplist = []
	centralitytemplist = []
	indegreetemplist = []
	outdegreetemplist = []

	fout = open(output_csv, "w")

        for item in degree_centrality:
                nametemplist.append(item)
		centralitytemplist.append(degree_centrality[item])

	for item in in_degree:
		indegreetemplist.append(in_degree[item])

        for item in out_degree:
                outdegreetemplist.append(out_degree[item])


	csv_headers = "Node ID,Degree Centrality,In-Degree,Out-Degree"

	fout.write(csv_headers)
	fout.write("\n")

	for c1, c2, c3, c4 in zip(nametemplist, centralitytemplist, indegreetemplist, outdegreetemplist):
		csv_row = c1 + "," + str(c2) + "," + str(c3) + "," + str(c4)
		fout.write(csv_row)
		fout.write("\n")

	fout.close()

	#print in_degree_centrality
	#print out_degree_centrality
	#print nx.degree(g)
	#print g.in_degree()
	#print g.out_degree()

	# return the necessary variables, this is not elegant but were in a time crunch
	'''return number_of_nodes, \
	       number_of_edges, \
               degree_centrality, \
	       in_degree_centrality, \
               out_degree_centrality, \
               closeness_centrality, \
	       betweenness_centrality, \
	       edge_betweenness_centrality, \
               eigenvector_centrality, \
               hits_centralities, \
	       katz_centrality, \
               load_centrality'''

	return 

def add_edges_to_python_graph(source, target):
	'''
	I realize this might be redunant since we can call this within the create json graph file function
	however, this way I can more eaily transform the source, target into ints or hash values if needed
	I am not using graph_tool anymore however, because it took way to long to compile, and while it is
	very fast, I definitely had a lot of issue with converting nodes to decimal ints, and then assigning
	labels to them.
	'''

	g.add_edge(source.strip("\n"), target.strip("\n"))

	return g

def create_json_graph_file():
	'''
	This is the main function of this library, it creates all the necessary json structures to be used
	in the web components, such as the json graph structure that d3 plots. This dunction needs a lot
	of work to clean things up. Right now it does some stupid, but fast enough, things like open the
	same csv twice and read it twice. We'll solve this eventually.
	'''

	# define fresh, empty, arrays (lists)
	users_array = []
	unique_users_array = []
	nodes_array = []
	edges_array = []
	nodes_array_weak = []
	edges_array_weak = []
	users_array_weak = []
	unique_users_array_weak = []
        nodes_array_ff = []
        edges_array_ff = []
        users_array_ff = []
        unique_users_array_ff = []
        nodes_array_strong = []
        edges_array_strong = []
        users_array_strong = []
        unique_users_array_strong = []

	# open the csv for reading
	file_in = open(input_csv, "r")

	# open the json graph file for writing
        file_out = open("./static/graphFile.json", "w")
        file_out_strong = open("./static/graphFile-Strong.json", "w")
        file_out_ff = open("./static/graphFile-FamFriends.json", "w")
        file_out_weak = open("./static/graphFile-Weak.json", "w")

	# setup the output files for each of the graph types
	for line in file_in:

		# parse the csv line so we can test the stength of the link
		source, edge_type, target = line.split(",")

		# calls our function to add the source and target to the python graph
		add_edges_to_python_graph(source, target)

		# check for the weak types
		if edge_type in ("has.degree", "has.ability", "has.title"):

	                # append all sources and targets to the node list
        	        users_array_weak.append(source)
                	users_array_weak.append(target.strip("\n"))

			# create a new list with only the unique nodes in it
                	unique_users_array_weak = list(set(users_array_weak))

                        edges_array_weak.append({"source": source, "target": target.strip("\n"), "value": 1 })

                # check for the strong types
                elif edge_type in ("employed.by", "connected.to.project", "connected.to.org"):

                        # append all sources and targets to the node list
                        users_array_strong.append(source)
                        users_array_strong.append(target.strip("\n"))

                        # create a new list with only the unique nodes in it
                        unique_users_array_strong = list(set(users_array_strong))

                        edges_array_strong.append({"source": source, "target": target.strip("\n"), "value": 1 })

                # check for the family and friends types
                elif edge_type in ("friends.with", "related.to"):

                        # append all sources and targets to the node list
                        users_array_ff.append(source)
                        users_array_ff.append(target.strip("\n"))

                        # create a new list with only the unique nodes in it
                        unique_users_array_ff = list(set(users_array_ff))

                        edges_array_ff.append({"source": source, "target": target.strip("\n"), "value": 1 })

        # for good mesure, close the input file
        file_in.close()

        # open the csv for reading (So So Dirty opening this file again)
        file_in = open(input_csv, "r")

	# this section creates the large json graph file
	# for line in csv
	for line in file_in:
		# split the line and populate source, edge, target variables
		source, edge_type, target = line.split(",")
		# append all sources and targets to the node list
		users_array.append(source)
		users_array.append(target.strip("\n"))
		# create a new list with only the unique nodes in it
		unique_users_array = list(set(users_array))

		# change the value field of the edge, (think color or weight), based on the connection type
		# this isn't the best way to do this but it will work for now
		if edge_type == "has.degree":
	        	edges_array.append({"source": source, "target": target.strip("\n"), "value": 1 })
		elif edge_type == "has.ability":
                	edges_array.append({"source": source, "target": target.strip("\n"), "value": 2 })
        	elif edge_type == "employed.by":
                	edges_array.append({"source": source, "target": target.strip("\n"), "value": 3 })
        	elif edge_type == "has.title":
                	edges_array.append({"source": source, "target": target.strip("\n"), "value": 4 })
        	elif edge_type == "friends.with":
                	edges_array.append({"source": source, "target": target.strip("\n"), "value": 5 })
        	elif edge_type == "related.to":
                	edges_array.append({"source": source, "target": target.strip("\n"), "value": 6 })
        	elif edge_type == "connected.to.project":
                	edges_array.append({"source": source, "target": target.strip("\n"), "value": 7 })
        	elif edge_type == "connected.to.org":
                	edges_array.append({"source": source, "target": target.strip("\n"), "value": 8 })

	# for item in that new unique user array
	for item in unique_users_array:
		#jsonify the nodes array
		nodes_array.append({"id": item, "group":1})

	# write to the output file and close it
	file_out.write(json.dumps({"nodes":nodes_array, "links":edges_array}))
	file_out.close()

        # for item in that new unique user array
        for item in unique_users_array_weak:
                #jsonify the nodes array
                nodes_array_weak.append({"id": item, "group":1})

        # write to the output file and close it
        file_out_weak.write(json.dumps({"nodes":nodes_array_weak, "links":edges_array_weak}))
        file_out_weak.close()

        # for item in that new unique user array
        for item in unique_users_array_ff:
                #jsonify the nodes array
                nodes_array_ff.append({"id": item, "group":1})

        # write to the output file and close it
        file_out_ff.write(json.dumps({"nodes":nodes_array_ff, "links":edges_array_ff}))
        file_out_ff.close()

        # for item in that new unique user array
        for item in unique_users_array_strong:
                #jsonify the nodes array
                nodes_array_strong.append({"id": item, "group":1})

        # write to the output file and close it
        file_out_strong.write(json.dumps({"nodes":nodes_array_strong, "links":edges_array_strong}))
        file_out_strong.close()

	# for good mesure, close the input file
	file_in.close()

	print overall_network_stats(g)

if __name__ == '__main__':
	# this is main, it calls everything
	create_json_graph_file()
