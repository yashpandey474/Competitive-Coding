
class Solution:
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [1]*len(accounts)
        
        def find(x1):
            while x1 != parent[x1]:
                parent[x1] = parent[parent[x1]]
                x1 = parent[x1]
            return x1
        #UNION-FIND PROBLEM
        def union(x1, x2):
            parent1, parent2 = find(x1), find(x2)

            if parent1 == parent2:
                return False

            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]

            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True


        #HASH MAP FOR EMAILS
        map_emails = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in map_emails:
                    union(map_emails[email], i)

                else:
                    map_emails[email] = i


        #CREATE GROUPS
        emailGroup = defaultdict(list)

        for email, index in map_emails.items():
            leader = find(index)
            emailGroup[leader].append(email)

        #RESULT
        res = []
        for index, emails in emailGroup.items():
            name = accounts[index][0]
            res.append([name] + sorted(emailGroup[index]))

        return res

                
