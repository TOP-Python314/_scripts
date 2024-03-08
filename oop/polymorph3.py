from abc import ABC, abstractmethod


class MapObject(ABC):
    @abstractmethod
    def info(self) -> str:
        pass


class BuildingObject(MapObject):
    def __init__(self, address: str, *organizations: str):
        self.address = address
        self.organizations: list[str] = list(organizations)
    
    def info(self, full: bool = False):
        result = f'Здание по адресу {self.address}'
        if full:
            result += '\n'.join((
            '\nОрганизации:', 
            *self.organizations, 
        ))
        return result


class TransportObject(MapObject):
    def __init__(self, name: str, kind: str, route: str, *routes: str):
        self.name = name
        self.kind = kind
        self.routes: list[str] = [route, *routes]
    
    def info(self) -> str:
        return '\n'.join((
            f'Остановка {self.name} ({self.kind})', 
            'Маршруты:', 
            *self.routes, 
        ))


b1 = BuildingObject(
    'улица Куйбышева, 67, Екатеринбург, Свердловская область, 620026',
    'Сбербанк', 'Сбер банкомат', 'Домклик'
)
t1 = TransportObject(
    'улица Белинского',
    'трамвай',
    '3', '4', '6', '10', '14', '20', '21'
)

for obj in (b1, t1):
    print(obj.info(), end='\n\n')

print(b1.info(full=True), end='\n\n')
