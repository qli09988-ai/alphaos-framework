# AlphaOS Backlog & Change Log

Version: AlphaOS Framework v0.1 FROZEN  
Last updated: 2026-10-06

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

## A3. CHG-013 — Final Approval Set / Freeze — 2026-10-06

Status: **Human Approved / 已合入 / AlphaOS Framework v0.1 FROZEN**。

正式批准原文：“批准 AlphaOS Framework v0.1 Final Approval Set，冻结 v0.1”。批准来源：当前用户封版任务；原对话同句批准可追溯至 `e09fb77e-bba7-4f39-899f-8cccfcd30bd0`，对话 `6a72cde8-968c-83e9-8e76-dbd98abc4935`。本条统一登记本次批准集，不将旧助手建议当作授权。

| 范围 | 合入位置 / 处理 |
|---|---|
| Execution | Core §14：OPEN 五项检查、ADD 新证据、RE-UNDERWRITE、成本纪律、Shock Review |
| Risk & Position | Core §14：确定性 Risk Engine、累计 Thesis 预算、四层风险、Conviction 边界、两类 sizing |
| Personal Policy | 独立 `alphaos_personal_policy.md`：动态权益、1R、Disaster Limit、Theme Hard Ceiling、Recovery；45% 仅 Runtime 校准 |
| Thesis Card / Monitor | Core §15：固定字段、五类更新触发；保留 Industrial 与 Event 字段 |
| Data Discipline | Core §20：字段与派生信号、Missing、来源/时间/新鲜度/provenance；不扩部署 |
| Review Loop | Core §17：Snapshot 至 Version Update、过程/结果分评、七类错误 |
| 既有 Approved | CHG-001–012 保留；Router、C0–C7、Event/Expectation、Why Now、源抽象、相对强弱控制组不重写 |
| 雷科 Acceptance Case | Case Lab #004；历史价格带与用户减仓分类仅属 Case |
| 工程治理 | README / Usage / Status、FREEZE、HANDOFF；AI 不自批或静默改 Core |

版本说明：此前 `v0.1.1-working` 是文档增量标识；本次正式发布名为 **AlphaOS Framework v0.1**，继承全部既有 Approved 内容，未用旧快照回退主档。

规则合并：可用本地主档未发现 AC-RISK / AC-EXEC 编号实体；将本次已批准内容及既有相关表述规范到 Core §14，避免另加两套近义编号。历史聊天编号不作为第二规范来源；旧 handoffs / artifacts / archives 原样保留。

## B. 原 v0.1 TODO 结项与 Runtime 移交

| 原 ID | Framework 规范状态 | 未完成实现 / 验收去向 |
|---|---|---|
| TODO-001 Risk & Position | 2026-10-06 Approved / FROZEN | 确定性 Risk Code、输入验证及预算聚合验收 → Runtime MVP |
| TODO-002 Thesis Card + Event Monitor | 固定字段/触发已冻结，既有事件规则保留 | 卡片持久化与运行验收 → Runtime；原 T-3~7 / T / T+1 实验安排不作为新增强制规则 |
| TODO-003 Data Requirement Mapping | 数据纪律与来源职责已冻结 | 逐字段覆盖、频率、备援、freshness 与 schema 验证 → Runtime MVP |
| TODO-004 Review / Evaluation Loop | 流程与错误分类已冻结 | Decision Snapshot / Outcome / Diagnosis 落盘和回放验收 → Runtime |

旧 TODO 原文见封版前备份，历史证据不删除。实现未完成不等于框架仍待审批；冻结不等于实盘能力已验收。

Freeze 后所有新问题先分类为 **Runtime Bug / Case Finding / CHG for v0.1.1 or v0.2**。Core 变更必须走：

`Case Finding → Gap → Proposed Change → Review → Human Approval → Core Update`

其中验证按 Core §17 执行；AI 可提议，不可自批或静默修改 Core。Personal Policy 的参数变更独立记录并由用户批准，不自动改变通用规则。

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


## F. Freeze 排除项登记 — 2026-10-06

Market Leadership = Experimental/Testing；Catalyst Quality Q0–Q3、Pre-Event Leader / Event Review = Proposed/Testing。低空经济完整案例留 Case Backlog；完整 Asset Realization Engine 留 Proposed；Product Trust / Debate Mode / Confidence / User Override 等产品能力留产品 Backlog。159039 vs 159559 留 Runtime/Case Validation。雷科 Dry Run 为 Acceptance Case，价格带与 Swing High 不进入 Core。

这些项目未因 CHG-013 变为 Approved。卡片既有证据置信度元数据不等于批准产品层 Confidence 模块。
