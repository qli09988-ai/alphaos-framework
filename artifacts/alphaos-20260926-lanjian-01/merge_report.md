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
