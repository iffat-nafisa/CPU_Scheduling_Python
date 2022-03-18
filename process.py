import sys
class Process:
    def __init__(self, name, tau):
        self.name = name
        self.num_bursts = 0
        self.t_arrival = float("-inf")
        self.tau = tau
        self.tau_remaining = 0
        self.wait_time = 0
        self.turnaround_time = 0
        self.cur_CPUBurst = 0
        self.cs_time_left = 0

        # // bool in_rq
        self.in_rq = False

        # / *will
        # pop
        # CPU and I / O
        # bursts
        # that
        # have
        # finished * /
        self.CPUBursts = []
        self.IOBursts = []

    def getName(self):
        return self.name

    def getNum_bursts(self):
        return self.num_bursts

    def getT_arrival(self):
        return self.t_arrival

    def getTau(self):
        return self.tau

    def getTauRemaining(self):
        return self.tau_remaining

    def getWaitTime(self):
        return self.wait_time

    def getTurnaround_time(self):
        return self.turnaround_time

    def getCur_CPUBurst(self):
        return self.cur_CPUBurst

    def getCS_time_left(self):
        return self.cs_time_left

    def getIn_rq(self):
        return self.in_rq

    def getCPUBurst(self, i):
        if i >= len(self.CPUBursts):
            print("Error: Invalid CPUBurst Index\n")
            sys.exit(2)
        else:
            return self.CPUBursts[i]

    def setNum_bursts(self, n):
        self.num_bursts = n

    def setName(self, a):
        self.name = a

    def setTau(self, t):
        self.tau = t

    def setTau_remaining(self, t):
        self.tau_remaining = t

    def setT_arrival(self, t):
        self.t_arrival = t

    def setWait_time(self, t):
        self.wait_time = t

    def setTurnaround_time(self, t):
        self.turnaround_time = t

    def setCur_CPUBurst(self, t):
        self.cur_CPUBurst = t

    def setCS_time_left(self, t):
        self.cs_time_left = t

    def addCPUBursts(self, c):
        self.CPUBursts.append(c)

    def addIOBursts(self, i):
        self.IOBursts.append(i)

    def setIn_rq(self, b):
        self.in_rq = False

    def add_or_subtract_cur_CPUBurst(self, i):
        self.cur_CPUBurst -= i

    def printProcess(self):
        print("Name -> {}".format(self.name))
        print("num_bursts  -> {}".format(self.num_bursts))
        print("t_arrival  -> {}".format(self.t_arrival))
        print("tau  -> {}".format(self.tau))
        print("tau_remaining  -> {}".format(self.tau_remaining))
        print("wait_time  -> {}".format(self.wait_time))
        print("turnaround_time  -> {}".format(self.turnaround_time))
        print("cur_CPUBurst  -> {}".format(self.cur_CPUBurst))
        print("cs_time_left  -> {}".format(self.cs_time_left))

        # // bool in_rq
        print("in_rq  -> {}".format(self.in_rq))

        # / *will
        # pop
        # CPU and I / O
        # bursts
        # that
        # have
        # finished * /
        # print("CPUBursts  -> ")
        # for i in range(len(self.CPUBursts)):
        #     print(self.CPUBursts[i])
        # print("IOBursts  -> ")
        # for i in range(len(self.IOBursts)):
        #     print(self.IOBursts[i])