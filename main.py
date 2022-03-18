# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import operator
import sys
from process import Process
from rand48 import Rand48
from copy import deepcopy

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def next_exp(lambda__, upper_bound__, rand__):
    # * Generates rand 0.00 to 1.00
    #  * Averages the random value using log and lambda
    #  * Makes sure to not exceed upper bound
    #  */
    avg_rand = 0
    for i in range(1):
        avg_rand = math.ceil(-(math.log(rand__.drand())) / lambda__)
        if avg_rand > upper_bound__:
            i -= 1
    return avg_rand


def getAlpha(i):
    # /* uses the iterator of Process creation to assign it a character name */
    a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if i >= 26:
        print("ERROR: Process limit is 26\n")
        sys.exit(2)
    return a[i]


def gen_process_info(lambda__, upper_bound__, p, rand__):
    t = int(math.ceil(1 / lambda__))
    p.setTau(t)
    p.setTau_remaining(t)
    t_arrival = next_exp(lambda__, upper_bound__, rand__)
    p.setT_arrival(t_arrival)
    num_bursts = int(math.ceil(rand__.drand()*100))
    p.setNum_bursts(num_bursts)
    for i in range(math.ceil(num_bursts)):
        CPUBurst = next_exp(lambda__, upper_bound__, rand__)
        p.addCPUBursts(int(math.ceil(CPUBurst)))
        if i != (math.ceil(num_bursts) - 1):
            IOBurst = next_exp(lambda__, upper_bound__, rand__)
            p.addIOBursts(int(math.ceil(IOBurst)) * 10)
    p.setWait_time(0)
    p.setTurnaround_time(0)
    p.setCur_CPUBurst(p.getCPUBurst(0))
    p.setIn_rq = False


def SJF(processes_, tau_, t_cs_, alpha_):
    # processes_ are sorted by arrival time
    cpu_time = 0
    processUsingCPU = None      # the processes that uses CPU
    readyQueue = list()
    waitingQueue = list()

    while len(processes_) > 0:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 8:
        print("ERROR: Invalid argument.")
        sys.exit(2)
    num_processes = int(sys.argv[1])
    seed = int(sys.argv[2])
    lambda_ = float(sys.argv[3])
    upper_bound = float(sys.argv[4])
    t_cs = float(sys.argv[5])
    alpha = float(sys.argv[6])
    t_slice = float(sys.argv[7])
    tau = 1 / lambda_

    # random process generator
    rand_ = Rand48(0)
    rand_.srand(seed)
    processes = []

    for x in range(num_processes):
        name = getAlpha(x)
        process = Process(name, tau)
        gen_process_info(lambda_, upper_bound, process, rand_)
        processes.append(process)
        process.printProcess()

    # sort processes by arrival time, and name
    processes.sort(key=operator.attrgetter('t_arrival', 'name'))
    # for x in range(num_processes):
    #     processes[x].printProcess()
    processes_FCFS = deepcopy(processes)    # FCFS
    processes_SJF = deepcopy(processes)    # SJF
    processes_SRT = deepcopy(processes)    # SRT
    processes_RR = deepcopy(processes)    # RR

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
