class Body:

    def __init__(self, body_type):
        self.body_type = body_type

    def get_body_type(self):
        return self.body_type

class Engine:

    def __init__(self, engine_type):
        self.engine_type = engine_type

    def get_engine_type(self):
        return self.engine_type



class Wheels:

    def __init__(self, wheels_type):
        self.wheels_type = wheels_type

    def get_wheels_type(self):
        return self.wheels_type


class Plane(Body, Engine, Wheels):
    def __init__(self, body_type, engine_type, wheels_type):
        Body.__init__(self, body_type)
        Engine.__init__(self, engine_type)
        Wheels.__init__(self, wheels_type)


plane = Plane('Пластик', 'ДВС', 'Резиновые')
print(plane.get_body_type())
print(plane.get_engine_type())
print(plane.get_wheels_type())

class PlaneComp:
    def __init__(self, body_obj: object = Body, engine_obj: object = Engine, wheels_obj: object = Wheels):
        self.body = body_obj
        self.engine = engine_obj
        self.wheels = wheels_obj

body = Body('Дерево')
engine = Engine('Электро')
wheels = Wheels('Полиуретан')
planeComp = PlaneComp(body, engine, wheels)

plane = PlaneComp(body, engine, wheels)
print(planeComp.body.get_body_type())
print(planeComp.engine.get_engine_type())
print(planeComp.wheels.get_wheels_type())