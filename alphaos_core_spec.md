# AlphaOS Core Spec — Framework v0.1 FROZEN

Version: AlphaOS Framework v0.1  
Last updated / Freeze date: 2026-10-06  
Baseline: v0.1.1-working（2026-09-26 文档增量；本次正式发布命名为 Framework v0.1，不回退既有内容）  
Approved changes: 保留 CHG-001–CHG-012；本次 Final Approval Set 见 CHG-013。
Human Approval（2026-10-06）：“批准 AlphaOS Framework v0.1 Final Approval Set，冻结 v0.1”。

Status: **FROZEN / Core Sole Source of Truth**  
Rule: only explicitly human-approved changes may be added here through version control.

冻结范围和排除项见 [FREEZE_v0.1.md](FREEZE_v0.1.md)；个人风险参数独立存于 [alphaos_personal_policy.md](alphaos_personal_policy.md)。AI may propose changes but may not self-approve or silently mutate Core. 本次是执行已获 Human Approval 的文档合入，不授予后续自行改写权限。

---

## 1. System goal

AlphaOS is a personal investment operating system for evidence-driven decision support.

It is NOT:
- an “AI that guarantees profit”;
- a model that invents trading numbers;
- a clone of the user’s thinking;
- a pure news-summary bot.

It SHOULD:
- preserve investment theses and decision history;
- track state changes;
- separate facts, inference, assumptions, and market expectations;
- use deterministic rules/code for numerical risk and position calculations;
- learn from review without allowing uncontrolled self-modification.

---

## 2. Core epistemic principle

> **Facts + Logic = View**

If facts and logic remain unchanged, the long-term view should not change merely because price fluctuates.

Short-term market state, sentiment, crowding, and expectation can change independently from long-term industry/company facts.

---

## 3. Main research chain

### Thesis Type Router — Approved / CHG-007

建卡先回答“收益兑现主要依赖什么”，再选研究路径；不是所有股票都按产业成长逻辑处理。

| Thesis Type | 主要研究路径 | 必须保留的约束 |
|---|---|---|
| Industrial | Direction → Lifecycle → CV → Bottleneck / Profit Pool → Company | 商业化与经济验证分开；CV 不等于买点 |
| Event-Driven | 事件事实 → Event State → 与公司价值的关联 → Expectation | 流程推进不代表公司盈利增加；公开证据先于判断 |
| Asset Realization | 穿透权益 → 资产价值 / 兑现路径 → Event State（适用时）→ Expectation | 核对权益比例、稀释、锁定、税费与退出条件；不强套 CV |
| Hybrid | 分别研究主业与事件 / 资产可选项，再汇总 | 标明 primary / secondary thesis，避免重复计价 |

路由只决定证据需求；所有类型继续经过 Expectation、Market Regime、Execution、Risk 与 Review。CV 不适用时写 N/A 并说明原因，不虚构资产类 CV 阶段。Asset Realization 的完整估值/概率模型仍在 Backlog，不因新增类型自动获批。

以下产业研究链继续适用于 Industrial，以及 Hybrid 的产业部分：

1. **Direction Engine** — why this direction / where real capital and policy resources are going
2. **Industry Lifecycle Engine** — where the industry is in its lifecycle
3. **Commercialization / Validation** — whether demand is real and repeatable
4. **Bottleneck Analysis** — what constrains scale
5. **Profit Pool Engine** — where excess profit can actually accumulate
6. **Company Position Engine** — which companies can capture that profit
7. **Expectation Engine** — what the market has already priced
8. **Execution Engine** — how to act
9. **Risk & Position Engine** — how much risk can be taken
10. **Review / Evaluation Loop** — what was right/wrong and what should be updated

---

## 4. 431 research framework

### 4 — four layers
- Macro
- Market
- Industry
- Company

### 3 — “three highs”
- High growth
- High profitability
- High moat

### 1 — key bottleneck
Find the true bottleneck / profit-pool node in the value chain.

Important:
- bottleneck ≠ moat
- bottleneck ≠ automatically a good investment
- low domestic penetration ≠ automatically high profit
- technical difficulty ≠ pricing power

---

## 5. Industry Lifecycle

