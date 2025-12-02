# Logistic 回归与 Linear 回归 梯度推导

> 我的问题：为什么logistic regression与linear regression的cost function的dj_dw和dj_b是一样的，log是不是默认的ln。

---

## 一、记号与统一表示

- 样本数：$m$。
- 第 $i$ 个样本：输入向量 $\mathbf{x}^{(i)}$，标签 $y^{(i)}\in\{0,1\}$（二分类场景）。
- 线性部分：
  \[ z^{(i)} = \mathbf{w}^\top \mathbf{x}^{(i)} + b. \]
- 预测（统一写作 $h^{(i)}$）：
  - 线性回归： $h^{(i)} = z^{(i)}$。
  - Logistic 回归： $h^{(i)} = \sigma(z^{(i)}) = \dfrac{1}{1+e^{-z^{(i)}}}$。

我们要推的是对参数 $\mathbf{w}$ 与 $b$ 的梯度：$\dfrac{\partial J}{\partial \mathbf{w}}$ 与 $\dfrac{\partial J}{\partial b}$。

---

## 二、线性回归（MSE）推导

代价函数（带 $\tfrac12$ 方便简化常数）：
\[ J(\mathbf{w},b)=\frac{1}{2m}\sum_{i=1}^m (h^{(i)}-y^{(i)})^2 = \frac{1}{2m}\sum_{i=1}^m (z^{(i)}-y^{(i)})^2. \]

对 $\mathbf{w}$ 求导：

\[
\begin{aligned}
\frac{\partial J}{\partial \mathbf{w}}
&=\frac{1}{2m}\sum_{i=1}^m 2(z^{(i)}-y^{(i)})\frac{\partial z^{(i)}}{\partial \mathbf{w}}\\
&=\frac{1}{m}\sum_{i=1}^m (z^{(i)}-y^{(i)})\mathbf{x}^{(i)}.
\end{aligned}
\]

对 $b$：
\[ \frac{\partial J}{\partial b}=\frac{1}{m}\sum_{i=1}^m (z^{(i)}-y^{(i)}). \]

写成 $h^{(i)}$ 的形式：
\[
\boxed{\;\frac{\partial J}{\partial \mathbf{w}}=\frac{1}{m}\sum_{i=1}^m (h^{(i)}-y^{(i)})\mathbf{x}^{(i)},\quad
\frac{\partial J}{\partial b}=\frac{1}{m}\sum_{i=1}^m (h^{(i)}-y^{(i)})\;}
\]

---

## 三、Logistic 回归（交叉熵）推导

单样本的损失（交叉熵）：
\[ \ell^{(i)} = -\big[ y^{(i)}\log h^{(i)} + (1-y^{(i)})\log(1-h^{(i)}) \big],\quad h^{(i)}=\sigma(z^{(i)}). \]

**关键：** 先对 $z^{(i)}$ 求导（链式法则），目标是得到 $\dfrac{\partial \ell^{(i)}}{\partial z^{(i)}}$。

先对 $h$ 求导：
\[
\frac{d\ell}{dh} = -\frac{y}{h} + \frac{1-y}{1-h}.
\]

sigmoid 的导数为：
\[ \frac{dh}{dz} = \sigma'(z) = \sigma(z)(1-\sigma(z)) = h(1-h). \]

于是：
\[
\begin{aligned}
\frac{d\ell}{dz} &= \left(-\frac{y}{h} + \frac{1-y}{1-h}\right) \cdot h(1-h) \\
&= -y(1-h) + (1-y)h \\
&= h - y.
\end{aligned}
\]

因此对参数的梯度同样是：
\[
\boxed{\;\frac{\partial J}{\partial \mathbf{w}}=\frac{1}{m}\sum_{i=1}^m (h^{(i)}-y^{(i)})\mathbf{x}^{(i)},\quad
\frac{\partial J}{\partial b}=\frac{1}{m}\sum_{i=1}^m (h^{(i)}-y^{(i)})\;}
\]

> 注意：与线性回归“形式上相同”的原因是链式法则与交叉熵对数导数（$1/h,1/(1-h)$）和 sigmoid 导数 $h(1-h)$ 完美抵消。

---

## 四、为什么 $\log$ 是自然对数（$\ln$）？

- 在数学上，任意底的对数都只差一个常数因子：
  \[ \log_a x = \frac{\ln x}{\ln a}. \]
- 如果用底为 $a$ 的对数，交叉熵会带上常数 $1/\ln a$：
  \[ \ell = -\frac{1}{\ln a}\big[ y\ln h + (1-y)\ln(1-h)\big]. \]
  求导后得到的梯度为 $\dfrac{h-y}{\ln a}$，比使用自然对数多一个常数系数。
- 当 $a=e$（自然对数）时，$\ln a=1$，该常数消失，梯度最简洁：$h-y$。

因此在 ML 文献与框架中默认 $\log=\ln$（单位为 nats），以保证推导与实现的简洁性与一致性。

---

## 五、向量化（矩阵）形式（便于实现）

令矩阵 \(X\in\mathbb{R}^{m\times n}\)（每行是一个样本的转置），向量化预测：
\[ z = Xw + b\mathbf{1},\quad h = \sigma(z)\ \text{（element-wise）}. \]
交叉熵（或 MSE）关于权重的梯度统一写成：
\[
\nabla_{w}J = \frac{1}{m} X^\top (h - y),\qquad
\nabla_{b}J = \frac{1}{m} \sum_{i=1}^m (h^{(i)}-y^{(i)}).
\]

其中 $y$、$h$ 都是 $m$ 维列向量（$y=[y^{(1)},\dots,y^{(m)}]^\top$）。

---

## 六、直观与小结

- 形式相同的本质：梯度总是“误差（预测 - 真实）”与输入（或常数 1）相乘并平均。
- 区别在于 $h$：线性回归 $h=z$，Logistic 回归 $h=\sigma(z)$。
- 交叉熵 + sigmoid 的组合不是巧合，而是统计—数学上的自然匹配（对数似然与 link function 的匹配）。

---

## 参考（建议阅读）

- Andrew Ng, *Machine Learning* 课堂笔记（Logistic Regression）
- 周志华《机器学习》相关章节

---

**文件信息**：若需要我可以把这份 Markdown 转为 PDF、PNG，或生成一页用于复习的图（带步骤），以及附上向量化的 NumPy 实现示例。

