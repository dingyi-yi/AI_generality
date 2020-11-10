'''
Created on 2020年10月24日
启发式搜索中的启发函数的定义，还有对逆序数的求解，对最短移动距离的求解。
其中启发函数1，2，3，4为本实验的扩展内容
启发函数5为根据启发函数2改变的
@author: dingxinlong
'''

Sg=[1,2,3,8,0,4,7,6,5]  #目标状态
def inverseNum(list):
    '''
    求取逆序数
    :param list:8数码列表
    :return:返回逆序数
    '''
    count = 0
    temlist = [i for i in list]
    temlist.remove(0)
    for i in range(7):
        for j in range(i + 1, 8):
            if temlist[i] > temlist[j]:
                count = count + 1
    return count

def minMove(indexA,indexB):
    '''
    两个点的最短移动距离
    :param indexA: 点A
    :param indexB: 点B
    :return: 移动的最短距离
    '''
    #将A作为较小
    if indexA>indexB:
        indexA,indexB=indexB,indexA
    differenceValue=indexB-indexA
    if(differenceValue>=3):   #如果差值大于3，则肯定不在同一行
        result=1+minMove(indexA+3,indexB)
    elif differenceValue==2:  #如果差值为2，则最短距离肯定为2
        result=2
    elif differenceValue==0:   #差值为0，则不用移动
        result=0
    else:                     #差值为1，可能移动1次也可能移动3次
        result=3 if (indexA+1)%3==0 else 1
    return result





def hfun_1(sn):
    '''
    启发函数_1,）启发函数 h(n)定义为当前节点与目标节点差异的度量：即当前节点与目标节点格局相比，位置不符的数字个数。
    :param sn:当前状态列表
    :return:启发函数值
    '''
    hun=0
    for i in range(9):
        if sn[i] != Sg[i] and sn[i] != 0:
            hun = hun + 1
    return hun

def hfun_2(sn):
    '''
    启发函数_2,）启发函数 h(n)定义为当前节点与目标节点距离的度量：当前节点与目标节点格局相比，位置不符的数字移动到目标节点中对应位置的最短距离之和。
    :param sn:当前状态列表
    :return:启发函数值
    '''
    count=0
    for i in range(9):
        if sn[i]!=Sg[i] and sn[i]!=0:
            count=count+minMove(i,Sg.index(sn[i]))
    return count



def hfun_3(sn):
    '''
     启发函数_3,启发函数 h(n)定义为每一对逆序数字乘以一个倍数。
    :param sn: 当前状态列表
    :return: 启发函数值
    '''
    inum=inverseNum(list=sn)
    return abs(inum-7)*3

def hfun_4(sn):
    '''
    启发函数_4,启发函数 h(n)定义为位置不符数字个数的总和与 3 倍数字逆序数目相加。
    :param sn:当前状态列表
    :return:启发函数值
    '''
    num1=inverseNum(list=sn)
    num2=hfun_1(sn)
    return num2+3*abs(num1-7)


def hfun_5(sn):
    '''
    启发函数_5,当前状态与所有目标状态位置不符的数字，在列表中的索引值的差值和
    :param sn:当前状态列表
    :return:启发函数值
    '''
    count = 0
    for i in range(9):
        if sn[i] != Sg[i] and sn[i] != 0:
            count=count+abs(i-Sg.index(sn[i]))
    return count