Working lifecycle:

- L0 — Technical exploration
- L1 — Commercial validation
- L2 — Production / scale-up
- L3 — Scale expansion
- L4 — Mature competition

The system must always output the **current stage**, not every historical stage.

Historical stages are shown only in Learning/Audit mode.

---

## 6. Commercial Validation (CV)

Working ladder:

- CV0 — Demo / concept only
- CV1 — customer testing / sample
- CV2 — paid pilot / small-batch order
- CV3 — clear batch delivery
- CV4 — repeat purchase / repeated expansion
- CV5 — cross-customer / cross-industry replication

Important:
- CV is **commercial validation**, NOT an automatic buy signal.
- Investment timing must combine CV with market expectation.
- Preferred hunting zone is often where validation is improving rapidly while expectation is not yet saturated.

For businesses already in batch delivery, **economic validation** must also be checked:
- revenue ramp
- margin ramp
- cash conversion
- return on invested capital / payback
- pricing power

---

## 7. Profit Pool Engine

A potential profit pool must pass four tests:

1. Demand elasticity
2. Supply expansion difficulty
3. Substitutability / indispensability
4. Profit-capture ability

Additional required risk:
- **Supply Expansion Risk**

A good industry can still be a poor investment if supply expands faster than demand.

Profit pools can migrate as the industry lifecycle changes.

---

## 8. Company Position Engine

Internal research fields:

1. Base Business
2. Product / technical position
3. Commercial Validation
4. Customer position
5. Capacity / production schedule
6. Economics (revenue, margin, profit)
7. R&D / strategic commitment
8. Moat / key risks
9. Earnings Elasticity
10. Expectation

Default user-facing output should be compressed to:
- Current state
- Strongest evidence
- Biggest missing evidence / risk
- Next confirmation event
- Market expectation state

---

## 9. Base Business / Optionality Separation

When a new business is still small:

- analyze the existing business separately;
- analyze the new growth option separately;
- do not attribute existing profit growth to the new theme without evidence.

Questions:
- What currently supports the valuation?
- How sustainable is the base business?
- How large must the optional business become to change the profit curve?

---

## 10. Earnings Quality

Profit growth must be checked against:
- operating cash flow
- receivables
- inventory
- gross margin
- net margin
- capital expenditure
- working-capital changes

Rule:
> Profit growth without cash conversion is a yellow flag that requires explanation.

Financial filing priority:
1. periodic report / financial filing
2. company announcement / inquiry reply
3. IR / investor communication
4. customer / tender / procurement information
5. news and secondary summaries
6. market commentary

---

## 11. Expectation Engine

States:

- E1 — underpriced / largely unpriced
- E2 — expectation forming
- E3 — substantially priced
- E4 — expectation overdraft / very demanding expectations

Do not infer expectation from price rise alone.

Inputs include:
- fundamentals / orders / shipment / earnings expectations
- valuation vs history and peers
- relative price behavior
- crowding / turnover / participation
- reaction to catalysts

### Event Progress vs Expectation Progress — Approved / CHG-009

**利好程度 ≠ 股票机会程度。** 对事件适用的 Thesis，同步记录：

- Event Progress：事件主体、C 状态及子节点、证据发布时间、变化消除了什么不确定性。
- Expectation Progress：E1–E4 前后状态、估值隐含要求、价格/相对强弱与催化反应；不能只凭上涨赋值。
- Business Reality：真实业务/现金流/资产权益变化，独立于事件流程和市场价格。

| 观察组合 | 允许的解释 | 还需验证 |
|---|---|---|
| 事件实质推进，预期要求变化有限 | 可能扩大预期差 | 价值传导、估值、风险与可执行性 |
| 事件停滞，预期要求明显抬升 | 可能透支预期 | 市场是否在交易其他已知事实 |
| 事件与预期同步推进 | 不能仅据利好加码 | 价格隐含目标与剩余不确定性 |
| 事件推进，股价冲高回落 | 可能兑现/分歧 | 控制组、持仓拥挤及其他事件 |

C 和 E 都是有序分类，不是可直接相减/相除的数值；不新增 E2.5 或 C3.5。首轮回复可记为 C3 内子节点。这里不定义自动交易、胜率、赔率改善阈值或仓位规则。

