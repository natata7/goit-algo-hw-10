import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


def monte_carlo_integral(func, a: float, b: float, num_experiments: int = 100_000) -> float:
    # Максимум функції на відрізку [a, b] для f(x) = x^2 це f(b) = b^2
    y_min, y_max = 0, func(b)

    # N випадкових точок у прямокутній області [a, b] x [y_min, y_max]
    x_rand = np.random.uniform(a, b, num_experiments)
    y_rand = np.random.uniform(y_min, y_max, num_experiments)

    # точки, що потрапили під криву y <= f(x)
    under_curve = np.sum(y_rand <= func(x_rand))

    # Площа прямокутника, що охоплює область
    box_area = (b - a) * (y_max - y_min)

    # Оцінка площі під кривою
    integral_mc = box_area * (under_curve / num_experiments)
    return integral_mc


if __name__ == "__main__":
    a, b = 0, 2
    N = 100_000

    # обчислення методом Монте-Карло
    mc_result = monte_carlo_integral(f, a, b, num_experiments=N)

    # обчислення за допомогою SciPy quad
    quad_result, error = spi.quad(f, a, b)

    # аналітичне обчислення: Integral(x^2 dx) = x^3 / 3 | (0 to 2) = 8/3
    exact_result = 8 / 3

    print(f"Результат Монте-Карло (N={N:,}): {mc_result:.6f}")
    print(f"Результат SciPy quad:                {quad_result:.6f} (абс. помилка: {error:.2e})")
    print(f"Аналітичний результат (8/3):          {exact_result:.6f}")
    print(f"Абсолютна відхилення МК від точного:  {abs(mc_result - exact_result):.6f}")
