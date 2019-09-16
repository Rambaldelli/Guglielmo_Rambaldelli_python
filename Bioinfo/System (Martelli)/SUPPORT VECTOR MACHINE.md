# SUPPORT VECTOR MACHINE

When you put a dividing line in a problem you want to allow for the **MAXIMUM MARGIN**.

​	-distance between the two parallel line touching the borders of the points.



**=> find support vectors: the points that lies on the margin**

​	Every other point is useless for the classification

## MARGIN CHOICE

We have to find an hyperplane as a boundary and than create the two parallel one as margin.

=> We rescale everything to write the two margin and their distance as:

![1567759651909](/home/rambo/.config/Typora/typora-user-images/1567759651909.png)

**We need to minimize the norm of W to maximize the margin.**

## CLASS SEPARATION

The distance of the point in the  positive class the distance from the border must be equal of greater of the distance of the margin from the border.

We need to find W and b and so we have **N+1 parameters** 

X = point as vector

Y = class of the point



![1567760547228](/home/rambo/.config/Typora/typora-user-images/1567760547228.png)

When we multiply by -1 in the other side of the plane we end up with only one condition:

![1567760756911](/home/rambo/.config/Typora/typora-user-images/1567760756911.png)

## CONCLUSION

We **minimize** half of the square to make it derivable and easier and rescale to make = 1. 

![1567760867454](/home/rambo/.config/Typora/typora-user-images/1567760867454.png)

**We have one constrains for each point of the set.**

**Lagrangian (but with sign + instead of -):**

![1567765128037](/home/rambo/.config/Typora/typora-user-images/1567765128037.png)

We can use **double** Lagrangian (**has to be MAXIMIZED**):

![1568020053517](/home/rambo/.config/Typora/typora-user-images/1568020053517.png)



**<u>If alpha is greater  than 0 the  point is a support vector.</u>**

# SOLUTION

-compute alpha from the double lagrangian

-compute W with the summation above **using only** the support vector.

-use the hyperplane formula for a point on the margin (=1 or =-1 depending on the side) to find b.



# LINEAR PROBLEM

Dual Lagrange multipliers.

![1568020089835](/home/rambo/.config/Typora/typora-user-images/1568020089835.png)

TEST A NEW POINT

![1568022994443](/home/rambo/.config/Typora/typora-user-images/1568022994443.png)



# NON LINEAR PROBLEM

## SOFT MARGIN (ALMOST LINEARLY SEPARABLE)

Some point can go to the other side of the margin but with a **positive** penalty (what is needed to 'bring' the point to the right side of the margin).

![1568106203973](/home/rambo/.config/Typora/typora-user-images/1568106203973.png)

We have to maximize the MARGIN (1\2 * ||W|| ^2) but minimize the error and so the constant C balance the two.

#### OPTIMIZATION

The optimization is the same as before with just an upper bound to C:



![1568107193573](/home/rambo/.config/Typora/typora-user-images/1568107193573.png)

MIU is the Lagrangian multiplier of PSI (the error)

SO:

![1568107425410](/home/rambo/.config/Typora/typora-user-images/1568107425410.png)

The solution depends on C:

-C going to infinite = hard margin

-C going to 0 (**NOT == 0**) = allow every error 

## KERNEL (NON LINEAR)

The scalar product is a Kernel and can be used to solve non linearly separable problem.

We need to find a transformation (theta) to remap the problem to feature  space (usually different dimensions).

ES.: In the XOR problem multiply x1 and x2.

Given that we operate in the feature space we have to replace the scalar product with tho one in the feature space.

=> replace the scalar product with another function and find the one that can solve the problem.



![1568110007299](/home/rambo/.config/Typora/typora-user-images/1568110007299.png)

SO the Lagrangian became:



![1567679539512](/home/rambo/.config/Typora/typora-user-images/1567679539512.png)

![1568110155055](/home/rambo/.config/Typora/typora-user-images/1568110155055.png)



And to test  a  new point Z:

![1568110289674](/home/rambo/.config/Typora/typora-user-images/1568110289674.png)

#### KERNEL

A function Theta that take two points of the input space and give out a number in the feature space(usually much bigger than the input space).

=> the standard scalar product is a basic kernel: it consider two point similar if the angle between them is smaller than 90 degree=> on the same side.

We don't need to know the feature space, it is enough to be able to compute the scalar product and so change the definition of similarity that it enforce.

Every function of a kernel is a kernel.

=> **we don't know the feature space we just know the kernel by trial and error.**

##### COMPUTE FEATURE SPACE

From the kernel we need to compute it and than divide each component in a way that make the scalar product evident (split the constant)

=> the number of dimension is the number of component  of the computed kernel.

![1568195978190](/home/rambo/.config/Typora/typora-user-images/1568195978190.png)

Once we know it we can use it to compute the transformation of the points in the feature space.

And then we can use:

![1568196406817](/home/rambo/.config/Typora/typora-user-images/1568196406817.png)

to compute the vector W.

=> it is **one** of the dimension of the feature space.

##### MERCER CONDITION FOR KERNEL

![1568111892596](/home/rambo/.config/Typora/typora-user-images/1568111892596.png)

##### BASIC KERNEL

![1568112018284](/home/rambo/.config/Typora/typora-user-images/1568112018284.png)

### POLYNOMIAL KERNEL

The size of the feature space depends on the degree of the polynomial, the component are:

**first type** (xy+1)^d: component of degree d

-feature space:![1568280286998](/home/rambo/.config/Typora/typora-user-images/1568280286998.png)

**second type** (xy)^d: all component up to degree d

-feature space roughly:  **n^d / d!**

or exactly :![1568280301329](/home/rambo/.config/Typora/typora-user-images/1568280301329.png)

### GAUSSIAN KERNELS (RBF)

![1568283952405](/home/rambo/.config/Typora/typora-user-images/1568283952405.png)

It is a Gaussian curve so it is max when the two vector are similar and smaller when different.

=> given that an exponential can be expressed as an infinite sum it is an infinite space kernel

##### SIGNMA

Very small we risk overfitting because it 'restrict' the definition of similarity.





#### HYPER PARAMETERS

-C (soft margin)

-Kernel and his constant (d)



### OVER FITTING

The number of support vectors in the feature space must be a small fraction of all the points to have a good solution. 

If we incerase to much d we end up with all the points as support vectors.