---

## 12. Reverse Expectation Model

Purpose:
> Ask what must happen in the future to justify today’s valuation.

Do NOT use it as a fake “fair price” calculator.

Process:
1. Base-business profit baseline
2. Current valuation requirement
3. Incremental profit gap
4. What new business revenue/margin/share would be required to fill the gap?
5. Compare implied requirements with industry reality

---

## 13. Market Regime Engine

States:
- R1 Fear / ice
- R2 Repair
- R3 Risk-on / main rise
- R4 Climax / overheating
- R5 Retreat

Inputs:
- index trend
- breadth
- turnover/liquidity
- sentiment structure
- mainline persistence

Market Regime gives risk posture, NOT exact position percentages.

### Relative Strength Controls — Approved / CHG-012

Market Monitor 同时观察个股相对 **市场 / 行业 / 事件篮子** 的表现，作为调查与预期判断的输入。

- 固定观察窗口、交易日、复权口径和收益定义，记录基准代码、名称、成分、权重与选取时间。
- `Return_nD = P_t / P_(t-n) - 1`；`Excess_Return_nD = Return_stock_nD - Return_control_nD`，超额以百分点展示，不称为因果 alpha。
- 等权篮子先按预先固定的成分求每日收益均值，再复合成多日收益。标的自身从其控制篮子剔除；缺失/停牌处理预先声明，禁止把缺失收益填零或事后换弱样本。
- 事件直接关联组必须有当时已公开的权益/供应/合作证据；泛主题板块仅是行业/主题 Beta，不等同事件关联组。
- 控制组不足时写 Unavailable，并限制结论；绝对上涨不能证明独立事件领先或内幕信息。

Market Leadership 的状态分类与识别阈值尚未 Approved，定义仅保留在 Case Lab / Backlog 的实验区，不作为 Core 决策条件。

---

## 14. Execution Engine

Keep three decisions separate:
- Investment Judgment
- Trade Judgment
- Risk Management

Exit taxonomy:
- S1 Thesis break
- S2 Expectation realization / overdraft
- S3 Swing structure break
- S4 Opportunity cost

Price stops are a last-resort risk fail-safe, not the primary thesis criterion.

### Execution — Approved / CHG-013

以下为本次 Execution 唯一规范表述；历史聊天中的 AC-EXEC 近义条目不构成并行规则。

1. **OPEN** 前必须通过 Thesis / Why Now / Expectation / Invalidation / Risk 五项检查。
2. **ADD** 必须有新增证据；**HOLD ≠ ADD**，原持有理由不自动构成加仓理由。
3. Thesis 改变必须 **RE-UNDERWRITE**；禁止 **Bought for A, held for B**。
4. 回本价 / 券商动态成本不得作为持有或加仓理由。
5. 重大监管、政策、事故、核心客户等冲击触发 **Shock Review**。

### Risk & Position — Approved / CHG-013

以下为本次 Risk 唯一规范表述；与 Execution 共用，不另保留重复 AC-RISK 条目。

1. LLM 不得直接编仓位；仓位必须由确定性 **Risk Engine** 计算。
2. 同一 Thesis 的首仓与所有加仓共享**累计 Risk Budget**，不得每次加仓重置预算。
3. 同时管理 **Single Instrument / Thesis / Theme-Cluster / Portfolio Risk**。
4. **Conviction** 只能在风险边界内调节，不能取消边界。
5. 有明确失效距离时使用 **Risk-Distance Sizing**；长期产业 Thesis 可使用 **Stress-Based Sizing**。

个人预算、权益基准、压力参数、上限与恢复约束读取 Personal Policy；本节不把个人参数规定为普适市场真理。Risk Engine 的代码实现和验收属于 Runtime MVP，本次冻结不代表代码已实现或已通过实盘验证。


---

## 15. Position Thesis Card

Each tracked position/company must store the following fixed fields:

