<!-- Macros: start -->
$\newcommand{\block}[2]{\begin{#1} #2 \end{#1}}$
$\newcommand{\cases}[1]{\block{cases}{#1}}$
$\newcommand{\up}[2]{\stackrel{#1}{#2}}$
$\def\dn#1#2{\mathrel{\mathop{#2}\limits_{#1}}}$
$\def\ident{\Longleftrightarrow}$
$\def\thus{\Rightarrow}$
$\newcommand{\set}[1]{ \{ #1 \} }$
$\newcommand{\bigset}[1]{ \left \{ #1 \right \} }$
$\newcommand{\bracs}[1]{ ( #1 ) }$
$\newcommand{\bigbracs}[1]{ \left ( #1 \right ) }$
$\newcommand{\bkets}[1]{\langle #1 \rangle}$
$\newcommand{\bigbkets}[1]{\left \langle #1 \right \rangle}$
$\newcommand{\mat}[1]{\block{Vmatrix}{#1}}$
$\newcommand{\det}[1]{\block{vmatrix}{#1}}$
$\newcommand{\pmat}[1]{\block{pmatrix}{#1}}$
$\newcommand{\emat}[1]{\block{matrix}{#1}}$
$\renewcommand{\geq}{\geqslant}$
$\renewcommand{\leq}{\leqslant}$
$\newcommand{\upline}[1]{\overline{#1}}$
$\newcommand{\dnline}[1]{\underline{#1}}$
$\def\ex{\exists}$
$\def\exo{\ex!}$
$\renewcommand{\phi}{\varphi}$
$\renewcommand{\epsilon}{\varepsilon}$
$\def\alp{\alpha}$
$\def\lam{\lambda}$
$\def\gam{\gamma}$
$\def\eps{\epsilon}$
$\newcommand{\NN}{\mathbb{N}}$
$\newcommand{\ZZ}{\mathbb{Z}}$
$\newcommand{\RR}{\mathbb{R}}$
$\newcommand{\CC}{\mathbb{C}}$
$\newcommand{\FF}{\mathbb{F}}$
$\newcommand{\QQ}{\mathbb{Q}}$
$\newcommand{\EE}{\mathbb{E}}$
$\newcommand\E{\mathbbold{e}}$
$\newcommand\F{\mathbbold{f}}$
$\newcommand\G{\mathbbold{g}}$
$\renewcommand{\int}{\intop}$
$\newcommand{\ans}[1]{\textbf{Ответ}: #1.}$
$\newcommand{\norm}[1]{\left \lVert #1 \right \rVert}$
$\newcommand{\ord}[1]{\operatorname{ord}(#1)}$
$\renewcommand{\gcd}{\text{НОД}}$
$\newcommand{\lcm}{\text{НОК}}$
<!-- Macros: end -->  

# Аналитическая геометрия  

```{contents} Аналитическая геометрия  
---  
depth: 3  
```  

Преподаватель - Михайлов Владислав Дмитриевич  

## Литература  

- [Клетник Д. В. - "Сборник задач по Аналитической Геометрии"](https://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/Сборник_задач_по_аналитической_геометрии_КлетеникДВ.pdf)  

## Лекция 02.09.2022  



### Векторы  

***Определение***  

- Вектор  - это направленный отрезок.  

- Длина вектора $|\vec{AB}|$  

- Краткая запись  $|\vec{a}|$  

***Факт***  
- Векторы коллинеарны, если они лежат на параллельных прямых или на одной прямой  

***Факт***  
- Два вектора называются равными, если равны их длины (модули) и они коллинеарны и соноправлены  

***Факт***  

- Если два вектора коллинеарны, то они отличаются на константу.  


***Свойства***  

**Сложение**  
- По правилу треугольника  
- По правилу паралелограмма  
1.  $ \vec{a} + \vec{b} = \vec{b} + \vec{a}$  
2. $$ \vec{a} + (\vec{b} + \vec{c}) = (\vec{a} + \vec{b}) + \vec{c} $$  

3. $$\exists \vec{0} : \vec{a} + \vec{0} = \vec{a}$$  

4. $$\forall \vec{v} \in \RR^n : \exists \vec{v}^{-1} : \vec{v} + \vec{v}^{-1} = \vec{0} $$  


- Вектором $\lambda \vec{a}$ называется вектор, такой что : $|\lambda\vec{a}| = |\lambda||\vec{a}|$  

- Вектор $\lambda \vec{a}$ коллинеарен вектору $\vec{a}$ и сонаправлен, если $\lambda \geq 0$  

***Свойства***  
**Умножение векторов на константу**  


- $$ \lambda (\vec{a} + \vec{b}) = \lambda\vec{b} + \lambda\vec{a}$$  

- $$ (\lambda + \mu)\vec{a} = \lambda\vec{a} + \mu\vec{b}4$$  

- $$\lambda(\mu\vec{a}) = (\lambda\mu)\vec{a}$$  

### Линейная зависимость системы векторов  


- $\vec{v} = \alpha_{1} \vec{a}_{1} + \alpha_{2} \vec{a}_{2} + ... + \alpha_{n} \vec{a}_{n}$ - линейная комбинация  

- Система линейно зависима, если для линейной комбинации существует $\alpha \in {\alpha_{1}, \alpha_{2}, ... , \alpha_{n}}$ такой, что $\alpha \neq 0$  


- Доказательство : пусть $\alpha_{i} \neq 0$ и линейная комбинация равна нулю.  


1. $\alpha_{1} \vec{a}_{1} + \alpha_{2} \vec{a}_{2} + ... + \alpha_{i - 1} \vec{a}_{i - 1} + \alpha_{i} \vec{a}_{i} + ... + \alpha_{n} \vec{a}_{n} = 0$  

2. $\alpha_{i} \vec{a}_{i} = - \alpha_{1} \vec{a}_{1} - \alpha_{2} \vec{a}_{2} ... - \alpha_{i - 1} \vec{a}_{i - 1} ... - \alpha_{n} \vec{a}_{n}$  

3. т.к. $\alpha_{i} \neq 0$, то можно разделить обе части на $\alpha_{i}$  

4. Получим: $\vec{a}_{i} = -\dfrac{\alpha_{1}}{\alpha_{i}}\vec{a}_{1} - -\dfrac{\alpha_{2}}{\alpha_{i}}\vec{a}_{2} - ... - -\dfrac{\alpha_{i - 1}}{\alpha_{i}}\vec{a}_{i - 1} ... -\dfrac{\alpha_{n}}{\alpha_{i}}\vec{a}_{n}$  

5. Назовем коэффициенты при $\vec{a}_{i}$ --- $\lambda_{i}$, тогда $\vec{a}_{i} = \lambda_{1} \vec{a}_{1} + \lambda_{2} \vec{a}_{2} + ... + \lambda_{i - 1} \vec{a}_{i - 1} + ... + \lambda_{n} \vec{a}_{n}$  

6. Получим представление $\vec{a}_{i}$ в виде остальных векторов  


### Достаточное условие линейной зависимости  
***Теорема***  
- Если в системе векторов присутсвует нулевой вектор, то система линейно зависима.  


***Факт***  
- Если часть векторов системы линейно зависима, то и остальные векторы линейно зависимы  


***Факт***  
 - Если система векторов не является линейно зависимой, то она линейно независима.  

***Теорема***  
- Система линейно независима, если единственная ее линейная комбинация равна нулю.  



***Следствие***  
- Два вектора линейно зависимы тогда и только тогда, когда они колинеарны  

- Если $\vec{a} = \lambda\vec{b}$, то векторы коллинеарны, это и есть линейная зависимость.  

- $3$ вектора линейно зависимы тогда и только тогда, когда они компланарны (лежат в одной или параллельных плоскостях)  

***Упражнение***  

- Пусть $\vec{a}, \vec{b}, \vec{c} $ - линейно зависимы. Доказать компланароность $\{\vec{a}, \vec{b}, \vec{c}\}$. Доказательство : По определению линейной зависимости $\vec{a} = \lambda \vec{b} + \gamma\vec{c}$, тогда $\vec{a}$ лежит в одной плоскости, по правилу паралелограмма. Обратно : Пусть $\vec{a}, \vec{b}, \vec{c} $ - компланарны. Доказать их линейную зависимость.  
- Доказательство : так как векторы лежат в одной плоскости, можно представить один вектор из системы в виде суммы двух других.  


***Утверждение***  

- Любые 4 вектора линейно зависимы в трехмерном пространстве.  

- Доказательство : Пусть даны произвольные 4 вектора $\vec{a}, \vec{b}, \vec{c}, \vec{d}$. Приведем к одному началу эти векторы. На любой тройке этих векторов образуем куб $ABCDA'B'C'D'$. В нем  

1. $\vec{AC} = \vec{AB} + \vec{BC}$  
2. $\vec{AC'} = \vec{AC} + \vec{AA'}$  
3. $\vec{AC'} = \vec{AB} + \vec{BC} + \vec{AA'}$ . Где $\vec{AB} = \alpha\vec{a}, {BC} = \beta \vec{b}, \vec{AA'} = \gamma \vec{c}$.  

4. Получим $\vec{AC'} = D$. Вывод : $D = \alpha\vec{a} + \beta \vec{b} + \gamma \vec{b}$. Следовательно $\{\vec{D}, \vec{a}, \vec{b}, \vec{c}\}$ - линейно зависима.  

***Определение***  

**Базисом** в трехмерном пространстве называется система из трех линейно независимых (неколлинеарных) векторов. Любой вектор соответствующего пространства может быть разложен и при том единственным образом. Коэффициенты этого разложения называются координатами вектора в этом базисе  

***Упражнение***  

- Дано $\{\vec{a}, \vec{b}, \vec{c}\}$ - Базис. Тогда $v \in \RR^3 : v = \alpha\vec{a} + \beta\vec{b} + \gamma\vec{c}.$ $(\alpha, \beta, \gamma)$ - коэффициенты вектора $v$ в базисе $\{\vec{a}, \vec{b}, \vec{c}\}$  

***Определение***  

- **Ортонормированный базис** - базис из попарно перпендикулярных (ортогональных) векторов длины 1. Такие векторы принято называть $\vec{i}, \vec{j}, \vec{k}$.  

**Следствие**  

1. $\vec{a} = X\vec{i} + Y\vec{j} + Z\vec{k}$, $X, Y, Z $ - проекции.  

2. $X^2 + Y^2 + Z^2 = |\vec{a}|^2 \\ $  

3. $\cos{\alpha}^2 + \cos{\beta}^2 + \cos{\gamma}^2 = 1$  



## Лекция 09.09.2022  

### Направляющие косинусы вектора  
- Пусть $\{\vec{a}, \vec{b}, \vec{c}\}$ - ортогональный базис в трехмерном постранстве. Построим паралелепипед $ABCDA'B'C'D'$ на этом наборе векторов. Тогда $\vec{d} = \alpha \vec{a} + \beta \vec{b} + \gamma \vec{c}$  
	1. $pr_{x}{\vec{d}} = X$  
	2. $pr_{y}{\vec{d}} = Y$  
	3. $pr_{z}{\vec{d}} = Z$  
- С другой стороны :   
	1. $X = |d| \cos{\alpha}$  
	2. $Y = |d| \cos{\beta}$  
	3. $Z = |d| \cos{\gamma}$  
- Получим : $X^2 + Y^2 + Z^2 = |d|^2(\cos{\alpha}^2 + \cos{\beta}^2 + \cos{\gamma}^2) \Rightarrow \cos{\alpha}^2 + \cos{\beta}^2 + \cos{\gamma}^2 = 1$  
### Скалярное произведение векторов  

***Определение***  
- Пусть даны два вектора $\vec{a}, \vec{b}$. Скалярным произведенимем этих векторов называют число, такое что $(\vec{a}, \vec{b}) = |\vec{a}||\vec{b}|\cos{\alpha}$  

***Альтернативное определение через проекции.***  
- Пусть даны два вектора $\vec{a}, \vec{b}$ , выходящие из одного начала $O$, с концами в точках $A$ и $B$. Тогда построим перпендикуляр к $\vec{b}$ из $A$. Получим перпендикуляр $AA'$. $OA' = pr_{\vec{b}}{\vec{a}} = |\vec{a}| \cos{\alpha} \Rightarrow (\vec{a}, \vec{b}) = |\vec{a}| pr_{\vec{a}}{\vec{b}} = |\vec{b}| pr_{\vec{b}}{\vec{a}}$  

***Алгебраические свойства***  
1. $(\vec{a}, \vec{b}) = (\vec{b}, \vec{a})$  
2. $(\vec{a} + \vec{b}, \vec{c}) = (\vec{a}, \vec{c}) + (\vec{b}, \vec{c})$  
3. $(\lambda \vec{a}, \vec{b}) = \lambda (\vec{a}, \vec{b})$  
4. $(\vec{a}, \vec{a}) = \vec{a}^2 = |\vec{a}|^2$  

***Упражнение***  
Докажем $(2)$:  
- $(\vec{a}, \vec{c}) = |c|pr_{\vec{c}}{\vec{a}}$  
- $(\vec{b}, \vec{c}) = |c|pr_{\vec{b}}{\vec{a}}$  
- $(\vec{a} + \vec{b}, \vec{c}) = |c|pr_{\vec{c}}{\vec{a} + \vec{b}} = |c|(pr_{\vec{c}}{\vec{a}} + pr_{\vec{c}}{\vec{b}})$  

***Геометрические свойства***  
1. $\vec{a} \perp \vec{b} \Rightarrow (\vec{a}, \vec{b}) = 0$. Стоит заметить что обратно не следует в том случае, если $\vec{a} = \vec{0}$ или $\vec{b} = \vec{0}$  
2. $\phi < 90 \Rightarrow (\vec{a}, \vec{b}) > 0$  $\textbf{Вытекает из определения скаляного произведения}$     
3. $\phi > 90 \Rightarrow (\vec{a}, \vec{b}) < 0 $  $\textbf{Вытекает из определения скаляного произведения}$  

***Определение***  

- $\cos{\phi} = \frac{(\vec{a}, \vec{b})}{|\vec{a}| |\vec{b}| }$  

***Упражнение***  
- Выразим скалярное произведение через координаты перемножаемых векторов. Рассмотрим векторы $\vec{a}, \vec{b}, \vec{c}$ в базисе $\{\vec{i}, \vec{j}, \vec{k}\}$.  
-  Тогда :  
1. $\vec{a} = X_{1}\vec{i} + Y_{1}\vec{j} + Z_{1}\vec{k}$  
2. $\vec{b} = X_{2}\vec{i} + Y_{2}\vec{j} + Z_{2}\vec{k}$  
- $(\vec{a}, \vec{b}) = (X_{1}\vec{i} + Y_{1}\vec{j} + Z_{1}\vec{k}, X_{2}\vec{i} + Y_{2}\vec{j} + Z_{2}\vec{k})$. Т.к. $\{\vec{i}, \vec{j}, \vec{k}\}$ - ортонормированный, то $(\vec{i}, \vec{j}) = (\vec{i}, \vec{k}) = (\vec{j}, \vec{k}) = 0$, а $(\vec{i}, \vec{i}) = (\vec{k}, \vec{k}) = (\vec{j}, \vec{j}) = 1$  $\Rightarrow (\vec{a}, \vec{b}) = X_{1}X_{2}(\vec{i}, \vec{i}) + Y_{1}Y_{2}(\vec{k}, \vec{k}) + Z_{1}Z_{2}(\vec{j}, \vec{j}) =X_{1}X_{2} +  Y_{1}Y_{2} + Z_{1}Z_{2}$  
    Скалярное произведение можно рассматривать как произведение силы $F$ на путь $AB$. $\vec{F} = |F||AB|\cos{\phi}$.  
### Векторное произведение векторов  
***Обозначение***  
- $[\vec{a}, \vec{b}]$  

***Определение***  
- $[\vec{a}, \vec{b}]$ - вектор, такой что: $|[\vec{a}, \vec{b}]| = |\vec{a}||\vec{b}| \sin \phi$. Кроме того этот вектор $\perp$ плоскости перемножаемых векторов.  

***Определение***  
- Векторы $\vec{a}, \vec{b}, \vec{c}$ образуют **правую тройку**, если с конца $\vec{a}$ вращение от $\vec{b}$ к $\vec{c}$ по кратчайшему направлению предоставляется происходящим против часовой стрелки, при условии приведения к одному началу.  

- Тут показывать надо, но попробую описать словами: берем правую руку, и нумеруем пальцы начиная с большого (большой — первый вектор, указательный — второй, средний — третий). Такую тройку векторов назовём «правой».Аналогично можно сделать для левой руки. Суть в том, что никакую правую тройку векторов невозможно перевести в  левую (так чтобы в процессе тройка оставалось базисом)  

***Пример***  

- $\{[\vec{a}, \vec{b}], \vec{a}, \vec{b}\}$ является правой тройкой векторов.  

***Геометрические свойства.***  
1. Если $\vec{a}, \vec{b}$ - коллинеарны, то $[\vec{a}, \vec{b}] = \vec{0}.$ Т.к $[\vec{a}, \vec{b}] = |\vec{a}||\vec{b}| \sin{\phi}$. $\phi = 0$ или $\phi = \pi \Rightarrow \sin{\phi} = 0$.  
2. $ \textbf{Геометрический смысл.}$ $|[\vec{a}, \vec{b}]| = S_{AB} $. $[\vec{a}, \vec{b}]$ = $S_{AB} \vec{e} $. Где $AB$ - паралелограмм, образованный на $\{\vec{a}, \vec{b}\}$, а $\vec{e}$ - единичный вектор вдоль $[\vec{a}, \vec{b}]$.  

***Алгебраические свойства***  

1. $[\vec{a}, \vec{b}] = - [\vec{b}, \vec{a}]$. Следует из ориентации.  
2. $[\vec{a} + \vec{b}, \vec{c}] = [\vec{a}, \vec{c}] + [\vec{b}, \vec{c}]$. Распределительное свойство.  
3. $[\vec{a}, \vec{a}] = \vec{0}$. $(\vec{a}$ - коллинеарен $\vec{a})$  

### Смешанное произведение векторов  
***Определение***  
- $([\vec{a}, \vec{b}], \vec{c})$  

***Геометрическое свойство***  
- $([\vec{a}, \vec{b}], \vec{c}) = V_{ABCDA'B'C'D'}$. Где $ABCDA'B'C'D'$ - паралелепипед, построенный на тройке $\{\vec{a}, \vec{b}, \vec{c}\}$. (Взят с плюсом, если тройка правая и с минусом иначе).  

***Упражнение***  
Докажем : $([\vec{a}, \vec{b}], \vec{c}) = V_{ABCDA'B'C'D'}$  
1. Действительно, $[\vec{a}, \vec{b}]$ - есть $\perp$ к плоскости $A_{\vec{b}, \vec{a}} \Rightarrow [\vec{a}, \vec{b}] = S_{AB}$.  
2. $([\vec{a}, \vec{b}], \vec{c}) = |\underbrace{[\vec{a}, \vec{b}]}_{S_{AB}}||\vec{c}|\cos{\gamma} = |[\vec{a}, \vec{b}]| \cdot pr_{[\vec{a}, \vec{b}]}(c) = V_{ABCDA'B'C'D'}$  

***Следствие***  
- $([\vec{a}, \vec{b}], \vec{c}) = (\vec{a}, [\vec{b}, \vec{c}]) = (\vec{a}, \vec{b}, \vec{c})$  

***Свойства смешанного произведения векторов***  
1. $(\vec{a}, \vec{b}, \vec{b}) = (\vec{a}, [\vec{b}, \vec{b}] = \vec{0}) = 0$  
2. Необходимое и достаточное условие компланарности трех векторов : $(\vec{a}, \vec{b}, \vec{c}) = 0$.  
3.  Выражение векторного произведения через координаты перемножаемых векторов. Пусть:   
1. $\vec{a} = X_{1}\vec{i} + Y_{1}\vec{j} + Z_{1}\vec{k}$  
2. $\vec{b} = X_{2}\vec{i} + Y_{2}\vec{j} + Z_{2}\vec{k}$  
3. $[\vec{a}, \vec{b}] = [X_{1}\vec{i} + Y_{1}\vec{j} + Z_{1}\vec{k}, X_{2}\vec{i} + Y_{2}\vec{j} + Z_{2}\vec{k}]= X_{1}X_2\underbrace{[\vec{i}, \vec{i}]}_{\vec{0}} + X_{1}Y_2\underbrace{[\vec{i}, \vec{j}]}_{\vec{k}} + Z_{1}Z_2\underbrace{[\vec{k}, \vec{k}]}_{\vec{0}} + X_{1}Z_{2}\underbrace{[\vec{i}, \vec{k}]}_{-\vec{j}} + Y_{1}Y_2\underbrace{[\vec{j}, \vec{j}]}_{\vec{0}} + Y_{1}Z_{2}\underbrace{[\vec{j}, \vec{k}]}_{\vec{i}} \dots =$  
   $\begin{equation*}  
                \begin{vmatrix}  
                \vec{i} & \vec{j} & \vec{k} \\  
                X_{1} & Y_{1} & Z_{1} \\  
                X_{2}  & Y_{2} & Z_{2}   
                \end{vmatrix}  
                =  
                \vec{i} \cdot  
                \begin{vmatrix}  
                Y_{1} & Z_{1} \\  
                Y_{2} & Z_{2}  
                \end{vmatrix}  
                -\vec{j} \cdot  
                \begin{vmatrix}  
                X_{2} & Z_{1} \\  
                X_{2} & Z_{2}  
                \end{vmatrix}   
               + \vec{k} \cdot  
                           \begin{vmatrix}  
                           X_{1} & Y_{1} \\  
                           X_{2} & Y_{2}  
                           \end{vmatrix}   
   \end{equation*}$  


***Свойства***  
1. $\vec{a} = X_{1}\vec{i} + Y_{1}\vec{j} + Z_{1}\vec{k}$  
2. $\vec{b} = X_{2}\vec{i} + Y_{2}\vec{j} + Z_{2}\vec{k}$  
3. $\vec{c} = X_{3}\vec{i} + Y_{3}\vec{j} + Z_{3}\vec{k}$  

Получим :  
- $ \begin{equation*}  
            (\vec{a}, \vec{b}, \vec{c}) = ([\vec{a}, \vec{b}], \vec{c}) \Rightarrow (\vec{a}, \vec{b}, \vec{c}) =   
            \begin{vmatrix}  
            X_{1} & Y_{1} & Z_{1} \\  
            X_{2}  & Y_{2} & Z_{2}  \\  
            X_{3}  & Y_{3} & Z_{3}   
            \end{vmatrix}  
        \end{equation*}$  

***Упражнение***  

**С помощью смешанного произведения легко доказываются свойства векторного произвдения}**  

1.  Тривиально  
2. Умножим скалярно обе части на $\vec{b}$. $([\vec{a} + \vec{b}, \vec{c}], \vec{b}) = ([\vec{a}, \vec{c}], \vec{b}) + \underbrace{([\vec{b}, \vec{c}], \vec{b})}_{0}$. Поскольку $\{[\vec{a} + \vec{b}, \vec{c}], \vec{a}, \vec{b}\} \perp \vec{c}$, значит они компланарны $\Rightarrow$ один из них - линейная комбинация двух других $\Rightarrow S_{[\vec{a} + \vec{b}, \vec{c}]} = S_{[\vec{a}, \vec{c}]} + S_{[\vec{b}, \vec{c}]}$.  