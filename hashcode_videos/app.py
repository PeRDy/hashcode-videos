from argparse import ArgumentParser
from typing import List

import datetime
import numpy as np

from hashcode_videos.base_app import BaseApp
from hashcode_videos.videos import Problem


class App(BaseApp):
    @staticmethod
    def read_int_line(f) -> List[int]:
        return [int(i) for i in f.readline().split()]

    def read_file(self, file_path):
        with open(file_path) as f:
            n_videos, n_endpoints, n_request, n_caches, cache_size = self.read_int_line(f)

            data_center_latency = np.zeros(n_endpoints)
            cache_latency = np.zeros((n_endpoints, n_caches))
            request_video = np.zeros((n_endpoints, n_videos))

            video_size = np.array(self.read_int_line(f))

            for endpoint in range(n_endpoints):
                dc_latency, n_caches = self.read_int_line(f)
                data_center_latency[endpoint] = dc_latency
                for _ in range(n_caches):
                    cache, latency = self.read_int_line(f)
                    cache_latency[endpoint][cache] = latency

            for i in range(n_request):
                video, endpoint, n = self.read_int_line(f)
                request_video[endpoint][video] = n

        return Problem(data_center_latency, cache_latency, request_video, video_size, cache_size)

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('input', help='input file')
        parser.add_argument('output', help='output file')
        parser.add_argument('-p', '--population', default=100, type=int, help='population')
        parser.add_argument('-e', '--epochs', type=int, help='epochs')
        parser.add_argument('-t', '--threshold', type=float, help='threshold [0,1]')
        parser.add_argument('-r', '--retain', type=float, help='retain [0,1]')
        parser.add_argument('-s', '--select', type=float, help='random selection [0,1]')
        parser.add_argument('-m', '--mutate', type=float, help='mutate [0,1]')

    def run(self, *args, **kwargs):
        problem = self.read_file(self.args['input'])
        # solution = SolutionSet(pizza, self.args['population'])
        before = datetime.datetime.now()
        try:
            import ipdb; ipdb.sset_trace()
            # solution.run(**self.args)
        except KeyboardInterrupt:
            self.logger.info('Interrupted')
        finally:
            after = datetime.datetime.now()
            self.logger.debug('Time: %ss.', (after - before).total_seconds())
            # self.logger.info(repr(solution.best))

            # with open(self.args['output'], 'w') as f:
            #     f.write(str(solution.best))

