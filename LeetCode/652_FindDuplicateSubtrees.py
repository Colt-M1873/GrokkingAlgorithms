# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # return [root]
        # 哈希表记录每一个节点
        # 发现相同节点再开始对比子树
        d={}
        # rec dfs?
        def compare(t1,t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            if t1.val==t2.val:
                return compare(t1.left,t2.left) and compare(t1.right,t2.right)
            else:
                return False
        # print(compare(root,root))
        # print(compare(root.left,root.right.left))
        # ret=[root]

        # basic recursive dfs traversal
        def recDSFtrav(root):
            if not root: return []
            return recDSFtrav(root.left)+[root.val]+recDSFtrav(root.right)
        # print(recDSFtrav(root))
        
        # recursive DFS traversal using nonlocal array
        ret=[]
        def recDSFtravNonlocal(root):
            if not root: return
            nonlocal ret
            recDSFtravNonlocal(root.left)
            ret.append(root.val)
            recDSFtravNonlocal(root.right)
            return
        # recDSFtravNonlocal(root)
        # print(ret)



        # 比较两个节点的子树是否相等，如果相等返回true和节点子树上的所有节点构成的list
        def compareAndRet(t1,t2):
            if not t1 and not t2:
                return True, []
            elif not t1 or not t2:
                return False, []
            if t1.val==t2.val:
                ret=[t1]
                leftSame,leftRet = compareAndRet(t1.left,t2.left)
                rightSame,rightRet = compareAndRet(t1.right,t2.right)
                return leftSame and rightSame, leftRet+ret+rightRet
            else:
                return False, []
        # return compareAndRet(root.left,root.right.left)[1]

        # # v-1 错在出现重复
        # def recDFS(curr):
        #     if not curr: return []
        #     nonlocal d
        #     ret=[]
        #     # 两种比较，第一种是比较value是否相等，value不相等那子树肯定不一样
        #     # 第二种是相等的value可能对应很多种子树，比如题目种的例子3，值为2的节点有三个，其中两个是相等的，所以要把每一种可能子树对应的节点都存起来，都比较过，才能看是否有相等
        #     # 两层判定，第一层是d中有没有当前节点的value,如果没有，就表明当前是一个新节点，加入到d中
        #     if curr.val not in d:
        #         d[curr.val]=[curr]
        #         return recDFS(curr.left)+ret+recDFS(curr.right)
        #     else:
        #         # 如果当前节点的value在d中能查到，d中有与curr值相等的节点，则进入下一层判定：
        #         # 这些值相等的节点，他们的子树是否与curr的子树相等
        #         for node in d[curr.val]:
        #             same,currRet=compareAndRet(node,curr)
        #             if same: # 如果有任意一个相等，表明在d中已经存储了相同子树对应的节点，直接把这个节点对应的所有子节点的list返回
        #                 ret+=currRet
        #                 return ret
        #         # 如果没有return，能执行到下面这一行，就表明d中虽然有与curr值相等的节点，但没有与curr子树相等的节点，这时候就要把curr加入到d中
        #         d[curr.val]+=[curr]
        #         return recDFS(curr.left)+ret+recDFS(curr.right)
        # return set(recDFS(root)) # 为什么此处的set也不能解决重复问题呢

        def nodeInNodelist(node,nodelist):
            for n in nodelist:
                if compare(node,n):
                    return True
            return False

        # v-2 错在超时
        seen=set()
        def recDFS(curr):
            if not curr: return []
            nonlocal d,seen
            ret=[]
            # 两种比较，第一种是比较value是否相等，value不相等那子树肯定不一样
            # 第二种是相等的value可能对应很多种子树，比如题目种的例子3，值为2的节点有三个，其中两个是相等的，所以要把每一种可能子树对应的节点都存起来，都比较过，才能看是否有相等
            # 两层判定，第一层是d中有没有当前节点的value,如果没有，就表明当前是一个新节点，加入到d中
            if curr.val not in d:
                d[curr.val]=[curr]
                return recDFS(curr.left)+ret+recDFS(curr.right)
            else:
                # 如果当前节点的value在d中能查到，d中有与curr值相等的节点，则进入下一层判定：
                # 这些值相等的节点，他们的子树是否与curr的子树相等
                for node in d[curr.val]:
                    same,currRet=compareAndRet(node,curr)
                    if same: # 如果有任意一个相等，表明在d中已经存储了相同子树对应的节点，直接把这个节点对应的所有子节点的list返回
                        for n in currRet:
                            if not nodeInNodelist(n,seen):
                                ret+=[n]
                                seen.add(n)
                        return ret
                # 如果没有return，能执行到下面这一行，就表明d中虽然有与curr值相等的节点，但没有与curr子树相等的节点，这时候就要把curr加入到d中
                d[curr.val]+=[curr]
                return recDFS(curr.left)+ret+recDFS(curr.right)
        ret = recDFS(root)
        # for r in ret:
        #     print(r)

        # print(compareAndRet(ret[0],ret[2]))
        return ret



# v1 copied https://leetcode.com/problems/find-duplicate-subtrees/discuss/106020/Python-easy-understand-solution
def findDuplicateSubtrees(self, root):
        def trv(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]

# v2 copied https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis
def findDuplicateSubtrees(self, root):
    def tuplify(root):
        if root:
            tuple = root.val, tuplify(root.left), tuplify(root.right)
            trees[tuple].append(root)
            return tuple
    trees = collections.defaultdict(list)
    tuplify(root)
    return [roots[0] for roots in trees.values() if roots[1:]]

def findDuplicateSubtrees(self, root, heights=[]):
    def getid(root):
        if root:
            id = treeid[root.val, getid(root.left), getid(root.right)]
            trees[id].append(root)
            return id
    trees = collections.defaultdict(list)
    treeid = collections.defaultdict()
    treeid.default_factory = treeid.__len__
    getid(root)
    return [roots[0] for roots in trees.values() if roots[1:]]