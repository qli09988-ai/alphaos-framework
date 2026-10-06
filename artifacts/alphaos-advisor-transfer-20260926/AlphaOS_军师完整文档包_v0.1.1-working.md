# AlphaOS｜给「交易助手大模型推荐」的当前文档交接

交接日期：2026-09-26。用户指定「交易助手大模型推荐」为军师。本包为现有文件的只读传递快照，不新建主档、不改变规则、不表示再次封板。

## 当前权威版本

AlphaOS **v0.1.1-working / 2026-09-26**。唯一主档为 `alphaos_core_spec.md`。此版本是 v0.1 的增量工作版，不代表 v0.1 已完成。

旧索引 `AlphaOS_Specification_v0.1.md` 的正文未在本地取得；不要用它替代本次提供的主档。根目录五份核心文档 + README 为当前工作文档，已与合入前原 ZIP 对比，并保留版本备份。

## 请先知道进行到了哪里

**已正式合入，避免重复设计：**

- CHG-007 Thesis Type Router：Industrial / Event-Driven / Asset Realization / Hybrid。
- CHG-008 Event State C0–C7，含证据、子节点、迁移和失败/延期记录。
- CHG-009 Event Progress vs Expectation Progress，保留 E1–E4；利好程度不等于股票机会程度。
- CHG-010 Thesis Card 的 Why Now? 字段。
- CHG-011 Data Source 可替换 / Derived Signals 为资产；thsdk 当日盘面、BaoStock 历史、公告/新闻事件时间戳。
- CHG-012 Relative Strength Controls：个股 vs 市场 / 行业 / 事件篮子。

**四项收尾仍开放：**

1. Risk & Position Engine：组合/单票风险预算、集中度与相关性、最大损失约束、确定性仓位计算尚未完成，不能让模型临时编比例。
2. Thesis Card + Event Monitor：核心字段与 C0–C7 已入档；完整卡片使用、状态迁移运行、主动更新与验收仍未闭环。
3. Data Requirement Mapping：数据源职责已确定；逐字段需求、更新频率、备援、质量与运行验收待补。
4. Review / Evaluation Loop：决策时点记录、结果、错误归因、改规则提议、验证和批准的实际闭环待完成。

另有依赖：Execution 的卖出分类已有，**买入逻辑未封板**；Company Position 仍为 v0.8；Market Regime 仍需数据接入，不能把概念完成等同实盘完成。

**仍为实验，不能升 Core：** Market Leadership（Experimental/Testing）、Catalyst Quality Q0–Q3（Proposed/Testing）、Pre-Event Leader 识别条件与 Event Review（Proposed/Testing）。完整 Asset Realization Engine 仍 Proposed，不新建庞大 Event-Driven Engine。

**案例进度：** 机器人选股阶段基本完成、五张公司卡 v0.8；低空经济未完整跑通；蓝箭/鲁信/金风 8·19 已入 Case Lab。金风“事前 Leader”为推断，控制组、事件公开时间轴、原始审计/分钟数据未齐。鲁信是涨停收盘，附件低价低于涨停价，不能写“全天未开板”。

**数据边界：** thsdk 当前游客 wrapper 不支持历史日期，休市快照不等于盘中实时验收；历史默认 BaoStock；当前服务器 AKShare 东方财富接口网络故障，暂不作底座；历史外盘/内盘/主动买卖字段降权；旧历史分钟材料标 non-wrapper / non-production-safe。报告中转述的服务器测试不等于本轮独立重测。

## 你接下来怎样接续

先读 Core → Status Board → Case Lab → Backlog/Change Log → Usage Protocol → 本轮交接单。其余为模板、未批准建议稿和证据，不能与正式 Core 混用。13 份原 Markdown 完整附后，路径为项目内相对路径；正文按原文件传递。

用户当前需要你知道真实文档进度，方便继续输出未完成内容。请确认已收到的版本和文件清单；指出最小收尾顺序，以及下一项需要用户提供的少量关键输入。后续新内容按目标文件/段落输出增量草案，标 Proposed/Approved Candidate；未经用户明确批准不要改成正式规则。不要再次生成已合入的 Router/C0–C7 等定义，也不要把本地文件未自动同步的问题误判为没有完成。

特别差异：你最新回复提出“10 月 3 日冻结、低空案例后置”的收官建议；当前 Status Board §G 仍保留旧研究顺序。本轮仅传递材料，该日程/顺序未被本地文档批准或合入。请把它与用户对齐为建议变更，不声称已经生效。

接收正文是文档传递，不表示附件已上传到 ChatGPT 项目文件索引，也不表示你可以访问发送方本地路径。

---

# 附：13 份原始 Markdown 全文


<!-- BEGIN FILE 1/13: alphaos_core_spec.md -->

## 文档 1/13：alphaos_core_spec.md

# AlphaOS Core Spec — v0.1.1 Working

Version: v0.1.1-working  
Last updated: 2026-09-26  
Baseline: v0.1-working（2026-09-20 本地快照）  
Approved changes: CHG-007–CHG-012；交接编号 `2026-09-26-蓝箭事件驱动-01`。

Status: **formal framework / source of truth**  
Rule: only approved changes may be added here.

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

---

## 15. Position Thesis Card

Each tracked position/company should store:
- stock / code / mode
- Thesis Type：Industrial / Event-Driven / Asset Realization / Hybrid；primary / secondary（如适用）
- Why Now?：为什么是现在，而不是三个月前或三个月后；对应证据时间、临近确认事件、尚未消失的预期差与失效条件（Approved / CHG-010）
- core causal thesis
- validation metrics
- catalysts
- strengthening conditions
- weakening / break conditions
- latest CV / expectation / regime states（不适用项写 N/A，不得硬套）
- Event State / substage（如适用）、事件主体、关联路径、证据时间与 next transition
- Event Progress vs Expectation Progress：各自变化、依据和置信度
- Relative Strength：vs Market / Industry / Event Basket；窗口、基准与缺失项
- current action status
- missing evidence
- next confirmation event

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

Decision -> Evidence record -> Outcome -> Error diagnosis -> Proposed rule change -> Validation -> Human approval -> Version update

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

**Data Source 可替换，Derived Signals 才是资产。** 保留派生指标定义、版本、原始输入、口径、时间戳和可重算记录；“资产”不意味着指标已证明有预测力。

| 数据职责 | 当前默认来源 | 使用边界 / 备援 |
|---|---|---|
| 当日实时盘面感知：竞价、Tick、盘口、分时 | thsdk 游客模式，经现有 run-readonly | 仅当日/最近交易日快照范围；历史能力不能从实时接口推定；检查行情时间和新鲜度 |
| 历史基准、个股/指数日线、控制组输入 | BaoStock | 按标的/字段验证覆盖、复权和单位；缺失则显式记录；其他源替换须先核对口径 |
| 事件事实与时间戳 | 公开公告、交易所/公司文件、新闻 | 事件发生时间、首次发布时间、采集时间分开；新闻不能自动替代一手事实 |
| 可选补充数据 | 经核验的备用源 | 不把单次跑通当生产保证；切换保留 provenance |

### 2026-09-26 部署审计快照（非永久能力承诺）

证据索引见 Case Lab Case #003 及本轮交接单。以下为已有报告/用户转述的审计结论，本轮未连接服务器重测：

- thsdk 1.7.18 当前游客 wrapper 不接受历史日期；适合当日实时盘面感知，不承担历史控制组。9/25 验收处于休市，返回 9/24 快照；盘中实时性与端到端延迟仍未验收。
- 历史控制组使用 BaoStock。转述测试称日线可用，但完整控制组结果、原始 CSV 和跨源核验日志未在本轮材料中提供；不推定所有 ETF/分钟/行业成分均可用。
- AKShare 的东方财富接口在当前服务器出现 502 / RemoteDisconnected / TCP timeout，故当前不作为底座。曾短暂成功与随后失败并存；不能推广成“AKShare 永久不可用”，网络故障成因也未被本轮独立确认。
- 历史外盘/内盘/主动买卖字段统一 `Low-confidence auxiliary field`；保留原值及口径问题，不用于主力净买入、内幕或 Leader 结论。未确认单位、累计/增量语义与方向编码前不参与核心派生信号。
- 回放 v1 部分历史分钟与 min_snapshot 来自 wrapper 外，标 `non-wrapper / non-production-safe`，仅作待核验历史材料；不得由此扩大当前接口能力或绕过入口复抓。

每次采集记录 source、method、symbol、event_time / published_at / market_time、received_at、timezone、复权、单位、原始文件位置、缺失原因与质量标记。未知字段保持 N/A/null；不以抓取成功代替有效性或新鲜度。

派生历史基准不包含被评估当天；样本不足、分母为零或口径冲突时输出 N/A 及原因。数据源更换后，先对同窗口样本核对再接续，避免把数据切换误记为状态迁移。


<!-- END FILE 1/13: alphaos_core_spec.md -->


<!-- BEGIN FILE 2/13: alphaos_status_board.md -->

## 文档 2/13：alphaos_status_board.md

# AlphaOS Status Board — v0.1.1-working

Last updated: 2026-09-26

Framework: `alphaos_core_spec.md` v0.1.1-working；本轮交接 `2026-09-26-蓝箭事件驱动-01`。Working 增量版本，不代表 v0.1 已封板。

Purpose: show exactly where the project is, what is finished, and where v0.1 stops.

---

## A. Current phase

**Phase: Framework Validation + v0.1 closure**

The project is NOT waiting for a “perfect framework”.
Real cases are used as pressure tests.

Cases do not automatically change the framework.

---

## B. Modules

| Module | Status | Notes |
|---|---|---|
| Investment Philosophy / Constitution | ✅ Mostly sealed | Facts + Logic = View; 431 |
| Direction Engine | ✅ v0.1 usable | capex / policy / real allocation |
| Industry Lifecycle | ✅ v0.1 usable | L0-L4 |
| Commercial Validation | ✅ v0.1 usable | CV0-CV5; economic validation added |
| Bottleneck Analysis | ✅ v0.1 usable | bottleneck separated from moat |
| Profit Pool Engine | ✅ v0.1 usable | 4 tests + supply expansion risk |
| Company Position Engine | 🟡 v0.8 | 10-field structure established |
| Base Business / Optionality split | ✅ added | validated in real cases |
| Earnings Quality | ✅ added | filing-first, cash conversion |
| Expectation Engine | ✅ Approved 增量已合入 | E1-E4 + Event Progress vs Expectation Progress；非自动交易规则 |
| Reverse Expectation | ✅ v0.1 usable | reverse-implied future |
| Market Regime | ✅ conceptual v0.1 | needs live data integration |
| Execution Engine | 🟡 partial | sell taxonomy exists; buy logic not sealed |
| Risk & Position Engine | 🔴 unfinished | must be sealed before full live use |
| Thesis Card / Event Monitor | 🟡 partial | Router、Why Now?、C0–C7 已 Approved；持续更新与运行验收未完成 |
| Data Requirement Mapping | 🟡 partial | thsdk 实时 / BaoStock 历史 / 公告新闻事件时间戳已定义；逐字段、频率、备援与生产验收待补 |
| Relative Strength Controls | ✅ 方法 Approved | 市场/行业/事件篮子口径已加入；蓝箭实证控制组未齐 |
| Market Leadership Monitor | 🧪 Experimental / Testing | None / Pre-Event / Confirmation / Exhaustion；未升 Core |
| Catalyst Quality | 🟡 Proposed / Testing | Q0–Q3；未升 Core |
| Review / Evaluation Loop | 🔴 unfinished | required for controlled self-improvement |
| Market Discovery / Information Latency | ⚪ v0.2 backlog | real-time anomaly -> investigation |
| OpenClaw / lobster integration | ⚪ not yet | after v0.1 closure |

---

## C. v0.1 definition of done

v0.1 is DONE when these four remaining items are closed:

1. **Risk & Position Engine**
2. **Thesis Card + Event Monitor**
3. **Data Requirement Mapping**
4. **Review / Evaluation Loop**

No additional major engine is allowed to block v0.1 unless it is a critical defect.

---

## D. Case-study progress

### Case #001 — Embodied Intelligence
Status: **selection phase substantially complete**

Completed:
- industry definition
- why now
- lifecycle
- commercialization
- bottleneck
- profit pool
- five-company pressure test

