# AlphaOS ETF evidence pack, 2026-09-30
Final completed trading session: 2026-09-29. The 20-session window is Sep 1–29; baseline Aug 31. Intraday snapshots are separate.

- share_delta = end-of-day shares - prior-session shares (SZSE). No changes in split factors were observed in the retrieved unit/cumulative NAV histories.
- estimated_net_subscription = share_delta * same-day NAV. This is value of net creation/redemption, not exact cash transfer and not gross creation/redemption.
- aum = shares * rounded published NAV; an estimate, not unrounded audited AUM.
- premium_pct = 100 * (close / NAV - 1), NOT intraday IOPV premium.
- turnover_pct = 100 * traded shares / same-day end shares; ignores vendor turnover due to historical denominator issues.
- main_flow = Eastmoney large + superlarge classified trading flow, NOT subscription and NOT verified THS metric.
- simple price/NAV returns; retrieved unit and cumulative NAV agree in all analyzed windows.
- volatility = sample standard deviation of daily close returns * sqrt(252).
- maximum drawdown includes the baseline close and each end-of-day close.
- tracking error = sample SD of NAV daily return minus CNI PRICE index daily return * sqrt(252). Not total-return-index alpha or official one-year tracking error.
- Actual holdings: IGW June 30 report. PCF is a creation/redemption basket and must not be labeled actual holdings. CNI endpoint provides all 50 names but only 10 weights. Requested historical weight date was ignored, so no historical weighted attribution was used.
- Historical ETF OHLC crosscheck: 72 overlapping Huaan and 160 IGW rows match Tencent exactly. CNI official index closes agree with Eastmoney to published rounding.
- No current user portfolio ledger or exact THS screen/metric provided. These remain MISSING.
