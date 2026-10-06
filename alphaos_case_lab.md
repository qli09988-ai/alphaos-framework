# AlphaOS Case Lab

Framework reference: AlphaOS Framework v0.1 FROZEN  
Last updated: 2026-10-06

Rule: this file contains experiments and observations.
Nothing here becomes a formal AlphaOS rule unless approved in the Change Log and added to Core Spec.

---

## Case #001 — Embodied Intelligence

### Key findings

1. Industry bottleneck and profit pool are not the same thing.
   - Current industry bottleneck may be reliable real-world task execution / generalization.
   - Investable profit pools may instead appear in high-reliability components, data infrastructure, deployment, or software platforms.

2. “Low localization rate” is not sufficient evidence of a good investment.
   - Must check supply expansion, pricing power, customer adoption, and economics.

3. Commercial validation must be separated from investment timing.
   - CV answers “is the business becoming real?”
   - Expectation answers “has the market already priced it?”

4. Batch delivery is not enough.
   - Economic validation matters:
     revenue growth + margin improvement + cash conversion.

5. Existing business and new optionality must be analyzed separately.

6. Financial filings should be the primary source for company financial conclusions.

### Company cards

#### 震裕科技 — v0.8
Working type:
- strong base business + robot optionality

Key monitoring:
- small batch -> stable batch / repeat purchase
- base-business cash flow / receivables
- robot revenue becoming separately visible

#### 福立旺 — v0.8
Working type:
- base-business recovery + higher robot earnings elasticity

Key monitoring:
- planetary roller screw from sample/intention -> real paid order
- 3C customer concentration and profit durability
- robot revenue crossing meaningful scale

#### 五洲新春 — v0.8
Working type:
- base business under pressure + aggressive robot capacity expansion

Key monitoring:
- batch orders AND margin improvement
- capacity utilization
- supply expansion vs demand

#### 贝斯特 — v0.8
Working type:
- stable base business + very early robot optionality

Key monitoring:
- sample -> first paid small-batch order
- avoid mistaking technical capability for commercial validation

#### 万向钱潮 — v0.8
Working type:
- large manufacturing platform + strategic robot migration

Key monitoring:
- batch order + separately visible robot revenue
- whether robot business becomes large enough to affect group profit

---

## Case — 垣信卫星 / 千帆星座

Use:
- test pre-commercial signals
- test infrastructure / platform businesses
- study where “commercialization proof” starts before mature profitability

Key insight:
- infrastructure build-out ≠ mature business
- key transition is network build -> paying users / ARPU / utilization / unit economics

Potential future experiment:
> Historical rewind: if we go back to 2022/2023, which public signals would have been enough to put the company into a core observation pool before major strategic investors entered?

---

## Case — 鲁信创投

Use:
- test whether CV logic works for asset / venture-capital platforms

Finding:
- CV is not a natural fit for venture-capital / asset realization businesses.

Possible alternative:
- Asset Realization Stage
- NAV revaluation
- catalyst / exit pipeline
- look-through ownership

Status:
- 原观察保留；2026-09-26 用户明确批准 Thesis Type Router（CHG-007），允许 Asset Realization 类型而不强套 CV。
- 完整 Asset Realization Engine、NAV/概率/退出模型仍未升 Core；本案例扩展见下方 Case #003。


---

## Case #003 — 蓝箭 / 鲁信 / 金风 8·19 事件回放

交接：`2026-09-26-蓝箭事件驱动-01`  
状态：**Case Observation / Testing**；Market Leadership 为 **Experimental/Testing**，Catalyst Quality 为 **Proposed/Testing**。  
对象：600783 鲁信创投、002202 金风科技；T = 2026-08-19；材料窗口 2026-08-05～2026-08-24；时区 Asia/Shanghai。  
问题：事件确认前谁更强、确认日谁承接、T+1 是否延续，以及这些差异能否排除市场/行业/事件篮子影响。