Companies:
- 震裕科技 — Company Card v0.8
- 福立旺 — Company Card v0.8
- 五洲新春 — Company Card v0.8
- 贝斯特 — Company Card v0.8
- 万向钱潮 — Company Card v0.8

Current working grouping:
- Core tracking: 震裕科技
- Conditional tracking: 福立旺 / 万向钱潮
- Pause / wait: 五洲新春 / 贝斯特

This grouping is a **research-priority grouping**, NOT a buy ranking.

### Case #002 — Low-altitude Economy
Status: **not yet fully run through the complete framework**

Next after embodied-intelligence closure.

### Case #003 — 蓝箭 / 鲁信 / 金风 2026-08-19
Status: **回放已归档；控制组与事件时间轴待补；Leadership Testing**。

- 8/17–18 金风在两股比较中持续更强；8/19 鲁信涨停收盘，金风涨停开盘回落至接近平盘；T+1 两者快速转弱。
- “金风更像 Pre-Event Leader”为推断，不能在缺少市场/风电/事件篮子控制结果时判为独立事件领先。
- v1 历史材料存在 non-wrapper provenance；具体开板/回封时间未确认。
- 详见 Case Lab；下一次补齐控制组、官方事件内容/首次公开时间和原始审计日志后更新。无已核实未来事件日期，不安排自动任务。

---

## E. Current research stop rule

Stop deeper research if it does NOT change at least one of:

1. whether the company enters the tracking pool;
2. CV / Thesis state;
3. expectation state;
4. execution / risk action.

This rule exists to prevent research from becoming an endless encyclopedia project.

---

## F. Current practical capability

### Already useful for
- industry direction filtering
- commercialization-stage judgment
- profit-pool analysis
- separating concept stocks from real commercialization
- company-level comparative research
- early expectation-gap screening

### Not yet mature for
- exact timing
- position sizing
- automatic risk budgeting
- real-time anomaly detection
- autonomous monitoring
- self-improving rule updates

---

## G. Next project sequence

1. Finish embodied-intelligence case closure
2. Run low-altitude-economy case with the same framework
3. Return to v0.1 closure:
   - Risk & Position
   - Thesis/Event Monitor
   - Data Mapping
   - Review Loop
4. Freeze AlphaOS v0.1
5. Only then start v0.2 expansion and deeper live-data integrations


---

## H. 本轮合入与数据审计边界 — 2026-09-26

CHG-007–CHG-012 已 Approved 并合入：Router、C0–C7、Event–Expectation 联动、Why Now?、Data Source Abstraction、Relative Strength Controls。授权为用户本次明确合入请求；不是旧聊天助手建议代替批准。

数据职责：thsdk 当前游客 wrapper 仅用于当日/最近交易日盘面；BaoStock 承担历史日线与控制组输入；公告/新闻承担事件时间戳；AKShare 因该服务器东方财富网络故障暂不作底座；历史外盘/内盘/主动买卖字段降权。本次为审计材料归档，未重跑服务器测试。

四项 v0.1 闭环仍未全部完成，Risk & Position、Review Loop 及执行买入逻辑仍待封板；本轮不改变既有研究顺序，不增加庞大 Event-Driven Engine。


<!-- END FILE 2/13: alphaos_status_board.md -->


<!-- BEGIN FILE 3/13: alphaos_case_lab.md -->

## 文档 3/13：alphaos_case_lab.md

# AlphaOS Case Lab

Version: v0.1.1-working  
Last updated: 2026-09-26

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


<!-- END FILE 3/13: alphaos_case_lab.md -->


<!-- BEGIN FILE 4/13: alphaos_backlog_changelog.md -->

## 文档 4/13：alphaos_backlog_changelog.md

# AlphaOS Backlog & Change Log

Version: v0.1.1-working  
Last updated: 2026-09-26

Purpose:
- prevent chat discoveries from silently mutating the framework;
- keep v0.1 and v0.2 boundaries clean.

---

## A. Approved changes already incorporated into Core Spec

### CHG-001
Source: embodied-intelligence case
Change:
- bottleneck != profit pool
Status: Approved / in Core Spec

### CHG-002
Source: component commercialization analysis
Change:
- add Supply Expansion Risk to Profit Pool
Status: Approved / in Core Spec

### CHG-003
Source: 震裕 / 福立旺 / 五洲 cases
Change:
- add Base Business / Optionality Separation
Status: Approved / in Core Spec

### CHG-004
Source: financial-statement review
Change:
- Financial Filing First
- add Earnings Quality checks
Status: Approved / in Core Spec

### CHG-005
Source: batch-delivery cases
Change:
- CV must include economic validation after scale begins
Status: Approved / in Core Spec

### CHG-006
Source: long-form output overload
Change:
- Decision / Learning / Audit output modes
Status: Approved / in Core Spec

---

## A2. 本轮明确批准并合入 — 2026-09-26

基准 v0.1-working（9/20 本地快照）→ v0.1.1-working。授权依据：用户本次明确要求合入第 1–6 项；不是从旧助手“可正式加入”的建议推定批准。交接编号 `2026-09-26-蓝箭事件驱动-01`。

| ID | 规则变更 | Core 位置 | 状态 / 边界 |
|---|---|---|---|
| CHG-007 | Thesis Type Router：Industrial / Event-Driven / Asset Realization / Hybrid | §3、§15 | Approved / 已合入；不批准完整 Asset Realization Engine |
| CHG-008 | Event State C0–C7 + 证据、子节点、迁移/失败条件 | §15 Event Monitor | Approved / 已合入；不等于具体事件事实或监管承诺 |
| CHG-009 | Event Progress vs Expectation Progress；利好程度≠股票机会程度 | §11、§15 | Approved / 已合入；不新增自动交易条件 |
| CHG-010 | Thesis Card 增加 Why Now? | §15 | Approved / 已合入；无证据写待验证 |
| CHG-011 | Data Source 可替换、Derived Signals 为资产；三类源分工及部署审计边界 | §20 | Approved / 已合入；不代表生产验收完成 |
| CHG-012 | Relative Strength Controls：vs 市场/行业/事件篮子 | §13、§15 | Approved / 已合入方法；案例控制组结果尚缺 |

同步修改 Status Board、Case Lab、Usage Protocol 与 README；Case Observation 和 Proposed/Testing 不因这次版本增加自动转为 Approved。原 CHG-001–006 不变。

---

## B. v0.1 MUST finish

### TODO-001 — Risk & Position Engine
Need:
- portfolio risk budget
- single-position risk budget
- volatility / structure inputs
- correlation / concentration
- max portfolio loss logic
- deterministic calculation rules
- no LLM-invented percentages

### TODO-002 — Thesis Card + Event Monitor
2026-09-26：Router、Why Now?、C0–C7 已 Approved；字段规范完成部分合入。下面持续运行与验收仍未完成，TODO 不关闭。
Need:
- state fields
- validation metrics
- strengthening / weakening / break conditions
- catalyst calendar
- T-3~7, T, T+1 behavior
- proactive updates

### TODO-003 — Data Requirement Mapping
2026-09-26：实时/历史/事件源分工与部署审计边界已合入 Core §20；需补每字段覆盖、备援与运行验收，不关闭 TODO。
For each decision point:
- data needed
- source
- frequency
- automation
- backup source
- timestamp / provenance / confidence

### TODO-004 — Review / Evaluation Loop
Need:
- record decision at time T
- outcome later
- diagnose data / reasoning / rule / execution failure
- propose rule change
- validate change
- human approval
- version update

---

## C. v0.2 backlog

### BL-001 — Market Discovery / Information Latency
Problem:
- large models often learn themes after the market has already moved.
- retail investors lack first-hand industrial research channels.

Goal:
- real-time market anomaly -> active investigation

Possible inputs:
- relative strength
- turnover / volume anomaly
- multi-stock co-movement
- sector diffusion
- unexplained strength
- order-flow / tick changes
- latest announcements / tenders / patents / IR

Rule:
- price anomaly triggers investigation, not investment.

### BL-002 — Pre-Commercial Signal Engine
Goal:
- identify “uncertainty falling before mature commercialization”.

Potential signal ladder:
- policy / resource allocation
- capacity construction
- procurement / tenders
- engineering deployment
- customer test
- repeat procurement
- revenue
- margin / cash flow

### BL-003 — Asset Realization Engine
Status: **Proposed**。CHG-007 仅批准 Thesis Type，未批准本完整引擎。优先在现有 Thesis Card / Event Monitor 中承载权益、兑现条件与事件证据；本轮不新建庞大 Event-Driven Engine。
Source:
- 鲁信创投 case

For venture-capital / asset platforms:
- look-through ownership
- NAV
- IPO / exit stage
- lock-up
- realization probability
- catalyst timing

### BL-004 — live market data layer
Status: **Testing / 未完成生产验收**。原“Potential”列为历史候选清单，不代表已接入或已授权账户。当前 thsdk 游客只读入口已最小验收，但盘中实时性未验证；完整数据分工和审计边界以 Core §20 为准。
Potential:
- tonghuasun-codex
- market data APIs
- WebSocket / MCP
- account state

Use:
- market reality layer
- expectation state refresh
- regime
- later market discovery

---

## C2. 本轮实验与缺口（未升 Core）

### GAP-005 — Market Leadership Monitor
- Date / Case: 2026-09-26 / Case #003 蓝箭 8·19。
- Existing rule: 相对价格表现可作为 Expectation 输入，但无正式 Leader 规则。
- Observed failure: 事前较强者与确认日承接者不同，确认日封板亦未延续到 T+1。
- Proposed change: None / Pre-Event / Confirmation / Exhaustion，定义见 Case Lab §E。
- Status: **Experimental / Testing**；不是 Approved 或 Approved Candidate。
- Validation needed: 固定窗口与口径，补市场/行业/事件控制组及公开消息时间轴；至少再跑两个独立案例并包含失败样本；事前识别与事后标签分开。
- v0.1 critical? no；不阻塞原四项封板，不进 Core 正式决策逻辑。

### GAP-006 — Catalyst Quality Q0–Q3
- Date / Case: 2026-09-26 / Case #003。
- Existing rule: 记录事件状态，不等于衡量每个节点消除的不确定性。
- Proposed change: Q0 流程、Q1 次要疑点、Q2 关键疑点、Q3 确定性跃迁；定义见 Case Lab §F。
- Status: **Proposed / Testing**。
- Validation needed: 一手文件前后对照、评分一致性、反例、与价格预期独立；不得根据股价结果倒推 Q。
- v0.1 critical? no；Core Spec 未增加强制 Q 评分。

### GAP-007 — Pre-Event Leader 识别条件与 Event Review
- Status: **Proposed / Testing**。
- 事件前谁先动、为何动、消息何时公开、确认后谁承接，先作为复盘问题。
- 连续正超额天数、Surge_A/B、成交额 Ratio/ZScore 阈值等旧聊天设想未经批准，不作为筛选/交易标准；本轮不将它们写入 Core。
- 固定方法后补控制组与样本外验证；不得从金风一例宣布识别有效。

### GAP-008 — 回放数据质量与来源复核
- Status: **Proposed**；需补证，不是可批准的交易规则。
- v1 历史部分 non-wrapper / non-production-safe；当前 wrapper 无历史查询能力，不能混用两者能力口径。
- 取得 BaoStock 跨源审计 CSV、历史分钟原始材料、公告时间轴；处理鲁信 T 日日线低点与“全天封板”叙述差异。
- 历史外盘/内盘/主动买卖字段已按本轮批准的审计处理要求降权；AKShare 在当前服务器东方财富故障期间不作为底座，具体故障根因待核验。

---

## D. Change-control template

Whenever a case reveals a problem, record:

- Gap ID:
- Date:
- Case:
- Existing rule:
- Observed failure:
- Proposed change:
- Why it matters:
- v0.1 critical? yes/no
- Validation needed:
- Status: Proposed / Testing / Approved Candidate / Approved / Rejected
- Approval evidence / scope: Approved Candidate 仍待明确批准，不得当作已生效规则
- Core Spec version updated:


## E. 版本和冲突记录 — 2026-09-26

