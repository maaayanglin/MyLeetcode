# 执行用时 :112 ms, 在所有 Python3 提交中击败了89.20%的用户
# 内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.30%的用户

# 思路：先将words里的子串用字典类型d存储，key为子串本身，value为子串在words中出现的次数
#       因为子串组成的字符串长度是固定的，因此可以每次在s中取固定长度l的字符串，即滑动窗口的大小，滑动窗口每次滑动距离为单个子串的长度m
#       将滑动窗口中的字符串拆分成多个长度为m的子串并加入字典t中， key为子串本身，value为出现次数，
#       再通过对比t与d是否一致，若一致则记录字符串的开始下标
#       滑动窗口初始偏移量+1，继续上述过程，即代码中的for i in range(m)代表滑动窗口初始偏移量。


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n=len(words)
        if n==0:
            return []
        m=len(words[0])
        l=m*n
        ans=[]
        N=len(s)-l+1
        
        d=collections.defaultdict(int)
        for c in words:
            d[c]+=1
            
        for i in range(m):
            t=collections.defaultdict(int)
            for j in range(i,i+l,m):
                t[s[j:j+m]]+=1
            for j in range(i,N,m):
                if t==d:
                    ans+=[j]
                t[s[j:j+m]]-=1
                if t[s[j:j+m]]==0:
                    t.pop(s[j:j+m])
                t[s[j+l:j+l+m]]+=1            
        return ans

