class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #approach

        #transaction_history[name]=[time,place]
        #if amt>1000: add info to invalid_transaction
        #check for name -> for 2 diff city exist, and time is less than 60

        invalid = []
        
        for i, t1 in enumerate(transactions):
            name1, time1, amount1, city1 = t1.split(',')
            if int(amount1) > 1000:
                invalid.append(t1)
                continue
            for j, t2 in enumerate(transactions):
                if i != j: 
                    name2, time2, amount2, city2 = t2.split(',')
                    if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
                        invalid.append(t1)
                        break
        
        return invalid


        # invalid_transaction,transaction_hist=[],collections.defaultdict(lambda:["",0,0])
        # for info in transactions:
        #     name,time,amount,city=info.split(",")
        #     if int(amount)>1000:
        #         invalid_transaction.append(info)
        #         continue
        #     for other_info in transactions:
        #         other_name,other_time,other_amount,other_city=other_info.split(",")
        #         if info!=other_info and name==other_name and city!=other_city and abs(int(time)-int(other_time))<=60:

        #             invalid_transaction.append(other_info)
        #             break

        # return invalid_transaction


        #<1000 or |ti-ti+1|<=60 and ni==ni+1 and ci!=ci+1
        #if n==1->check for amount only 
        #maintain a dictionary and check for exisiting name if the second condition match then invalid addition
    #     if not transactions:
    #         return []

    #     n=len(transactions)
        
    #     if n==1:
    #         name,time,amount,place=transactions[i].split(",")
    #         if int(amount)>1000:
    #             return [transactions[0]]
    #         else:
    #             return []
        
    #     res=[]
    #     transaction_dict = defaultdict(list)
    #     for i,transaction in enumerate (transactions):
    #         name, time, amount, city = (int(i) if i.isnumeric() else i for i in transaction.split(','))
    #         if amount > 1000:                   
    #             res.append(transaction)               
                 
    #         if name in transaction_dict:                    
    #             for t in transaction_dict[name]:         
    #                 _, prev_time, _, prev_city =(int(i) if i.isnumeric() else i for i in  t.split(','))
    #                 if abs(time-prev_time) <= 60 and prev_city != city:  
    #                     res.append(t) 
    #                     res.append(transaction)                    
            
    #         transaction_dict[name].append(transaction)
    #     return res

    #     out = [] #list of all the invalid transactions to return 
    # names = defaultdict(lambda: defaultdict(set)) #{name: {time: city}}
    
    
    # for t in transactions:
    #     name,time,amount,city = t.split(",")
    #     names[name][time].add(city)
        
    # #-if a certain person is at more than one city at a time then we know it's an invalid transaction
	# #-if the city we're at is not in the set it means the transaction has been made at two places within the 60 min limit
	
	# #I want to preface the rest of this solution by saying this has worked so far but I'm unsure if there's ever a testcase
	# #in which this would not function correctly. This was a very tricky question and it definitely took me a while 
	# #to even come up with a working solution
    
    # for t in transactions:
    #     name, time, amount, city = t.split(",")
    #     if int(amount) > 1000:
    #         out.append(t)            
    #     else:
    #         for num in names[name].keys():
    #             if -60 <= int(time) - int(num) <= 60 and (len(names[name][num]) > 1 or city not in names[name][num]):
    #                 out.append(t)
    #                 break
            
    #     return out

