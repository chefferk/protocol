import time


class Survey:
    def __init__(self):
        print('Survey object created.')
        self.timer_running = False
        self.visited_1 = False
        self.visited_2 = False
        self.visited_3 = False
        self.visited_4 = False
        self.visited_5 = False
        self.visited_6 = False
        self.visited_7 = False
        self.visited_8 = False
        self.visited_9 = False
        self.visited_10 = False
        self.visited_11 = False
        self.visited_12 = False
        self.visit_count_1 = 0
        self.visit_count_2 = 0
        self.visit_count_3 = 0
        self.visit_count_4 = 0
        self.visit_count_5 = 0
        self.visit_count_6 = 0
        self.visit_count_7 = 0
        self.visit_count_8 = 0
        self.visit_count_9 = 0
        self.visit_count_10 = 0
        self.visit_count_11 = 0
        self.visit_count_12 = 0

    def start_timer(self):
        self.start = time.time()
        self.timer_running = True
        print(f'Timer started at: {self.start}')

    def end_timer(self):
        self.end = time.time()
        self.timer_running = False
        self.elapsed = self.end - self.start
        print(f'Timer ended at: {self.end} \n Elapsed time: {self.elapsed}')

    def __repr__(self):
        return (
            f'Elapsed time: {self.elapsed}\n'
            f'Page 1 visited: {self.visit_count_1} times\n'
            f'Page 2 visited: {self.visit_count_2} times\n'
            f'Page 3 visited: {self.visit_count_3} times\n'
            f'Page 4 visited: {self.visit_count_4} times\n'
            f'Page 5 visited: {self.visit_count_5} times\n'
            f'Page 6 visited: {self.visit_count_6} times\n'
            f'Page 7 visited: {self.visit_count_7} times\n'
            f'Page 8 visited: {self.visit_count_8} times\n'
            f'Page 9 visited: {self.visit_count_9} times\n'
            f'Page 10 visited: {self.visit_count_10} times\n'
            f'Page 11 visited: {self.visit_count_11} times\n'
            f'Page 12 visited: {self.visit_count_12} times\n'
        )
