---
podcast: The Weekly Show with Jon Stewart
date: 2026-10-28
source_transcript: data/podcasts/transcripts/The_Weekly_Show_with_Jon_Stewart/2026-10-28_Bursting_the_AI_Bubble_with_Ed_Zitron.md
---

# The Weekly Show with Jon Stewart — "Bursting the AI Bubble with Ed Zitron"

**Host:** Jon Stewart. **Guest:** Ed Zitron (CEO, Easy Primary Research; writer, "Where's Your Ed At?" newsletter; AI economics analyst).

## TL;DR

- **NVIDIA controls the AI ecosystem via GPU monopoly** — they supply the $50,000–$60,000 chips required to train and run AI models, sold in million-dollar-plus racks to Microsoft, Google, Meta, Amazon, Oracle, and SpaceX; NVIDIA is printing money while customers are taking on debt.
- **AI companies aren't generating enough revenue to justify infrastructure spending** — Microsoft, Google, Amazon, and Meta have spent $265+ billion on AI GPUs and data centers since 2022 yet are running cash-flow negative, taking on debt, and laying off employees.
- **80% of Anthropic and OpenAI's revenue comes from 1% of customers—unprofitable AI startups** — companies like Harvey (legal AI) and Perplexity (search) use the API but run at a loss; their growth signals are entirely artificial, propped up by venture capital rather than real economic value.
- **Anthropic has $430 billion in non-cancellable 7–10 year lease commitments** — they've pledged to rent compute at prices and volumes they may not be able to afford if revenue growth stalls; their S1 filing shows latest quarterly data is blank, but investor day numbers suggest they lose billions annually.
- **The entire industry is built on cascading debt and circular money flows** — CoreWeave (a NeoCloud) has $30–$40 billion in debt, buys GPUs using debt, and relies on Microsoft, Google, Anthropic, and Meta as customers; NVIDIA invests in all these companies; everyone is leasing compute from each other while the actual revenue doesn't exist.
- **Valuation and "exit liquidity" represent a wealth transfer, not investment** — Anthropic is going public at $1.5–$2 trillion valuation (up from $20 billion two years ago), far higher than Google ($23 billion IPO), Microsoft ($700 million IPO), or Amazon ($300 million IPO); public investors are funding venture capitalists' exits, not backing a profitable company.
- **When one major player fails, debt stops issuing and GPUs stop selling** — most companies outside Microsoft cannot sustain GPU purchases from operating cash flow; a financial shock comparable to 2008's 7% mortgage crisis could trigger a cascade collapse.
- **The stock market's gains are heavily concentrated in the "Magnificent Seven"** — 45% of Nasdaq 100 value is in these seven tech stocks, all betting on unsustainable AI demand; if AI demand plateaus, the market faces a serious correction.

---

**NVIDIA's Monopoly and the GPU Choke Point**

Zitron explains that GPUs—graphics processing units designed by NVIDIA for parallel processing—are the foundation of the entire AI infrastructure. Each chip costs $50,000–$60,000 and is sold in racks costing millions of dollars; companies need hundreds of thousands to build functional data centers. NVIDIA's dominance stems from CUDA, proprietary software libraries that make their GPUs the de facto standard. While AMD and Broadcom technically offer alternatives, NVIDIA controls the supply chain. Their customer base is extremely concentrated: Microsoft, Google, Meta, Amazon, Oracle, and SpaceX. These companies have sunk $30–$50 billion per quarter into AI chips and data centers, yet NVIDIA's sales tell a troubling story—all that spending is being financed through debt rather than generated through operating profits.

**How AI Companies Make Money—And How Little They Actually Do**

Stewart asks the fundamental question: how do Anthropic, OpenAI, Meta, and others monetize AI? Zitron outlines two revenue streams: subscriptions (paying $20–$200 monthly for limited access) and API usage (pay-per-token for services integrated into third-party applications). A token is roughly three-quarters of a word; companies are charged on a per-million-token basis.

However, the real problem emerges when examining actual financials. Anthropic's recent S1 filing (for their upcoming IPO) shows blank data for the latest quarter, but investor disclosures reveal staggering losses. OpenAI's audited financials showed similar red flags. Critically, neither company discloses how much it costs to run their GPU infrastructure—a deliberate opacity that obscures the fact that compute costs may exceed revenue by multiples.

**The Customer Base Problem: 80% Revenue from 1% of Customers Who Are Themselves Unprofitable**

Zitron cites Ramp (a payment processor) data: 80% of Anthropic and OpenAI's revenues come from just 1% of their customers. Those customers are venture-backed AI startups—Harvey (legal AI), Perplexity (search), and others—that run their services at a massive loss. When you pay Perplexity $20 monthly, they may rack up $60–$80 in token costs. These startups survive only because venture capital keeps funding them; the moment that funding dries up, the revenue disappears with it. Zitron calls this cohort "ninja borrowers from the great financial crisis of the AI generation," echoing the predatory lending that preceded 2008. The growth everyone celebrates in Anthropic and OpenAI—framed as a diversified, explosive market—is actually a fragile house of cards where one venture capital drought could collapse entire revenue bases.

**The Hyperscaler Data Center Buildout: Capacity Without Revenue**

All major tech companies—Microsoft, Google, Amazon, Meta—are spending tens of billions quarterly on AI data centers. Microsoft has committed to $265 billion since 2022. Yet none of them is profitable on AI operations. The reason: they believe they need to build capacity *ahead* of demand, mimicking the strategy of platforms like Amazon Web Services (which eventually became profitable). The difference, Zitron argues, is structural. Amazon's AWS capital expenditures from 2003 to 2015 totaled $29.7 billion (adjusted for inflation) across all infrastructure over 12 years. Anthropic alone raised $65 billion in May 2026; Amazon spent $45 billion in a single recent quarter.

