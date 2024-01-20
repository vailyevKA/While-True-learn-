# The-Abyssal-Conundrum v1.4.3

Наш проект - это игра жанра horror-adventure, разработанная с использованием библиотеки PyGame. Она будет основана на технике рейкастинга, позволяющей эмулировать трехмерное отображение в двухмерном пространстве. Игроку предстоит исследовать лабиринт и найти выход, собирая ключи, разбросанные по уровню.

Для создания псевдо 3D эффекта рейкастинг использует стрельбу лучами (rays) в направлении игрока по каждому горизонтальному столбцу экрана. Каждый луч проверяет пересечение с объектами в сцене и определяет расстояние до ближайшего объекта. Благодаря этому процессу игрок видит объекты в 3D-проекции от первого лица.

В нашей игре будут присутствать элементы хоррора, такие как зловещая атмосфера, мистические существа и разнообразные звуковые эффекты, которые подчеркивают напряженность и ужас окружающего мира. Графика будет выполнена в темных тонах с использованием специальных эффектов, чтобы создать подходящую атмосферу.

Кроме того, мы также реализуем возможность игроку собирать ключи, чтобы открыть выход из лабиринта. Это добавляет элемент головоломки и требует от игрока стратегического мышления и исследовательского подхода.

Наша цель - создать захватывающую игру, которая погрузит игрока в зловещую и атмосферную атмосферу хоррора. Мы постарались максимально использовать возможности PyGame и рейкастинга, чтобы достичь удивительного визуального эффекта и создать уникальный геймплей.





## Интерфейс:

### Кнопка "Продолжить":

Запускает игру с места последней остановки 

### Кнопка "Создать свой уровень":

Запускает редактор уровней(см. дальше)

### Кнопка "Пройти свой уровень":

Позволяет пройти созданный уровень

### Кнопка "Новая игра":

Сбрасывает все данные

### Кнопка "⚙️":

Открывает настройки



## Управление в игре:

W - вперёд

A - поворот влево

S - назад

D - поворот вправо





## Изменения в новой версии:

-Багфикс

-Улучшения в редакторе уровней

-Рандомная генерация уровней

-Улучшена механика поведения мобов

-Улучшен ввод размеров карты





## Ссылки:

[ТЗ](https://drive.google.com/file/d/1xODTfngfSECFaphNRwCinq4V2_vXJDQq/view?usp=sharing)



# Простой-Редактор-Уровней-v1.3

При запуске нужно ввести размеры поля (в клетках) через пробел, если окно просто пропало, была ошибка в указании размеров, попробуйте снова. Нажатием ЛКМ можно создавать и убирать стены, для переключения между режимами нужно нажимать на цифры (1 - белые стены, 2 - фиолетовые стены(ключи), 3 - рандомная генерация уровня). При каждом действии карта обновляется


