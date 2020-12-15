#!usr/bin/python

def eval_expr_du(string):
    stack =[]
    pr = string.split(" ")


    for s in pr:
        if s.isdigit():
            stack.append(s)
        else :
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if s=="+":
                stack.append(op2+op1)
            elif s=="-":
                stack.append(op2-op1)
            elif s=="*":
                stack.append(op2*op1)
            elif s=="/":
                stack.append(int(op2/op1))
            else :
                print("Syntax error, operand" +s+" not recognized!")
                stack.append(0)
                break
    return stack.pop()


def eval_expr(string,d={}):
    stack = []
    pr = string.split(" ")
    #print(string)
    #print(pr)
    prx=[]
    for st in pr:
        if st in d.keys():
            prx.append(str(d[st]))
        else:
            prx.append(st)
    #print(pr)
    for s in prx:
        if s.isdigit():
            stack.append(s)
        else:
            op2= int(stack.pop())
            op1 = int(stack.pop())
            if s == "+":
                stack.append(op1 + op2)
            elif s == "-":
                stack.append(op1 - op2)
            elif s == "*":
                stack.append(op1 * op2)
            elif s == "/":
                stack.append(int(op1 / op2))
            else:
                print("Syntax error, operand" + s + " not recognized!")
                stack.append(0)
                break
    return stack.pop()

def to_inflix(t):
    tl=t.split(" ")
    stack=[]
    for j in range(len(tl)):
        if tl[j].isdigit() or tl[j].isalpha():
            stack.append(tl[j])
        else :
            op1=stack.pop()
            op2=stack.pop()
            stack.append("(" + " " + op2 + " " + tl[j] + " " + op1 + " " +")")
    return stack.pop()

def to_postfix(t):
    stack = []
    pr = t.split(" ")
    #print(text)
    #print(pr)
    for element in pr:
        if element == ")":
            op2 = stack.pop()
            operator = stack.pop()
            op1 = stack.pop()
            junk = stack.pop()
            stack.append(op1 + " " +  op2 + " " + operator + " ")
        else:
            stack.append(element)
    return stack.pop()



# print(eval_expr("1 x +",{"x":2}))
# print(eval_expr("x x +",{"x":2}))
# print(eval_expr("2 x * x +",{"x":3}))
# print(eval_expr("x",{"x":3}))
# print(eval_expr("x y +",{"x":3,"y":2}))
# print(eval_expr("x y + 2 *",{"x":3,"y":2}))
# print(eval_expr("x y + y *",{"x":3,"y":2}))
# print("INFLIX")
# print(to_inflix("1 a 3 * +"))
# print("POSTFIX")
# print(to_postfix("( ( 10 + 1 ) * ( 2 / 3 ) )"))
# print(to_postfix("1"))
# print(to_postfix("( 1 + 2 )"))
