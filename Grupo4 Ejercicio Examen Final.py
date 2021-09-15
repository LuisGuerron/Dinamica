#!/usr/bin/env python
# coding: utf-8

# **Rick y Morty descubren la Teoría del Caos**
# 
# Mientras Rick y Morty daban un paseo, encontraron una estructura gigante en medio de la nada, notaron que se comprendía por dos eslabones unidos por una articulación. Rick no podía esperar a disparar en el eslabón inferior para ver lo que sucedía, la fuerza aplicada fue tan grande que los dos eslabones empezaron a moverse de  forma extraña, mientras el eslabon superior solamente giraba al rededor del punto superior, el eslabón inferior  daba vueltas y se movía de forma caótica. Fue así, que decidieron estudiar este sistema más a fondo.

# ![g4_rickymorty.png](attachment:g4_rickymorty.png)

# **Evaluación Final**
# 
# **Resuelva el siguiente ejercicio:**
# 
# **Encuentre las ecuaciones de movimiento del péndulo doble que encontraron Rick y Morty.**

# ![g4_ejercicioenunciado.png](attachment:g4_ejercicioenunciado.png)

# **Planteamiento y aclaraciones**
# 
# -Los eslabones tienen longitudes $l_1$ y $l_2$ respectivamente, así como también masas $m_1$ y $m_2$ respectivamente.
# 
# -Para encontrar las ecuaciónes, suponga que el péndulo doble ya se encuentra oscilando lentamente cuando la fuerza es apicada.
# 
# -Dentro del cálculo de los grados de libertad y el análisis de restricciones se debe considerar las mismas para cada cuerpo de forma independiente.
# 
# -Dado que el sistema es dinámicamente complejo, se puede asumir que la masa y longitud de los eslabones son iguales. Se recomienda aplicar esta suposición en la resolución por Leyes de Newton.
# 
# -Para el cálculo por el método de Lagrange, se considera la posición y velocidad del centro de masa de cada uno de los eslabones, esto debido a que son sólidos rígidos.
# 
# -Durante la resolución utilizando Lagrange, se recomienda tener claros los conceptos de derivaciónes parciales ya que se pueden cometer errores en el proceso.

# **Grados de libertad**
# 
# En el sistema se cuenta con dos sólidos rígidos que se pueden modelar como barras de masa $m_1$ y $m_2$ respectivamente y longitudes $l_1$ y $l_2$ respectivamente.
# 
# $$gdl= 6c+3p-R $$
# 
# $$gdl= 6(2)+3(0)-R $$
# 
# $$gdl=12-\left\{\begin{matrix} \vec{x_{1}} & \vec{x_{2}} \\ 
# \vec{y_{1}} & \vec{y_{2}} \\ \vec{k_{1}} & \vec{k_{2}} \\ \vec{\circlearrowright{x_{1}}} & \vec{\circlearrowright{x_{1}}}\\ \vec{\circlearrowright{y_{1}}} & \vec{\circlearrowright{y_{1}}}\\ \end{matrix}\right.$$
# 
# $$ gdl= 12-10 $$
# 
# $$ gdl= 2$$
# 
# Finalmente, en el sistema de péndulo doble hay dos grados de libertad correspondientes a rotación con respecto al eje $\vec{k}$
# 

# **Método: Leyes de Newton**
# 
# Para aplicar las leyes de Newton en el sistema de estudio, se procede a realizar los diagramas de cuerpo libre y se determina un sstema de ejes coordenados para la resolución.
# 
# **Diagrama de cuerpo libre**
# 
# En las siguientes imágenes se indican las fuerzas que actúan en cada uno de los eslabones y además también se eindica que el sistema de referncia determinado es el Radial - Transversal, dado que los grados de libertad del movimiento son de rotación y este sistema simplifica el análisis.
# 
# ![DCL.png](attachment:DCL.png)

# En este caso, es conveniente realizar el diagrama de cuerpo libre de cada uno de los eslabones, por lo que se tiene lo siguiente:

# **DCL 1**
# ![DCL1.1.png](attachment:DCL1.1.png)

# **DCL 2**
# ![DCL1.2.png](attachment:DCL1.2.png)