- **Thesis Type**：Industrial / Event-Driven / Asset Realization / Hybrid；primary / secondary（如适用）
- **Core Thesis**：核心因果论点
- **Why Now**：为什么是现在，而不是三个月前或三个月后；对应证据时间、临近确认事件、尚未消失的预期差与失效条件（保留 CHG-010）
- **Evidence For**：支持证据
- **Evidence Against**：反对证据
- **Expectation**：市场预期状态及依据
- **Invalidation**：失效条件
- **Risk State**：当前风险状态
- **Current Action**：当前行动
- **Next Confirmation**：下一确认事件/条件
- **Missing Evidence**：缺失证据

保留原有扩展字段，不以固定字段替换类型所需信息：

- stock / code / mode；validation metrics；catalysts；strengthening conditions；weakening / break conditions
- Industrial 及 Hybrid 产业部分保留 **Lifecycle / CV / Economics**；Expectation / Market Regime 状态保留，不适用项写 N/A 并说明原因
- Event-Driven 保留 Event State / substage / event_status、事件主体、关联路径、证据时间与 next transition
- Event Progress vs Expectation Progress：各自变化、依据和置信度
- Relative Strength：vs Market / Industry / Event Basket；窗口、基准与缺失项

卡片**只在五类触发更新**：新事实 / 状态迁移 / 交易动作 / Shock / Deadline Miss。没有触发时不因模型重新措辞而改写状态。

The card stores **state + transition conditions**, not “good/bad company” labels.

Why Now? 没有证据时写“待验证”，不补造紧迫感。实验性的 Market Leadership / Catalyst Quality 如需附在卡上，必须单独标记 Proposed/Testing，不能用于自动买卖或仓位输出。

### Event Monitor：Event State C0–C7 — Approved / CHG-008

该枚举是 AlphaOS 对 IPO / 资产兑现事件的研究记录约定，并非所有地区监管流程的统一法律定义。每个事件附 jurisdiction / venue；不适用节点写 N/A，依据具体公开文件映射。非 IPO 事件保留原事件名称与里程碑，不强套 C0–C7。

| 状态 | 名称 | 记录证据与子节点 |
|---|---|---|
| C0 | 传闻 | 来源、首次可见时间与未核实标记；传闻不等于事实 |
| C1 | 辅导 | 适用市场的正式辅导备案/进展材料 |
| C2 | 受理 | 受理披露；不等于审核通过 |
| C3 | 问询 | 问询/回复文件、轮次、关键待解决问题 |
| C4 | 上市委 / 聆讯 | 通知、召开、审议结果分别记录；通知不等于通过 |
| C5 | 注册 / 发行 | 提交、获准、发行等子节点分别记录；不得混为完成 |
| C6 | 上市 | 正式上市事实；上市不等于关联股东可以退出 |
| C7 | 解禁 / 退出 | 解禁日期与条件、可退出规模、实际退出及现金回收分别记录 |

每次更新保存 `from → to`、证据链接/文档、发布时间、采集时间、下一确认条件、预期窗口（事实或假设）、延迟/失败条件。允许同一 C 状态内多轮更新；不是自动前进或保证成功的直线。

中止、撤回、终止、延期和失败用独立 `event_status` 及原因记录，保留最后已证实的 C 状态，不虚构 C8 或强行回退。未见原始文件时写状态“待核实”，不能仅凭旧聊天判定当前进度。

本轮扩展整合在 Thesis Card + Event Monitor / Expectation / Data Layer 内，不新建 Event-Driven Engine。

---

## 16. Information hierarchy

A — Confirmed facts:
- filings
- exchange / regulator
- official procurement/tender
- customer disclosures

B — Leading evidence:
- IR
- supplier expansion
- hiring
- project filing / EIA
- industry conferences
- customer deployment

C — Weak signals:
- media reports
- social media
- supply-chain rumor
- expert chatter

Rule:
> Weak signals trigger investigation; they do not directly trigger investment action.

---

## 17. Controlled learning

AlphaOS should improve through:

**Decision Snapshot → Outcome → Error Diagnosis → Proposed Change → Validation → Human Approval → Version Update**

Decision Snapshot 保存当时可见证据、判断和规则版本。复盘必须分别评价 **Process Good/Bad** 与 **Outcome Good/Bad**；两者可独立组合，禁止“涨了 = 判断正确”。

