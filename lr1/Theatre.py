class Theatre:
    def __init__(self, name, location):
        self.__name: str = name
        self.__location: str = location
        self.__afisha: dict = {}

    @property
    def name(self):
        return self.__name

    def add_performance(self, performance, stage):
        self.__afisha[performance] = stage

    def show_afisha(self):
        performances = list(self.__afisha.keys())
        for i in range(len(performances)):
            print(f"{i + 1}: {performances[i].name}")

    def get_performance(self, index):
        performances = list(self.__afisha.keys())
        return performances[index]

    def get_stage(self, performance):
        return self.__afisha[performance]

    def start_performance(self):
        for performance in self.__afisha:
            print(performance.name)

        index = int(input("Choose performance: ")) - 1

        performance = list(self.__afisha.keys())[index]

        stage = self.__afisha[performance]
        print(f"Начинается представление {performance.name} на сцене номер {stage.number}!")
        performance.start()
