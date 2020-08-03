class Container(object):
    def __init__(self, name: str, image: str, entry_point: str, work_dir: str):
        self.name = name
        self.image = image
        self.entry_point = entry_point
        self.work_dir = work_dir