Error taxonomy：

- Data Error
- Thesis Error
- Expectation Error
- Timing-Execution Error
- Risk-Position Error
- Process Violation
- No Error-Variance

Outcome 不直接触发 Core 修改；改动需完成上述验证与 Human Approval。

AI must NOT silently rewrite rules.

Use a Rule Registry / Change Log.

---

## 18. Output modes

### Decision Mode
Show:
- current state
- what changed
- implication
- next signal to watch

### Learning Mode
Expand:
- causal chain
- definitions
- comparisons
- why the conclusion follows

### Audit Mode
Show:
- source
- timestamp
- calculation
- assumptions
- confidence
- rule version

---

## 19. Foundation Model Test

For every module ask:

> If the next foundation model is 10x stronger, does this module still matter?

Durable assets:
- private state/history
- data
- thesis memory
- deterministic risk rules
- decision logs
- longitudinal evaluation

Model-only analysis is not the moat.


---

## 20. Data Layer / Data Source Abstraction — Approved / CHG-011

**字段定义与 Derived Signals 是资产，Data Source 可替换。** 保留派生指标定义、版本、原始输入、口径、时间戳和可重算记录；“资产”不意味着指标已证明有预测力。

| 数据职责 | 当前默认来源 | 使用边界 / 备援 |
|---|---|---|
| 当日实时盘面感知：竞价、Tick、盘口、分时 | thsdk 游客模式，经现有 run-readonly | 仅当日/最近交易日快照范围；历史能力不能从实时接口推定；检查行情时间和新鲜度 |
| 历史基准、个股/指数日线、控制组输入 | BaoStock | 按标的/字段验证覆盖、复权和单位；缺失则显式记录；其他源替换须先核对口径 |
| 事件与基本面事实及时间戳 | 官方公告 / 财报 / 监管 / 公司材料优先；新闻为补充 | 事件发生时间、首次发布时间、采集时间分开；新闻不能自动替代一手事实 |
| 可选补充数据 | 经核验的备用源 | 不把单次跑通当生产保证；切换保留 provenance |

**Missing is Missing**：禁止模型补造数据。事实必须保留 **source / timestamp / freshness / provenance**；无法判定新鲜度时明确写未知，不得冒充实时。OpenClaw 具体数据部署属于 Runtime MVP，不因封版继续扩框架。

### 2026-09-26 部署审计快照（历史记录，非永久能力承诺）

证据索引见 Case Lab Case #003 及本轮交接单。以下为已有报告/用户转述的审计结论，本轮未连接服务器重测：

- thsdk 1.7.18 当前游客 wrapper 不接受历史日期；适合当日实时盘面感知，不承担历史控制组。9/25 验收处于休市，返回 9/24 快照；盘中实时性与端到端延迟仍未验收。
- 历史控制组使用 BaoStock。转述测试称日线可用，但完整控制组结果、原始 CSV 和跨源核验日志未在本轮材料中提供；不推定所有 ETF/分钟/行业成分均可用。
- AKShare 的东方财富接口在当前服务器出现 502 / RemoteDisconnected / TCP timeout，故当前不作为底座。曾短暂成功与随后失败并存；不能推广成“AKShare 永久不可用”，网络故障成因也未被本轮独立确认。
- 历史外盘/内盘/主动买卖字段统一 `Low-confidence auxiliary field`；保留原值及口径问题，不用于主力净买入、内幕或 Leader 结论。未确认单位、累计/增量语义与方向编码前不参与核心派生信号。
- 回放 v1 部分历史分钟与 min_snapshot 来自 wrapper 外，标 `non-wrapper / non-production-safe`，仅作待核验历史材料；不得由此扩大当前接口能力或绕过入口复抓。

每次采集记录 source、method、symbol、event_time / published_at / market_time、received_at、timezone、复权、单位、原始文件位置、缺失原因与质量标记。未知字段保持 N/A/null；不以抓取成功代替有效性或新鲜度。

派生历史基准不包含被评估当天；样本不足、分母为零或口径冲突时输出 N/A 及原因。数据源更换后，先对同窗口样本核对再接续，避免把数据切换误记为状态迁移。
