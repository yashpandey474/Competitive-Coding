class Solution(object):
    def canFinish(self, numCourses, prereq):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course_to_prereq = {}
        indegrees = [0]*numCourses

        #FORM THE MAP OF EDGES
        for i in prereq:
            if i[1] in course_to_prereq:
                course_to_prereq[i[1]].append(i[0])
            else:
                course_to_prereq[i[1]] = [i[0],]
            #CALCULATE INDEGREES
            indegrees[i[0]]+=1

        

        #TOPOLOGICAL SORT USING KAHN'S ALGORITHM
        queue = []
        #ADD ALL NODES WITH INDEGREE == 0
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
            
        while queue:
            #POP FROM QUEUE
            current = queue.pop(0)

            #REDUCE INDEGREE OF ALL NEIGHBORS
            if current in course_to_prereq:
                for i in course_to_prereq[current]:
                    indegrees[i] -= 1
                    #ADD TO QUEUE IF INDEGREE == 0
                    if indegrees[i] == 0:
                        queue.append(i)

        #CHECK IF ALL HAVE INDEGREE REDUCED TO 0
        for i in range(numCourses):
            if indegrees[i] != 0:
                return False
        return True

        





                
    
        

            