### A. 证据登记与可信度

| ID | 来源 / 日期 / 对应期间 | 本地位置 | 本次核验边界 |
|---|---|---|---|
| EVID-01 | 原聊天附件 `case_lanjian_20260819.md`；创建时间未记载，9/26 取得；行情期 8/5～8/24 | [原件副本](artifacts/alphaos-20260926-lanjian-01/case_lanjian_20260819.source.md) | 已读取 Markdown 表格；未获得底层逐笔/分钟 CSV；原件自述 min_snapshot 超出 allowlist |
| EVID-02 | 9/26 用户转述 Reachability / Provenance Audit；测试涉及最近交易日 9/24 | [转述审计摘录](artifacts/alphaos-20260926-lanjian-01/source_audit_excerpts.json)，turn `2f97fc06-df5d-433d-bbd3-6b14119aef8a` | 当前 wrapper 历史不支持；v1 历史分钟来自 wrapper 外。远端 reports/reachability_20260926/ 原始日志未取得，本轮未重测 |
| EVID-03 | 9/26 用户转述免费源测试；历史测试期及标的细节部分缺失 | 同一摘录，turn `afb6731f-c007-4181-9d8b-62db4b400adc` | 据转述 BaoStock 可用，13 日 close 差为 0、amount 差 <0.1%；无原始核对表，不作为本次独立验证结果 |
| EVID-04 | 9/25 本地验收报告；返回 9/24 数据 | [只读验收报告](artifacts/ths-validation/核验报告.md)、[运行限制](artifacts/ths-validation/LOCAL_RUNTIME.md) | 游客只读入口、异常字段、休市快照与实时性限制有本地报告；未重测 |
| EVID-05 | 9/26 当前用户合入指令与[原对话](chatgpt-conversation://6a72cde8-968c-83e9-8e76-dbd98abc4935) | 本轮交接单 | 授权规则范围、案例观察和待验证假设；聊天引用标记不当作已取得原公告 |

以下 FACT 是“附件报告的行情事实”，不是本轮独立行情认证。v1 历史分钟/相关扩展数据标记 **non-wrapper / non-production-safe**，仅用于描述待核验样本，不据此绕过入口补抓。

### B. 新增事实（FACT：据 EVID-01）

| 日期 | 鲁信创投 | 金风科技 | 可支持的描述 |
|---|---|---|---|
| 8/17（T-2） | 收 18.89，+2.89% | 收 21.76，+3.97% | 金风当日涨幅较高 |
| 8/18（T-1） | 收 18.35，-2.86% | 收 22.01，+1.15% | 金风连续两日上涨，鲁信未延续 |
| 8/19（T） | 开/高/收 20.19，低 19.83；收 +10.03% | 开/高 24.21，低 22.00，收 22.03；收 +0.09% | 按回放材料，鲁信封板收盘，金风涨停开盘后回落至接近平盘 |
| 8/20（T+1） | 收 18.62，-7.78% | 收 19.84，-9.94% | 两者快速转弱；确认日强势未延续 |

原表金风 8/19 09:35 为 22.99、较昨收 +4.453%，属于未经原始 CSV 复核的分钟摘要。鲁信各列采样点处于涨停价，但日线低点 19.83 < 20.19，**不能写“全天未开板”**。只确认材料中的涨停收盘；是否开板/回封及具体时点待核验。

T 是用户指定的“确认日”研究锚点；本轮材料没有对应官方公告的完整正文、标题及首次公开时间，不能把 8/19 自动映射为某个 C 状态跃迁，亦不能证明异动早于公开消息。

### C. 计算（CALCULATION：仅从附件价格重算）

价格单位元；收益按收盘比值计算，百分比四舍五入至两位。未与外部行情独立交叉核验，复权口径仍待原始元数据确认。

| 指标 | 输入与公式 | 鲁信 | 金风 |
|---|---|---:|---:|
| 8/17–18 累计收益 | 8/18收盘 ÷ 8/14收盘 − 1 | 18.35/18.36−1 = -0.05% | 22.01/20.93−1 = +5.16% |
| T 日收益 | 8/19收盘 ÷ 8/18收盘 − 1 | +10.03% | +0.09% |
| T+1 日收益 | 8/20收盘 ÷ 8/19收盘 − 1 | -7.78% | -9.94% |
| T 日高点至收盘收益 | 收盘 ÷ 最高 − 1 | 20.19/20.19−1 = 0.00% | 22.03/24.21−1 = -9.00% |

8/17–18 金风相对鲁信两日收益差约 **5.21 个百分点**；这是两股比较，**不是**相对市场、风电或蓝箭篮子的超额。T 日成交额为 8.97 / 94.64 亿元（鲁信/金风，据原表），但未计算 20 日异常指标：原附件仅 14 个交易日，样本不足。

市场/行业/事件篮子超额、Amount_Ratio_20D、Amount_ZScore_20D：**Unavailable**，等待统一口径历史日线。基准必须用当日前 20 个交易日，不把当日放入均值；零方差/零分母记 N/A。

### D. 推断与假设（INFERENCE / HYPOTHESIS）

- **事件前金风更像 Pre-Event Leader**：仅基于两股相对表现的实验性解释。风电行业 Beta、市场 Beta、泛航天主题及公司自身其他消息尚未排除，不能升级为“已确认蓝箭特异性领先”。
- T 日鲁信更像 Confirmation，金风表现与 Exhaustion 特征相容；这是事后标签，未建立事前识别阈值，也不能证明谁在买卖或提前知情。
- T+1 快速转弱提示“确认日封板”不等于持续承接，更不等于可获利的交易规则。
- Thesis 工作分类：鲁信以 Asset Realization 为主、Event-Driven 为辅；金风为 Hybrid（Industrial Base + Event Optionality）。权益比例、价值传导和可兑现规模需一手文件支持，本轮不估 NAV。
- Why Now? 工作问题：下一公开节点能否实质降低不确定性，且相对于当前预期仍有增量？目前只有回放与时间窗口假设，不能据此给出当前买入结论。
- 原对话讨论的“10/11 月首轮回复、11 月至 2027Q1 上会”保留为 **用户时间窗口假设，非已确认日程**；聊天称 C3 亦未在本轮取得官方材料核实。当前 C/E 状态均待证据，不直接赋值。

### E. Market Leadership Monitor — Experimental / Testing

| 实验状态 | 工作定义（尚非正式规则） |
|---|---|
| None | 数据充分但没有形成领先证据；数据缺失应另记 Unavailable，不默认 None |
| Pre-Event | 公开确认前持续相对强势的候选，需市场/行业/事件篮子控制 |
| Confirmation | 公开确认后出现承接与相对强势的候选，需观察持续性 |
| Exhaustion | 高开回落、收盘远离高点或其他衰竭特征的候选，不能由单一字段自动赋值 |

状态不是必经线性路径，也不是买卖信号。识别窗口、持续天数、成交额阈值及事后标注一致性均为 Proposed/Testing。先固定规则、补足控制组和公开信息时间轴，再用蓝箭以外至少两组独立案例（机器人、低空经济候选）检验，包括失败样本；样本增加也不自动升级，仍需人工批准。

### F. Catalyst Quality Q0–Q3 — Proposed / Testing

| 等级 | 暂定含义 |
|---|---|
| Q0 | 纯流程推进 |
| Q1 | 消除次要不确定性 |
| Q2 | 解决关键审核/商业化疑点 |
| Q3 | 重大确定性跃迁 |

本轮仅登记分级建议，不给蓝箭某节点强行赋 Q 值。需要节点前后证据、未解决问题、反证和可重复判定标准；高 Q 不等于高股票机会，也不能自动改变 E 状态/仓位。

### G. 数据源审计结论（据 EVID-02–04）

- **thsdk 游客模式只适合当日实时盘面感知**；当前 wrapper 无历史日期参数，休市可能只返回最近交易日。报告称 klines 返回 4 根、intraday 返回 241 行、auction anomaly 返回市场级 794 行；不代表历史或目标个股异常已可用。
- **BaoStock 用于历史控制组/日线**；本轮只取得测试结论转述，尚未拿到风电/事件篮子计算结果。新浪曾被报告可作补充，未据此自动更改默认底座。
- **AKShare 当前不作为底座**：该服务器东方财富接口由短暂成功转为 502/断连/TCP 超时；不能把“网络层拦截/限流”的推测写成已证明根因，也不能推定所有 AKShare 数据源不可用。
- **历史外盘/内盘/主动买卖字段降权**：鲁信 T 日涨停收盘而原表主动买入占比仅 4.09%，加上单位/累计口径未明，统一 Low-confidence auxiliary field，不用于 Leader、抢筹或净流入判断。
- v1 的 wrapper 外 provenance 原样保留；授权改规则不等于认可这些输入已达生产质量。

### H. 缺失证据 / 下一确认

1. 补充 T 日官方事件内容、首次发布时间及事件前公开消息时间轴；才能判定 Event State 与信息先后。
2. 取得 BaoStock 原始日线、复权/单位/交易日元数据及审计 CSV；固定市场基准、风电控制组、事件直接关联组与泛主题代理，留存成分当时可见证据、排除被测标的，再计算超额。
3. 补充历史分钟原始数据和合法可复现来源；核对鲁信开板/回封与金风日内轨迹。未补齐前保留描述，不作识别规则验证通过。
4. 下一次材料到达即更新卡片；窗口假设届满而无披露时登记延迟并复核 thesis，不把预测日期当事实。无已核实硬期限，不在本轮开启自动监控。

本案例只为六项已获授权的方法更新提供问题背景；Leadership、Q 分级及 Pre-Event Leader 阈值均未升为 Core。


---

## Case #004 — 雷科防务（002413）v0.1 Acceptance Case

状态：**Acceptance Case / Case only**；记录日期 2026-10-06，时区 Asia/Shanghai。用于检验事实纠错与行动分类，不新增 Core 价格规则。

- **FACT（历史证据）**：2026-08-07 日线高 9.52，收 9.17 元。已归档分钟核验显示：14:15 标签分钟K线起突破 9.18，14:20 时段冲至 9.52，之后回落至 9.18 附近，最终收 9.17。分钟标签不等于秒级成交时刻。
- **Case conclusion**：`9.18不是8/07硬压力高点`；`9.10–9.25 = Historical Acceptance/Rejection Zone（Partial）`；`9.52 = Confirmed prior Swing High`。Partial 不表示经过多轮独立检验，也不是当前买卖信号。
- **FACT（用户交易陈述）**：用户 2026-09-24 在 8.97 涨停日部分减仓。
- **Action classification**：**Pre-emptive Tactical Reduction**；依据为接近上一轮接受失败区，而不是已确认突破失败。不据后续涨跌反推过程正确。
- **Source / timestamp / freshness / provenance**：[v2 完整历史证据交接](artifacts/leike-20260807-verification/发送至AlphaOS_chat_完整交接正文_v2.md)。日线来源腾讯/搜狐，采集于 2026-09-27，历史观察截至 2026-09-24；分钟来源及采集记录见该交接内分钟补充报告和原始清单。本次沿用归档核验与用户批准结论，未重新抓行情，不代表 10/06 实时数据。
- **Missing Evidence / limits**：本轮未取得券商成交回单，交易动作按用户陈述登记；历史分钟跨源差异及覆盖边界沿用原证据，不宣称逐条完全一致。原始分钟数据保留在 artifacts，不复制进 Core。
