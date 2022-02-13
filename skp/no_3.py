import heapq

class Friend:
    def __init__(self, email):
        self.email = email
        self.friends = []

    def add_friendship(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def dfs(self, friend, visit_queue):
        stack = [self]
        while stack:
            j = stack.pop()
            if self not in visit_queue:
                heapq.heappush(self, visit_queue)
                
        heapq.heappop(self, visit_queue)

    def can_be_connected(self, friend):
        visit_queue = [self]
        is_friend = False

        print(visit_queue)
        def dfs(self, friend, visit_queue, is_friend):
            stack = [self]
            while stack:
                j = stack.pop()
                if j not in visit_queue:
                    heapq.heappush(j, visit_queue)
                for fr in range(len(j.friends)):
                    if fr == friend:
                        is_friend = True
                    dfs(j,friend,visit_queue, is_friend)


        heapq.heapify(visit_queue)

        # print(self.friends)
        return is_friend
    

if __name__ == "__main__":
    a = Friend("A")
    b = Friend("B")
    c = Friend("C")
    
    a.add_friendship(b)
    b.add_friendship(c)

    a.can_be_connected(c)
    
    # print (a.can_be_connected(c))