# AlphaOS Framework v0.1 — Freeze Record

Framework Version: **v0.1**  
Status: **FROZEN**  
Human Approval / Freeze date: **2026-10-06（Asia/Shanghai）**  
Core Sole Source of Truth: [alphaos_core_spec.md](alphaos_core_spec.md)

## Human Approval

用户明确批准：“批准 AlphaOS Framework v0.1 Final Approval Set，冻结 v0.1”。当前封版任务明确指定最终批准内容；批准审计见 Change Log CHG-013。无需再次确认规则。

基准为 2026-09-26 的 `v0.1.1-working` 文档增量；正式发布命名为 Framework v0.1，不删除既有 Approved 内容，不用旧 `AlphaOS_Specification_v0.1.md` 覆盖 Core。

## 冻结范围

| 范围 | 已冻结内容 / 权威位置 |
|---|---|
| Execution | OPEN 五项；ADD 新证据、HOLD ≠ ADD；RE-UNDERWRITE；回本价/动态成本纪律；Shock Review → Core §14 |
| Risk & Position | 确定性 Risk Engine；累计 Thesis Risk Budget；Single Instrument / Thesis / Theme-Cluster / Portfolio；Conviction 边界；Risk-Distance / Stress-Based Sizing → Core §14 |
| Personal Risk Policy | 动态权益与本次快照、1R、Disaster Limit、Theme Stress / Hard Ceiling、Recovery / Hard Guard → 独立 Personal Policy，不是通用市场规则 |
| Thesis Card / Monitor | 十一固定字段、五类触发；Industrial 的 Lifecycle / CV / Economics；既有 Event 字段 → Core §15 |
| Data Discipline | 字段定义与派生信号资产、Missing、source / timestamp / freshness / provenance、三类数据源职责 → Core §20 |
| Review / Evaluation | Decision Snapshot 至 Version Update；过程和结果分别评价；七类错误 → Core §17 |
| 既有批准 | Router、C0–C7、Event Progress vs Expectation Progress、Why Now、源可替换、相对市场/行业/事件篮子控制组保持现状 |

规范文本只在 Core 维护；本文件为发布索引，不构成重复投资规则集。

## 明确排除

- Market Leadership：Experimental/Testing。
- Catalyst Quality Q0–Q3、Pre-Event Leader / Event Review：Proposed/Testing。
- 低空经济完整案例；完整 Asset Realization Engine。
- Product Trust / Debate Mode / Confidence / User Override 等产品层能力。
- 159039 vs 159559：Runtime/Case Validation。
- 雷科 Dry Run：仅 Acceptance Case；历史价格带 / Swing High 等具体数值只在 Case 和证据中。
- 单一证券 45% 临时 Guard：仅 Runtime 校准，不冻结为长期正式规则。
- OpenClaw 的具体数据部署、生产验收及代码实现：Runtime MVP。

## Freeze 后治理与下一阶段

`OpenClaw Runtime MVP → Data Adapters / Schema / Validator / Risk Code → Shadow Mode`

新问题进入 Runtime Bug / Case Finding / CHG for v0.1.1 or v0.2。Core 修改走 `Case Finding → Gap → Proposed Change → Review → Human Approval → Core Update`，并依 Core §17 验证。AI may propose changes but may not self-approve or silently mutate Core。

历史 handoffs / artifacts / archives 保留；工作路线建议稿仍是历史建议。冻结仅确认文档规范，不宣称 Risk Code、数据生产服务或云端同步已完成。

## 版本库

[仓库](https://github.com/qli09988-ai/alphaos-framework) · [冻结分支](https://github.com/qli09988-ai/alphaos-framework/tree/freeze/alphaos-v0.1)。计划提交消息：`freeze: AlphaOS Framework v0.1`。未创建 tag（无既定策略），不创建 PR。实际提交 SHA 与远端核验见 [Post-Freeze Audit](artifacts/alphaos-freeze-20261006/POST_FREEZE_AUDIT.md)；不要用本说明替代远端成功证据。