- 合入前，根目录 README 与五份主文档均与 `archives/AlphaOS_v0.1_portable_docs.zip` 逐字节一致；本轮基准无本地内容分叉。
- 本地与原对话附件同名 `AlphaOS_增量交接单.md` 完全一致；保留模板，新增一张已填写交接单，不覆盖模板。
- 旧聊天提及 `AlphaOS_Specification_v0.1.md`，本地和已取得附件均未找到正文，因此无法比较其内容；记录为外部旧版本未取得，不将其当最新主档。
- 本地主档已合入 v0.1.1-working；保留合入前 ZIP、哈希与 diff。历史部署页面/上传包未改，不能作为当前框架版本。


<!-- END FILE 4/13: alphaos_backlog_changelog.md -->


<!-- BEGIN FILE 5/13: alphaos_usage_protocol.md -->

## 文档 5/13：alphaos_usage_protocol.md

# AlphaOS Usage Protocol

Version: v0.1.1-working  
Last updated: 2026-09-26

Use this file when giving AlphaOS to another model/platform.

---

## 1. Reading order

1. `alphaos_core_spec.md`
2. `alphaos_status_board.md`
3. `alphaos_case_lab.md`
4. `alphaos_backlog_changelog.md`
5. 本文件；再读 `handoffs/` 中相关增量交接单；模板见 `templates/AlphaOS_增量交接单.md`。

---

## 2. Source-of-truth rule

`alphaos_core_spec.md` is authoritative.

以同一版本的一组文件为准，当前 v0.1.1-working / 2026-09-26。`archives/` 是历史快照，`deployment/` 是旧案例展示，`artifacts/` 是证据/差异，不是平行主档。旧名 `AlphaOS_Specification_v0.1.md` 本次未找到正文，不据聊天提及覆盖现有主档。

Do NOT:
- treat an old chat answer as a formal rule;
- promote a case observation to a system rule automatically;
- overwrite formal definitions based on one new example.

---

## 3. When analyzing a new company

先读取 Thesis Type Router，判断 Industrial / Event-Driven / Asset Realization / Hybrid，并填写 Why Now?。Event-Driven / Asset Realization 先核对事件事实、权益传导与兑现条件，再走 Expectation / Market Regime / Execution / Risk；CV 不适用时写 N/A。Hybrid 分开研究主业与可选项，避免重复计价。

Industrial 及 Hybrid 的产业部分沿用以下顺序：

1. Industry / Direction
2. Lifecycle
3. Commercial Validation
4. Bottleneck
5. Profit Pool
6. Base Business
7. Company Position
8. Earnings Quality
9. Earnings Elasticity
10. Expectation
11. Reverse Expectation when needed
12. Market Regime
13. Execution / Risk

Use only the depth required to change a decision.

---

## 4. Evidence discipline

Every important conclusion should identify whether it is:

- FACT
- CALCULATION
- INFERENCE
- HYPOTHESIS
- MISSING EVIDENCE

Use first-party filings before secondary reporting for financial facts.

---

## 5. State updates

A company card should change only when new evidence changes:
- CV（适用时）
- Event State / substage / event_status（适用时）
- Thesis strength
- Expectation
- risk / action

“No news” can itself become negative evidence if a time-sensitive thesis repeatedly fails to progress.

---

## 6. Preventing memory drift

At the end of a meaningful research session:

1. update the relevant Case Lab entry;
2. add any new gap to Backlog;
3. update Status Board if project progress changed;
4. update Core Spec ONLY for approved rules;
5. increment version when formal behavior changes.

---

## 7. Platform migration prompt

Use:

> You are continuing development of AlphaOS.  
> Read the attached AlphaOS files in this order: Core Spec, Status Board, Case Lab, Backlog/Change Log, Usage Protocol.  
> Treat Core Spec as the authoritative framework.  
> Do not silently merge case observations or backlog ideas into Core Spec.  
> Preserve version boundaries.  
> When you find a framework gap, record it as a proposed change first.  
> Distinguish facts, calculations, inference, hypotheses, and missing evidence.


---

## 8. 本轮批准边界与材料处理

- CHG-007–CHG-012 为 Approved；市场领先分类保持 Experimental/Testing，Catalyst Quality 保持 Proposed/Testing，Pre-Event Leader 阈值保持 Proposed/Testing。Approved Candidate 是候选，不等于 Approved，未经明确批准不得加入正式行为。
- 实验标签可附于研究卡的独立区；不得当作正式过滤器、买入信号、退出规则或仓位参数。没有证据不能为了填满字段而强行分类。
- Event Progress 和 Expectation Progress 分开维护；C0–C7 与 E1–E4 不做数字运算，业务现实状态独立记录。
- 历史控制组优先使用经口径核验的 BaoStock 日线；thsdk 当前游客 wrapper 负责当日盘面，休市快照不得冒充实时。当前服务器 AKShare/东方财富故障记录在案，作为底座须重新验收。
- 公告/新闻保留首次发布时间与采集时间；没有官方文件就不把旧聊天中的“当前阶段”和时间窗口写成事实。
- 历史外盘/内盘/主动买卖数据降权，non-wrapper 历史材料只作待核验资料；不绕过 run-readonly 补抓。
- 个股相对市场/行业/事件篮子使用一致窗口；固定控制组，不事后选样；缺失项写 Unavailable。

## 9. 增量合入与版本冲突

沿用 `templates/AlphaOS_增量交接单.md` 的全部字段：核对交接编号是否重复 → 比较基准版本/哈希与目标文件 → 保存旧版 → 按批准边界合入 → 同步版本/状态板/Case Lab/Change Log → 记录合入结果和差异。

案例 FACT 表示材料报告了什么，同时注明是否独立核实；CALCULATION 写输入、单位、公式与结果；INFERENCE/HYPOTHESIS 不能写成事实。服务器转述报告不等于本次重测。

同名不同内容必须保留与说明冲突，不能按修改时间静默覆盖。`sources/` 及同步项目文件只读；当前根目录六份文档有原 ZIP 解包记录，属于可编辑本地主档。本轮保留备份与逐文件 diff，不新建另一套框架。


<!-- END FILE 5/13: alphaos_usage_protocol.md -->


<!-- BEGIN FILE 6/13: README.md -->

## 文档 6/13：README.md

# AlphaOS Portable Docs

Version: v0.1.1-working  
Last updated: 2026-09-26  
Purpose: keep AlphaOS portable across ChatGPT, Claude, DeepSeek, local agents, OpenClaw, etc.

## Files

- `alphaos_core_spec.md` — formal framework / source of truth
- `alphaos_status_board.md` — current progress and version boundary
- `alphaos_case_lab.md` — real-world cases used to pressure-test the framework
- `alphaos_backlog_changelog.md` — gaps, proposed changes, and approved version changes
- `alphaos_usage_protocol.md` — how any model/agent should use these files without causing memory drift

- `templates/AlphaOS_增量交接单.md` — 既有模板，保持原样
- `handoffs/2026-09-26-蓝箭事件驱动-01.md` — 本轮增量交接与合入结果

## Current revision

唯一当前主档仍为本目录 `alphaos_core_spec.md`；本轮 Approved：Router、C0–C7、Event–Expectation、Why Now?、数据源抽象、相对强弱控制组。Market Leadership 与 Catalyst Quality 仍为 Proposed/Testing，定义放在 Case Lab / Backlog，不是 Core 正式规则。

v0.1.1-working 是 v0.1 的文档增量修订，不代表风险/仓位、持续监控和评估闭环已完成。

[增量交接单](handoffs/2026-09-26-蓝箭事件驱动-01.md) · [合入与冲突报告](artifacts/alphaos-20260926-lanjian-01/merge_report.md)

`archives/` 为历史备份，`artifacts/` 为证据与差异，`deployment/` 为旧案例展示；都不是另一套 Source of Truth。`sources/` 及同步参考文件保持只读。根目录主档是原 ZIP 解包的可编辑工作文件；本轮在原文件更新，没有另建框架。

## Governance rule

**Core Spec is the source of truth.**

A case result does NOT automatically become a framework rule.

Any new rule must follow:

`Case finding -> Gap -> Proposed change -> Review -> Approved change -> Core Spec update`

This prevents memory drift and “chat-based rule mutation”.

## Migration

When moving to a new platform/model, provide these files first and instruct the model:

> Read `alphaos_core_spec.md` first. Treat it as the source of truth.  
> Use `alphaos_status_board.md` to continue from the current project state.  
> Use `alphaos_case_lab.md` only as evidence/cases, not as formal rules.  
> Do not promote anything in `alphaos_backlog_changelog.md` into Core Spec unless explicitly marked Approved.


<!-- END FILE 6/13: README.md -->


<!-- BEGIN FILE 7/13: templates/AlphaOS_增量交接单.md -->

## 文档 7/13：templates/AlphaOS_增量交接单.md

# AlphaOS 增量交接单

状态：待核对合入；本模板不是正式框架变更。

- 交接编号：日期-案例-序号
- 基准主档版本/日期：
- 当前案例与问题：
- 本次材料截止时间：
- 本次新增证据：来源、发布日期、对应期间、摘录/附件位置
- 新增事实：
- 计算：输入、单位、公式、结果
- 推断与假设：
- 当前状态 → 建议状态及理由：
- 缺失证据与分歧：
- 下一确认事件/期限：
- 建议修改的文件与段落：
- 框架缺口：仅 Proposed；无则写无
- 用户明确批准的规则变更：无则写无，不得推定
- 合入结果：待处理 / 已合入及版本 / 冲突待处理

## 可复制到日常聊天的请求

请按照上述字段输出本轮 AlphaOS 增量交接单，只记录相对最近主档与已交接记录的变化。保留来源和日期，区分事实、计算、推断、假设与缺失证据；不补造历史数字，不把案例观察升级为规则。不重新分析整个案例；未能核实的内容明确标注。输出一个可保存的 Markdown 文档。


<!-- END FILE 7/13: templates/AlphaOS_增量交接单.md -->


<!-- BEGIN FILE 8/13: handoffs/2026-09-26-蓝箭事件驱动-01.md -->

## 文档 8/13：handoffs/2026-09-26-蓝箭事件驱动-01.md

# AlphaOS 增量交接单

状态：**已合入本地主档 v0.1.1-working / 2026-09-26**；实验项仅入 Case Lab / Backlog。模板沿用 `templates/AlphaOS_增量交接单.md`，未覆盖空白模板。

## 交接编号

`2026-09-26-蓝箭事件驱动-01`

## 基准主档版本/日期

`alphaos_core_spec.md` — v0.1-working；基准日期 2026-09-20（Status Board 日期及本地解包记录；旧 Core 未单独标注日期）。README 和 Usage Protocol 均指定它为 Source of Truth。

已读取并比较根目录 README、Core、Status Board、Case Lab、Backlog/Change Log、Usage Protocol 及模板。六份文档与 `archives/AlphaOS_v0.1_portable_docs.zip` 逐字节一致；本地模板与原对话附件同名模板也完全一致。根目录是已记录的 ZIP 解包可编辑文件，`sources/` 只读且本次为空。

合入前备份：[AlphaOS_pre_20260926_lanjian_01.zip](../archives/AlphaOS_pre_20260926_lanjian_01.zip)；[基准哈希](../artifacts/alphaos-20260926-lanjian-01/baseline_sha256.json)。不以文件修改时间替代内容比对。

## 当前案例与问题

Case #003：蓝箭事件驱动，600783 鲁信创投 / 002202 金风科技，T = 2026-08-19。问题：事前相对强弱、确认日承接/兑现与 T+1 转弱如何分开记录；在未排除市场/风电/事件篮子影响前，是否只能把金风看作 Pre-Event Leader 候选。

## 本次材料截止时间

资料截至 **2026-09-26 22:49（Asia/Shanghai）** 的本地文件、原对话已取得内容及当前用户合入指令；行情附件截止 **2026-08-24**。服务器审计为 9/25 本地报告及 9/26 用户转述，原始日志/CSV 未全部取得。此时间不是行情刷新时间，也不表示随后仍处于同一事件状态。本轮不做实时行情/监管状态刷新，不连接服务器重测。

## 新增证据

