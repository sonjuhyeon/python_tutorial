# 객체 지향: 캡슐화, 상속, 다형성
# 캡슐화: 변수와 함수를 하나의 단위로 묶어서 사용. 주로 클래스를 통해 구현
# 상속: 자식 클래스가 부모 클래스의 속성과 메서도를 그대로 물려받아 사용
# 다형성: 하나의 변수 또는 함수가 상황에 따라 다른 의미로 해석되어 사용

class myClass:
  x = 5

p1 = myClass # p1은 myClass의 인스턴스
print(p1.x)

# 생성자:클래스의 인스턴스가 생성될 때 호출, 초기화를 담당하는 함수
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person(name = "juhyeon", age = 28)
print(p2.name)
print(p2.age)

class Student(Person):
  def __init__(self, name, age, grade):
    super().__init__(name, age) # 부모 클래스에서 self를 제외한 생성자 호출
    self.grade = grade

  def print_info(self): # 부모의 클래스의 메서드를 
    print(f"이름:{self.name}, 나이:{self.age}, 학년:{self.grade}")
  
x = Student("Juhyeon", 28, 4)
x.print_info()