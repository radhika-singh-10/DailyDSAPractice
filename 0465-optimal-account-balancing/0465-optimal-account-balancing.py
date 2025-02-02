from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        #goldmann sachs oa
        #apporach
        #make a dictionary of to, from and value is amount(+,-)
        #remove zero balance account transaction
        #apply greedy, backtracking for settlement
        transaction_dict=defaultdict(int)
        for from_per,to_per,amount in transactions:
            transaction_dict[from_per]-=amount
            transaction_dict[to_per]+=amount
        net_transaction=[trans for trans in transaction_dict.values() if trans!=0]
        n=len(net_transaction)
        def settle_debt(i):
            while i<n and net_transaction[i]==0:
                i+=1
            if i==n:
                return 0
            min_transaction=float('inf')
            for j in range(i+1,n):
                if net_transaction[i]*net_transaction[j]<0:
                    net_transaction[j]+=net_transaction[i]
                    min_transaction=min(min_transaction,1+settle_debt(i+1))
                    net_transaction[j]-=net_transaction[i]
            return min_transaction




        res=settle_debt(0)
        return res if res!=float('inf') else 0


        