| ID | 来源 / 发布或记录日期 / 对应期间 | 摘录或位置 | 证据等级与限制 |
|---|---|---|---|
| EVID-01 | 原对话附件 `case_lanjian_20260819.md`；创建时间未知，9/26 取得；8/5～8/24 行情 | [原件副本](../artifacts/alphaos-20260926-lanjian-01/case_lanjian_20260819.source.md)，§1 日线、§2 分钟摘要 | 已读表格；底层原始行情未取得，部分历史数据 non-wrapper |
| EVID-02 | 原对话 9/26 用户转述 Reachability / Provenance 审计 | [摘录 JSON](../artifacts/alphaos-20260926-lanjian-01/source_audit_excerpts.json)，turn `2f97fc06-df5d-433d-bbd3-6b14119aef8a` | 当前 wrapper 无历史参数；旧历史数据来自 wrapper 外；远端原始日志未取得 |
| EVID-03 | 原对话 9/26 用户转述 BaoStock/AKShare 测试 | 同一 JSON，turn `afb6731f-c007-4181-9d8b-62db4b400adc` | BaoStock 可用、AKShare 东方财富连接故障是转述结论，不是本轮重测 |
| EVID-04 | 9/25 本地只读验收；行情时间 9/24 | [核验报告](../artifacts/ths-validation/核验报告.md)、[运行限制](../artifacts/ths-validation/LOCAL_RUNTIME.md) | 休市快照、只读范围、字段问题；盘中实时性未验收 |
| EVID-05 | 当前用户 9/26 明确合入指令及[原对话](chatgpt-conversation://6a72cde8-968c-83e9-8e76-dbd98abc4935) | 本单批准范围及 Change Log CHG-007–012 | 原助手建议不等于批准；批准以本次用户指令为依据 |

## 新增事实

以下为 EVID-01 报告的行情，尚未经本轮独立行情源认证：

- 8/17、8/18 金风分别 +3.97%、+1.15%；鲁信分别 +2.89%、-2.86%。
- 8/19 鲁信开/高/收均 20.19 元、低 19.83 元，收 +10.03%，回放称封板收盘；不能写成“全天未开板”。
- 8/19 金风开/高 24.21 元，收 22.03 元、+0.09%，表现为涨停开盘后回落至接近平盘。
- T+1（8/20）鲁信 -7.78%、金风 -9.94%，两者快速转弱。
- 数据源审计结论已按环境和日期入档：thsdk 当前游客 wrapper 仅适合当日盘面；历史控制组用 BaoStock；AKShare 因当前服务器东方财富接口网络问题暂不作为底座；历史外盘/内盘/主动买卖字段降权。

“8/19 确认日”来自用户研究锚点；本轮未取得相应公告全文/首次发布时间，不把它推成具体 C 状态迁移事实。

## 计算

价格元，收益百分比；依据原附件价格重算，结果四舍五入两位：

| 项目 | 输入 / 公式 | 结果 |
|---|---|---|
| 金风 8/17–18 累计收益 | (22.01 / 20.93 − 1) × 100% | +5.16% |
| 鲁信 8/17–18 累计收益 | (18.35 / 18.36 − 1) × 100% | -0.05% |
| 金风相对鲁信两日差 | 上述未舍入收益之差 | +5.21 个百分点，非控制组超额 |
| 金风 T 日高至收回落 | (22.03 / 24.21 − 1) × 100% | -9.00% |
| 鲁信 / 金风 T+1 收益 | 分别为 (18.62/20.19−1)×100% 与 (19.84/22.03−1)×100% | -7.78% / -9.94% |

市场/行业/事件篮子超额及 20 日成交额基准：**Unavailable**。原件仅 14 个交易日，不能伪造 20 日基准或用绝对涨跌代替控制组。复权/单位与原始数据仍待核验。

## 推断与假设

- 金风在两股比较中更像 Pre-Event Leader；尚未证明蓝箭特异性领先，行业/市场 Beta 等替代解释未排除。
- 鲁信 T 日更像 Confirmation，金风更接近 Exhaustion；这些是实验性事后描述，不是可交易规则。
- 鲁信工作路由为 Asset Realization + Event-Driven；金风为 Hybrid。权益传导及可兑现规模待原始文件，不计算估值目标。
- “2026 年 10/11 月首轮回复、11 月至 2027Q1 上会”为原对话的时间窗口假设，不是官方日程。当前 C3 说法来自旧对话，本轮未独立核实；当前 C/E 不强行赋值。
- 利好程度与股票机会程度可能背离；具体机会仍需价值传导、估值预期及风险条件，不从本例产生买入规则。

## 当前状态 → 建议状态及理由

| 对象 | 合入前 → 本轮状态 | 理由 / 限制 |
|---|---|---|
| 文档版本 | v0.1-working → v0.1.1-working，已合入 | 六项方法获本次用户明确授权；未封板 |
| Thesis Card / Event Monitor | 概念 partial → 规范 partial | Router、Why Now?、C0–C7 完成文档合入；运行闭环未完成 |
| Expectation | E1–E4 → 保留 E1–E4 并加入联动 | 事件、预期、业务现实分开；不新增 E2.5/C3.5 |
| Data Mapping | unfinished → partial | 角色与审计边界明确；逐字段/频率/备援验收待补 |
| Leadership | 无正式定义 → Experimental/Testing | 单案例与控制组缺失，不升 Core |
| Catalyst Quality | 无正式定义 → Proposed/Testing | Q0–Q3 尚无可重复验证标准 |
| Case #003 | 未归档 → 观察及缺口已归档 | 不等于确认具体 C/E 或交易状态迁移 |

## 缺失证据与分歧

1. 未取得完整市场/行业/直接关联事件控制组、原始 CSV、复权单位元数据和跨源核验日志，不能确认独立领导性。
2. 旧聊天“全天基本维持涨停”与“从未开板”不可混同；附件低点支持存在日内低于涨停价，精确开板/回封需原始分钟/逐笔验证。本轮采用“封板收盘”的受限表述。
3. v1 历史数据来自 wrapper 外与当前 wrapper 无历史参数不是同一能力；原件保留，标 non-wrapper / non-production-safe，不静默洗成合规生产数据。
4. AKShare 曾成功而后失败可并存；本轮记录环境性网络故障，不认定“机房拦截/限流”根因，也不宣称永久不可用。
5. 旧名 `AlphaOS_Specification_v0.1.md` 仅见于聊天提及，未取得正文，无法内容比对。现有正式主档的本地版本无冲突；若以后取得旧档，需内容对比后再判断是否有遗漏。

## 下一确认事件/期限

- 下一批官方问询/回复/审议文件到达时：核实首次发布时间、事件主体、C 子节点及关键未解问题，再更新 Thesis Card；无已核实固定日期。
- 下一次 v2 数据交付时：取得 BaoStock 原始控制组日线、成分证据和审计日志，重算相对强弱，核对旧分钟数据。
- 原时间窗口只作假设；届满无进展则记录延迟并复核，不把无消息自动当终止。
- Leadership/Q 的升级门槛：固定定义、补充独立案例及反例、Review、用户明确批准；本轮不设自动升级或监控任务。

## 建议修改的文件与段落

以下已完成；模板保持不变：

| 文件 | 段落 / 合入内容 |
|---|---|
| [Core Spec](../alphaos_core_spec.md) | §3 Router；§11 Event–Expectation；§13 Relative Strength；§15 Why Now? / C0–C7；§20 Data Layer 与审计快照 |
| [Status Board](../alphaos_status_board.md) | B 模块、D Case #003、H 本轮边界；四项闭环继续开放 |
| [Case Lab](../alphaos_case_lab.md) | 原鲁信案例交叉引用；Case #003 证据、事实、计算、推断、实验定义及缺口 |
| [Backlog / Change Log](../alphaos_backlog_changelog.md) | CHG-007–012；TODO-002/003 部分进展；BL-003/004 边界；GAP-005–008；版本冲突记录 |
| [Usage Protocol](../alphaos_usage_protocol.md) | 阅读顺序、路由、状态更新、实验边界、源审计、备份与合入流程 |
| [README](../README.md) | 同步版本、唯一主档、交接/证据入口及历史文件角色 |

## 框架缺口（Proposed）

GAP-005 Leadership（Experimental/Testing）、GAP-006 Q 分级（Proposed/Testing）、GAP-007 Pre-Event Leader 识别与 Event Review（Proposed/Testing）、GAP-008 回放来源与质量复核（Proposed）。原 BL-003 完整资产兑现引擎仍 Proposed；不增设庞大 Event-Driven Engine。

## 用户明确批准的规则变更

本次用户明确要求合入并允许标 Approved 或 Approved Candidate；六项按 **Approved** 记录：

- CHG-007 Thesis Type Router；
- CHG-008 Event State C0–C7；
- CHG-009 Event Progress vs Expectation Progress；
- CHG-010 Why Now?；
- CHG-011 Data Source Abstraction / Derived Signals 及本次审计处理边界；
- CHG-012 Relative Strength Controls。

批准的是方法与字段规范，不是案例市场判断、数据准确性、预测日期、交易阈值、仓位或完整生产运行。用户明确要求 Market Leadership 与 Catalyst Quality 不升正式 Core，已遵守。无需为已授权合入再请求批准。

## 合入结果

**已合入：v0.1.1-working / 2026-09-26，现有根目录六份文档原位更新，新建本张交接单。** 保留原模板、旧 ZIP、合入前备份、原件证据与逐文件差异；未修改 sources/、原有验收报告或部署页。

本地同名/基准版本无内容冲突；外部旧名主档未取得，保留为可追补资料缺口，不阻塞已授权合入。需后续确认的是案例事实与实验有效性，不是本次已批准的六项规则。详见[合入与核验报告](../artifacts/alphaos-20260926-lanjian-01/merge_report.md)。


<!-- END FILE 8/13: handoffs/2026-09-26-蓝箭事件驱动-01.md -->


<!-- BEGIN FILE 9/13: AlphaOS_工作方式与产品路线_建议稿.md -->

## 文档 9/13：AlphaOS_工作方式与产品路线_建议稿.md

# AlphaOS：省额度工作方式与产品路线

日期：2026-09-20。状态：建议稿，未批准为 Core Spec 规则。

## 1. 本次保存范围

原 ZIP 中的六个 Markdown 已原样保存到本项目根目录，文件内容与压缩包逐字节一致，可编辑。原 ZIP 保存在 archives/。未改动 sources/ 同步参考区。

这是 v0.1-working 的文档快照，不是完整聊天或原始研究数据库。包内案例主要是摘要，未附完整财报、公告、逐条证据链接及全部历史判断。包外新增的聊天结论尚未合入。保存工作草案不等于批准或封板。

当前状态板列出的四个未完成项：Risk & Position Engine、Thesis Card + Event Monitor、Data Requirement Mapping、Review / Evaluation Loop。执行模块的买入逻辑也未封板；关闭上述四项时应核查这一依赖。

## 2. 当前推荐：一个日常讨论入口，一套本地主档

日常案例继续在用户最方便的普通聊天中讨论。每完成一个有意义的阶段，只要求模型生成一份“增量交接单”；不必每条消息整理，更不必在 Work 把同一案例再跑一次。

本地主档作为已落盘版本；尚未落盘的交接单作为待合入记录。下一次讨论使用“最近主档 + 尚未合入的交接单”。Work 按需批量处理文件、检查冲突、制作版本快照，不承担所有日常陪聊。

合入步骤：核对基准版本 → 检查重复交接编号 → 对照目标段落 → 保存旧版 → 合入案例事实或已授权修改 → 返回变更清单。正式规则的变更仍需用户批准。发现版本冲突时保留两份，不按时间新旧盲目覆盖。

重要限制：普通聊天不自动读取或写入本地目录；本次也没有配置自动同步。因此短期仍需一次交接文件传递，但无需重复研究、逐份维护六个文档。平台迁移时完整带走主档与待处理交接单，不能只带摘要。

## 3. 节省额度的操作方式

- 第一次启动案例：提供规则、状态板及该案例材料。后续主要提供新增证据与当前案例卡；切换模型或规则版本时重新提供必要上下文。
- 每轮只问一个会影响判断的问题，例如“新公告是否足以把 CV 从当前阶段推进到下一阶段”，避免反复全行业重做。
- 日常输出限于：新增事实、状态变化、缺失证据、下一步验证。需要讲原理时再展开学习模式。
- 整理和排版可选轻量模型；证据冲突、重要推理、规则审查再使用更强模型。不得为了省额度删掉关键证据核查。
- 有实质新材料或确认事件再更新；不让智能体无目标地全天循环研究。
- 同一轮可以批量合入几个交接单，但仍逐项核对。减少对话次数不等于无限长任务更便宜。
- 成本改善需要观察：每个案例耗时、工具调用、返工次数与额度消耗。这里不承诺具体节省比例。

官方用量参考：https://learn.chatgpt.com/docs/pricing
查询日期：2026-09-20。官方页面说明 Work 与 Codex 共享用量，较小模型可延长额度使用；API 用量按 API 价格另计。不能以“消息几次”当作固定预算，也不能假定换 OpenClaw 就免费。当前未读取用户账户的实时额度。

## 4. 从聊天补回资料

建议先在原聊天生成“相对这六份文档的新增内容清单”，附原始来源、日期和不确定项。不要要求凭记忆重建全部财务数字。优先补回会改变判断的证据、已确认定义、尚未解决分歧；需要审计的原聊天可另行导出归档。

框架引用的是规则；案例引用的是证据。两者分开存放。每条关键证据至少保存来源、发布日期、采集日期、对应期间、原文摘录或文件位置；每条判断保存依据、反证条件、当时可见信息与规则版本。

## 5. 产品方向：先做研究与跟踪工作台

建议第一版服务一个人群：愿意自己做最终判断、但难以长期维护研究证据与跟踪记录的投资者。先解决“为什么关注、什么变了、下一步验证什么”，再讨论复杂交易能力。

首个使用闭环：输入一家公司和研究问题 → 导入可信材料 → 形成带来源的案例卡 → 登记下一确认事件 → 新证据到来时更新卡片 → 保留前后差异并复盘。

首版界面可以只有四个页面：观察池、公司卡、证据与事件、复盘记录。框架编辑是维护者功能，普通使用者不能随意更改共享规则。

## 6. 不绑定某个平台的分层设计

| 层 | 保存什么 | 迁移原则 |
|---|---|---|
| 规则 | 版本化 Markdown、批准记录 | 人可读，保持版本可追溯 |
| 数据 | 证据、事件、案例卡、判断历史 | 先用文件，后用数据库；保留 JSON/CSV 导出 |
| 计算 | 财务与风险公式、输入和结果 | 使用确定性计算；公式须先定义验证 |
| 工作流 | 获取材料、提取、检查、更新 | 可接普通程序或 Agent，不依赖某个聊天历史 |
| 模型 | 解释、推理、证据冲突识别 | 通过适配层替换供应商，换模型后用固定案例回测 |
| 界面 | 网页、报告、聊天入口 | 展示相同规则与数据，不各自保存另一套真相 |

HTML 是网页界面的基础；Agent 框架负责执行流程。二者可组合。这里没有评测 OpenClaw 的当前功能或成本，也不把它设为必须依赖。单文件网页可做本地查看与导入导出；多人持久化协作通常需要后端、账户和数据库。

## 7. 给别人使用时的边界

共享规则与公共证据；个人观察池、笔记、持仓、判断记录按用户隔离。共享案例结论必须带日期和规则版本，不能自动变成所有人的个人行动。

部署时密钥放在服务端，设置每用户任务与支出上限；相同公共材料可在权限允许时复用处理结果，个人结果不能跨用户混用。先决定由产品方承担调用费还是用户接自己的模型服务，不能默认个人 Plus 覆盖产品运营成本。

首版范围建议为研究、证据追踪与复盘，不包含自动下单或尚未验证的精确仓位输出。是否扩展到个性化荐股、收费分发及交易执行，应在确定服务地区和具体功能后另行核查相关要求与数据授权；本建议不作法律资格判断。

## 8. 何时进入下一阶段

阶段 A：个人文档版。用少量真实案例检验交接流程，并补齐 v0.1 四项；可先做研究，未完成风控不表示可以完整实盘运行。

阶段 B：小范围网页试用。先测试陌生使用者是否能看懂证据、状态和下一步；支持完整导出。优先手动触发更新，测量单次任务成本。

阶段 C：必要时加入 Agent。仅自动化已经稳定、重复且有明确触发条件的步骤。加入失败重试上限、费用硬上限、数据过期标识和人工审查入口。

验收重点：重要结论能否追溯来源；未知能否明确标出；重复输入是否稳定；旧记录是否保留；是否误用未来信息；单任务成本是否可控。先证明这些，再用长期样本评估决策质量，不能用几次盈利案例证明系统有效。

下一步最小行动：在原聊天就一个正在研究的公司生成增量交接单，合入一次，验证是否无需复述就能继续。此建议不更改原状态板的研究顺序。


<!-- END FILE 9/13: AlphaOS_工作方式与产品路线_建议稿.md -->


<!-- BEGIN FILE 10/13: artifacts/ths-validation/核验报告.md -->

## 文档 10/13：artifacts/ths-validation/核验报告.md

# AlphaOS / OpenClaw 同花顺 Skill 安装与只读验收报告

验收日期：2026-09-25，北京时间约21:10–21:15。

## 安装状态

- 云服务器：racknerd-b72658b（192.3.226.167），Ubuntu / x86_64，Python 3.12.3，OpenClaw 2026.3.8，ClawHub CLI 0.7.0。
- 通过服务器 ClawHub CLI 从 https://clawhub.ai 原始源安装 bensema/ths-advanced-analysis 1.0.4。
- 安装目录：`/root/.openclaw/workspace/skills/ths-advanced-analysis`。
- OpenClaw 最终检查：`source=openclaw-workspace`，`eligible=true`，`disabled=false`，`blockedByAllowlist=false`。已确认发现与资格检查，未让会话自动执行交易分析。
- 依赖一致性检查通过；测试运行目录未生成 account.session。
- 依赖：`thsdk==1.7.18`，独立解释器 `/root/.openclaw/venvs/ths-advanced-analysis-1.7.18/bin/python`。
- PyPI 2.0.2 已更改接口，不兼容旧 THS 类，故不使用上游未固定版本的升级命令。
- 上游文件初始 SHA256 与先前原始下载包逐项一致。SKILL.upstream.txt 保留原文，SKILL.md 仅追加本地环境与只读入口提示；新增 LOCAL_RUNTIME.md、run-readonly。
- 未读取账户/持仓/自选股，未下单，未配置个人密钥，未创建持续监控任务。测试只使用文档游客模式，日志已抑制敏感输出。

## 最小调用结果

两只股票先用 search_symbols 解析为 USHA600783（鲁信创投）、USZA002202（金风科技）。所有下列调用均返回成功且非空。

| 能力 / SDK 方法 | 鲁信记录数 | 金风记录数 | 单次请求耗时（秒，鲁信/金风） |
|---|---:|---:|---|
| 1分钟K / `klines()` | 4 | 4 | 0.313 / 0.237 |
| 五档盘口 / `depth()` | 1 | 1 | 0.273 / 0.207 |
| Tick / `tick_level1()` | 4407 | 4868 | 0.559 / 1.86 |
| 日内分时 / `intraday_data()` | 241 | 241 | 0.85 / 0.737 |
| 大单流向 / `big_order_flow()` | 86 | 905 | 0.287 / 0.506 |
| 集合竞价快照 / `call_auction()` | 44 | 63 | 0.242 / 0.237 |
| 集合竞价异动（市场级） / `call_auction_anomaly()` | 794 | 720 | 0.718 / 0.473 |

竞价异动记录数分别为沪市与深市全市场数量，不是两只目标股票的异动次数。K线请求 count=3，实测返回4行，调用方应自行按需要截取，不能假定服务端严格限制行数。

## 实时性与延迟

- 9月25日至27日为中秋休市；最近交易日为9月24日。分钟K与分时末条均为2026-09-24 15:00，符合休市快照情形，不能据此证明盘中实时服务。
- 依据：[上交所2026年休市安排](https://www.sse.com.cn/disclosure/dealinstruc/closed/c/c_20251222_10802510.shtml)、[深交所中秋节休市通知](https://investor.szse.cn/disclosure/notice/general/t20260917_622911.html)。
- Tick 相邻时间间隔中位数为3秒；鲁信4025个间隔为3秒、金风4742个间隔为3秒。这是数据时间粒度，不能当作网络/行情延迟。
- 行情查询实测约0.207–1.860秒，游客初次连接约5.7–8.4秒；样本量小，不是服务等级承诺。
- 五档无行情时间戳，无法单独判定数据年龄。Tick 末条分别为9月24日15:27:58、15:28:30，超出普通连续交易时段，时间语义仍待核对。
- 盘中端到端延迟、更新持续性、交易日09:15–09:25竞价新鲜度尚未验证。需在开市时比较采集时间与可靠行情时间，并与独立行情源核对；未安排自动后续任务。

## 受限能力与数据质量

- 分钟K、五档和分时价格/成交量字段通过基础读取检查；未声称完成全字段正确性校验。
- Tick 成交方向含异常占位值：鲁信44条、金风63条。分时“领先指标”均为占位值，不能使用。
- 集合竞价快照成功，但竞价异动大量字段不可用：沪市155个价格、612个总金额值异常；深市231个价格、438个总金额值异常。该能力仅部分可用，不能直接据此计算抢筹金额。
- 大单有86/905条记录，但“委托买入价/委托卖出价”的数值与股价量级不符，字段含义尚未确认，不能解释为真实挂单价格。
- 只读入口将数值4294967295、2147483648及上述未确认的大单字段置为null，报告数量，不补造数据。不对未知编码做买卖方向映射。
- 游客数据权限和稳定性未作生产保证；未验证 Level-2、逐笔委托/撤单、订阅推送。

## AlphaOS 可调用入口

这是服务器本地 CLI / Python 接口，未创建HTTP服务或MCP服务。OpenClaw 读取 Skill 时应先使用 LOCAL_RUNTIME.md 的解释器和入口。

```bash
/root/.openclaw/workspace/skills/ths-advanced-analysis/run-readonly --symbol 鲁信创投 --method depth --include-data
/root/.openclaw/workspace/skills/ths-advanced-analysis/run-readonly --symbol 金风科技 --method klines --include-data
```

允许的方法：`klines`、`depth`、`tick_level1`、`intraday_data`、`big_order_flow`、`call_auction`、`call_auction_anomaly`；默认`all`运行全套最小核验。`search_symbols`是内部前置步骤。

响应为JSONL，包含接口状态、记录数、采集时间、行情时间（若存在）、请求耗时、异常值计数；`--include-data`返回清洗后的完整数据。默认仅摘要与末条样例。`ok=true`仅代表接口成功，不能作为实时性或交易信号。

其他上游接口（例如历史分时、板块、指数、问财、新闻）不在本次验收范围。

## 证据文件

- `openclaw-skill-info.json`：最终OpenClaw发现结果。
- `luxin-results.jsonl`、`goldwind-results.jsonl`：最小请求与响应摘要。
- `entrypoint-check.jsonl`：AlphaOS入口完整五档调用验证。
- `LOCAL_RUNTIME.md`：部署/调用与限制说明。
- `api-static-check.json`：SDK接口静态核对。

原始来源：[ClawHub bensema](https://clawhub.ai/bensema/skills/ths-advanced-analysis)、[PyPI thsdk 1.7.18](https://pypi.org/project/thsdk/1.7.18/)。


<!-- END FILE 10/13: artifacts/ths-validation/核验报告.md -->


<!-- BEGIN FILE 11/13: artifacts/ths-validation/LOCAL_RUNTIME.md -->

## 文档 11/13：artifacts/ths-validation/LOCAL_RUNTIME.md

# AlphaOS 部署说明（本地补充，非上游原文）

部署：racknerd-b72658b，2026-09-25。
上游：bensema/ths-advanced-analysis 1.0.4，ClawHub 原始源。
Skill 目录：/root/.openclaw/workspace/skills/ths-advanced-analysis
独立解释器：/root/.openclaw/venvs/ths-advanced-analysis-1.7.18/bin/python
依赖固定 thsdk==1.7.18。不要运行上游未固定版本的 pip install --upgrade thsdk：2.0.2 已改变接口，不兼容本文的 THS 类。

## 只读入口

优先调用同目录的 run-readonly；它使用独立环境、清空继承的认证环境变量、采用文档游客模式，不读取用户账户、持仓或自选股，不允许下单及任意方法分发。

```bash
/root/.openclaw/workspace/skills/ths-advanced-analysis/run-readonly --symbol 鲁信创投 --method depth --include-data
/root/.openclaw/workspace/skills/ths-advanced-analysis/run-readonly --symbol 金风科技 --method klines --include-data
```

方法 allowlist：klines（1m、请求3条，服务端实测返回4条）、depth、tick_level1、intraday_data、big_order_flow、call_auction、call_auction_anomaly。默认 --method all 为全套最小核验；--include-data 输出净化后的完整返回记录，省略则仅输出摘要和末行。先通过 search_symbols 解析唯一A股证券，多候选则停止。

输出为 JSONL。ok 仅表示接口成功，不能表示数据实时。提供 received_at、latest_market_time、elapsed_seconds、rows、fields、invalid_value_count 等证据。elapsed_seconds 为请求耗时，不是行情延迟。五档响应没有行情时间戳，不能单凭成功响应判断新鲜度。未接入完整交易日历，不自动将上一交易日快照解释为实时信号。

SDK 日志与原生标准输出被抑制，错误只报告分类，不打印认证对象或原始异常。游客连接失败则停止，不能自动升级到用户账户登录。需要个人授权时由用户自行完成，禁止要求用户在聊天中发送密码或密钥。游客模式不保证生产稳定性与专业数据权限。

## 数据限制

- 本次为2026-09-25休市时测试，返回9月24日记录。盘中实时性和端到端延迟未验证。
- 原始响应出现 4294967295、2147483648 异常占位数值。只读入口将其置为 null 并统计，不可据此触发信号。
- 大单的“委托买入价/委托卖出价”字段实测数值明显不符合股价量级，含义未确认；入口暂置 null，禁止解释为挂单价格或自动缩放。
- Tick 标为3秒粒度，不代表逐笔委托/撤单，更不代表3秒内到达。实测包含15:00之后的时间戳，时间语义仍需交易时段核对；不得直接用其计算端到端延迟。
- 集合竞价异动是市场级扫描，不能仅因返回非空就认定目标股票存在异动。
- 本次未创建轮询任务或交易策略，不会持续监控或自动下单。

SDK 原始 Python 方法见上游 SKILL.md。SKILL.upstream.txt 保存安装时原文；SKILL.md 仅增加指向本说明的本地部署提示。


<!-- END FILE 11/13: artifacts/ths-validation/LOCAL_RUNTIME.md -->


<!-- BEGIN FILE 12/13: artifacts/alphaos-20260926-lanjian-01/merge_report.md -->

## 文档 12/13：artifacts/alphaos-20260926-lanjian-01/merge_report.md

# AlphaOS 本轮合入与冲突报告

日期：2026-09-26。交接编号：`2026-09-26-蓝箭事件驱动-01`。结果：**已合入原有本地主档，v0.1.1-working**，未重建重复体系；不是 v0.1 封板或部署上线。

## 主档识别与比较

- Source of Truth：[alphaos_core_spec.md](../../alphaos_core_spec.md)。基准是 v0.1-working，日期按旧状态板及解包记录为 2026-09-20。
- 已读六份便携 Markdown、模板、工作路线建议稿、9/25 thsdk 核验报告/运行说明、原对话最近 10 轮及附件案例。
- 合入前六份便携 Markdown 与原始 ZIP 逐字节一致。根目录文件来自原 ZIP 解包，已有材料明确记为可编辑；`sources/` 为空且保持未改。
- 两份同名交接模板（本地和原对话附件）完全一致；没有静默覆盖分叉。空白模板仍保持原样，已填写交接单放入 `handoffs/`。
- `AlphaOS_工作方式与产品路线_建议稿.md` 仍是未批准建议；`deployment/` HTML/上传 JSON 是旧鲁信展示，不是框架主档，均未修改。
- 旧聊天提到 `AlphaOS_Specification_v0.1.md`，但本次未取得其正文，不能比较；保留此资料缺口，不用旧名取代已确认的 Core Spec。

## 文件变更

| 文件 | 修改内容 | 最终版本 / 日期 |
|---|---|---|
| [Core Spec](../../alphaos_core_spec.md) | §3 Router、§11 事件/预期联动、§13 相对强弱、§15 Why Now? 与 C0–C7、§20 数据源分工及审计 | v0.1.1-working / 2026-09-26 |
| [Status Board](../../alphaos_status_board.md) | 同步各模块 Approved/partial/Testing；增加 Case #003；保留四项未完成闭环 | 同上 |
| [Case Lab](../../alphaos_case_lab.md) | 蓝箭/鲁信/金风回放，来源、事实/计算/推断/假设与缺失项；Leadership、Q 实验定义 | 同上 |
| [Backlog / Change Log](../../alphaos_backlog_changelog.md) | CHG-007–012 批准记录、GAP-005–008、旧 Asset Realization Engine 边界和冲突说明 | 同上 |
| [Usage Protocol](../../alphaos_usage_protocol.md) | 路由、阅读顺序、实验/正式边界、证据纪律与增量合入流程 | 同上 |
| [README](../../README.md) | 统一版本、唯一主档、交接入口、历史文件角色 | 同上 |
| [增量交接单](../../handoffs/2026-09-26-蓝箭事件驱动-01.md) | 新建一张实例，沿用原模板全部 15 个字段并写入合入结果 | 编号 2026-09-26-蓝箭事件驱动-01；合入 v0.1.1-working |

## 批准与实验边界

已批准并合入 CHG-007–012：Thesis Type Router、Event State C0–C7、Event Progress vs Expectation Progress、Why Now?、Data Source Abstraction、Relative Strength Controls。依据是本次用户明确合入指令，不是把旧聊天助手建议当成批准。

仍未升 Core：Market Leadership **Experimental/Testing**；Catalyst Quality Q0–Q3 **Proposed/Testing**；Pre-Event Leader 识别阈值与 Event Review **Proposed/Testing**。BL-003 完整资产兑现引擎仍 Proposed。所有新内容整合在原有卡片、事件、预期及数据层，没有新建 Event-Driven Engine。

## 数据审计与案例分歧处理

- thsdk 当前游客 wrapper 定位当日实时盘面感知；9/25 是休市快照验收，不能表示盘中实时性已证实。
- BaoStock 为历史日线/控制组默认源；服务器测试结论仅取得用户转述，未重新拉取或验证原始 CSV。
- AKShare 当前服务器的东方财富接口故障，因此不作底座；短暂成功与后续失败分别保留，不夸大为永久失效，也未确认网络阻断根因。
- 历史外盘/内盘/主动买卖字段降权；v1 wrapper 外历史数据标 non-wrapper / non-production-safe。
- 案例保留金风事前更像 Leader、鲁信确认日涨停收盘/金风回落、T+1 两股转弱；前者明确为推断。原表鲁信日内低点低于涨停价，因此不写“全天未开板”。
- 缺市场/行业/事件控制组结果、完整官方消息时间轴、服务器原始审计日志及分钟原件。未用缺失数据赋 C/E/Q 状态、预期日期或交易规则。

## 备份、差异和核验

[合入前备份](../../archives/AlphaOS_pre_20260926_lanjian_01.zip) · [基准 SHA256](baseline_sha256.json) · [机器核验摘要](verification.json)

逐文件差异：[Core](alphaos_core_spec.diff)、[Status](alphaos_status_board.diff)、[Case](alphaos_case_lab.diff)、[Backlog](alphaos_backlog_changelog.diff)、[Usage](alphaos_usage_protocol.diff)、[README](README.diff)。

已核对版本日期、交接字段、CHG 编号、实验隔离、文档本地链接、旧版备份哈希与模板不变；案例两日收益、T 日/T+1 收益及高点至收盘回落从附件价格重算一致。核验针对文档与算术，不代表市场事实或远端服务已经独立复测。

没有阻塞本轮合入的版本冲突，无需重新批准已授权的六项规则。后续需补的是旧名主档正文（如仍需比较）与上述案例证据；实验项若要升为正式规则，仍需验证后明确批准。


<!-- END FILE 12/13: artifacts/alphaos-20260926-lanjian-01/merge_report.md -->


<!-- BEGIN FILE 13/13: artifacts/alphaos-20260926-lanjian-01/case_lanjian_20260819.source.md -->

## 文档 13/13：artifacts/alphaos-20260926-lanjian-01/case_lanjian_20260819.source.md

# CASE 蓝箭 2026-08-19 数据复盘

**股票**：600783 鲁信创投 / 002202 金风科技
**窗口**：T-10 (2026-08-05) ~ T+3 (2026-08-24)，14 个交易日
**说明**：
- 🔴 红涨 / 🟢 绿跌（中国市场约定）
- 时区 Asia/Shanghai
- 沪深300 / 行业板块指数历史日线在游客权限下接口返回空（"not data"），对应字段标 "N/A"
- 换手率 / 量比历史值游客权限拉不到，仅实时值；标注 "N/A"
- min_snapshot（外/内盘）超出 run-readonly allowlist，是为响应"主动买卖特征"需求而直接调用的只读接口

## 1. 日线数据

### 1.1 鲁信创投 600783

| 日期 | 开 | 高 | 低 | 收 | 涨跌幅% | 振幅% | 实体% | 成交额(亿) | 成交量(万) | 量比 | 换手率 | 沪深300 | 所属板块 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-05 | 17.06 | 18.29 | 17.0 | 18.12 | nan | 7.56 | 6.21 | 5.99 | 3377.5 | N/A | N/A | N/A | N/A |
| 2026-08-06 | 17.8 | 18.72 | 17.61 | 18.34 | 1.21 | 6.24 | 3.03 | 6.76 | 3710.4 | N/A | N/A | N/A | N/A |
| 2026-08-07 | 18.45 | 18.65 | 17.79 | 18.45 | 0.60 | 4.66 | 0.00 | 6.77 | 3705.6 | N/A | N/A | N/A | N/A |
| 2026-08-10 | 18.53 | 18.6 | 17.5 | 18.02 | -2.33 | 5.94 | -2.75 | 5.47 | 3029.0 | N/A | N/A | N/A | N/A |
| 2026-08-11 | 16.39 | 17.46 | 16.25 | 17.15 | -4.83 | 7.38 | 4.64 | 6.32 | 3739.6 | N/A | N/A | N/A | N/A |
| 2026-08-12 | 17.3 | 18.16 | 17.0 | 17.65 | 2.92 | 6.71 | 2.02 | 5.01 | 2855.8 | N/A | N/A | N/A | N/A |
| 2026-08-13 | 17.71 | 19.05 | 17.71 | 18.54 | 5.04 | 7.57 | 4.69 | 6.70 | 3608.8 | N/A | N/A | N/A | N/A |
| 2026-08-14 | 18.55 | 18.78 | 17.92 | 18.36 | -0.97 | 4.64 | -1.02 | 3.87 | 2120.9 | N/A | N/A | N/A | N/A |
| 2026-08-17 | 18.5 | 18.91 | 18.25 | 18.89 | 2.89 | 3.57 | 2.11 | 3.72 | 2003.1 | N/A | N/A | N/A | N/A |
| 2026-08-18 | 18.7 | 18.88 | 18.32 | 18.35 | -2.86 | 2.99 | -1.87 | 3.84 | 2070.6 | N/A | N/A | N/A | N/A |
| 2026-08-19 | 20.19 | 20.19 | 19.83 | 20.19 | 10.03 | 1.78 | 0.00 | 8.97 | 4443.2 | N/A | N/A | N/A | N/A |
| 2026-08-20 | 19.38 | 19.54 | 18.17 | 18.62 | -7.78 | 7.07 | -3.92 | 14.91 | 8046.7 | N/A | N/A | N/A | N/A |
| 2026-08-21 | 18.37 | 18.51 | 16.99 | 17.1 | -8.16 | 8.27 | -6.91 | 5.64 | 3233.2 | N/A | N/A | N/A | N/A |
| 2026-08-24 | 16.75 | 16.92 | 15.7 | 16.1 | -5.85 | 7.28 | -3.88 | 3.95 | 2442.3 | N/A | N/A | N/A | N/A |

### 1.2 金风科技 002202

| 日期 | 开 | 高 | 低 | 收 | 涨跌幅% | 振幅% | 实体% | 成交额(亿) | 成交量(万) | 量比 | 换手率 | 沪深300 | 所属板块 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-05 | 19.5 | 20.35 | 19.5 | 20.16 | nan | 4.36 | 3.38 | 28.15 | 14059.7 | N/A | N/A | N/A | N/A |
| 2026-08-06 | 20.1 | 21.58 | 20.09 | 20.76 | 2.98 | 7.41 | 3.28 | 36.62 | 17576.7 | N/A | N/A | N/A | N/A |
| 2026-08-07 | 20.43 | 21.88 | 20.43 | 21.8 | 5.01 | 7.10 | 6.71 | 41.66 | 19439.9 | N/A | N/A | N/A | N/A |
| 2026-08-10 | 21.9 | 21.9 | 20.88 | 21.68 | -0.55 | 4.66 | -1.00 | 39.49 | 18521.8 | N/A | N/A | N/A | N/A |
| 2026-08-11 | 20.01 | 20.34 | 19.76 | 19.92 | -8.12 | 2.90 | -0.45 | 45.45 | 22665.4 | N/A | N/A | N/A | N/A |
| 2026-08-12 | 19.89 | 20.95 | 19.57 | 20.44 | 2.61 | 6.94 | 2.77 | 27.02 | 13356.4 | N/A | N/A | N/A | N/A |
| 2026-08-13 | 20.77 | 21.41 | 20.62 | 20.93 | 2.40 | 3.80 | 0.77 | 31.60 | 14988.8 | N/A | N/A | N/A | N/A |
| 2026-08-14 | 20.94 | 21.15 | 20.48 | 20.93 | 0.00 | 3.20 | -0.05 | 19.11 | 9201.2 | N/A | N/A | N/A | N/A |
| 2026-08-17 | 21.4 | 21.76 | 21.01 | 21.76 | 3.97 | 3.50 | 1.68 | 26.01 | 12142.0 | N/A | N/A | N/A | N/A |
| 2026-08-18 | 21.75 | 22.18 | 21.3 | 22.01 | 1.15 | 4.05 | 1.20 | 31.79 | 14615.2 | N/A | N/A | N/A | N/A |
| 2026-08-19 | 24.21 | 24.21 | 22.0 | 22.03 | 0.09 | 9.13 | -9.00 | 94.64 | 40822.2 | N/A | N/A | N/A | N/A |
| 2026-08-20 | 21.5 | 21.53 | 19.83 | 19.84 | -9.94 | 7.91 | -7.72 | 54.75 | 26937.5 | N/A | N/A | N/A | N/A |
| 2026-08-21 | 19.24 | 19.5 | 18.9 | 19.19 | -3.28 | 3.12 | -0.26 | 30.43 | 15884.1 | N/A | N/A | N/A | N/A |
| 2026-08-24 | 18.9 | 19.1 | 18.0 | 18.3 | -4.64 | 5.82 | -3.17 | 24.78 | 13460.5 | N/A | N/A | N/A | N/A |

## 2. 5m 分钟级 — 鲁信创投 600783

| 日期 | 竞价涨幅% | 价@09:35 | @09:35较昨收% | 价@09:50 | @09:50较昨收% | 价@10:00 | @10:00较昨收% | 价@11:30 | @11:30较昨收% | 价@14:00 | @14:00较昨收% | 价@15:00 | @15:00较昨收% | 首拉时点 | 首拉涨幅% | 盘中最大回撤% | 尾盘价 | 尾盘较昨收% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-05 | 0.0 | 17.06 | 0.0 | 17.18 | 0.703 | 17.33 | 1.583 | 17.72 | 3.869 | 18.09 | 6.038 | 18.12 | 6.213 | 10:10 | 1.482 | 2.611 | 18.12 | 6.213 |
| 2026-08-06 | -1.766 | 18.35 | 1.269 | 18.3 | 0.993 | 18.21 | 0.497 | 17.94 | -0.993 | 18.03 | -0.497 | 18.34 | 1.214 | 14:50 | 1.16 | 4.808 | 18.34 | 1.214 |
| 2026-08-07 | 0.6 | 17.93 | -2.236 | 18.32 | -0.109 | 18.19 | -0.818 | 18.4 | 0.327 | 18.29 | -0.273 | 18.45 | 0.6 | 09:50 | 1.891 | 4.045 | 18.45 | 0.6 |
| 2026-08-10 | 0.434 | 17.7 | -4.065 | 17.66 | -4.282 | 18.07 | -2.06 | 18.15 | -1.626 | 18.12 | -1.789 | 18.02 | -2.331 | 09:55 | 1.642 | 5.914 | 18.02 | -2.331 |
| 2026-08-11 | -9.046 | 16.65 | -7.603 | 16.83 | -6.604 | 17.11 | -5.05 | 17.11 | -5.05 | 17.32 | -3.885 | 17.15 | -4.828 | 09:55 | 1.783 | 4.13 | 17.15 | -4.828 |
| 2026-08-12 | 0.875 | 17.14 | -0.058 | 17.22 | 0.408 | 17.25 | 0.583 | 17.78 | 3.673 | 17.63 | 2.799 | 17.65 | 2.915 | 11:20 | 2.282 | 3.8 | 17.65 | 2.915 |
| 2026-08-13 | 0.34 | 18.38 | 4.136 | 18.67 | 5.779 | 18.84 | 6.742 | 18.5 | 4.816 | 18.52 | 4.929 | 18.54 | 5.042 | 09:45 | 1.629 | 4.011 | 18.54 | 5.042 |
| 2026-08-14 | 0.054 | 18.34 | -1.079 | 18.24 | -1.618 | 18.41 | -0.701 | 18.13 | -2.211 | 18.25 | -1.564 | 18.36 | -0.971 | 13:25 | 1.109 | 4.579 | 18.36 | -0.971 |
| 2026-08-17 | 0.763 | 18.51 | 0.817 | 18.55 | 1.035 | 18.45 | 0.49 | 18.48 | 0.654 | 18.55 | 1.035 | 18.89 | 2.887 | 09:50 | 0.98 | 2.145 | 18.89 | 2.887 |
| 2026-08-18 | -1.006 | 18.75 | -0.741 | 18.48 | -2.17 | 18.52 | -1.959 | 18.49 | -2.118 | 18.57 | -1.694 | 18.35 | -2.859 | 13:35 | 0.755 | 2.966 | 18.35 | -2.859 |
| 2026-08-19 | 10.027 | 20.19 | 10.027 | 20.19 | 10.027 | 20.19 | 10.027 | 20.19 | 10.027 | 20.19 | 10.027 | 20.19 | 10.027 | 09:40 | 0.0 | 1.783 | 20.19 | 10.027 |
| 2026-08-20 | -4.012 | 18.17 | -10.005 | 18.17 | -10.005 | 18.55 | -8.123 | 18.32 | -9.262 | 18.18 | -9.955 | 18.62 | -7.776 | 09:55 | 3.137 | 7.011 | 18.62 | -7.776 |
| 2026-08-21 | -1.343 | 17.81 | -4.35 | 17.62 | -5.371 | 17.4 | -6.552 | 17.06 | -8.378 | 17.06 | -8.378 | 17.1 | -8.163 | 11:15 | 0.528 | 8.212 | 17.1 | -8.163 |
| 2026-08-24 | -2.047 | 16.65 | -2.632 | 16.47 | -3.684 | 16.31 | -4.62 | 15.81 | -7.544 | 15.76 | -7.836 | 16.1 | -5.848 | 15:00 | 1.834 | 7.21 | 16.1 | -5.848 |

## 2. 5m 分钟级 — 金风科技 002202

| 日期 | 竞价涨幅% | 价@09:35 | @09:35较昨收% | 价@09:50 | @09:50较昨收% | 价@10:00 | @10:00较昨收% | 价@11:30 | @11:30较昨收% | 价@14:00 | @14:00较昨收% | 价@15:00 | @15:00较昨收% | 首拉时点 | 首拉涨幅% | 盘中最大回撤% | 尾盘价 | 尾盘较昨收% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-05 | 0.0 | 19.65 | 0.769 | 19.7 | 1.026 | 19.87 | 1.897 | 20.24 | 3.795 | 20.29 | 4.051 | 20.16 | 3.385 | 10:00 | 1.068 | 1.671 | 20.16 | 3.385 |
| 2026-08-06 | -0.298 | 20.89 | 3.621 | 21.03 | 4.315 | 21.02 | 4.266 | 20.7 | 2.679 | 20.6 | 2.183 | 20.76 | 2.976 | 09:40 | 1.388 | 5.653 | 20.76 | 2.976 |
| 2026-08-07 | -1.59 | 20.8 | 0.193 | 21.77 | 4.865 | 21.4 | 3.083 | 21.67 | 4.383 | 21.5 | 3.565 | 21.8 | 5.01 | 09:50 | 3.078 | 3.215 | 21.8 | 5.01 |
| 2026-08-10 | 0.459 | 21.0 | -3.67 | 21.0 | -3.67 | 21.17 | -2.89 | 21.15 | -2.982 | 21.25 | -2.523 | 21.68 | -0.55 | 14:15 | 1.216 | 4.658 | 21.68 | -0.55 |
| 2026-08-11 | -7.703 | 20.0 | -7.749 | 20.2 | -6.827 | 20.19 | -6.873 | 20.2 | -6.827 | 20.0 | -7.749 | 19.92 | -8.118 | 09:45 | 1.1 | 2.852 | 19.92 | -8.118 |
| 2026-08-12 | -0.151 | 19.82 | -0.502 | 20.04 | 0.602 | 20.05 | 0.653 | 20.46 | 2.711 | 20.38 | 2.309 | 20.44 | 2.61 | 11:15 | 0.995 | 2.912 | 20.44 | 2.61 |
| 2026-08-13 | 1.614 | 20.9 | 2.25 | 21.21 | 3.767 | 21.21 | 3.767 | 21.17 | 3.571 | 21.0 | 2.74 | 20.93 | 2.397 | 10:40 | 1.137 | 2.569 | 20.93 | 2.397 |
| 2026-08-14 | 0.048 | 21.02 | 0.43 | 20.76 | -0.812 | 20.81 | -0.573 | 20.62 | -1.481 | 20.86 | -0.334 | 20.93 | 0.0 | 13:30 | 0.632 | 3.168 | 20.93 | 0.0 |
| 2026-08-17 | 2.246 | 21.14 | 1.003 | 21.2 | 1.29 | 21.12 | 0.908 | 21.39 | 2.198 | 21.54 | 2.914 | 21.76 | 3.966 | 13:15 | 0.606 | 1.822 | 21.76 | 3.966 |
| 2026-08-18 | -0.046 | 21.56 | -0.919 | 21.41 | -1.608 | 21.42 | -1.562 | 21.66 | -0.46 | 21.79 | 0.138 | 22.01 | 1.149 | 14:40 | 0.727 | 2.114 | 22.01 | 1.149 |
| 2026-08-19 | 9.995 | 22.99 | 4.453 | 23.08 | 4.861 | 23.41 | 6.361 | 22.97 | 4.362 | 23.19 | 5.361 | 22.03 | 0.091 | 09:55 | 2.47 | 9.128 | 22.03 | 0.091 |
| 2026-08-20 | -2.406 | 20.21 | -8.261 | 20.34 | -7.671 | 20.39 | -7.444 | 20.24 | -8.125 | 20.03 | -9.079 | 19.84 | -9.941 | 10:05 | 1.226 | 7.896 | 19.84 | -9.941 |
| 2026-08-21 | -3.024 | 19.14 | -3.528 | 19.4 | -2.218 | 19.3 | -2.722 | 19.11 | -3.679 | 19.01 | -4.183 | 19.19 | -3.276 | 09:50 | 0.675 | 2.667 | 19.19 | -3.276 |
| 2026-08-24 | -1.511 | 18.99 | -1.042 | 18.61 | -3.022 | 18.43 | -3.96 | 18.2 | -5.159 | 18.16 | -5.367 | 18.3 | -4.638 | 14:50 | 0.604 | 5.759 | 18.3 | -4.638 |

## 3. 1min 分钟级（主动买卖 + 异动）— 鲁信创投 600783

| 日期 | 09:30开盘价 | 09:30开盘量(手) | 09:30开盘额(万) | 外盘总量(万股) | 内盘总量(万股) | 主动买入占比% | 净主动买入(万股) | 首拉时点 | 首拉涨幅% | 首拉外盘占比% | 首拉量(手) | 尾盘外盘占比% | 尾盘净买入(万股) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-05 | 17.06 | 1074 | 183.2 | 272697.9 | 187146.7 | 59.3 | 85551.2 | 13:58:00 | 1.222 | 61.06 | 251785 | 58.29 | 5776.5 |
| 2026-08-06 | 17.8 | 6345 | 1129.4 | 285700.5 | 306329.1 | 48.26 | -20628.7 | 09:38:00 | 1.598 | 48.08 | 68878 | 49.91 | -66.2 |
| 2026-08-07 | 18.45 | 3212 | 592.6 | 244721.2 | 250275.9 | 49.44 | -5554.7 | 09:37:00 | 1.46 | 40.14 | 64154 | 51.62 | 1215.1 |
| 2026-08-10 | 18.53 | 2326 | 431.0 | 197369.6 | 217532.5 | 47.57 | -20162.9 | 10:03:00 | 0.829 | 43.16 | 123449 | 50.06 | 38.1 |
| 2026-08-11 | 16.39 | 32554 | 5335.7 | 309872.9 | 315108.6 | 49.58 | -5235.6 | 09:35:00 | 2.085 | 40.23 | 100107 | 50.32 | 247.1 |
| 2026-08-12 | 17.3 | 2572 | 445.0 | 214837.5 | 143799.4 | 59.9 | 71038.1 | 11:12:00 | 1.395 | 60.17 | 98672 | 58.44 | 4864.1 |
| 2026-08-13 | 17.71 | 2448 | 433.5 | 294647.2 | 262410.6 | 52.89 | 32236.5 | 09:36:00 | 2.231 | 59.29 | 64214 | 52.14 | 1580.1 |
| 2026-08-14 | 18.55 | 1901 | 352.6 | 135959.1 | 145283.5 | 48.34 | -9324.3 | 13:25:00 | 0.941 | 47.21 | 142204 | 50.71 | 304.6 |
| 2026-08-17 | 18.5 | 1543 | 285.5 | 120663.1 | 113684.3 | 51.49 | 6978.7 | 09:33:00 | 0.704 | 36.67 | 13581 | 56.16 | 2520.1 |
| 2026-08-18 | 18.7 | 1616 | 302.2 | 110235.2 | 122621.9 | 47.34 | -12386.7 | 09:32:00 | 0.591 | 59.93 | 9474 | 49.21 | -324.0 |
| 2026-08-19 | 20.19 | 23622 | 4769.3 | 38867.8 | 910611.6 | 4.09 | -871743.8 | 09:32:00 | 0.0 | 0.0 | 191720 | 3.71 | -44842.0 |
| 2026-08-20 | 19.38 | 13244 | 2566.7 | 820557.1 | 449928.4 | 64.59 | 370628.7 | 09:52:00 | 3.908 | 84.26 | 257061 | 61.85 | 19403.2 |
| 2026-08-21 | 18.37 | 5899 | 1083.6 | 220222.3 | 309422.0 | 41.58 | -89199.7 | 10:21:00 | 0.925 | 42.33 | 194662 | 42.1 | -5229.3 |
| 2026-08-24 | 16.75 | 2846 | 476.7 | 164146.1 | 198876.8 | 45.22 | -34730.7 | 15:00:00 | 1.513 | 47.29 | 244234 | 47.05 | -1453.1 |

## 3. 1min 分钟级（主动买卖 + 异动）— 金风科技 002202

| 日期 | 09:30开盘价 | 09:30开盘量(手) | 09:30开盘额(万) | 外盘总量(万股) | 内盘总量(万股) | 主动买入占比% | 净主动买入(万股) | 首拉时点 | 首拉涨幅% | 首拉外盘占比% | 首拉量(手) | 尾盘外盘占比% | 尾盘净买入(万股) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-05 | 19.5 | 7107 | 1386.0 | 1091798.6 | 854039.5 | 56.11 | 237759.2 | 09:32:00 | 0.766 | 52.59 | 57993 | 55.29 | 15451.5 |
| 2026-08-06 | 20.1 | 13412 | 2695.8 | 1439612.3 | 1256721.3 | 53.39 | 182891.0 | 09:38:00 | 2.672 | 67.87 | 416292 | 52.57 | 9226.5 |
| 2026-08-07 | 20.43 | 12892 | 2633.8 | 1613104.2 | 1107000.1 | 59.3 | 506104.1 | 09:50:00 | 2.303 | 67.95 | 619411 | 58.25 | 32775.5 |
| 2026-08-10 | 21.9 | 20399 | 4467.4 | 1084685.8 | 1509641.0 | 41.81 | -424955.3 | 09:40:00 | 0.669 | 33.11 | 527030 | 45.46 | -16950.2 |
| 2026-08-11 | 20.01 | 83853 | 16779.2 | 1589703.7 | 1676596.1 | 48.67 | -86892.4 | 09:33:00 | 2.07 | 48.22 | 428172 | 47.79 | -10401.4 |
| 2026-08-12 | 19.89 | 13733 | 2731.5 | 1003958.1 | 879024.1 | 53.32 | 124934.0 | 13:01:00 | 1.222 | 56.14 | 912146 | 53.82 | 10754.5 |
| 2026-08-13 | 20.77 | 7805 | 1621.1 | 1254551.5 | 957135.4 | 56.72 | 297416.1 | 09:40:00 | 1.005 | 58.73 | 269329 | 53.74 | 11551.3 |
| 2026-08-14 | 20.94 | 3406 | 713.2 | 570557.2 | 720703.9 | 44.19 | -150146.7 | 09:34:00 | 0.479 | 35.37 | 66833 | 46.72 | -6210.8 |
| 2026-08-17 | 21.4 | 7739 | 1656.1 | 852339.8 | 701817.7 | 54.84 | 150522.1 | 10:07:00 | 0.52 | 49.55 | 356702 | 56.18 | 15460.9 |
| 2026-08-18 | 21.75 | 9056 | 1969.7 | 773012.4 | 783599.9 | 49.66 | -10587.4 | 14:37:00 | 0.636 | 53.22 | 1150816 | 52.78 | 8219.6 |
| 2026-08-19 | 24.21 | 204644 | 49544.3 | 3431730.9 | 3174818.1 | 51.94 | 256912.8 | 09:33:00 | 2.214 | 48.76 | 758212 | 52.48 | 20820.7 |
| 2026-08-20 | 21.5 | 37616 | 8087.5 | 1811612.1 | 2381449.2 | 43.2 | -569837.1 | 09:33:00 | 0.927 | 39.63 | 389436 | 43.57 | -35948.5 |
| 2026-08-21 | 19.24 | 18045 | 3471.9 | 1110375.3 | 1181387.1 | 48.45 | -71011.8 | 14:44:00 | 0.785 | 49.55 | 1457835 | 49.89 | -375.5 |
| 2026-08-24 | 18.9 | 7897 | 1492.5 | 992457.0 | 1090095.0 | 47.66 | -97638.0 | 09:42:00 | 0.429 | 44.84 | 259040 | 49.89 | -293.6 |

## 4. 同步异动（鲁信 vs 金风 1min 同时段同向且涨幅均 > 0.3%，每日前 8 个时点）

| 日期 | 时点 | 鲁信涨幅% | 金风涨幅% | 鲁信量(万股) | 金风量(万股) |
|---|---|---|---|---|---|
| 2026-08-05 | 09:32:00 | 0.527 | 0.766 | 84 | 580 |
| 2026-08-05 | 09:53:00 | 0.350 | 0.305 | 515 | 2520 |
| 2026-08-05 | 09:58:00 | 0.407 | 0.457 | 575 | 2936 |
| 2026-08-05 | 10:00:00 | 0.522 | 0.404 | 614 | 3201 |
| 2026-08-05 | 10:06:00 | 0.798 | 0.498 | 890 | 4491 |
| 2026-08-05 | 10:18:00 | 0.616 | 0.548 | 1474 | 5929 |
| 2026-08-06 | 09:31:00 | 1.404 | 1.891 | 162 | 949 |
| 2026-08-06 | 09:32:00 | 1.551 | 2.490 | 245 | 1692 |
| 2026-08-06 | 09:38:00 | 1.598 | 2.672 | 689 | 4163 |
| 2026-08-06 | 10:51:00 | 0.442 | 0.383 | 2445 | 10454 |
| 2026-08-06 | 13:43:00 | 0.449 | 0.343 | 3028 | 14431 |
| 2026-08-06 | 14:01:00 | 0.555 | 0.388 | 3112 | 15069 |
| 2026-08-07 | 09:33:00 | 0.552 | 0.778 | 229 | 1088 |
| 2026-08-07 | 09:37:00 | 1.460 | 2.021 | 642 | 2028 |
| 2026-08-07 | 09:40:00 | 0.333 | 0.994 | 774 | 3163 |
| 2026-08-07 | 09:43:00 | 0.444 | 1.232 | 909 | 4100 |
| 2026-08-07 | 09:50:00 | 1.440 | 2.303 | 1075 | 6194 |
| 2026-08-07 | 10:38:00 | 0.656 | 0.793 | 1727 | 10355 |
| 2026-08-07 | 11:25:00 | 0.327 | 0.651 | 2151 | 11972 |
| 2026-08-07 | 14:44:00 | 0.325 | 0.460 | 3169 | 17333 |
| 2026-08-10 | 09:40:00 | 0.514 | 0.669 | 744 | 5270 |
| 2026-08-10 | 10:03:00 | 0.829 | 0.379 | 1234 | 8131 |
| 2026-08-10 | 13:13:00 | 0.442 | 0.330 | 1922 | 11746 |
| 2026-08-10 | 14:12:00 | 0.493 | 0.419 | 2201 | 13899 |
| 2026-08-11 | 09:33:00 | 0.799 | 2.070 | 856 | 4282 |
| 2026-08-11 | 09:37:00 | 0.357 | 0.599 | 1233 | 5771 |
| 2026-08-12 | 11:22:00 | 1.121 | 0.342 | 1629 | 7787 |
| 2026-08-12 | 13:16:00 | 0.396 | 0.342 | 2196 | 10150 |
| 2026-08-13 | 09:31:00 | 2.654 | 0.385 | 123 | 600 |
| 2026-08-13 | 09:35:00 | 1.100 | 0.723 | 500 | 1462 |
| 2026-08-13 | 09:40:00 | 0.436 | 1.005 | 869 | 2693 |
| 2026-08-13 | 09:44:00 | 0.642 | 0.615 | 1168 | 3886 |
| 2026-08-13 | 09:54:00 | 0.430 | 0.568 | 1484 | 5438 |
| 2026-08-13 | 10:38:00 | 0.376 | 0.473 | 2247 | 8347 |
| 2026-08-13 | 14:18:00 | 0.539 | 0.381 | 2941 | 12380 |
| 2026-08-13 | 14:56:00 | 0.434 | 0.383 | 3534 | 14747 |
| 2026-08-14 | 09:34:00 | 0.659 | 0.479 | 227 | 668 |
| 2026-08-14 | 09:51:00 | 0.768 | 0.337 | 542 | 2112 |
| 2026-08-17 | 09:37:00 | 0.326 | 0.426 | 200 | 1616 |
| 2026-08-17 | 09:41:00 | 0.382 | 0.331 | 262 | 2036 |
| 2026-08-17 | 13:13:00 | 0.488 | 0.372 | 1025 | 7532 |
| 2026-08-18 | 09:35:00 | 0.375 | 0.466 | 146 | 1077 |
| 2026-08-18 | 09:42:00 | 0.429 | 0.325 | 264 | 1778 |
| 2026-08-18 | 10:08:00 | 0.540 | 0.419 | 565 | 3833 |
| 2026-08-18 | 11:03:00 | 0.326 | 0.416 | 878 | 5453 |
| 2026-08-18 | 14:37:00 | 0.321 | 0.636 | 1563 | 11508 |
| 2026-08-20 | 10:04:00 | 1.122 | 0.584 | 3618 | 12540 |
| 2026-08-20 | 10:08:00 | 1.064 | 0.729 | 3954 | 13094 |
| 2026-08-20 | 10:10:00 | 0.994 | 0.435 | 4321 | 13297 |
| 2026-08-21 | 09:42:00 | 0.746 | 0.733 | 1038 | 3566 |
| 2026-08-21 | 09:46:00 | 0.683 | 0.415 | 1175 | 4014 |
| 2026-08-21 | 10:27:00 | 0.637 | 0.313 | 2003 | 7763 |
| 2026-08-24 | 09:31:00 | 0.537 | 0.529 | 116 | 369 |
| 2026-08-24 | 09:33:00 | 0.783 | 0.424 | 216 | 757 |

<!-- END FILE 13/13: artifacts/alphaos-20260926-lanjian-01/case_lanjian_20260819.source.md -->
