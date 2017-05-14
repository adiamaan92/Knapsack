
# Stopping Criteria for stagnated solution for n number of iterations


class StoppingCriteria(object):

    def __init__(self, curr_best=0, prev_best=0, iterations=10):
        self.curr_best = curr_best
        self.prev_best = prev_best
        self.iterations = iterations
        self.count = 0

    def stop_stagnation(self, best):
        self.curr_best = best
        if self.curr_best == self.prev_best:
            self.count += 1
        else:
            self.count = 0
        if self.count >= self.iterations:
            self.curr_best, self.prev_best = 0, 0
            return True
        else:
            self.prev_best = self.curr_best
            return False


