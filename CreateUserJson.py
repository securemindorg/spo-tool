#!/bin/python
#
# Written by: Joshua White
#

import simplejson as json

def create_json_graph_file():

	# define fresh, empty, arrays (lists)
	users_array = []
	unique_users_array = []
	nodes_array = []
	edges_array = []

	# open the csv for reading
	file_in = open("./data/spo-tool-data.csv", "r")

	# open the json graph file for writing
	file_out = open("./static/graphFile.json", "w")

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

	# for good mesure, close the input file
	file_in.close()

if __name__ == '__main__':
	create_json_graph_file()
