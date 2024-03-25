# 계산기 클래스 
class FourCal:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result
  def sub(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result

a = FourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

-----------------------------------------------------------------
# 오버로딩으로 제곱 메서드 확장
class MoreFourCal(FourCal):
  def pow(self):
    result = self.first ** self.second
    return result

b = MoreFourCal(8, 3)
print(b.add())
print(b.pow())

------------------------------------------------------------------
# 오버라이딩으로 div 메서드 수정
class SafeFourCal(FourCal):
  def div(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second
    
c = SafeFourCal(4, 0)
print(c.div())

------------------------------------------------------------------
# 클래스 변수 

class Family:
  lastname = "김"


d = Family()
e = Family()

print(d.lastname)
print(e.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)
# 클래스로 만든 모든 객체에 변수 값을 공유 

a.lastname = "최"

print(a.lastname)
print(b.lastname)

# 객체 변수는 공유되지 않는다. 