# **Análisis de fuerzas**
# 
# Para el Cuerpo 1, se establece la sumatoria de fuerzas en el eje radial y en el eje transveral.
# 
# $$ \varSigma \vec{F_{er}} = m_{1} \vec{a_{er}}$$ 
# 
# $$-  \vec{R_{L}} + m_{1}g cos\theta_{1} + R_{L2/L1}cos(\theta_{2} - \theta_{1}) = m_{1} \vec{a_{er}} $$
# 
#  $$\varSigma \vec{F_{e\theta}} = m_{1}\vec{a_{e\theta}}$$
# 
# $$ - m_{1}g sin\theta_{1} + R_{L2/L1} sin(\theta_{2} - \theta_{1}) = m_{1} \vec{a_{e\theta}}$$
# 
# Hay  que  notar  que:
# 
# $ \vec{a} = \vec{a_{er}} + \vec{a_{e\theta}}$
# 
# $ \vec{a} = \left( \ddot{r} - r\dot{\theta} \right)\vec{er} + \left(r \ddot{\theta} + 2\dot{r}\dot{\theta} \right)\vec{e\theta}$
# 
# De donde para nuestro caso: 
# 
# 
# $\vec{a_{er}} = - \frac{L}{2} \dot{\theta}\vec{er}$
# 
# $\vec{a_{e\theta}} =  \frac{L}{2} \ddot{\theta}\vec{e\theta}$
# 
# Por lo tanto:
# 
# $$ Ec(1)$$  $ - R_{L} + m_{1} g cos\theta_{1} + R_{L2/L1} * cos \left( \theta_{2} - \theta_{1} \right) = - m_{1} \frac{L}{2} \dot{\theta}\vec{er} $ 
# 
# $$ Ec(2)$$  $ - m_{1} g sin\theta_{1} + R_{L2/L1} * sin\left(\theta_{2} - \theta_{1}\right) = m_{1} \frac{L}{2} \ddot{\theta} \vec{e\theta}$
# 
# Sea ahora:
# 
# $$ Ec(3) $$ $\varSigma\vec{\tau_{|M}} = \frac{d\vec{H_{k/M}}}{dt} + \vec{V_{M/o}} x \vec {p_{k/o}}$
# 
# 
# Notamos que 
# 
# $\vec{V_{k/o}} x \vec {p_{k/o}} = 0$
# ya que poseen la misma dirección de la velocidad, y con el producto cruz se hace cero.
# 
# entonces:
# 
# $\varSigma\vec{\tau_{|M}} = \frac{d\vec{H_{k/M}}}{dt}$
# 
# $\vec{H_{k/M}} = I_{zz/M} * \dot{\theta}\vec{k}$ ,  considerando; $ I_{zz/M} = \frac{m_{1}*L^2}{3}$
# 
# $\vec{H_{k/M}} = \frac{m_{1}*L^2}{3} * \dot{\theta}\vec{k}$
# 
# $\frac{d\vec{H_{k/M}}}{dt} = \frac{m_{1}*L^2}{3} * \ddot{\theta}\vec{k} $ 
# 
# Luego, por la sumatoria de torques tenemos:
#     
# $\frac{d\vec{H_{k/M}}}{dt} = - m_{1} g \frac{L}{2}  * sin\theta_{1}\vec{k} + R_{L2/L1} L * sin \left( \theta_{2} - \theta_{1} \right)$
# 
# de donde se obtendría la siguiente expresión:
# 
# $ \frac{m_{1}*L^2}{3} * \ddot{\theta}\vec{k} = - m_{1} g \frac{L}{2}  * sin\theta_{1}\vec{k} + R_{L2/L1} L * sin \left( \theta_{2} - \theta_{1} \right)\vec{k}$
# 
# De las ecuaciones Ec(1) y Ec(2) se tiene que:
# 
# $R_{L2/L1}\vec{er} = \left( \frac{R_{L} - m_{1}g * cos\theta_{1} - m_{1}\frac{L}{2}\dot{\theta}}{ cos(\theta_{2} - \theta_{1})}\right)\vec{er}$
# 
# $R_{L2/L1}\vec{e\theta} = \left( \frac{ m_{1}g * sin\theta_{1} + m_{1}\frac{L}{2}\ddot{\theta_{1}}}{ sin(\theta_{2} - \theta_{1})}\right)\vec{e\theta}$
# 
# Notamos que podemos expresarlas como:
# 
# $R_{L2/L1}\vec{er} = A \vec{er}$
# 
# $R_{L2/L1}\vec{e\theta} = B \vec{e\theta}$
# 
# Vamos a considerar el torque que realiza esta fuerza:
# 
# \begin{equation}
# \begin{pmatrix}
# \vec{er} & \vec{e\theta} & \vec{k}\\
# L & 0 & 0\\
# A & B & 0
# \end{pmatrix}
# \end{equation}
# 
# De forma que el resultado:
# 
# $LB\vec{k}$
# 
# De forma que las expresiones anteriores nos quedan de la siguiente manera:
# 
# $$Ec(4)$$  $$ \frac{m_{1}*L^2}{3} * \ddot{\theta}\vec{k} = - m_{1} g \frac{L}{2}  * sin\theta_{1}\vec{k} + \left( \frac{m_{1}Lg * sin\theta_{1} + m_{1} \frac{L^2}{2} \ddot{\theta_{1}}}{sin \left( \theta_{2} - \theta_{1} \right)} \right) \vec{k}$$
# 
# $$ \ddot{\theta}\left(  \frac{m_{1}L^2}{3} - \frac{m_{1}\frac{L^2}{2}}{sin(\theta_{2} - \theta_{1})}\right) \vec{k} = \left( \frac{m_{1}L g * sin\theta_{1}}{sin(\theta_{2} - \theta_{1}} - m_{1}g\frac{L}{2}sin\theta_{1}\right)$$
# 
# $$ \ddot{\theta_{1}}\vec{k} = \frac{3g sin\theta_{2} * \left(1 - \frac{sin(\theta_{2} - \theta_{1})}{2}\right)}{sin(\theta_{2} - \theta_{1}) - \frac{3}{2}}\vec{k}$$
# 
# Luego considerndo la segunda parte de la articulación:
# 
# Para el Cuerpo 2 se establece la sumatoria de fuerzas en el eje radial y en el eje transversal.
# 
# e tiene que:
# 
# $ \varSigma \vec{F_{er}}  = m_{2} * \vec{a_{er}}$
# 
# $ F sin\theta_{2} -  R_{L2/L1}*cos(\theta_{2} - \theta_{1}) + m_{2} g * cos \theta_{2} = m_{2} \vec{a_{er}}  $
# 
# $ \varSigma \vec{F_{e\theta}} = m_{2} * \vec{a_{e\theta}}$
# 
# $ F cos\theta_{2} + R_{L2/L1}*sin(\theta_{2} - \theta_{1}) + m_{2} g * sin \theta_{2} = m_{2} \vec{a_{e\theta}}  $
# 
# de la misma manera:
# 
# $\vec{a_{er}} = - \frac{L}{2} \dot{\theta}\vec{er}$
# 
# $\vec{a_{e\theta}} =  \frac{L}{2} \ddot{\theta}\vec{e\theta}$
# 
# Se tiene por definición que:
# 
# $$ Ec(5) $$ $\varSigma\vec{\tau_{|k}} = \frac{d\vec{H_{B/k}}}{dt} + \vec{V_{k/o}} x \vec {p_{B/o}}$
# 
# Para este caso notamos que:
# 
# $\vec{V_{k/o}} = L \dot{\theta_{1}} * cos\theta_{1} \vec{i} + L \dot{\theta_{1}} * sin\theta_{1} \vec{j}$
# 
# $\vec{V_{k/o}} = C1  \vec{i} + C2 \vec{j} $
# 
# 
# además:
# 
# $\vec{V_{B/o}} = \vec{V_{k/o}} + \vec{V_{B/k}}$
# 
# Entonces:
# 
# $\vec{V_{B/o}} = \left( L \dot{\theta_{1}} * cos\theta_{1} + L \dot{\theta_{2}} * cos\theta_{2} \right) \vec{i} + \left(  L \dot{\theta_{1}} * sin\theta_{1} + L \dot{\theta_{2}} * sin\theta_{2}\right) \vec{j}$
# 
# $\vec{V_{B/o}} = D1  \vec{i} + D2 \vec{j} $ , Sabiendo que: $\vec{p_{B/o}} = m * \vec{V_{B/o}}$
# 
# Por lo que:
# 
# $\vec{V_{k/o}} x \vec {p_{k/o}} = $
# 
# \begin{equation}
# \begin{pmatrix}
# \vec{i} & \vec{j} & \vec{k}\\
# C1 & C2 & 0\\
# m D1 & m D2 & 0
# \end{pmatrix}
# \end{equation}
# 
# 
# $ = \left( C1 * m D2 - C2 * m D1\right) \vec{k} $
# 
# Se tiene entonces que la expresión simplificada esta dada por:
# 
# $$Ec(6)$$ $\vec{V_{k/o}} x \vec {p_{k/o}} = 0 \vec{k} $
# 
# Luego se considera la sumatoria de torques con respecto a k:
# 
# $\varSigma\vec{\tau_{|k}} = - \frac{L}{2} m_{2} g sin \theta_{2} + L F sin (90 - \theta_{2})$
# 
# $$ Ec(7) $$ $\varSigma\vec{\tau_{|k}} = - \frac{L}{2} m_{2} g sin \theta_{2} + L F cos (\theta_{2})$
# 
# Teniendo en cuenta a las expresiones Ec(6) y Ec(7) con la Ec(5), y además, conociendo que:
# 
# $\frac{d\vec{H_{B/k}}}{dt} = I_{zz|k} * \ddot{\theta_{2}} \vec{k}$
# 
# De donde:
# 
# $$I_{zz|k} = \frac{m_{2} L^2}{3}$$
# 
# Entonces:
# 
# $$- \frac{L}{2} m_{2} g sin \theta_{2} + L F cos (\theta_{2}) = \frac{m_{2} L^2}{12} * \ddot{\theta_{2}}\vec{k} $$
# 
# De forma que tenemos:
# 
# $$ \ddot{\theta_{2}} \vec{k} = \left[ \frac{3 F}{m_{2}L}cos\theta_{2} - \frac{g}{6 L}sin\theta_{2} \right] \vec{k}$$
# 
# 
# 
# 
#     

