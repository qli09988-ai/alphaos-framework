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
