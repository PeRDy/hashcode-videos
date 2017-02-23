class Problem:
    def __init__(self, data_center_latency, cache_latency, request_video, video_size, cache_size):
        self.data_center_latency = data_center_latency
        self.cache_latency = cache_latency
        self.request_video = request_video
        self.video_size = video_size
        self.cache_size = cache_size
