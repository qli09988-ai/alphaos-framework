# AlphaOS Usage Protocol

Version: AlphaOS Framework v0.1 FROZEN  
Last updated: 2026-10-06

Use this file when giving AlphaOS to another model/platform.

---

## 1. Reading order

Work / OpenClaw 启动时先同步并锁定 GitHub 当前冻结提交，再按同一 commit 读取：

1. `HANDOFF_RUNTIME_v0.1.md` 与 `FREEZE_v0.1.md`
2. `alphaos_core_spec.md`（Core Sole Source of Truth）
3. `alphaos_personal_policy.md`
4. 本文件与 `alphaos_status_board.md`
5. `alphaos_case_lab.md` 与 `alphaos_backlog_changelog.md`
6. `README.md`；再读相关 `handoffs/`、`templates/AlphaOS_增量交接单.md` 和证据 artifacts。

连接失败时记录实际使用的本地 commit 与新鲜度，不能宣称已取得 GitHub 最新版本。

---

## 2. Source-of-truth rule

`alphaos_core_spec.md` is authoritative.

以同一版本的一组文件为准，当前 AlphaOS Framework v0.1 FROZEN / 2026-10-06。`archives/` 是历史快照，`deployment/` 是旧案例展示，`artifacts/` 是证据/差异，不是平行主档。旧名 `AlphaOS_Specification_v0.1.md` 本次未找到正文，不据聊天提及覆盖现有主档。

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

Missing is Missing：禁止补造；事实必须保留 source / timestamp / freshness / provenance。Risk / 仓位数字必须来自确定性 Risk Engine 及其可追溯输入，LLM 不得自编。

---

## 5. State updates

卡片固定字段与类型扩展字段引用 Core §15。只在 **新事实 / 状态迁移 / 交易动作 / Shock / Deadline Miss** 五类触发时更新；状态迁移保留前后值、证据和时间。

“No news” can itself become negative evidence if a time-sensitive thesis repeatedly fails to progress；须关联原先记录的确认窗口 / Deadline Miss，不虚构到期日。

---

## 6. Preventing memory drift

At the end of a meaningful research session:

1. update the relevant Case Lab entry;
2. add any new gap to Backlog;
3. update Status Board if project progress changed;
4. Core 默认只读；仅执行用户明确批准且范围可追溯的版本变更，不自批；
5. increment version when formal behavior changes.

---

## 7. Platform migration prompt

Use:

> You are continuing development of AlphaOS.  
> Read the pinned GitHub frozen commit using the reading order in this protocol, including Runtime Handoff and Personal Policy.  
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


## 10. Freeze 后 Runtime / Work / OpenClaw 权限

| 层 | 默认权限 | 可写边界 |
|---|---|---|
| Core / Freeze 文件 | 只读 | 仅执行明确 Human Approval 的版本更新；AI 不自批 |
| Personal Policy | 读取已批准参数 | 参数变动需用户批准并独立记录，不能反向改写通用 Core |
| Case / Decision Snapshot / Outcome | 按任务增量读写 | 保留事实、计算、推断、Missing 与证据；不升级为正式规则 |
| Runtime 适配、Schema、Validator、Risk Code、日志 | 在授权任务范围内实现、修复、记录 | 不因运行问题改变 Core；确定性数值输出，缺输入写 Missing |
| Backlog / Status / Handoff | 记录进度、Bug、Finding 与 Proposed Change | 不得自行标 Approved 或伪造部署/推送成功 |
| 历史 handoffs / artifacts / archives / sources | 读取 | 既有历史证据不覆盖、不删除；同步项目文件只读 |

**AI may propose changes but may not self-approve or silently mutate Core.**

Core 变更：`Case Finding → Gap → Proposed Change → Review → Human Approval → Core Update`；Validation 按 Core §17 执行，更新版本与批准记录。Freeze 后问题进入 Runtime Bug / Case Finding / CHG for v0.1.1 or v0.2。

GitHub 是文档与云端 OpenClaw 的同步桥梁 / 版本库。工作前检查 branch、commit 和未提交修改；有分叉先比较，不能覆盖用户工作，不 force push。Work 提交后核实远端 commit，再通知使用方；OpenClaw 不因 main 名称或最新时间而自动采用未批准内容。同步本身不意味着服务器已部署。