# **Método de Lagrange**
# 
# El Lagrangiano viene dado por:
# $$ \mathscr{L}= T-V $$
# Dónde:
# T: Energía cinética
# V: Energía potencial
# 
# El método de Lagrange establece que:
# $$ \frac{\mathrm{d} }{\mathrm{d} t}\left ( \frac{\partial{\mathscr{L}}}{\partial \dot{q_j}} \right )-\frac{\partial{\mathscr{L}}}{\partial {q_j}}=Q_j $$
# $$ \frac{\mathrm{d} }{\mathrm{d} t}\left ( \frac{\partial{T}}{\partial \dot{q_j}} \right )-\frac{\mathrm{d} }{\mathrm{d} t}\left ( \frac{\partial{V}}{\partial \dot{q_j}} \right )-\frac{\partial{T}}{\partial {q_j}}+\frac{\partial{T}}{\partial {q_j}}=Q_j $$
# Dónde:
# $$q_j: coordenadas generales$$
# $$Q_j: fuerzas generalizadas$$
# 
# De la expresión, se puede decir que:
# $$ \frac{\mathrm{d} }{\mathrm{d} t}\left ( \frac{\partial{V}}{\partial \dot{q_j}} \right )=0 $$
# 
# Porque la energía potencial se caracteriza por depender de la posición del cuerpo o partícula analizado, y no por la velocidad que este posee.
# 
# **Paso 1: g.d.l del sistema y designación de las coordenadas generales.**
# 
# -Por el ítem 1.2 se conoce que el sistema cuenta con dos grados de libertad de rotación con respecto al eje de referencia $\vec{k}$.
# 
# -Determinamos a las coordenadas generales $q_j$, tal que cada eslabón tiene sus propias coordenadas polares, por lo tanto se tiene a los ejes transversales: $\theta_1$ y $\theta_2$.
# 
# Se emplea un sistema de referencia inercíal $xy$ para facilitar algunos cálculos posteriores.
# 
# **Paso 2: Verificación del sistema**
# 
# -Las coordenadas generales escogidas son independientes ya que cuando se fijan todos menos una coordenada, aún conserva rango de movimiento completo en la coordenada libre. Si fijamos a $\theta_1$, el movimiento del sistema aún es posible en la segunda coordenada, y de igual forma, si fijamos a $\theta_2$, el movimiento sigue existiendo.
# 
# -Las coordenadas son completas porque son capacess de localizar todas las partes deld sistema, todo el tiempo, siendo los necesarios para caracterizar el movimiento del sistema.
# 
# -El sistema es holonómico, debido a que la se tienen dos coordenadas generales y dos grados de libertad que definen al movimiento.
# 
# **Paso 3: Análisis de energías**
# 
# -**Energía cinética:** De forma general, la energía cinética se define como:
# $$ T= \frac{1}{2}mv^2 $$
# 
# Es decir, que el término depende de la masa y velocidad del cuerpo, por lo tanto, observando el caso particular de un péndulo doble, se observa que los dos eslabones tendrán velocidad lineal cuando una fuerza genere el movimiento del sistema, o incluso si este se deja caer desde determinada altura.
# 
# Además, ambos eslabones tienen movimientos rotacionales, por lo que se determina un tipo de energía cinética que depende de la inergia del cuerpo y su velocidad angular:
# $$ T= \frac{1}{2} J\dot{ \theta }^{2} $$
# 
# Entonces:
# $$ T= \frac{1}{2} m_{1}(\dot{x_1}^{2}+\dot{y_1}^{2})+ \frac{1}{2} m_{2}(\dot{x_2}^{2}+\dot{y_2}^{2})+ \frac{1}{2} J_{1}\dot{ \theta_1 }^{2}+J_{2}\dot{ \theta_2 }^{2} $$
# 
# -**Energía potencial:** De forma general, la energía cinética se define como:
# $$ V=mg{y} $$
# 
# El término depende de la masa del cuerpo, la aceleración de la gravedad y su posición vertical, por lo tanto, existe una energía potencial para cada uno de los eslabones, tal que:
# 
# $$ V=m_{1}g{y_1}+m_{2}g{y_2} $$
# 
# -**Localización del centro de masa:** Al ser sólidos rígidos, se toma el centro de masa de cada eslabón para analizar su posición, velocidad y aceleración, entonces:
# 
# **Para la posición:**
# 
# $$ x_{1}= \frac{l_1}{2} sin({ \theta_1 }) $$  ,   $$ y_{1}= -\frac{l_1}{2} cos({ \theta_1 }) $$
# 
# $$x_{2}=l_1sin({ \theta_1 })+\frac{l_2}{2} sin({ \theta_2}) $$  ,  $$y_{2}=-l_1cos({ \theta_1 })-\frac{l_2}{2} cos({ \theta_2}) $$
# 
# **Para la velocidad:** se deriva de la posición
# 
# $$\dot{x_{1}}= \frac{l_1}{2} \dot{\theta_1}cos({ \theta_1 }) $$    ,    $$\dot{y_{1}}= \frac{l_1}{2} \dot{\theta_1}sin({ \theta_1 }) $$
# 
# $$ \dot{x_{2}}= l_1\dot{\theta_1}cos({ \theta_1 }) +\frac{1}{2} l_2\dot{\theta_2} cos({ \theta_2 }) $$    ,    $$\dot{y_{2}}= l_1\dot{\theta_1}sin({ \theta_1 }) +\frac{1}{2} l_2\dot{\theta_2} sin({ \theta_2 }) $$
# 
# Reemplazando las velocidades en la energía cinética se tiene:
# 
# $$ T= \frac{1}{2} m_{1}\left [ \frac{1}{4} l_{1}^2{\theta_1}^2(cos^2(\theta_1)+sin^2(\theta_1)) \right ]+ \frac{1}{2} m_{2}\left [l_{1}^2{\theta_1}^2(cos^2(\theta_1)+sin^2(\theta_1)) +\frac{1}{4} l_{2}^2{\dot{\theta_2}}^2(cos^2(\theta_2)+sin^2(\theta_2))+ l_{1}l_{2}{\dot{\theta_1}}{\dot{\theta_2}}(cos(\theta_1)cos(\theta_2)+sin(\theta_1)sin(\theta_2)\right ]+ \frac{1}{2} J_{1}{\dot{\theta_1}}^2+ \frac{1}{2} J_{2}{\dot{\theta_2}}^2 $$
# 
# $$ T= \frac{1}{2}\left ( \frac{1}{4}m_{1}l_{1}^2+ \frac{1}{12}m_{1}l_{1}^2+m_{2}l_{1}^2 \right ){\dot{\theta_1}}^2+ \frac{1}{2}\left ( \frac{1}{4}m_{2}l_{2}^2+ \frac{1}{12}m_{2}l_{2}^2 \right ){\dot{\theta_2}}^2+ \frac{1}{2}m_{2}l_{1}l_{2}{\dot{\theta_1}}{\dot{\theta_2}}cos({\theta_1}+{\theta_2}) $$
# 
# $$ T= \frac{1}{2}\left ( \frac{1}{3}m_{1}l_{1}^2+m_{2}l_{1}^2 \right ){\dot{\theta_1}}^2+ \frac{1}{2}\left ( \frac{1}{4}m_{2}l_{2}^2+ \frac{1}{12}m_{2}l_{2}^2 \right ){\dot{\theta_2}}^2+ \frac{1}{2}m_{2}l_{1}l_{2}{\dot{\theta_1}}{\dot{\theta_2}}cos({\theta_1}+{\theta_2})$$
# 
# Para agilizar los  cálculos, se describen las siguientes variables:
# 
# $$ J_a=\frac{1}{3}m_{1}l_{1}^2+m_{2}l_{1}^2 $$
# $$ J_b=\frac{1}{3}m_{2}l_{2}^2 $$
# $$ J_x=\frac{1}{2}m_{2}l_{1}l_{2} $$
# 
# Por lo tanto, la energía cinética del sistema es:
# 
# $$ T= \frac{1}{2}J_a{\dot{\theta_1}}^2+ \frac{1}{2}J_b{\dot{\theta_2}}^2+J_x{\dot{\theta_1}}{\dot{\theta_2}}cos({\theta_1}+{\theta_2}) $$
# 
# Se reemplaza la posición vertical de los centros de masa en el análisis de la energía potencial:
# 
# $$ V=-\frac{1}{2}m_1gl_1cos({ \theta_1 })-m_2g\left (l_1cos({ \theta_1 })+\frac{1}{2}cos({ \theta_2 })\right) $$
# 
# $$V=-\left (\frac{1}{2}m_1+m_2\right )gl_1cos({ \theta_1 })-\frac{1}{2}m_2gl_2cos({ \theta_2 }) $$
# 
# Para agilizar los  cálculos, se describen las siguientes variables:
# 
# $$ \mu_1=\left (\frac{1}{2}m_1+m_2\right )gl_1 $$
# 
# $$ \mu_2=\frac{1}{2}m_2gl_2 $$
# 
# Por lo tanto, la energía potencial del sistema es:
# 
# $$ V=-\mu_1cos({ \theta_1 })-\mu_2cos({ \theta_2 }) $$
# 
# **Paso 4: Cálculo del Lagrangiano**
# 
# $$ \mathscr{L}= T-V $$
# $$ \mathscr{L}= \frac{1}{2}J_a{\dot{\theta_1}}^2+ \frac{1}{2}J_b{\dot{\theta_2}}^2+J_x{\dot{\theta_1}}{\dot{\theta_2}}cos({\theta_1}+{\theta_2})+\mu_1cos({ \theta_1 })+\mu_2cos({ \theta_2 }) $$
# 
# Dónde:
# 
# $$ \frac{\mathrm{d} }{\mathrm{d} t}\left (\frac{\partial \mathscr{L}}{\partial \dot{q_i}} \right )-\frac{\partial \mathscr{L} }{\partial q_i} =Q_i $$
# 
# Cálculamos el para $\theta_1$: $ \frac{\mathrm{d} }{\mathrm{d} t}\left (\frac{\partial \mathscr{L}}{\partial \dot{\theta_1}} \right )-\frac{\partial \mathscr{L} }{\partial {\theta_1}} =$
# 
# $$ J_a{\ddot{\theta_1}}^2+J_x{\ddot{\theta_2}}cos({\theta_1}-{\theta_2})- J_x{\dot{\theta_2}}sin({\theta_1}+{\theta_2}) \cdot({\dot{\theta_1}-\dot{\theta_2}}) -\left [- J_x{\dot{\theta_1}}{\dot{\theta_2}}sin({\theta_1}-{\theta_2}) -\mu_1sin({ \theta_1 }) \right ] $$
# 
# $$ J_a{\ddot{\theta_1}}^2+J_x{\ddot{\theta_2}}cos({\theta_1}-{\theta_2})- J_x{\dot{\theta_1}}{\dot{\theta_2}}sin({\theta_1}-{\theta_2}) +J_x{\dot{\theta_2}^2}sin({\theta_1}-{\theta_2})+J_x{\dot{\theta_1}}{\dot{\theta_2}}sin({\theta_1}-{\theta_2}) -\mu_1sin({ \theta_1 }) $$
# 
# $$  J_a{\ddot{\theta_1}}^2+J_x{\ddot{\theta_2}}cos({\theta_1}-{\theta_2}) +J_x{\dot{\theta_2}^2}sin({\theta_1}-{\theta_2})+\mu_1sin({ \theta_1 }) $$
# 
# Cálculamos el para $\theta_2$: $ \frac{\mathrm{d} }{\mathrm{d} t}\left (\frac{\partial \mathscr{L}}{\partial \dot{\theta_2}} \right )-\frac{\partial \mathscr{L} }{\partial {\theta_2}} =$
# 
# $$ J_b{\ddot{\theta_2}}^2+J_x{\ddot{\theta_1}}cos({\theta_1}-{\theta_2})- J_x{\dot{\theta_1}}sin({\theta_1}-{\theta_2}) \cdot({\dot{\theta_1}-\dot{\theta_2}}) -\left [J_x{\dot{\theta_1}}{\dot{\theta_2}}sin({\theta_1}-{\theta_2}) -\mu_2sin({ \theta_2 }) \right ] $$
# 
# $$ J_b{\ddot{\theta_2}}^2+J_x{\ddot{\theta_1}}cos({\theta_1}-{\theta_2})+J_x{\dot{\theta_1}}{\dot{\theta_2}}sin({\theta_1}-{\theta_2}) -J_x{\dot{\theta_1}^2}sin({\theta_1}-{\theta_2})-J_x{\dot{\theta_1}}{\dot{\theta_2}}sin({\theta_1}-{\theta_2})+\mu_2sin({ \theta_2 }) $$
# 
# $$ J_b{\ddot{\theta_2}}^2+J_x{\ddot{\theta_1}}cos({\theta_1}-{\theta_2}) -J_x{\dot{\theta_1}^2}sin({\theta_1}-{\theta_2})+\mu_2sin({ \theta_2 }) $$
# 
# **Fuerzas Generalizadas**
# 
# Ahora, procedemos a encontrar las fuerzas generalizadas $Q_j$, las mismas que son fuerzas no conservativas, para ello, nombramos al Punto de aplicación de la fuerza externa como punto P y harramos su ubicación en función del $\theta_1$ y $\theta_2$.
# 
# $$ \vec{r_p}=\left(l_1sin({\theta_1})+l_2sin(\theta_2) \right )\vec{i}+\left(-l_1cos({\theta_1})-l_2cos(\theta_2) \right )\vec{j} $$
# 
# Derivamos parcialmente para cada coordenada generalizada:
# 
# $$ \frac{\partial r_p}{\partial \theta_1}=l_1cos(\theta_1))\vec{i}+l_1sin(\theta_1))\vec{j} $$
# 
# $$ \frac{\partial r_p}{\partial \theta_2}=l_2cos(\theta_2))\vec{i}+l_2sin(\theta_2))\vec{j} $$
# 
# En este caso, la fuerza aplizada F es horizontal por lo que unicamente tiene componente en x tal que:
# 
# $$ Q_{\theta_1}= F \cdot\frac{\partial r_p}{\partial \theta_1} =F_x\vec{i}\cdot\left(l_1cos(\theta_1)\vec{i}+l_1sin(\theta_1)\vec{j}\right) $$
# $$ Q_{\theta_1}=F_xl_1cos(\theta_1) $$
# 
# $$ Q_{\theta_2}= F \cdot\frac{\partial r_p}{\partial \theta_2} =F_x\vec{i}\cdot\left(l_2cos(\theta_2)\vec{i}+l_2sin(\theta_2)\vec{j}\right) $$
# $$ Q_{\theta_2}=F_xl_2cos(\theta_2) $$
# 
# **Trabajo Virtual**
# 
# Además, calculamos el trabajo virtual realizado por cada uno de los eslabones:
# 
# $$ \delta W^{NC}=Q_{\theta_1}\delta\theta_1+Q_{\theta_2}\delta\theta_2 $$
# $$ \delta W^{NC}=\left(F_xl_1cos(\theta_1)\right)\delta\theta_1+\left(F_xl_2cos(\theta_2)\right)\delta\theta_2 $$
# 
# **Ecuaciones del movimiento**
# 
# Finalmente, las ecuaciones son:
# 
# Ecuaciones para $\theta_1$
# 
# $$ J_a{\ddot{\theta_1}}^2+J_x{\ddot{\theta_2}}cos({\theta_1}-{\theta_2}) +J_x{\dot{\theta_2}^2}sin({\theta_1}-{\theta_2})+\mu_1sin({ \theta_1 })=F_xl_1cos(\theta_1) $$
# 
# Ecuaciones para  $\theta_2$
# 
# $$ J_b{\ddot{\theta_2}}^2+J_x{\ddot{\theta_1}}cos({\theta_1}-{\theta_2}) -J_x{\dot{\theta_1}^2}sin({\theta_1}-{\theta_2})+\mu_2sin({ \theta_2 })=F_xl_2cos(\theta_2) $$
# 
# Dónde:
# 
# $$ J_a=\frac{1}{3}m_{1}l_{1}^2+m_{2}l_{1}^2 $$
# $$ J_b=\frac{1}{3}m_{2}l_{2}^2 $$
# $$ J_x=\frac{1}{2}m_{2}l_{1}l_{2} $$
# $$ \mu_1=\left (\frac{1}{2}m_1+m_2\right )gl_1 $$
# $$ \mu_2=\frac{1}{2}m_2gl_2 $$
# 

