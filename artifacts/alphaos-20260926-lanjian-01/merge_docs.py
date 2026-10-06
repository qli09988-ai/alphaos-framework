from pathlib import Path
root=Path(__file__).resolve().parents[2]
version='v0.1.1-working'
date='2026-09-26'
def read(f): return (root/f).read_text()
def save(f,s): (root/f).write_text(s)
def replace(s,a,b):
 assert s.count(a)==1, (a[:100],s.count(a))
 return s.replace(a,b,1)
core=read('alphaos_core_spec.md')
core=replace(core,'# AlphaOS Core Spec — v0.1 Working','# AlphaOS Core Spec — v0.1.1 Working\n\nVersion: v0.1.1-working  \nLast updated: 2026-09-26  \nBaseline: v0.1-working（2026-09-20 本地快照）  \nApproved changes: CHG-007–CHG-012；交接编号 `2026-09-26-蓝箭事件驱动-01`。')
core=replace(core,'## 3. Main research chain\n','''## 3. Main research chain

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
''')
core=replace(core,'- reaction to catalysts\n','''- reaction to catalysts

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
''')
core=replace(core,'## 14. Execution Engine','''### Relative Strength Controls — Approved / CHG-012

Market Monitor 同时观察个股相对 **市场 / 行业 / 事件篮子** 的表现，作为调查与预期判断的输入。

- 固定观察窗口、交易日、复权口径和收益定义，记录基准代码、名称、成分、权重与选取时间。
- `Return_nD = P_t / P_(t-n) - 1`；`Excess_Return_nD = Return_stock_nD - Return_control_nD`，超额以百分点展示，不称为因果 alpha。
- 等权篮子先按预先固定的成分求每日收益均值，再复合成多日收益。标的自身从其控制篮子剔除；缺失/停牌处理预先声明，禁止把缺失收益填零或事后换弱样本。
- 事件直接关联组必须有当时已公开的权益/供应/合作证据；泛主题板块仅是行业/主题 Beta，不等同事件关联组。
- 控制组不足时写 Unavailable，并限制结论；绝对上涨不能证明独立事件领先或内幕信息。

Market Leadership 的状态分类与识别阈值尚未 Approved，定义仅保留在 Case Lab / Backlog 的实验区，不作为 Core 决策条件。

---

## 14. Execution Engine''')
core=replace(core,'- stock / code / mode\n','''- stock / code / mode
- Thesis Type：Industrial / Event-Driven / Asset Realization / Hybrid；primary / secondary（如适用）
- Why Now?：为什么是现在，而不是三个月前或三个月后；对应证据时间、临近确认事件、尚未消失的预期差与失效条件（Approved / CHG-010）
''')
core=replace(core,'- latest CV / expectation / regime states\n','''- latest CV / expectation / regime states（不适用项写 N/A，不得硬套）
- Event State / substage（如适用）、事件主体、关联路径、证据时间与 next transition
- Event Progress vs Expectation Progress：各自变化、依据和置信度
- Relative Strength：vs Market / Industry / Event Basket；窗口、基准与缺失项
''')
core=replace(core,'The card stores **state + transition conditions**, not “good/bad company” labels.','''The card stores **state + transition conditions**, not “good/bad company” labels.

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

本轮扩展整合在 Thesis Card + Event Monitor / Expectation / Data Layer 内，不新建 Event-Driven Engine。''')
core+='''

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
'''
save('alphaos_core_spec.md',core)

