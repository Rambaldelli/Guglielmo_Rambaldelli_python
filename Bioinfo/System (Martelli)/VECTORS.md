# VECTORS

### sterling formula (aprox of factorial)

n! ~ (n/e)^n * sqrt(2* pi* n)

### SCALAR PRODUCT

Between two vectors is the sum of the multiplication of each element 

SVM:

computer scalar vector matrix than => put the element with a solution, multiply by the class combination and by the scalar product itself 

### HYPERPLANE

-A plane passing through the origin can be defined with as the set of the vectors that are perpendicular to a given vector W

-A particular line not passing trough the origin is fixed when the projection of points of the line on vector W is  fixed to a value p 

(the sign of p determinate the side of the W vector the line is in: positive in the same direction as W)

=> ![1567680545111](/home/rambo/.config/Typora/typora-user-images/1567680545111.png)

**N.B.: If we multiply everything by a number the plane dose not change**

### PARALLEL HYPERPLANE

Modifying b we create parallel HP.

## DISTANCE 

### TWO HP

It is the difference between the  projection on W of the two plane.

![1567758861492](/home/rambo/.config/Typora/typora-user-images/1567758861492.png)

### POINT TO HP

![1567759113300](/home/rambo/.config/Typora/typora-user-images/1567759113300.png)

# LAGRANGE MULTIPLIERS (EQUALITY CONST.)

Maximize or minimize a function under a equality constrain.

=> when the function is parallel to a level line = the function is perpendicular to the gradient = the two gradient are collinear we are in a max \ min

**The relationship between the two is the Lagrange multy.**

N.B.: In SVM the sign became + instead of -

![1567763253981](/home/rambo/.config/Typora/typora-user-images/1567763253981.png)

**<u>Then minimize the function computing all the partial derivative in respec to the parameters and of the Lagrangian function and put them = 0.</u>**

​	-If we have more than one constrain we need a Lagrangian multy for each one.

![1567763711550](/home/rambo/.config/Typora/typora-user-images/1567763711550.png)

## INEQUALITY

<img src="/home/rambo/.config/Typora/typora-user-images/1567764125989.png" alt="1567764125989" style="zoom:50%;" />

When the two gradient have opposite direction (lambda negative in the Lagrangian) it mean that we are not in a max \ min.

### Karush-Kuhn-Tucker conditions

**N.B.: In support vector machine the lagrangian is written with the opposite sign and so the  condition are the  opposite** (es here)

![1567764311953](/home/rambo/.config/Typora/typora-user-images/1567764311953.png)

AND

![1567764777356](/home/rambo/.config/Typora/typora-user-images/1567764777356.png)

And so we can put =0 the one that are outside the KKT condition.

## DUAL LAGRANGIAN

Make the Lagrangian only dependent on the Lagrangian multy.

=> make partial derivative of Lagrangian in respect to variables (W,b(got eliminated in the simplification),y) than substitute it in the original Lagrangian to leave only the Lagrangian multy in the Lagrangian

**=> we have the dual Lagrangian to maximize that is only in ALPHA.**

![1568021082240](/home/rambo/.config/Typora/typora-user-images/1568021082240.png)

REMEMBER THIS FORMULA



Then:

![1568020053517](/home/rambo/.config/Typora/typora-user-images/1568020053517.png)

![1568020686611](/home/rambo/.config/Typora/typora-user-images/1568020686611.png)

# SCALAR PRODUCT

It is the sum between the multiplication between the elements of two vectors.