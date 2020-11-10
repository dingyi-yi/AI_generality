'''
Created on 2020年10月24日
全局优先搜锁
@author: dingxinlong
'''
import time
import  OPEN as Open
import NODE as Node
import HFunction as hf
class globalOptimal():
    '''
    全局优先搜索
    '''

    def __init__(self):
        self.open=Open.Open()
        self.S0=[]   #初始状态
        self.Sg=[1,2,3,8,0,4,7,6,5]   #目标状态
        self.Sindex=-1  #记录最后一个节点序号 -1尚没有节点，0初始节点
        self.closed={}
        self.targetPath=[]  #解路径


    def constructionNode(self,Sn,depth,parentIndex,direction):
        '''
        构造节点
        :param Sn: 该节点的8数码列表
        :param depth: 该节点的深度
        :param parentIndex: 该节点的父亲节点序号
        :param direction: 该节点如何得到
        :return:
        '''
        #新创建一个节点
        newnode=Node.Node()
        #为该节点分配一个序号
        self.Sindex=self.Sindex+1
        #计算机该节点的估计值
        hun=hf.hfun_3(Sn)
        fund=hun+depth
        #构造该节点
        newnode.construction(index=self.Sindex,parentIndex=parentIndex,list=Sn,fund=fund,depth=depth,direction=direction)
        #将该节点加入open表
        self.open.append(node=newnode)

    def closedPush(self,node):
        '''
        将从open表中取出的节点放到closed表中
        :param node: 要放置的节点
        :return:
        '''
        index=node.index
        self.closed[index]=node


    def isTarget(self,node):
        '''
        判断是否为目标解
        :param node: 当前节点
        :return: true,是目标节点，false 不是目标节点
        '''
        for i in range(9):
            if node.list[i]!=self.Sg[i]:
                return False
        return True


    def getTarget(self,node):
        '''
        求取解路径
        :param node:最终解的节点
        :return:
        '''
        self.targetPath.append(node)  #将解节点放入路径表中
        while node.parentIndex!=-1:  #当路径上的节点还有父节点时
            index=node.parentIndex   #获取父节点序号
            node=self.closed[index]  #获取父节点
            self.targetPath.append(node)  #将节点加入路径表


    def moveNoed(self,parNode,direction):
        '''
        8数码中空白格的移动
        :param parNode: 待移动的节点（父节点
        :param direction: 需要移动的方向
        :return:
        '''
        #构造移动后的8数码
        zeroIndex=parNode.zeroIndex
        ss=[i for i in parNode.list]
        tem=ss[zeroIndex+direction]
        ss[zeroIndex]=tem
        ss[zeroIndex+direction]=0
        #构造新节点
        self.constructionNode(Sn=ss,depth=parNode.depth+1,parentIndex=parNode.index,direction=direction)


    def extendNode(self,node):
        '''
        向下扩展的节点
        :param node: 待扩展的节点
        :return:
        '''
        zeroindex=node.zeroIndex
        #向左移动
        if zeroindex%3!=0 and node.direction!=1:
            self.moveNoed(node,direction=-1)
        #向右移动
        if (zeroindex+1)%3!=0 and node.direction!=-1:
            self.moveNoed(node,direction=1)
        #向上移动
        if zeroindex>2 and node.direction!=3:
            self.moveNoed(node,direction=-3)
        #向下移动
        if zeroindex<6 and node.direction!=-3:
            self.moveNoed(node,direction=3)


    def solve(self):
        '''
        对问题进行求解
        :return:
        '''
        # 构造初始节点，并将其加入open表
        self.constructionNode(Sn=self.S0,depth=0,parentIndex=-1,direction=0)
        #open表不为空，继续执行
        while(self.open.isEmpty()==False):
            #取open表中的第一个元素
            node=self.open.pop()
            #将该节点放入closed表中
            self.closedPush(node=node)
            if self.isTarget(node=node)==True:  #如果是解节点
                self.getTarget(node=node)  #求取解路径
                return True
            else:   #否则向下扩展
                self.extendNode(node=node)
        return False


    def start(self,S0):
        '''
        求解的起始函数，调用函数可以进行
        :param S0: 初始状态列表
        :return: 该函数无返回值，会控制台打印结果。
        '''
        self.S0=S0
        if hf.inverseNum(S0)%2!=1:
            print("无解")
        else:
            start = time.perf_counter()
            bool=self.solve()
            end = time.perf_counter()
            if bool==True:
                print("总扩展节点",self.Sindex,"   解路径长度",len(self.targetPath),"  用时",(end - start))
                print("路径如下")
                for i in self.targetPath:
                    print(i.list)
            else:
                print("error")

