import queue
import numpy as np

def main(filename, part2=True):
    file = [line.strip() for line in open(filename).readlines()]

    temporary = np.empty([8,9],dtype=str)

    for index, line in enumerate(file):
        if index > 7 : 
            continue

        add_line = np.array(list(line[1::4]),dtype=str)
        if (size := np.shape(add_line)[0]) < 9 :
            add_line = np.append(add_line,np.empty([9-size,],dtype=str))
    
        temporary[index] = add_line
       
    temporary = np.rot90(temporary,3)

    ship = []
    for line in temporary:
        lq = queue.LifoQueue()
        [lq.put(i) for i in line if (i != ' ' and i)]
        ship.append(lq)
    
    evaluate_command = lambda string : [int(num) for num in string.split() if num.isnumeric()]

    for index, line in enumerate(file):
        if index <= 9 : 
            continue
        
        qty, fro, to = evaluate_command(line)
        fro, to = fro-1, to-1

        if part2:
            crane = queue.LifoQueue()
            for _ in range(qty):
                crane.put(ship[fro].get())
            for _ in range(qty):
                ship[to].put(crane.get())
        else:
            for _ in range(qty):
                ship[to].put(ship[fro].get())

    [print(line.get(), end='') for line in ship]
    print()


main('input_5.txt', False)
main('input_5.txt')