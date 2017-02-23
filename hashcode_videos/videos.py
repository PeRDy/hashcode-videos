from random import randint

from hashcode_videos.genetic import Individual, Population


class Problem:
    def __init__(self, data_center_latency, cache_latency, request_video, video_size, cache_size):
        self.data_center_latency = data_center_latency
        self.cache_latency = cache_latency
        self.request_video = request_video
        self.video_size = video_size
        self.cache_size = cache_size


class Solution(Individual):
    END_OF_LINE = "\n"

    def __init__(self, problem, cache):
        self.problem = problem
        self.cache = cache

    @staticmethod
    def random(pizza, stability=0.2, nth=3):
        solution = Solution(pizza, [])
        for i in range(nth):
            solution.mutate()

    @property
    def is_valid(self):
        cache_size = (self.cache * self.problem.video_size.T).sum(1)
        cache_diff = self.problem.cache_size - cache_size
        return any(cache_diff[cache_diff < 0])

    def mutate(self):
        valid = False
        while not valid:
            x = randint(0, self.cache.shape[0])
            y = randint(0, self.cache.shape[1])
            self.cache[x, y] = int(not(self.cache[x, y]))
            valid = self.is_valid

            if not valid:
                self.cache[x, y] = int(not(self.cache[x, y]))

    def breed(self, mother: 'Individual') -> 'Individual':
        # Mix two solutions
        father_sol = self.cache
        mother_sol = mother.cache

        father_sol[::2] = 0
        mother_sol[1::2] = 0

        return Solution(self.problem, father_sol + mother_sol)

    def fitness(self) -> float:
        # Current score
        pass

    def __str__(self):
        # Output file
        output_str = ""
        cache_used_len = 0

        # Each of the subsequent N lines should describe the videos cached in a single cache server
        for row_id in range(len(self.cache)):
            row = self.cache[row_id]

            # ID of the cache server being described, the IDs of the videos stored in this cache server
            line_data = self._get_cache_row_data(row)

            if len(line_data) > 0:
                # Sum 1 to num of caches used and prepend cache id
                cache_used_len += 1
                line_data.insert(0, str(row_id))
                output_str += self._new_str_line(line_data)

        # Line containing a single number N - the number of cache server descriptions to follow
        output_str = self._new_str_line([str(cache_used_len), ]) + output_str

        return output_str

    @staticmethod
    def _get_cache_row_data(cache_row):
        line_data = []
        for col_id in range(len(cache_row)):
            col_val = cache_row[col_id]

            # Add video id
            if col_val == 1:
                line_data.append(str(col_id))

        return line_data

    def _new_str_line(self, line):
        # Build new line for str with corresponding end of line symbol
        return ' '.join(line) + self.END_OF_LINE


class SolutionSet(Population):
    def __init__(self, problem, size, *args, **kwargs):
        self.problem = problem
        self.individuals = [Solution.random(problem) for _ in range(size)]


if __name__ == '__main__':
    import numpy
    zer = numpy.zeros((3, 5))
    zer[0][2] = 1
    zer[1][3] = 1
    zer[1][1] = 1
    zer[2][0] = 1
    zer[2][1] = 1
    oc = Solution(None, zer)
    print(str(oc))
