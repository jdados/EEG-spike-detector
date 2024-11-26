class max_heap:
    def __init__(self):
        self.data = []

    def heapify_up(self, i):
        while i > 0:
            p = (i - 1)//2
            # Order the heap based on amplitude, not time
            if self.data[i][1] > self.data[p][1]:
                t = self.data[i]
                self.data[i] = self.data[p]
                self.data[p] = t
                i = p
            else:
                break

    def heapify_down(self,i):
        lc = 2*i + 1
        rc = 2*i + 2
        max_val = i

        if lc < len(self.data) and self.data[lc][1] > self.data[max_val][1]:
            max_val = lc
        
        if rc < len(self.data) and self.data[rc][1] > self.data[max_val][1]:
            max_val = rc
        
        if max_val != i:
            t = self.data[i]
            self.data[i] = self.data[max_val]
            self.data[max_val] = t
            self.heapify_down(max_val)

    def insert_data_point(self, t, a):
        self.data.append((t,a))
        self.heapify_up(len(self.data) - 1)
    
    def extract_max(self):
        if len(self.data) == 0:
            return None
    
        t = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]
        self.data[len(self.data) - 1] = t
  
        max = self.data.pop()

        self.heapify_down(0)
        
        return max