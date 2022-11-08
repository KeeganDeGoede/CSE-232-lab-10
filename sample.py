n = 60 # number of nodes
B = nx.Graph() # initialize graph

## initialize empty edge lists
edge_list_complete_1 = [] 
edge_list_complete_2 = []
edge_list_path = []

## generate node lists
node_list_complete_1 = np.arange(int(n/3))
node_list_complete_2 = np.arange(int(2*n/3),n)
node_list_path = np.arange(int(n/3)-1,int(2*n/3))

## generate edge sets for barbell graph
for u in node_list_complete_1:
    for v in np.arange(u+1,int(n/3)):
        edge_list_complete_1.append((u,v))
        
for u in node_list_complete_2:
    for v in np.arange(u+1,n):
        edge_list_complete_2.append((u,v))

for u in node_list_path:
    edge_list_path.append((u,u+1))

# G.remove_edges_from([(3,0),(5,7),(0,7),(3,5)])

## add edges
B.add_edges_from(edge_list_complete_1)
B.add_edges_from(edge_list_complete_2)
B.add_edges_from(edge_list_path)


## draw graph
pos=nx.spring_layout(B) # positions for all nodes

### nodes
nx.draw_networkx_nodes(B,pos,
                       nodelist=list(node_list_complete_1),
                       node_color='c',
                       node_size=400,
                       alpha=0.8)
nx.draw_networkx_nodes(B,pos,
                       nodelist=list(node_list_path),
                       node_color='g',
                       node_size=200,
                       alpha=0.8)
nx.draw_networkx_nodes(B,pos,
                       nodelist=list(node_list_complete_2),
                       node_color='b',
                       node_size=400,
                       alpha=0.8)


### edges
nx.draw_networkx_edges(B,pos,
                       edgelist=edge_list_complete_1,
                       width=2,alpha=0.5,edge_color='c')
nx.draw_networkx_edges(B,pos,
                       edgelist=edge_list_path,
                       width=3,alpha=0.5,edge_color='g')
nx.draw_networkx_edges(B,pos,
                       edgelist=edge_list_complete_2,
                       width=2,alpha=0.5,edge_color='b')


plt.axis('off')
plt.show() # display
