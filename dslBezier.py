import numpy as np
import matplotlib.pyplot as plt 
from enum import Enum
from skimage.draw import line_aa, bezier_curve

class Direction(Enum):
    N = 0   #0,1   #-1,0
    NE = 1  #1,1   #-1,1
    E = 2   #1,0   #0,1
    SE = 3  #1,-1  #1,1
    S = 4   #0,-1  #1,0
    SW = 5  #-1,-1 #1,-1
    W = 6   #-1,0  #0,-1
    NW = 7  #-1,1 #-1,-1

class Length(Enum) : 
    short = 5 
    medium = 10
    long = 15

class Radius(Enum) : 
    low = 3 
    medium = 5
    high = 8

class Orient(Enum) : 
    right = 0
    left = 1

class DslBezier : 

    def __init__(self) : 
    
        self.canvas = np.zeros((28,28))
        self.position = np.array([5,5])                
        self.done = False        

        #discrete direction changes according to direction enum 
        self.cycle = np.array([[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]])
        
        #self.Direction_list = list(Direction.__members__)
        #self.Length_list = list(Length.__members__)
        #self.Radius_list = list(Radius.__members__)
        #self.Orient_list = list(Orient.__members__)

        self.Direction_list = [l.value for l in Direction]
        self.Length_list = [l.value for l in Length]
        self.Radius_list = [l.value for l in Radius]
        self.Orient_list = [l.value for l in Orient]


    def _reset(self) : 

        self.canvas = np.zeros((28,28))
        self.done = False

    def __cut(self, rr, cc) : 
        '''
        Cut out overlay
        '''
        
        xs, ys = [], []
        for i in range(len(rr)) : 
            if rr[i] >= 0 and rr[i] <28 :
                if cc[i] >= 0 and cc[i] <28 : 
                    xs.append(rr[i])
                    ys.append(cc[i])

        return xs, ys

    def __check(self) : 

        if self.position[0] < 0 or self.position[0] >27 : 
            if self.position[1] < 0 or self.position[1] > 27 : 
                self.done

    def position_pen(self, x, y): 
        """
        reposition anywhere in discrete quarter
        random position within quarter
        input: (4,4)  
        """

        #a = np.random.randint(7*y, 7*(y+1))
        #b = np.random.randint(7*x, 7*(x+1))
        
        a = 7*y+3
        b = 7*x+3

        self.position = np.array([b,a])
        
        #TODO complete phrase
        phrase = 'reposition you pen '


    def straight_line(self, direction, length) : 
        """
        Draw a straight line of length l in a discrete direction 
        (N, S, W, E, NE, NW, SE, SW)
        the command direction is 0-7        
        Then direction is changed by random amount
        length up to 3/4 iterations?
        inputs: direction 0-7
        length: 0-1
        """

        #TODO add check of out of canvas

        #obtain direction in numpy basic lin vector
        diff = length.value*self.cycle[direction.value]
        target = self.position + diff

        #obtain middle point
        middle = (self.position + target)/2
        middle = middle.astype(np.int32)

        '''
        #add random factor to middle and target point 
        ran = np.random.randint(-2,2, size=(2,2))
        target += ran[0]
        middle += ran[1]
        '''

        rr, cc = bezier_curve(self.position[0],self.position[1], middle[0], middle[1], target[0], target[1] ,3)
        xs, ys = self.__cut(rr, cc)
        self.canvas[xs, ys] = 1
        
        #update pen position
        self.position = target 

        #TODO complete phrase
        phrase = 'draw a straight line'


    def curve(self, direction, orient, length, radius) : 
        """
        Draw a curve 
        direction: gradient 
        inputs: orientation 0 left, 1 right
        radius: 0-2 strong, medium, light 
        full: 0-1 equivalent to iterations
        """
       

        diff = length.value*self.cycle[direction.value]
        target = self.position + diff
        
        middle = (self.position + target)/2
        middle = middle.astype(np.int32)

        if orient.value == 0 :
            dist = self.cycle[direction.value - 2]
        else : 
            dist = self.cycle[(direction.value + 2) % 8]  #hard-coded

        middle += radius.value*dist
        middle = middle.astype(np.int32)

        '''
        #add random
        ran = np.random.randint(-2,2, size=(2,2))
        target += ran[0]
        middle += ran[1]
        '''

        rr, cc = bezier_curve(self.position[0],self.position[1], middle[0], middle[1], target[0], target[1] ,3)

        xs, ys = self.__cut(rr,cc)
        self.canvas[xs,ys] = 1

        #update pen position
        self.position = target 

        #TODO insert value in string
        phrase = 'draw a curve'

    def _simulate(self, feat) : 
        """
        Convert feature to program execution 
        """
                
        #[0,0,0,0,0]  #no instruction
        #[1,3,3,0,0]  position   #should be restricted to start???
        #[2,7,2,0,0]  straight line
        #[3,7,1,2,2] curve

        instructions = np.split(feat, int(len(feat)/5))
        instructions = np.array(instructions)

        #overwrite instructions to initialize program with reposition
        instructions[:,0][0] = 0.25

        first = True
        for inst in instructions : 
            #if first : 
            #    inst[0] = 0.25
            #    first = False
            if np.round(4*inst[0]) == 0 : 
                pass 
            elif np.round(4*inst[0]) == 1 : 
                ref = [1,3,3,0,0]
                norm = inst*ref
                norm = np.round(norm)
                self.position_pen(int(norm[1]),int(norm[2]))
                #print('position')
            elif np.round(4*inst[0]) == 2 : 
                ref = [2,7,2,0,0]
                norm = inst*ref
                norm = np.round(norm)                
                self.straight_line(Direction(self.Direction_list[int(norm[1])]), Length(self.Length_list[int(norm[2])]))                
                #print('straight')
            elif np.round(4*inst[0]) == 3 : 
                ref = [3,7,1,2,2]
                norm = inst*ref
                norm = np.round(norm)
                self.curve(Direction(self.Direction_list[int(norm[1])]), Orient(self.Orient_list[int(norm[2])]), Length(self.Length_list[int(norm[3])]), Radius(self.Radius_list[int(norm[4])]))
                #print('curve')

    def _convert(self, feat) : 
        """
        Convert feature vector to program 
        """

        #[0,0,0,0,0]  #no instruction
        #[1,3,3,0,0]  position   #should be restricted to start???
        #[2,7,2,0,0]  straight line
        #[3,7,1,2,2] curve

        lines = []

        lines.append('d = DslBezier()')
        lines.append('')

        instructions = np.split(feat, int(len(feat)/5))
        instructions = np.array(instructions)

        #overwrite instructions to initialize program with reposition
        instructions[:,0][0] = 0.25

        #print(instructions)
        #print(len(instructions))

        #Filter double reposition instructions
        a = np.round(4*instructions[:,0])
        #print(4*instructions[:,0])
        #print(a)
        res = [a[i] == 1 and a[i] == a[i+1] for i in range(len(a)-1)]
        #print(res)
        res.insert(-1, False)
        instructions = instructions[np.where(np.array(res)==False)]
    
        #print(len(instructions))
        #print(instructions)

        #first = True
        for inst in instructions : 
            #if first : 
            #    inst[0] = 0.25
            #    first = False

            #print(4*inst[0])

            if np.round(4*inst[0]) == 0 : 
                pass 
            elif np.round(4*inst[0]) == 1 : 
                ref = [1,3,3,0,0]
                norm = inst*ref
                norm = np.round(norm)
                #self.position_pen(int(norm[1]),int(norm[2]))
                lines.append(f'd.position_pen({int(norm[1])},{int(norm[2])})')
                #print('__position')
            elif np.round(4*inst[0]) == 2 : 
                ref = [2,7,2,0,0]
                norm = inst*ref
                norm = np.round(norm)                
                #self.straight_line(Direction(self.Direction_list[int(norm[1])]), Length(self.Length_list[int(norm[2])]))                
                lines.append(f'd.straight_line(Direction.{Direction(self.Direction_list[int(norm[1])]).name}, Length.{Length(self.Length_list[int(norm[2])]).name})')
                #print('__straight')
            elif np.round(4*inst[0]) == 3 : 
                ref = [3,7,1,2,2]
                norm = inst*ref
                norm = np.round(norm)
                #self.curve(Direction(self.Direction_list[int(norm[1])]), Orient(self.Orient_list[int(norm[2])]), Length(self.Length_list[int(norm[3])]), Radius(self.Radius_list[int(norm[4])]))
                lines.append(f'd.curve(Direction.{Direction(self.Direction_list[int(norm[1])]).name}, Orient.{Orient(self.Orient_list[int(norm[2])]).name}, Length.{Length(self.Length_list[int(norm[3])]).name}, Radius.{Radius(self.Radius_list[int(norm[4])]).name})')
                #print('__curve')

        lines.append('')
        lines.append('d.end()')

        return lines

    def visualize(self) : 
        plt.imshow(self.canvas, cmap = 'bone')
        plt.show()

    def _save(self, name) : 
        #np.save(f'./imgs/{name}' ,self.canvas)
        plt.imshow(self.canvas, cmap = 'bone')
        plt.savefig(f'./imgs_quickDraw/{name}.png')
        plt.close()

    def _saveProgram(self, lines, name) : 
    
        with open(f'./imgs_quickDraw/{name}.py', 'w') as f : 
            #f.writelines(lines)
            for line in lines : 
                f.write(line+'\n')


#x, y order !!

'''
d = DslBezier() 
d.position_pen(0,0)

d.straight_line(Direction.S, Length.short)

d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)  #distance, rad
d.curve(Direction.S, Orient.left, Length.short, Radius.low)  #distance, rad
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)  #distance, rad
'''

'''
d = DslBezier() 

for i in range(100) :     
    d._reset()
    feat = np.random.rand(5*4)
    d._simulate(feat)
    lines = d._convert(feat)
    #d._saveProgram(lines, )
    d._save(i)
'''

#d.visualize()
