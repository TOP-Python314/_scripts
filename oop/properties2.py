class Square:
    def __init__(self, edge: float):
        self.__edge: float = edge
        self.__area: float = edge**2
    
    @property
    def edge(self) -> float:
        return self.__edge
    
    @edge.setter
    def edge(self, new_edge: float):
        self.__edge = new_edge
        self.__area = new_edge**2
    
    @property
    def area(self) -> float:
        return self.__area
    
    @area.setter
    def area(self, new_area: float):
        self.__edge = new_area**0.5
        self.__area = new_area


sq1 = Square(5)


