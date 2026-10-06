# AlphaOS Runtime Handoff — v0.1

这是工程治理交接文件，不是新增投资规则。

- Framework Version：**AlphaOS Framework v0.1 / FROZEN**
- Human Approval / Freeze date：**2026-10-06（Asia/Shanghai）**
- Core Sole Source of Truth：`alphaos_core_spec.md`
- GitHub：`https://github.com/qli09988-ai/alphaos-framework`
- Frozen branch：`freeze/alphaos-v0.1`
- Tag：未创建；无既定 tag 策略
- Commit：启动时读取并记录远端冻结分支实际 SHA；发布结果见本次 Post-Freeze Audit。不将本文件所在提交 SHA 写入自身以制造循环引用。

## 必读文件

按同一冻结 commit 读取：

1. `FREEZE_v0.1.md` 与 `alphaos_core_spec.md`
2. `alphaos_personal_policy.md` 与 `alphaos_usage_protocol.md`
3. `alphaos_status_board.md`、`alphaos_case_lab.md`、`alphaos_backlog_changelog.md`、`README.md`
4. 当前任务相关 `handoffs/`、`templates/AlphaOS_增量交接单.md` 和 artifacts；涉及 thsdk 时读取 `artifacts/ths-validation/核验报告.md`、`LOCAL_RUNTIME.md`，按历史审计日期解释，不推定当前服务能力。

## 读写权限

| 层 | Runtime / Work / OpenClaw 权限 |
|---|---|
| Core / Freeze | 默认只读；只能执行范围明确、已获 Human Approval 的版本变更 |
| Personal Policy | 读取已批准个人参数；修改须独立记录并由用户批准 |
| Case / Snapshot / Outcome | 任务范围内增量写入；保留 evidence / provenance 与前后状态，不晋升 Core |
| Runtime / Schema / Validator / Risk Code / Logs | 按授权任务实现和修复；不得借 Runtime 修改 Core 或自创风险规则 |
| Backlog / Status / Handoff | 记录 Runtime Bug、Case Finding、Proposed Change 和实际进度，不自行标 Approved |
| 历史 handoffs / artifacts / archives / 同步 sources | 历史材料只读；新增证据用新文件，旧记录不覆盖、不删除 |

**AI may propose changes but may not self-approve or silently mutate Core.**

Core 变更路径：`Case Finding → Gap → Proposed Change → Review → Human Approval → Core Update`；验证与版本更新依 Core §17。新问题分类为 Runtime Bug / Case Finding / CHG for v0.1.1 or v0.2。

## OpenClaw 下一步顺序

1. **Data Adapters**：按既有 thsdk 盘面 / BaoStock 历史 / 官方公告财报监管公司材料职责接入；不扩大未验收能力。
2. **Schema**：落实卡片固定字段、类型扩展字段、个人参数与证据时间/来源结构。
3. **Validator**：验证缺失、新鲜度、provenance、单位和字段口径；Missing is Missing，不补造。
4. **Risk Code**：依据已批准 Core 和 Personal Policy 实现确定性计算、累计预算和四层风险。LLM 不直接编仓位；未给定或未经批准的计算口径登记缺口，不自行设计成正式规则。
5. **Shadow Mode**：保存 Decision Snapshot、运行输出、Outcome 和 Error Diagnosis，验证实现遵守冻结规范；本交接不授权自动下单或本次立即启动部署。

## GitHub 同步原则

- 先检查本地分支、commit 和未提交改动，保留其他工作；有分叉先比较，不强推、不静默覆盖。
- 从冻结分支获取版本并固定到实际 commit；Core、Policy、Usage 必须来自同一提交，不混用旧聊天/附件。
- 提交修改到独立分支；推送后核对 remote SHA。仅上传成功不表示服务器已拉取或服务已部署。
- main 若仅含初始化 README，不是冻结文档入口；使用上述冻结分支及核验后的提交。
- 连接/权限失败如实记录；没有实际远端证据不能宣称已同步。默认只读 Core 的权限不因连接方式变化而放宽。
