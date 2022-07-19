from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.end = list()
        self.next = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s, idx):
        cur = self.root
        for c in s:
            cur = cur.next[c]
        cur.end.append(idx)

    def search(self, prefix):
        """ 搜索 prefix 为前缀的单词数量 """
        p = self.root
        for c in prefix:
            if c in p.next:
                p = p.next[c]
            else:
                return set()
        return self.dfs(p, set())

    def dfs(self, root, ans):
        """ 对字典树结点进行深度优先搜索 """
        for idx in root.end:
            ans.add(idx)
        for c, node in root.next.items():
            self.dfs(node, ans)
        return ans


class WordFilter:

    def __init__(self, words):
        self.pref, self.suff = Trie(), Trie()
        for idx, w in enumerate(words):
            self.pref.add(w, idx)
            self.suff.add(reversed(w), idx)

    def f(self, pref: str, suff: str) -> int:
        p = self.pref.search(pref)
        s = self.suff.search(reversed(suff))
        ans = p & s
        if ans:
            return max(ans)
        return -1


# 作者：meteordream
# 链接：https: // leetcode.cn / problems / prefix - and -suffix - search / solution / by - meteordream - awo2 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。