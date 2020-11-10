'''
Created on 2020年10月24日
保存待扩展的节点
@author: dingxinlong
'''
import operator
import NODE  as Node
class Open():

    def __init__(self):
        self.nodelist=[] #保存节点的列表
        self.cmpfun = operator.attrgetter('fund','depth') #open表排序条件 估计值优先，其次是深度

    def sortfun(self):
        '''
        对open表进行排序
        :return:
        '''
        #根据条件对open表进行排序
        self.nodelist.sort(key=self.cmpfun)



    def append(self,node):
        '''
        向节点列表中添加节点
        :param node:
        :return:
        '''
        #节点列表中添加一个新的节点
        self.nodelist.append(node)
        #对节点列表（open表）进行排序
        self.sortfun()

    def pop(self):
        '''
        从open表中取一个节点
        :return:node
        '''
        #从open表中取出一个节点
        return self.nodelist.pop(0)


    def isEmpty(self):
        '''
        判断open表是否为空
        :return: true 为空，false 不为空
        '''
        if self.nodelist:
            return False
        else:
            return True

