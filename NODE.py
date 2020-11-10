
'''
Created on 2020年10月24日
保存节点的相关数据
@author: dingxinlong
'''
class Node():
    def __init__(self):
        self.index=0  #节点的序号，作为节点的唯一标识
        self.parentIndex=0 #节点父亲的序号
        self.zeroIndex=0  #0号的位置
        self.list=[]  #该节点的8数码（type=list)
        self.fund=0 #该节点的估计值
        self.depth=0 #该节点的深度
        self.direction=0  #该节点有父亲节点如何移动得到 -3（0向上移），3（0向下移动），-1（0向左移动），1（向右移动）

    def construction(self,index,parentIndex,list,fund,depth,direction):
        '''
        对节点进行构造
        '''
        self.index=index
        self.parentIndex=parentIndex
        self.list=list
        self.fund=fund
        self.depth=depth
        self.direction=direction
        self.zeroIndex=self.list.index(0)
