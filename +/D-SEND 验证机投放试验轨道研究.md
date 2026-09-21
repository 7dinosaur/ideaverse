---
标题: Dynamic Programming Trajectory Optimization and its application to D-SEND #2 Low Sonic-boom Research Project
作者: Yoshikazu Miyazawa, Akinori Harada, Jun'ichiro Kawaguchi, Tetsujiro Ninomiya, Hirokazu Suzuki, Hiroshi Tomita
期刊: AIAA Guidance, Navigation, and Control Conference 2012, AIAA 2012-4827（九州大学 & JAXA）
原文献: "[[Dynamic Programming Trajectory Optimization and its application to D-SEND2 Low Sonic-boom Research Project.pdf]]"
引用格式: "MIYAZAWA Y, HARADA A, KAWAGUCHI J, et al. Dynamic Programming Trajectory Optimization and its Application to D-SEND #2 Low Sonic-boom Research Project[C]//AIAA Guidance, Navigation, and Control Conference. Minneapolis: AIAA, 2012. AIAA 2012-4827. DOI:10.2514/6.2012-4827."
---
### 要点：
- **研究问题**：为 D-SEND #2 验证机（气球投放→自主加速超声速→按指定条件掠过测量站）设计参考轨迹；靠航程调节扩大投放允许域、提高任务成功率；当时缺乏工程师易用的轨迹优化工具（HSFD-II 靠飞行员经验）
- **解决方法**：自研 DP 轨迹优化工具——以比能量 E* 为自变量降阶 +(E*, V, γ) 网格 Bellman 最优性递推；提出 ACV 增广控制变量法解决单控制量（升力）对三状态量的可控性问题
- **局限性**：维度灾难（个人电脑上限约 3 维）；量化误差依赖网格密度，需人工调整；ACV 不适用于所有性能指标（负荷因子类改用 LGS 法）；最大航程解偏保守（附加阻力≥0）；横向机动算例未含 M=1.1 下界
- **全文脉络**：DP 特性综述（优点：全局最优/无迭代/约束易加；缺点：维度灾难/量化误差）→ 任务需求（终端条件由声爆测量要求给定）→ 动力学建模与能量降阶 → 最大航程（最优终末航迹角 -48°）→ 最小航程（自由终末角约 8 km；-45° 时航程可调范围 >20 km）→ 纵向航程调节（加负荷因子惩罚）→ 横向转弯航程调节算例 → 计算加速技术 → 结论

**方法提炼（只列）：**
- 质点动力学方程 dV/dt、dγ/dt、dH/dt、dφ/dt、dψ/dt（控制量：升力系数 C_L、倾侧角 σ）——Eq.(1)–(5)
- 气动：L、D 查表插值；配平极曲线近似 C_D = C_D0(M,H) + K(M,H)·C_L² ——Eq.(6)–(8)
- 能量降阶：E* = ½V² + g₀H_p（H_p 位势高度）；降阶状态方程 dV/dE*、dγ/dE*、dφ/dE*、dψ/dE* ——Eq.(12)–(18)
- DP 最优性递推：相邻能量层网格点间转移取 max ——Eq.(20)
- ACV 法：增广控制变量 C*_D（附加阻力；最大航程附加阻力≥0，最小航程取负即等效推力）——Eq.(25)(27)
- LGS 法（最小误差网格点选择）：每段航迹角变化仅选一个速度网格点，最小化阻力误差
- 性能指标：航程积分（Eq.19）；航程 + 负荷因子偏差加权（Eq.28/29）；航程 + 总转角加权（Eq.31）
- 加速：搜索空间显式限幅（|dV/dE*|、|dγ/dE*|）+ 迭代部分空间 DP（类梯度法，绕初始轨迹局部搜索）

## 总结：
**工程应用型文章：核心贡献是把 DP+ACV 做成简单可靠的轨迹优化工具，服务 D-SEND #2 的 GNC 设计（最大/最小航程、航程调节），数学关键在于"能量作自变量降阶"与"人工增广控制量补可控性"，同一工具换性能指标即可覆盖多种问题，思路可借鉴到航迹规划类工作**

> [!aircraft] +涉及飞行器参数
> 无动力验证机：长 7.7 m、翼展 3.5 m、翼面积 4.89 m²、质量 1 t
> 约束：M 1.1–1.7、L/mg ≤ 3.5、C_L 上下限、EAS 上限
> 测量终端条件：V = 400 m/s、H = 10 km、γ 指定（-45°/-48°）；投放高度约 30 km
