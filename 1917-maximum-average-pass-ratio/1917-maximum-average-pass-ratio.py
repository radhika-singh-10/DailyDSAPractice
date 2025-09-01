import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #edge cases-> 
        #1. total no of students == pass students -> no assignment to them as ratio remains the same
        #2. total no of students == fail students -> assign all the brilliant students to that class as the ratio will increase
        #3. if ratio of a few classes same then assign the students equally int(students/classes)
        #4. can total==0 or pass==0? no 
        #5. extrastudents==0? no
        #approach -> 
        #for each class, store the ratio = pass/total, assign the students to the lowest ratio and then compare with max(prev_ratio,new_ratio) 
        #sort in increasing order(max heap)
        #get min ratio of pass and add students there -> first index by focusing on the increase in the gain ratio
        #gain ratio wpuld decrease once we increase the no of pass students/ total students

        #tc- 0(n+logn.n), sc=0(n)

        def calculateGainRatio(passStudents, totalStudents):
            return (passStudents+1)/(totalStudents+1) - (passStudents)/(totalStudents)
        mod=10^-5
        ratios,res,n=[],0.0,len(classes)
        for i in range(n):
            gainRatio = calculateGainRatio(classes[i][0],classes[i][1])
            ratios.append((-gainRatio,classes[i][0],classes[i][1]))
        heapq.heapify(ratios)
        for _ in range(extraStudents):
            currentGain,passStudents,totalStudents=heapq.heappop(ratios)
            heapq.heappush(ratios,(-calculateGainRatio(passStudents+1,totalStudents+1),passStudents+1,totalStudents+1))
        totalRatio=sum(passes/totalStudents for _,passes,totalStudents in ratios)
        return totalRatio/len(classes)

            


