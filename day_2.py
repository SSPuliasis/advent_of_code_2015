#Part 1
class box:
    def __init__ (self, l, w, h):
        self.l = l
        self.w = w
        self.h = h
        
        lxw = self.l * self.w
        lxh = self.l * self.h
        wxh = self.w * self.h
        self.smallest_side = min(lxw, lxh, wxh)
        
    def wrapping_paper(self):
        self.paper_amount = 2*(self.l*self.w + self.l*self.h + self.w*self.h) + self.smallest_side
        #print('wrapping paper needed: ', self.paper_amount)
        
total_amount_of_wrapping_paper = 0
with open('day2_input.txt') as inputfile:
    for line in inputfile:
        l = int(line.split('x')[0])
        w = int(line.split('x')[1])
        h = line.split('x')[2]
        h = h.replace('\n', '')
        h = int(h)
        single_box = box(l, w, h)
        single_box.wrapping_paper()
        total_amount_of_wrapping_paper += single_box.paper_amount
print('wrapping paper: ', total_amount_of_wrapping_paper)
