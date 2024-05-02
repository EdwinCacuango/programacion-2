class Pokemon:
    def __init__(self, id: str, name: str, skills: list, power_rate: float, level: int) -> None:
        self.id: int = id
        self.name: str = name
        self.skills: list = skills
        self.power_rate: float = power_rate
        self.level: int = level
    


