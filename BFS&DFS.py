# Original question in <Gorkking Algorithm> Chapter6 Page85

graph = {}
graph['you0']=['alice1','bob1','claire1']
graph['ghdd4']=['ihb5']
graph['claire1']=['jonny2','thom2']
graph['anuj2']=['bz3','alif3','peggy2']
graph['peggy2']=['zd3','ewfa3']
graph['jonny2']=['zhbfhdb3','ljfas3']
graph['thom2']=['ds3','ewad3','trdsg3','etrg3']
graph['zd3']=['ghdd4','dsfwe4']
graph['bob1'] =['anuj2','peggy2']
graph['alice1'] =['peggy2'] 
graph['etrg3']=['oiuh4']

# def BFS_wrong(graph:dict):
#     # 这一版相当于简单遍历，并不是广度优先搜索，错得很离谱，甚至没有用到图论
#     queue=[] # a list being accessed only with head and tail can be seen as a queue
#     searched=set()
#     for item in graph:
#         if item not in searched:
#             ##
#             queue.append(item)
#             print(queue)
#             if queue[0]=='ihb5':
#                 return 'target found'
#             else:
#                 searched.add(queue[0])
#                 queue.pop(0)
#             ##
#             # 以上这一段代码等价于
#             # if item == 'thom':
#             #     return 'thom found'
#             # else:
#             #     searched.add(item)
#             # 队列并没有用上，依然相当于一个一个在查找
#         for subitem in graph[item]:
#             if subitem not in searched:     

#                 queue.append(subitem)
#                 print(queue)
#                 if queue[0]=='ihb5':
#                     return 'target found'
#                 else:
#                     searched.add(queue[0])
#                     queue.pop(0)
#                     # print(searched)
# BFS_wrong(graph) 
               
def BFS(graph:dict,initnode):
    # using queue to perform BFS
    queue=[]
    queue.append(initnode)
    seen=set()
    seen.add(initnode)
    while len(queue)>0:
        print(queue[0])
        vertex=queue.pop(0)
        if vertex in graph.keys():
            node=graph[vertex]
            for item in node:
                if item not in seen:
                    queue.append(item)
                    seen.add(item)

# 整个过程利用了队列，从初始的节点（或者说根节点开始），先把根节点添加到队列，
# 检查根节点（在这个程序里表现为print()）并弹出，然后将与根节点相连的一级子节点添加到队列，
# 然后检查第一个一级子节点，并弹出，然后将与第一个一级子节点相连的二级子节点添加到队列，
# 然后检车第二个以及子节点并弹出，然后将与第二个一级子节点相连的二级子节点添加到队列，
# 直到一级子节点检查完毕并全部弹出，
# 再从第一个二级子节点开始检查并弹出并添加与第一个二级子节点相连的三级子节点
# 因此队列中从前往后就一直保持着由n级子节到n+1级子节点的顺序
            
BFS(graph,'you0')

print('-'*100)

def DFS(graph:dict,initnode):
    # using stack to perform DFS
    stack=[]
    seen=set()
    stack.append(initnode)
    seen.add(initnode)
    while len(stack)>0:
        print(stack[-1])
        vertex=stack.pop(-1)
        if vertex in graph.keys():
            nodes=graph[vertex]
            for item in nodes:
                if item not in seen:
                    stack.append(item)
                    seen.add(item)

DFS(graph,'you0')


