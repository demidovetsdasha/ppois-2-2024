class Director:
    def __init__(self, name, experience_years):
        self.__name: str = name
        self.experience_years: int = experience_years
        self.directed_plays: list = []

    @property
    def directed_plays_count(self):
        return len(self.directed_plays)

    def add_directed_play(self, play):
        self.directed_plays.append(play)

    def display_info(self):
        print(f'Name: {self.__name}, {self.experience_years} years of experience, list of directed projects:')
        for project in self.directed_plays:
            print(project.name)
