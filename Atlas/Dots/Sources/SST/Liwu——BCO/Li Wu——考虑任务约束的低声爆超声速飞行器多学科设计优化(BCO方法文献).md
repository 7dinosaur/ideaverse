---
标题: Multidisciplinary Design Optimization of Low-Boom Supersonic Aircraft with Mission Constraints
作者: Wu Li and Karl Geiselhart
期刊: AIAA Journal 10.2514/1.J059237
原文献: "[[Multidisciplinary Design Optimization of Low-BoomSupersonic Aircraft with Mission Constraints.pdf]]"
引用格式: "LI W, GEISELHART K. Multidisciplinary Design Optimization of Low-Boom Supersonic Aircraft with Mission Constraints[J]. AIAA Journal, 2021, 59(1): 165-179. DOI:10.2514/1.J059237."
---
### 要点：
- 基准是经验搭建的，正好对应市场分析的研究动机
- 使用经过缩放的逆向等效面积目标，因为CFD得到的等效截面积与低保真结果存在偏差
- 涉及推力和有限元结构的计算，后续多学科可以参考
- 对设计问题做了拆解
	- 设计探索，找到合适基准构型（利用发动机推力等手段最小化基准MTOGW）
	- 使用多个机翼尾翼变量在配平约束下最小化低声爆目标函数
	- 使用多个机身变量继续优化低声爆目标
	- tips：实际上优化应该是获得一个新的基准面积分布，然后在误差上下限内优化这个面积分布得到低声爆目标，也就是优化对象实际上是面积分布的上下限
- 
## 总结：
**本质上是结合多学科约束的低声爆目标生成方法，低声爆思路为使目标和基准的差距足够小说明我的目标可达，重点在于任务约束与低声爆需求的权衡**

> [!aircraft] +涉及飞行器参数
> 40座，巡航马赫数1.6，巡航高度45000ft，长度242ft