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
	file_in = open("./data/spo-tool-data.csv", "r")

	# open the json graph file for writing
        file_out = open("./static/graphFile.json", "w")
        file_out_strong = open("./static/graphFile-Strong.json", "w")
        file_out_ff = open("./static/graphFile-FamFriends.json", "w")
        file_out_weak = open("./static/graphFile-Weak.json", "w")

	# setup the output files for each of the graph types
	for line in file_in:

		# parse the csv line so we can test the stength of the link
		source, edge_type, target = line.split(",")

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
        file_in = open("./data/spo-tool-data.csv", "r")

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

if __name__ == '__main__':
	create_json_graph_file()
