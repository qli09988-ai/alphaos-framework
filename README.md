# AlphaOS Framework v0.1 — FROZEN

Version: AlphaOS Framework v0.1 FROZEN  
Human Approval / Freeze date: 2026-10-06  
Purpose: keep AlphaOS portable across ChatGPT, Claude, DeepSeek, local agents, OpenClaw, etc.

## Files

- `alphaos_core_spec.md` — formal framework / source of truth
- `alphaos_status_board.md` — current progress and version boundary
- `alphaos_case_lab.md` — real-world cases used to pressure-test the framework
- `alphaos_backlog_changelog.md` — gaps, proposed changes, and approved version changes
- `alphaos_usage_protocol.md` — how any model/agent should use these files without causing memory drift
- `alphaos_personal_policy.md` — 独立的个人风险参数，不是普适市场规则
- `FREEZE_v0.1.md` — 批准范围、排除项与封版说明
- `HANDOFF_RUNTIME_v0.1.md` — Work / OpenClaw 启动与读写权限
- [Post-Freeze Audit](artifacts/alphaos-freeze-20261006/POST_FREEZE_AUDIT.md) — 变更、核验与 GitHub 发布状态

- `templates/AlphaOS_增量交接单.md` — 既有模板，保持原样
- `handoffs/2026-09-26-蓝箭事件驱动-01.md` — 本轮增量交接与合入结果

## Current revision

`alphaos_core_spec.md` 是 **Core Sole Source of Truth**；旧 `AlphaOS_Specification_v0.1.md` 不是当前权威，不能覆盖 Core。

2026-10-06 用户正式批准 Final Approval Set 并冻结 Framework v0.1。既有 CHG-001–012 保留；Execution、Risk、Thesis Card / Monitor、Data Discipline、Review Loop 按 CHG-013 合入；个人参数独立。Market Leadership / Catalyst Quality 等实验项不进入正式 Core 行为。

此前 `v0.1.1-working` 是文档增量标识，本次正式发布名为 Framework v0.1，保留全部已批准内容。下一阶段：**OpenClaw Runtime MVP → Data Adapters / Schema / Validator / Risk Code → Shadow Mode**。

[增量交接单](handoffs/2026-09-26-蓝箭事件驱动-01.md) · [合入与冲突报告](artifacts/alphaos-20260926-lanjian-01/merge_report.md)

`archives/` 为历史备份，`artifacts/` 为证据与差异，`deployment/` 为旧案例展示；都不是另一套 Source of Truth。`sources/` 及同步参考文件保持只读。根目录主档是原 ZIP 解包的可编辑工作文件；本轮在原文件更新，没有另建框架。

## Governance rule

**Core Spec is the source of truth.**

A case result does NOT automatically become a framework rule.

Any new rule must follow:

`Case Finding → Gap → Proposed Change → Review → Human Approval → Core Update`

This prevents memory drift and “chat-based rule mutation”.

## GitHub / OpenClaw 同步

GitHub 是 AlphaOS 文档与云端 OpenClaw 的**同步桥梁 / 版本库**。

- 仓库：[qli09988-ai/alphaos-framework](https://github.com/qli09988-ai/alphaos-framework)
- 冻结分支：`freeze/alphaos-v0.1`；入口：[冻结文档](https://github.com/qli09988-ai/alphaos-framework/tree/freeze/alphaos-v0.1)
- Work / OpenClaw 启动时从 GitHub 读取当前冻结版本，记录实际 commit；依照 [Runtime Handoff](HANDOFF_RUNTIME_v0.1.md) 读取 Core、[Personal Policy](alphaos_personal_policy.md)、Usage、Status 和案例记录。
- 默认只读 Core；AI may propose changes but may not self-approve or silently mutate Core。
- Core 修改须走上述治理流程；Missing 不补造，仓位由确定性 Risk Engine 计算。
- 先检查分支及未提交改动，再同步；禁止静默覆盖分叉或强推。不能以 push 成功推定云服务器已部署。
- 没有既定 tag 策略，本次不创建 tag；不创建 PR。冻结分支的实际发布结果及提交 SHA 以封版审计和远端记录为准。

## Migration

迁移平台/模型时提供同一 GitHub commit 的整组文档，并使用 [Usage Protocol](alphaos_usage_protocol.md) 的读取顺序。Case / Backlog 是证据和候选项，不是平行规则源。历史工作路线建议稿和旧交接按各自日期解释，不覆盖当前冻结状态。
