import math

def vec_2_dist(x0:float, y0:float, x1:float, y1:float):
  """
  Функция для нахождения дистанции по двум точкам
  на двухмерной плоскости
  """

  return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

def solve_sss_trig(s0:float, s1:float, s2:float):
  """
  Функция для нахождения углов треугольника по его сторонам
  через теорему косинусов
  """

  a = (s0 ** 2 + s2 ** 2 - s1 ** 2) / (2 * s0 * s2)
  b = (s0 ** 2 + s1 ** 2 - s2 ** 2) / (2 * s0 * s1)
  c = (s1 ** 2 + s2 ** 2 - s0 ** 2) / (2 * s2 * s1)

  a = math.degrees(math.acos(a))
  b = math.degrees(math.acos(b))
  c = math.degrees(math.acos(c))

  return a, b, c

# Обратная кинематика в 2D
def solve_2_ik(l0:float, l1:float, x:float, y:float):
  """
  Функция для решения задач обратной кинематики для
  манупяляторов с двумя степенями свободы
  на двухмерной плоскости
  """

  try:
    l2 = vec_2_dist(0, 0, x, y)

    if l2 < l0 + l1:
      a, b, c = solve_sss_trig(l0, l1, l2)

      # Угол между a и x y
      atan = math.degrees(math.atan2(y, x))

      # Приводим углы к нужному результату
      A = 180 - (a + atan) # Угол A
      B = 180 - b  	      # Угол B

      return True, [A, B]
    else:
      return False, "Failed to solve IK! (l2 > l0 + l1)"
  except Exception as e:
    return False, e

def get_point_on_circle(angle:float):
  return math.cos(math.radians(angle)), math.sin(math.radians(angle))
