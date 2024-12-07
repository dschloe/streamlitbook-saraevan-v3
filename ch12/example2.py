class Animal:
    # 클래스 속성
    species = "동물"
    count = 0
    
    # 클래스 메서드
    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def increment_count(cls):
        cls.count += 1
        
    # 인스턴스 속성
    age = 0
    weight = 0
    
    # 인스턴스 메서드 
    def grow(self):
        self.age += 1
        return f"{self.name}이(가) {self.age}살이 되었습니다."
        
    def eat(self, food):
        self.weight += 0.1
        return f"{self.name}이(가) {food}을(를) 먹었습니다."

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}이(가) 소리를 냅니다."