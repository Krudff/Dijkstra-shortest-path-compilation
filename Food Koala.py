#using a modified priority queue from week 10 (I think?)
class prioqueue:
    def __init__(self):
    #I want to start root at index 1
        self.arr = [None]
        self.size = 0
    def left_child(self,idx):
    #returns index of left child
        return idx*2
    def right_child(self,idx):
    #returns index of right child
        return idx*2+1
    def parent(self,idx):
    #returns index of parent
        return idx//2
    def swap_nodes(self,a,b):
    #swaps the value of both indexes
        self.arr[a],self.arr[b]=self.arr[b],self.arr[a]

    def bob_down(self,idx):
    #bob down the selected idx if big
    #we want min at top
        left_idx=self.left_child(idx)#index of left child
        right_idx=self.right_child(idx)#index of right child
        if(left_idx>self.size):#if left child doesnt exist, then right doesnt exist too. just go home
            return
        elif(right_idx>self.size):#if right child doesn't exist, neither does left child's children, but go left
            left_val = self.arr[left_idx][1]#value of left child
            current_val = self.arr[idx][1]#value of current
            if(left_val<current_val):
                self.swap_nodes(left_idx,idx)
        else:#if both exists
            left_val = self.arr[left_idx][1]#value of left; number of monsters
            right_val = self.arr[right_idx][1]#value of right; number of monsters
            current_val = self.arr[idx][1]#value of child; number of monsters
            if(right_val < left_val):#if right is less than left, then evaluate if right is also less than current
                if(right_val < current_val):#if right is less, swap then repeat
                    self.swap_nodes(right_idx,idx)
                    self.bob_down(right_idx)
            else:#if either works, then evaluate if left is less than current
                if(left_val < current_val):#if left is less, swap then repeat
                    self.swap_nodes(left_idx,idx)
                    self.bob_down(left_idx)
    def bob_up(self,idx):
    #bob up the selected idx if smol
    #we want min at top
        parent_idx = self.parent(idx)#index of parent
        parent_val = self.arr[parent_idx][1]#value of parent
        current_val = self.arr[idx][1]#value of current index
        if(idx == 1):#if index is the root, then no parent
            return
        if(current_val < parent_val):#if smaller than parent
            self.swap_nodes(parent_idx,idx)#then swap
            
            if(parent_idx > 1):#if current val is not root
                self.bob_up(parent_idx)#bob up more
    def insert(self,val):
    #inserting elements
        self.size+=1#increment size
        idx=self.size#inserted element is last
        self.arr.append(val)#append tuple to end of array      
        if(idx>1):#if not root
            self.bob_up(idx)
    def get(self):
    #get the minimum, which is prolly on top
        self.swap_nodes(1,self.size)#swap with last node first
        result = self.arr.pop()#then store that last node on var and remove
        self.size-=1#then decrease size
        if(self.size>0):#if queue is not empty
            self.bob_down(1)#then bob down the first element
        return result#then return result


H,S,R,U = input().split()
H=int(H)
S=int(S)
R=int(R)
U=int(U)
#H is number of houses
#S is number of streets
#R is start node
#U is end node
world_map=[None]
visited = [None]+[0 for j in range(H)]#mark all houses as unvisited
for house in range(H):#populating world map with houses
    world_map.append([None]+[1001 for j in range(H)])

for j in range(S):
    house1,house2,time,orientation=input().split()
    house1=int(house1)
    house2=int(house2)
    time=int(time)
    orientation=int(orientation)
    #declaring variables
    world_map[house1][house2]=time
    #put path from house 1 to 2
    if(orientation>1):#if two way, then put path from house 2 to 1
        world_map[house2][house1]=time
#now we go search
pq=prioqueue()
visited[R]=1#declaring start node as visited
world_map[R][R]=0#declaring that start node takes time zero from itself
pq.insert((R,0,[R]))#inserting start node to priority queue; from node, time it takes, then the path
while(pq.size>0):#while not empty
    current = pq.get()
    node=current[0]
    time=current[1]
    path=current[2]
    visited[node]=1#marking as visited
    minimap=world_map[node]#creates a minimap from world map for easier navigation
    if(node==U):
        for something in path:
            print(something,end=" ")
        print()
        print(time)
        break
    for neighbor in range(1,H+1):#check distance to every house cuz u nub!
        if(visited[neighbor]==0):#if you realized haven't visited a house yet
            if(minimap[neighbor]<1001):#if you think it doesn't take 1001 minutes to take there (lul)
                pq.insert((neighbor,time+minimap[neighbor],path+[neighbor]))
        
    