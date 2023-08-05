# -*- coding: UTF-8 -*-

# 原文：https://blog.csdn.net/TaiJi1985/article/details/72942947
'''
Created on 2017-6-8

@author: Administrator

二元运算符    特殊方法
+    __add__,__radd__
-    __sub__,__rsub__
*    __mul__,__rmul__
/    __div__,__rdiv__,__truediv__,__rtruediv__
//    __floordiv__,__rfloordiv__
%    __mod__,__rmod__
**    __pow__,__rpow__
<<    __lshift__,__rlshift__
>>    __rshift__,__rrshift__
&    __and__,__rand__
^    __xor__,__rxor__
|    __or__,__ror__
+=    __iaddr__
-=    __isub__
*=    __imul__
/=    __idiv__,__itruediv__
//=    __ifloordiv__
%=    __imod__
**=    __ipow__
<<=    __ilshift__
>>=    __irshift__
&=    __iand__
^=    __ixor__
|=    __ior__
==    __eq__
!=,<>    __ne__
>    __get__
<    __lt__
>=    __ge__
<=    __le__

'''


class E:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.type = 'n'
        self.f = 0
        pass

    def isOp(self, op):
        return self.type == 'op' and self.f == op

    def isZero(self):
        return self.type == 'float' and abs(self.f) < 1e-5

    def isOne(self):
        return self.type == 'float' and abs(self.f - 1) < 1e-5

    def isNum(self):
        return self.type == 'float'

    def float(self, a):  #
        self.f = a
        self.left = self.right = None
        self.type = 'float'
        return self

    def sym(self, name):
        self.type = 'sym'
        self.f = name
        return self

    def withOp(self, op, left, right):
        self.f = op
        self.type = 'op'

        if type(left) == int or type(left) == float:
            left = E().float(left)

        if type(right) == int or type(right) == float:
            right = E().float(right)

        if left != None:
            self.left = left.clone()
            self.left.parent = self
        else:
            self.left = None
        if right != None:
            self.right = right.clone()
            self.right.parent = self
        else:
            self.right = None
        return self

    def clone(self):  # 深度复制
        x = E()
        x.type = self.type
        x.f = self.f
        if self.left == None:
            x.left = None
        else:
            x.left = self.left.clone()

        if self.right == None:
            x.right = None
        else:
            x.right = self.right.clone()
        return x

    def __radd__(self, x):
        # print '__radd__ ',x
        r = E().withOp('+', x, self)
        return r

    def __rsub__(self, x):
        # print '__rsub__ ',x
        r = E().withOp('-', x, self)
        return r

    def __rmul__(self, x):
        r = E().withOp('*', x, self)
        return r

    def __rdiv__(self, x):
        r = E().withOp('/', x, self)
        return r

    def __neg__(self):
        r = E().withOp('*', E().float(-1), self)
        return r

    def __add__(self, x):
        # print 'add ',x
        r = E().withOp('+', self, x)
        return r

    def __sub__(self, x):
        r = E().withOp('-', self, x)
        return r

    def __mul__(self, x):
        r = E().withOp('*', self, x)
        return r

    def __div__(self, x):
        r = E().withOp('/', self, x)
        return r

    def __pow__(self, x):
        r = E().withOp('^', self, x)
        return r

    def isConstOf(self, x):  # 求导时，对于x是否是一个常数
        if self.type == 'float':
            return True
        if self.type == 'sym':
            return self.f == x.f

        return (self.left == None or self.left.isConstOf(x)) and (self.right == None or self.right.isConstOf(x))

    def op_diff(self, x):
        # do something with None left or right
        if self.left == None:
            d_left = None
        else:
            d_left = self.left.diff(x)
        if self.right == None:
            d_right = None
        else:
            d_right = self.right.diff(x)

        if self.f == '+':
            return d_left + d_right
        if self.f == '-':
            return d_left - d_right
        if self.f == '*':
            return d_left * self.right + self.left * d_right
        if self.f == '/':
            return (d_left * self.right - self.left * d_right) / (self.right * self.right)
        if self.f == '^':
            left_c = d_left == E().float(0)
            right_c = d_right == E().float(0)

            if left_c and right_c:
                return E().float(0)
            elif right_c:  # f(x)^a  ()' = a*f(x)^(a-1)*f'(x)
                return self.right * self.left ** (self.right - 1) * d_left
            elif left_c:  # 指数 a^g(x)  ()' = a^g(x)*loga*g'(x)
                return self.left ** self.right * self.left.log() * d_right
            else:
                print
                'unsupport f(x)^g(x) style!! now '
                exit(1)
        pass

    def diff(self, x):  # 对x求偏导数
        if self.type == 'float':
            return E().float(0)
        elif self.type == 'sym':
            if x.f == self.f:  # 是同一个变量
                return E().float(1)
            else:
                return E().float(0)  # 不是同一个变量。
        elif self.type == 'op':
            return self.op_diff(x)

        pass

    def eq(self, x, y):
        if x == None:
            return y == None
        else:
            return x == y

    def __eq__(self, x):
        if x == None:
            return False
        if x.type != self.type:
            return False
        if x.type == 'float':
            return abs(x.f - self.f) < 1e-5
        if x.type == 'sym':
            return x.f == self.f
        if x.type == 'op':
            if x.f != self.f:
                return False
            return self.eq(self.left, x.left) and self.eq(self.right, x.right)

    def printme(self):
        self.setParent()
        self._printme()
        print('')

    def _op_toi(self, op):
        if op == '+' or op == '-':
            return 10
        if op == '*' or op == '/':
            return 20
        if op == '^':
            return 30
        return 40

    def _compare_op(self, a, b):  # 比较两个符号，谁的优先级高
        # print 'compare ',a,b,self._op_toi(a) - self._op_toi(b)
        return self._op_toi(a) - self._op_toi(b)

    def _printme(self):
        if self.type == 'float':
            print(self.f)
        elif self.type == 'op':
            useBrack = True
            if self.parent == None:
                useBrack = False
            elif self._compare_op(self.f, self.parent.f) >= 0:
                useBrack = False

            if useBrack:
                print('(',)
            # 如果是 -1*x ，直接输出 -x
            if self.left != None and self.left == E().float(-1) and self.isOp('*'):
                print('-',)
            else:
                if self.left != None:
                    self.left._printme()
                print(self.f,)
            if self.right != None:
                self.right._printme()
            if useBrack:
                print(')',)
        elif self.type == 'sym':
            print(self.f,)
        pass

    def child_pattern(self, x):
        if x == None:
            return 'none'
        if x.left == None:
            lc = "N"
        elif x.left.isOne():
            lc = '1'
        elif x.left.isZero():
            lc = '0'
        elif x.left.type == 'float':
            lc = 'F'
        else:
            lc = 'A'

        if x.right == None:
            rc = "N"
        elif x.right.isOne():
            rc = '1'
        elif x.right.isZero():
            rc = '0'
        elif x.right.type == 'float':
            rc = 'F'
        else:
            rc = 'A'

        pt = str(lc) + str(x.f) + str(rc)
        # print "PT=",pt," -------------"
        # x.printme()

        return pt

    def evalue(self, op, a, b):
        if op == '+':
            r = a.f + b.f
        if op == '-':
            r = a.f - b.f
        if op == '*':
            r = a.f * b.f
        if op == '/':
            r = a.f / b.f
        return r

    def _node_op(self, r, op, v):
        # 在以r为根的树中，查找一个满足从根r到该节点整条路径上节点都与op相同的float节点，并将v中的数据应用op进去。
        if r == None:
            return False
        if r.type == 'float':  # 如果当前节点就是一个float节点，把v的值乘在这里。
            r.f = r.evalue(op, r, v)
            return True

        if r.type != 'op' or r.f != op:  # 当前节点不满足op相等条件
            return False

        if self._node_op(r.left, op, v):
            return True

        if self._node_op(r.right, op, v):
            return True

        return False

        pass

    def _node_join(self, r, x, y):
        # 合并两个节点 2+(2+x) => 4+x
        # r 如果不能合并应返回的值
        # x 判断x是否是一个数字，如果是，则看能否和y中节点合并
        if x == None or y == None or x.type != 'float':
            return r

        succ = self._node_op(y, r.f, x)  # 如果成功将x乘进了y，则删除x，把y作为父。
        if succ:
            return y
        return r
        # 在y中查找

    #         if y.type == 'op' and y.type == r.type  and y.f == r.f:
    #             if y.left != None and y.left.type=='float':
    #                 y.left.f = self.evalue(y.f, x, y.left)
    #
    #                 return y
    #             if y.right != None and y.right.type=='float':
    #                 y.right.f = self.evalue(y.f, x, y.right)
    #                 return y
    #
    #        return r

    def _opt_node(self, x):
        # 左子树 0,1检测
        r = x
        if x == None:
            return x

        pt = self.child_pattern(x)
        if pt == 'F-1':
            pt = pt  # for debug

        if pt == '0*A' or pt == '0/A' or pt == 'A*0':
            r = E().float(0)
        if pt == '0+A' or pt == '0+1':
            r = x.right
        if pt == 'A+0' or pt == '1+0':
            r = x.left
        if pt == 'A*1':
            r = x.left

        # 左子树常数化简
        pt = self.child_pattern(x)
        pt = pt.replace('0', 'F').replace('1', 'F')
        # print '#####', pt

        if pt == 'F+F':
            r = E().float(x.left.f + x.right.f)
        if pt == 'F-F':
            r = E().float(x.left.f - x.right.f)
        if pt == 'F*F':
            r = E().float(x.left.f * x.right.f)
        if pt == 'F/F':
            r = E().float(x.left.f / x.right.f)
        return r

    def optm(self):  # 优化式子
        # 后续遍历，从下网上优化
        if self.left != None:
            self.left = self.left.optm()
        if self.right != None:
            self.right = self.right.optm()

        self.left = self._opt_node(self.left)
        self.right = self._opt_node(self.right)

        r = self._opt_node(self)

        # 0-x -> -1*x
        if self.isOp('-'):
            if self.left != None and self.left == E().float(0):
                self.f = '*'
                self.left = E().float(-1)

        # 优化常数项（多个常数项相乘，如2*3*x ->6*x)
        r = self._node_join(r, r.left, r.right)
        r = self._node_join(r, r.right, r.left)

        if r.left != None and r.left == r.right:
            if r.isOp('*'):
                r.f = '^'
                r.right = E().float(2)

        # 优化乘方
        if r.isOp('^') and r.right != None and r.right.isOne():
            return r.left

        return r
        pass

    # 求以e为底的对数
    def log(self):
        if self.type == 'sym' and self.f == 'e':
            return E().float(1)
        r = E().withOp('log', None, self)
        return r

    # 设置所有parent指针

    def setParent(self):
        if self.left != None:
            self.left.parent = self
            self.left.setParent()
        if self.right != None:
            self.right.parent = self
            self.right.setParent()


pass

# class Optmer:
#     def __init__(self):
#         pass
#     def addParentPointer(self,tree):
#         if tree.left != None:
#             tree.left.parent = tree
#             self.addParentPointer(tree.left)
#         if tree.right != None:
#             tree.right.parent = tree
#             self.addParentPointer(tree.right)
#
#     def optNode(self,node):
#         self.addParentPointer(node)
#
#     def _zeroOptNode(self,node):
#         if node == None:
#             return
#         if node.isZero():
#             node.parent.
#         pass

x = E().sym('x')
# c = 2*x**2+3*x**4+E().float(4)**x
e = E().sym('e')
w = E().sym('w')
b = E().sym('b')
c = 1 / (1 + e ** (-(w * x + b)))
c.printme()

d = c.diff(w)
d.printme()
d.optm().optm().printme()