# **Comparación Newton-Lagrange**
# 
# **Diferencias de métodos**
# 
# **Lagrange**
# 
# Como se puede ver ambos métodos presentan un grado de dificultad diferente, lo cual puede ser beneficioso más para uno de los casos que para el otro. Por ejemplo, el método aplicando el lagrangeano resulta ser más sencillo en cuanto al desarrollo de los cálculos, ya que basta con poner atención a las derivadas parciales y con respecto al tiempo.La parte más importante de este método es tener en cuenta las coordenadas generales que se emplean y verificar su utilidad, para ello, es necesario que se cumplan los parámetros y requisitos que se vieron en clase previamente como es el caso de que el sistema tenga un carácter; homólogo, completo con respecto a $q_j$, e independiente.
# 
# **Leyes de Newton**
# 
# Con respecto al método de resolución por Leyes de Newton, se puede poner en consideración que resulta más dificultoso el proceso para hallar las ecuaciones de movimiento, ya que es necesario considerar al comportamiento de dos cuerpos por separado y analizar que es lo que le ocurre a cada uno con respecto al sistema inercial de referencia. Con este método se requerirán más ecuaciones para la resolución y conviene ir relacionándolas conforme se va desarrollando el ejercicio. Al igual que en el método anterior es importante notar el sistema de referencia utilizado y las coordenadas auxiliares empleadas, que en este caso se empleó radial transversal.
# 
# 
# **Conclusión**
# 
# Podemos concluir que el método de Lagrange resulta ser más cohesivo y práctico que el método de Newton. Sin embargo, lo más importante a tener en consideración son las coordenadas empleadas y saber que estas deben cumplir con los requisitos ya mencionados en los análisis anteriores.
# 
# 

