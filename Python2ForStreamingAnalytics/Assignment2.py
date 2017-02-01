#Task 1 Install numpy/scipy/matplotlib
#Task 2 Install the library PIL
#Task 3 Install the library openCV
import scipy
import matplotlib
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import sys


#GREEN = "\033[92m"

#Task 4.1 Return to the future
mario_image = Image.open('mario.png')
iar = np.asarray(mario_image)
#print(iar)
#Task 4.2 Santa Claus Time

class Tree:
    def __init__ (self, leaves, trunk, root):
        self.leaves = leaves
        self.trunk = trunk
        self.root = root

    def get_leaves(self):
        return self.leaves

    def set_leaves(self, leaves):
        self.leaves = leaves

    def get_trunk(self):
        return self.trunk

    def set_trunk(self, trunk):
        self.trunk = trunk

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def __repr__(self):
        return "Tree:{} leaves:{} trunk:{} root:{}".format('tree', self.leaves, self.trunk,self.root)

mytree=Tree(5,2,1)
#print(mytree)

class ChristmasTree(Tree):
    def __init__(self, height, leaves, trunk, root):
        self.height = height
        #super(Tree, self).__init__(leaves, trunk, root)
        Tree.__init__(self,leaves, trunk, root)
    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height=height


    def __repr__(self):
        return "Christmas tree-> leaves:{}, Height:{}".format(self, self.leaves, self.height)

    def DisplayTree(self):
        z = self.height - 1
        x = 1
        line = ''
        for i in range(self.height):
            line = line + (' ' * z + self.leaves * x + ' ' * z + '\n')
            x+=2
            z-=1

       # print GREEN + line
        return line

ctree = ChristmasTree(7,'*',1,1)
ctree_image = ctree.DisplayTree()

# Square Tree
class SquareTree(Tree):
    def __init__(self, height, leaves, trunk, root):
        self.height = height
        Tree.__init__(self,leaves, trunk, root)
    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height=height


    def __repr__(self):
        return "Square tree-> leaves:{}, Height:{}".format(self, self.leaves, self.height)

    def DisplayTree(self):

        line = ''
        for i in range(self.height):
            line = line + (self.leaves * self.root + '\n')


       # print GREEN + line
        return line

stree = SquareTree(height=5,leaves='$',trunk=1,root=10)
stree_image = stree.DisplayTree()

# oval tree
class OvalTree(Tree):
    def __init__(self, height, leaves, trunk, root):
        self.height = height
        Tree.__init__(self,leaves, trunk, root)
    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height=height


    def __repr__(self):
        return "Oval tree-> leaves:{}, Height:{}".format(self, self.leaves, self.height)

    def DisplayTree(self):

        width, height = 11, 11
        a, b = 5, 5
        r = 5
        EPSILON = 2.2

        map_ = [[' ' for x in range(width)] for y in range(height)]

        for y in range(height):
            for x in range(width):
                if (x - a) ** 2 + (y - b) ** 2 <= (r ** 2 - EPSILON ** 2):
                    map_[y][x] = "#"
        for line in map_:
            print(' '.join(line))


#print(stree_image)
otree = OvalTree(height=5,leaves='#',trunk=1,root=10)
otree_image = otree.DisplayTree()
print(otree_image)
#print(ctree_image)
#print(stree_image)
#print(otree_image)
#4.3 mario likes trees
def draw_mario_tree(c_display, s_display):#, o_display):
    draw = ImageDraw.Draw(mario_image)
    font = ImageFont.truetype("arial.ttf", 50)
    draw.text((950, 0), c_display, (0,255,0), font=font)
    draw.text((1050, 300), s_display, (0, 255, 0), font=font)
    #draw.text((1150, 600), o_display, (0, 255, 0), font=font)
    mario_image.show()
    mario_image.save("modified_mario.jpg")

draw_mario_tree(ctree_image, stree_image)#, otree_image)


#how to make text into an image, image draw, imageFont, create new image object
#then draw this image, put stuff in empty file, save the tree we created
#into dtext, draw = imageDraw(img) draw.text(  )  image.save("name")
#create a function
#all the classes for trees in tree.py
#other file mario_trees.py (new file) has import stuff
#from tree import ctree...otree....stree
#xtree = ctree('*',10,1,10)
#dtext = xtree.displayTree (return, not just print)
# or you can append arrays to the mario array
#from array function, comes from class image, image.fromarray

#4.4 Thresholding
#np.mean, give it the array overall.mean = np.mean(mario)
#calc the mean for every pixel,

# for a in mario:
  #  for b in a:
   #     pixel-mean = np.mean(b)
   #     if ... >= :
   #         #create black pixel
      #  b[0] =0
      #  1
      ##  3
        #for loop to do this, change the transparency
#1. Create a list of pixel means

def list_of_means(iar):
    meanslist = []
    for i in iar:
        for b in i:
            meanslist.append(np.mean(b))
    return meanslist

def invert_colors(iar, threshold):
    iar.flags.writeable = True
    for outer_list in iar:
        for pixel in outer_list:
            #print pixel
            if np.mean(pixel) >= threshold:
                #white pixel
                #print pixel
                pixel[0] = 255
                pixel[1] = 255
                pixel[2] = 255
                pixel[3] = 255
            else:
                # black pixel
                #print pixel
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
                pixel[3] = 255
    return iar


def main():

    #list_of_means(iar)
    #2. Find the mean of pixel means
    threshold = np.mean(list_of_means(iar))
    print(threshold)

    data = invert_colors(iar, threshold)
    #data.print
    #print(data)
    img = Image.fromarray(data)
    img.save('inverted.png')
    img.show()


main()