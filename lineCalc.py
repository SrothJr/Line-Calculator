import operator

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}

inp = input("Enter your calculation: ")


line = inp.strip().split(" ")

res = 0

while len(line) != 1:
    have_div = "/" in line
    have_mul =  "*" in line
    have_add = "+" in line
    if have_div:
        for i in range(1, len(line) - 1, 2):
            if line[i] == "/":
                res = ops[line[i]](float(line[i-1]),float(line[i+1]))
                del line[i-1:i+2]
                line.insert(i-1,str(res))
                print(line)
                break
    else:
        if have_mul:
            for i in range(1, len(line) - 1, 2):
                if line[i] == "*":
                    res = ops[line[i]](float(line[i-1]),float(line[i+1]))
                    del line[i-1:i+2]
                    line.insert(i-1,str(res))
                    print(line)
                    break
        else:
            if have_add:
                for i in range(1, len(line) - 1, 2):
                    if line[i] == "+":
                        res = ops[line[i]](float(line[i-1]),float(line[i+1]))
                        del line[i-1:i+2]
                        line.insert(i-1,str(res))
                        print(line)
                        break
            else:
                for i in range(1, len(line) - 1, 2):
                    if line[i] == "-":
                        res = ops[line[i]](float(line[i-1]),float(line[i+1]))
                        del line[i-1:i+2]
                        line.insert(i-1,str(res))
                        print(line)
                        break

print(line)