
import time


class Logging:
    def __init__(self, log_file):
        self.log_file = log_file
        self.boggle_list = []
        self.start_time = 0
        # self.size = 0
        self.row = 0
        self.column = 0

    def write_log(self, log):
        with open(self.log_file, 'a') as f:
            # f.write(f'\n>>>>>>\n')
            f.writelines(log)
            f.write(f'execution time: {time.time()-self.start_time}\n')

    def read_list(self):
        """

        :param boggle_list:
        :return:
        """
        self.start_time = time.time()
        f = open(self.log_file, 'r')

        size = (f.readline().split())
        self.column = int(size[0])
        self.row = int(size[1])

        for i in range(self.column):
            input_row = f.readline().split()
            if len(input_row) == self.row:
                self.boggle_list.append(input_row)
            else:
                print("error : LOG.txt format does not match")
                return
        f.close()

    def reset_time(self):
        self.start_time = time.time()

def main():
    pass

if __name__ == '__main__':
    main()