Furthermore, massive capital commitments are decoupled from actual installed capacity. Microsoft reported bringing a gigawatt of AI compute capacity online each quarter in its last three reports; Bloomberg and Guardian reporting revealed that Microsoft actually has only two gigawatts of operational capacity total, with the rest sitting in warehouses awaiting power infrastructure. Amazon has billions of dollars in chips either unable to be plugged in due to power constraints or sitting in unbuilt data centers. The hyperscalers, running out of growth ideas, followed OpenAI's ChatGPT moment and simply began buying massive quantities of chips. As Zitron notes, they're not sophisticated: "November 2022 rolls around, ChatGPT comes out. ... Microsoft did this ChatGPT thing. We should all buy these chips, more chips now, big, big."

**Non-Cancellable Commitments and the Debt Structure**

The true shock emerges when examining contractual commitments. Anthropic has signed "take-or-pay" lease agreements—non-cancellable commitments to pay for data center capacity regardless of whether they use it—totaling $430 billion over the next 7–10 years. Anthropic's annual operating expenses will hit $75–$100 billion within a year or two, whether or not revenue grows proportionally. For context, Microsoft—a $330 billion annual revenue company—has operating expenses around $150 billion. Anthropic is betting it will grow to Microsoft's revenue scale in just a few years, despite currently losing billions annually and showing no path to profitability.

OpenAI has signed a $300 billion deal with Oracle over five years (announced September 2025, part of a projected $750 billion spend by 2030). Anthropic pays SpaceX $3.1 billion monthly starting December 2026 for compute, a payment structure that only exists because traditional banks won't lend to unprofitable AI companies. The result: Oracle (through Larry Ellison) is building $400 billion worth of data centers for Sam Altman (OpenAI's CEO) on the promise that Altman will pay $300 billion, but neither company has existing assets or the ability to finance this independently. NVIDIA, as the chip monopolist, has become "the GE Capital of this all"—investing in OpenAI, SpaceX, Anthropic, CoreWeave (a NeoCloud company), and profiting from every transaction while controlling the underlying supply.

**CoreWeave and the NeoCloud Spiral**

Zitron introduces CoreWeave, a "NeoCloud" company that exemplifies the debt spiral. CoreWeave raises debt, buys GPUs using that debt, and leases capacity to Microsoft, Google, Anthropic, and Meta. But CoreWeave uses those same GPUs as collateral to borrow more money to buy more GPUs—a leveraged pyramid that only works if demand and financing never falter. Morgan Stanley estimated CoreWeave will need $100 billion more in debt. CoreWeave's customers are the hyperscalers, who are themselves the AI labs' customers, creating circular dependencies where the same $30–$40 billion in real capital circulates endlessly, never actually generating value.

**Valuation and IPO as "Exit Liquidity"**

Zitron pivots to Anthropic's impending IPO—announced at a $1.5–$2 trillion valuation. He introduces the concept of "exit liquidity": venture capitalists who invested in Anthropic at much lower valuations are able to sell their shares to public market retail investors at a massive markup, exiting the company and converting private gains to cash. Google went public at $23 billion (now worth $3–$4 trillion); Microsoft at $700 million (now in the trillions); Amazon at $300 million (now in the trillions). Anthropic at $1.5–$2 trillion is an outlier.

Stewart pushes back: couldn't the same be true for AI as it was for Google and Amazon? Zitron concedes that Google and Amazon eventually became profitable and valuable, but notes three critical differences. First, Google and Amazon actually built assets and offered services that proved indispensable to billions of people. Second, their capital expenditures were far more modest relative to today's spending. Third, they had clear paths to revenue before their massive infrastructure buildouts. Anthropic, by contrast, has "negative EBITDA" (negative earnings before interest, taxes, depreciation, and amortization), meaning it loses money even before accounting for all the actual financial costs of doing business.

**The Brittle Customer Base and Market Concentration Risk**

The combination of unprofitable AI startups as primary customers and a concentrated revenue base creates systemic fragility. Zitron compares it to the 2008 financial crisis: "7% of mortgages went underwater and that destroyed the entire derivatives market around it. So it's not going to take that big a hit to ripple through this industry and create a disastrous domino effect."

Moreover, the stock market itself is highly concentrated in AI bets. The "Magnificent Seven" tech companies (the hyperscalers and NVIDIA) drive 45% of the Nasdaq 100's value. Their valuations rest entirely on the assumption that AI will be transformative and that demand is insatiable. If demand plateaus—as Stewart notes streaming did—then the entire justification for massive capex evaporates. Companies like Microsoft cannot sustain GPU purchases from operating cash flow; Meta, Google, Amazon are all running cash-flow negative. The moment debt stops being issued or demand truly flatlines, the entire ecosystem collapses.

**The Missing Proof**

Zitron's central argument is stark: despite over a trillion dollars invested in AI chips and infrastructure, there is no clear proof of proportional economic payoff. No AI company has achieved sustained profitability at scale. No "killer app" has emerged that justifies the infrastructure. The Torsten Slog, chief economist at Apollo, stated publicly that "there has been no payoff from AI." Zitron concludes: people conflate media hype and venture capital enthusiasm with actual demand. The logic of the hyperscalers is "extremely childish"—OpenAI and Anthropic are growing fast, so they must grow even faster forever, therefore we need to buy infinite chips. But there's no underlying evidence that the public will spend meaningfully on AI, that existing startups will remain funded, or that the compute being built will ever run at profitable capacity utilization.
