from hashcode_videos.genetic import Individual, Population


class Problem:
    def __init__(self, data_center_latency, cache_latency, request_video, video_size, cache_size):
        self.data_center_latency = data_center_latency
        self.cache_latency = cache_latency
        self.request_video = request_video
        self.video_size = video_size
        self.cache_size = cache_size


class Solution(Individual):
    def __init__(self, problem, cache):
        self.problem = problem
        self.cache = cache

    @staticmethod
    def random(pizza, stability=0.2, nth=3):
        solution = Solution(pizza, [])
        for i in range(nth):
            solution.mutate()

    def mutate(self):
        # Randomly modify current solution
        pass

    def breed(self, mother: 'Individual') -> 'Individual':
        # Mix two solutions
        pass

    def fitness(self) -> float:
        # Current score
        pass

    def __str__(self):
        # Output file
        pass


class SolutionSet(Population):
    def __init__(self, problem, size, *args, **kwargs):
        self.problem = problem
        self.individuals = [Solution.random(problem) for _ in range(size)]