status=read('alphaos_status_board.md')
status=replace(status,'# AlphaOS Status Board — v0.1','# AlphaOS Status Board — v0.1.1-working')
status=replace(status,'Last updated: 2026-09-20','Last updated: 2026-09-26\n\nFramework: `alphaos_core_spec.md` v0.1.1-working；本轮交接 `2026-09-26-蓝箭事件驱动-01`。Working 增量版本，不代表 v0.1 已封板。')
status=replace(status,'| Expectation Engine | ✅ v0.1 usable | E1-E4 |','| Expectation Engine | ✅ Approved 增量已合入 | E1-E4 + Event Progress vs Expectation Progress；非自动交易规则 |')
status=replace(status,'| Thesis Card / Event Monitor | 🟡 partial | state-machine concept established |','| Thesis Card / Event Monitor | 🟡 partial | Router、Why Now?、C0–C7 已 Approved；持续更新与运行验收未完成 |')
status=replace(status,'| Data Requirement Mapping | 🔴 unfinished | source/frequency/backup mapping needed |','| Data Requirement Mapping | 🟡 partial | thsdk 实时 / BaoStock 历史 / 公告新闻事件时间戳已定义；逐字段、频率、备援与生产验收待补 |\n| Relative Strength Controls | ✅ 方法 Approved | 市场/行业/事件篮子口径已加入；蓝箭实证控制组未齐 |\n| Market Leadership Monitor | 🧪 Experimental / Testing | None / Pre-Event / Confirmation / Exhaustion；未升 Core |\n| Catalyst Quality | 🟡 Proposed / Testing | Q0–Q3；未升 Core |')
status=replace(status,'### Case #002 — Low-altitude Economy\nStatus: **not yet fully run through the complete framework**\n\nNext after embodied-intelligence closure.','''### Case #002 — Low-altitude Economy
Status: **not yet fully run through the complete framework**

Next after embodied-intelligence closure.

### Case #003 — 蓝箭 / 鲁信 / 金风 2026-08-19
Status: **回放已归档；控制组与事件时间轴待补；Leadership Testing**。

- 8/17–18 金风在两股比较中持续更强；8/19 鲁信涨停收盘，金风涨停开盘回落至接近平盘；T+1 两者快速转弱。
- “金风更像 Pre-Event Leader”为推断，不能在缺少市场/风电/事件篮子控制结果时判为独立事件领先。
- v1 历史材料存在 non-wrapper provenance；具体开板/回封时间未确认。
- 详见 Case Lab；下一次补齐控制组、官方事件内容/首次公开时间和原始审计日志后更新。无已核实未来事件日期，不安排自动任务。''')
status+='''

---

## H. 本轮合入与数据审计边界 — 2026-09-26

CHG-007–CHG-012 已 Approved 并合入：Router、C0–C7、Event–Expectation 联动、Why Now?、Data Source Abstraction、Relative Strength Controls。授权为用户本次明确合入请求；不是旧聊天助手建议代替批准。

数据职责：thsdk 当前游客 wrapper 仅用于当日/最近交易日盘面；BaoStock 承担历史日线与控制组输入；公告/新闻承担事件时间戳；AKShare 因该服务器东方财富网络故障暂不作底座；历史外盘/内盘/主动买卖字段降权。本次为审计材料归档，未重跑服务器测试。

四项 v0.1 闭环仍未全部完成，Risk & Position、Review Loop 及执行买入逻辑仍待封板；本轮不改变既有研究顺序，不增加庞大 Event-Driven Engine。
'''
save('alphaos_status_board.md',status)

usage=read('alphaos_usage_protocol.md')
usage=replace(usage,'# AlphaOS Usage Protocol','# AlphaOS Usage Protocol\n\nVersion: v0.1.1-working  \nLast updated: 2026-09-26')
usage=replace(usage,'4. `alphaos_backlog_changelog.md`','4. `alphaos_backlog_changelog.md`\n5. 本文件；再读 `handoffs/` 中相关增量交接单；模板见 `templates/AlphaOS_增量交接单.md`。')
usage=replace(usage,'`alphaos_core_spec.md` is authoritative.','''`alphaos_core_spec.md` is authoritative.

以同一版本的一组文件为准，当前 v0.1.1-working / 2026-09-26。`archives/` 是历史快照，`deployment/` 是旧案例展示，`artifacts/` 是证据/差异，不是平行主档。旧名 `AlphaOS_Specification_v0.1.md` 本次未找到正文，不据聊天提及覆盖现有主档。''')
usage=replace(usage,'Default order:\n\n1. Industry / Direction','''先读取 Thesis Type Router，判断 Industrial / Event-Driven / Asset Realization / Hybrid，并填写 Why Now?。Event-Driven / Asset Realization 先核对事件事实、权益传导与兑现条件，再走 Expectation / Market Regime / Execution / Risk；CV 不适用时写 N/A。Hybrid 分开研究主业与可选项，避免重复计价。

Industrial 及 Hybrid 的产业部分沿用以下顺序：

1. Industry / Direction''')
usage=replace(usage,'- CV\n- Thesis strength','- CV（适用时）\n- Event State / substage / event_status（适用时）\n- Thesis strength')
usage+='''

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
'''
save('alphaos_usage_protocol.md',usage)
print('Updated Core Spec, Status Board, Usage Protocol.')
