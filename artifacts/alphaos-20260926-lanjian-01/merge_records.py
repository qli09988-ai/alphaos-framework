from pathlib import Path
root=Path(__file__).resolve().parents[2]
def read(f): return (root/f).read_text()
def save(f,s): (root/f).write_text(s)
def replace(s,a,b):
 assert s.count(a)==1,(a[:80],s.count(a))
 return s.replace(a,b,1)
case=read('alphaos_case_lab.md')
case=replace(case,'# AlphaOS Case Lab','# AlphaOS Case Lab\n\nVersion: v0.1.1-working  \nLast updated: 2026-09-26')
case=replace(case,'Status:\n- not yet promoted to Core Spec','''Status:
- 原观察保留；2026-09-26 用户明确批准 Thesis Type Router（CHG-007），允许 Asset Realization 类型而不强套 CV。
- 完整 Asset Realization Engine、NAV/概率/退出模型仍未升 Core；本案例扩展见下方 Case #003。''')
case+='''

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
'''
save('alphaos_case_lab.md',case)

back=read('alphaos_backlog_changelog.md')
back=replace(back,'# AlphaOS Backlog & Change Log','# AlphaOS Backlog & Change Log\n\nVersion: v0.1.1-working  \nLast updated: 2026-09-26')
back=replace(back,'## B. v0.1 MUST finish','''## A2. 本轮明确批准并合入 — 2026-09-26

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

## B. v0.1 MUST finish''')
back=replace(back,'### TODO-002 — Thesis Card + Event Monitor\nNeed:','''### TODO-002 — Thesis Card + Event Monitor
2026-09-26：Router、Why Now?、C0–C7 已 Approved；字段规范完成部分合入。下面持续运行与验收仍未完成，TODO 不关闭。
Need:''')
back=replace(back,'### TODO-003 — Data Requirement Mapping\nFor each decision point:','''### TODO-003 — Data Requirement Mapping
2026-09-26：实时/历史/事件源分工与部署审计边界已合入 Core §20；需补每字段覆盖、备援与运行验收，不关闭 TODO。
For each decision point:''')
back=replace(back,'### BL-003 — Asset Realization Engine\nSource:','''### BL-003 — Asset Realization Engine
Status: **Proposed**。CHG-007 仅批准 Thesis Type，未批准本完整引擎。优先在现有 Thesis Card / Event Monitor 中承载权益、兑现条件与事件证据；本轮不新建庞大 Event-Driven Engine。
Source:''')
back=replace(back,'### BL-004 — live market data layer\nPotential:','''### BL-004 — live market data layer
Status: **Testing / 未完成生产验收**。原“Potential”列为历史候选清单，不代表已接入或已授权账户。当前 thsdk 游客只读入口已最小验收，但盘中实时性未验证；完整数据分工和审计边界以 Core §20 为准。
Potential:''')
back=replace(back,'## D. Change-control template','''## C2. 本轮实验与缺口（未升 Core）

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

## D. Change-control template''')
back=replace(back,'- Status: Proposed / Testing / Approved / Rejected','- Status: Proposed / Testing / Approved Candidate / Approved / Rejected\n- Approval evidence / scope: Approved Candidate 仍待明确批准，不得当作已生效规则')
back+='''

## E. 版本和冲突记录 — 2026-09-26

- 根目录 README 与五份主文档均与 `archives/AlphaOS_v0.1_portable_docs.zip` 逐字节一致；本轮基准无本地内容分叉。
- 本地与原对话附件同名 `AlphaOS_增量交接单.md` 完全一致；保留模板，新增一张已填写交接单，不覆盖模板。
- 旧聊天提及 `AlphaOS_Specification_v0.1.md`，本地和已取得附件均未找到正文，因此无法比较其内容；记录为外部旧版本未取得，不将其当最新主档。
- 本地主档已合入 v0.1.1-working；保留合入前 ZIP、哈希与 diff。历史部署页面/上传包未改，不能作为当前框架版本。
'''
save('alphaos_backlog_changelog.md',back)

readme=read('README.md')
readme=replace(readme,'Version: v0.1-working','Version: v0.1.1-working  \nLast updated: 2026-09-26')
readme=replace(readme,'## Governance rule','''- `templates/AlphaOS_增量交接单.md` — 既有模板，保持原样
- `handoffs/2026-09-26-蓝箭事件驱动-01.md` — 本轮增量交接与合入结果

## Current revision

唯一当前主档仍为本目录 `alphaos_core_spec.md`；本轮 Approved：Router、C0–C7、Event–Expectation、Why Now?、数据源抽象、相对强弱控制组。Market Leadership 与 Catalyst Quality 仍为 Proposed/Testing，定义放在 Case Lab / Backlog，不是 Core 正式规则。

v0.1.1-working 是 v0.1 的文档增量修订，不代表风险/仓位、持续监控和评估闭环已完成。

[增量交接单](handoffs/2026-09-26-蓝箭事件驱动-01.md) · [合入与冲突报告](artifacts/alphaos-20260926-lanjian-01/merge_report.md)

`archives/` 为历史备份，`artifacts/` 为证据与差异，`deployment/` 为旧案例展示；都不是另一套 Source of Truth。`sources/` 及同步参考文件保持只读。根目录主档是原 ZIP 解包的可编辑工作文件；本轮在原文件更新，没有另建框架。

## Governance rule''')
save('README.md',readme)
print('Updated Case Lab, Backlog/Change Log, README.')
