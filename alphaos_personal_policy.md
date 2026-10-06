# AlphaOS Personal Risk Policy

Framework reference: AlphaOS Framework v0.1 FROZEN  
Policy approval date: 2026-10-06  
Status: **Human Approved / Personal Policy**

本文件只承载用户个人风险参数，与 `alphaos_core_spec.md` 的通用规则分层。这些参数不是普适市场真理，也不是推荐仓位。后续调整须记录用户批准与参数版本；AI 不得自行批准变更。

| 参数 | 本次批准内容 | 使用边界 |
|---|---|---|
| Current Account Equity | 动态账户权益；本次基线快照约 **¥231,732** | 来源：用户 Final Approval Set；本次未读取账户或刷新截图，不得把快照写死为实时权益 |
| 1R | **Account Equity × 1%** | 由确定性 Risk Engine 使用当时有效权益计算；本文件不直接输出仓位 |
| Disaster Limit | **-30%** | 灾难边界，不是正常运行预算 |
| Theme Stress / Hard Ceiling | 单主题 **-20%** 压力情景最多允许约 **-10%** 账户损失 → **Theme Hard Ceiling ≈ 50%** | 个人 Hard Ceiling，不是目标/推荐仓位；仍受 Core 四层风险约束 |
| Recovery / Hard Guard | 从账户高水位 **Drawdown ≤ -20%** 时进入 | 原则上禁止净扩大总组合风险；允许经重新验证的换仓 / 风险重构 |
| 单一证券 45% 临时 Guard | **Runtime 校准项，未冻结为长期正式规则** | 不能被模型自动当作正式固定上限，也不能视为建议持有比例 |

Theme Ceiling 的批准推导为 `10% / 20% ≈ 50%`，只表达该个人压力情景下的上界，不构成收益或最大损失保证。账户高水位与动态权益的来源、时间、新鲜度以及 Runtime 具体口径须记录；缺失时保持 Missing，不由 LLM 补造。

执行与多层预算规范引用 [Core §14](alphaos_core_spec.md#14-execution-engine)，运行权限引用 [Usage Protocol](alphaos_usage_protocol.md) 和 [Runtime Handoff](HANDOFF_RUNTIME_v0.1.md)。