# **Plus: Teoría del caos:**
# 
# Esta teoría declara que existen cierto tipo de sistemas cuyo comportamiento es prácticamente imposible de predecir, pues este es dependiente de diversas variables como pueden serlo el tiempo, en sistemas dinámicos, e interacciones, por los sistemas complejos. El péndulo doble es uno de los sistemas caóticos más simples que existen. Se observa su trayectoria irregular, además dando al péndulo una posición inicial ligeramente diferente se obtiene una trayectoria completamente diferente pasado un tiempo.

# ![g4_trayectoria%20%281%29.png](attachment:g4_trayectoria%20%281%29.png)

# **Gráficas adicionales**
# 

# In[3]:


import math
import numpy as np
from matplotlib import pyplot as plt

#Datos para el gráfico
l1=10
l2=13
m1=5
m2=8
g=10
mu_1=(1/2*m1+m2)*g*l1
mu_2=1/2*m2*g*l2
tetha_2= np.arange(0,181,45)
tetha_1= np.arange(0,181,45)
E_pot=-mu_1*np.cos(tetha_1)-mu_2*np.cos(tetha_2)

plt.ion()
plt.plot(tetha_1,E_pot,'-')
plt.xlabel("Ángulo de desplazamiento 1 (Tetha_1)")
plt.ylabel("Energía Potencial")
plt.legend(['Energía Potencial'])
plt.title("Energía Potencial vs desplazamiento angular 1")


# In[4]:


import math
import numpy as np
from matplotlib import pyplot as plt

#Datos para el gráfico
l1=10
l2=13
m1=5
m2=8
g=10
w1=3.5
w2=4.8
Ja=1/3*m1*l1*l1+m2*l1*l1
Jb=1/3*m2*l2*l2
Jx=1/2*m2*l1*l2
tetha_2=np.arange(0,181,45)
tetha_1= np.arange(0,181,45)
E_cin=1/2*Ja*w1**2+1/2*Jb*w2**2+Jx*w1*w2*np.cos(tetha_1+tetha_2)

plt.ion()
plt.plot(tetha_1,E_cin,'-')
plt.xlabel("Ángulo de desplazamiento 1 (Tetha_1)")
plt.ylabel("Energía Cinética")
plt.legend(['Energía cinética'])
plt.title("Energía cinética vs desplazamiento angular 1")


# 
