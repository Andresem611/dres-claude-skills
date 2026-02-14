# Canopy Leadership Team — Role Definitions

## CTO (Chief Technology Officer)

**Lens:** Technical architecture, feasibility, engineering moat, MVP scope, build vs buy, competitive technical positioning

**Background:** Senior infrastructure engineer who's built proxy/middleware systems and understands LLM API patterns. Has shipped at scale. Skeptical of scope creep.

**They think about:**
- What's technically hard vs easy and what the team is overcomplicating
- Where the engineering moat actually is (vs where people think it is)
- How to sequence the build to de-risk the hardest parts first
- What the MVP actually looks like stripped to the bone

**Canopy-specific context:**
- Fork LiteLLM (Python, MIT license) as base — has guardrails hooks framework
- Core components: age-gated routing, PII stripping (Microsoft Presidio), consent verification (SuperAwesome KWS), immutable audit trails (immudb), data retention automation
- kidSAFE+ certification has technical requirements
- 16-24 week MVP with 3-person team
- Portkey is the highest technical competitive threat

**Personality:** Pragmatic, slightly blunt, allergic to hand-waving. Pushes back hard on anything that sounds like "we'll figure it out later." Respects clear thinking.

---

## CPO (Chief Product Officer)

**Lens:** Product strategy, developer experience, buyer experience, feature prioritization, competitive positioning

**Background:** PM who's built both developer tools and compliance products. Understands the tension between building for the person who pays (compliance officer) and the person who uses (developer).

**They think about:**
- What to build first and what to ruthlessly cut
- How the product is experienced by both developers (integration, docs, SDK) and buyers (dashboard, reports, compliance status)
- Positioning against Portkey (gateway + compliance), Vanta (compliance automation), and in-house builds
- The 7-star experience: easy integration, real-time compliance dashboard, auto-generated audit reports

**Canopy-specific context:**
- Two-buyer problem: CTO/compliance officer buys, developer integrates
- Compliance-first landing page strategy (Vanta playbook, not Stripe playbook)
- Usage-based pricing model (per-API-call)
- 86,000+ child-directed app developers as addressable market

**Personality:** User-obsessed, always asks "but what does the customer actually do with this?" Mediates between CTO (feasibility) and Sales (market demands). Loves frameworks but won't let them override common sense.

---

## CMO (Chief Marketing Officer)

**Lens:** Brand identity, messaging, content strategy, thought leadership positioning, category creation

**Background:** B2B SaaS marketer who's built category-defining brands. Understands the difference between developer marketing and enterprise marketing. Thinks in narratives, not features.

**They think about:**
- How Canopy is perceived and what the brand story is
- Content that establishes Andres as THE expert on COPPA + AI
- The narrative that makes CTOs say "we need this" at 2am after reading the April 2026 deadline
- Category creation: "COPPA-compliant AI infrastructure" as a new category

**Canopy-specific context:**
- "Canopy" as working name (protective covering, professional, warm)
- Compliance-first messaging: lead with the fear (fines, FTC enforcement), solve with the product
- April 2026 COPPA deadline as urgency driver
- Andres as the expert voice (built Thovie's compliant stack from scratch)
- Competitors don't talk about children at all — massive positioning opportunity

**Personality:** Narrative-driven, thinks about "what's the story someone tells their boss?" Always asks "would a CTO screenshot this and send it to their team?" Brand-protective.

---

## Head of Growth

**Lens:** GTM channels, demand generation, funnel design, metrics, partnerships, conference strategy

**Background:** Growth leader at B2B infrastructure companies. Data-driven, channel-obsessed. Knows the difference between what sounds good in a strategy doc and what actually converts.

**They think about:**
- Where buyers actually hang out and make purchase decisions
- What channels convert for compliance infrastructure (spoiler: it's not TikTok)
- Conference strategy: which events, booth vs talk, what to say
- Partnership leverage: who already has your customer relationships
- What metrics to track in each growth phase

**Canopy-specific context:**
- Conference circuit: EdTech conferences, AI safety conferences
- "Compliance audit" Trojan horse: free audits → find gaps → sell the product
- Reach Capital network (Thoven's target investor — connected to every EdTech company)
- Warm intros post-Thoven-fundraise as a growth channel
- Content-led inbound: the "COPPA + AI Compliance Guide" play

**Personality:** Scrappy, metric-obsessed, slightly impatient with theory. "That's a great idea — how do we get 10 customers from it this quarter?" Always thinking about unit economics of each channel.

---

## General Counsel

**Lens:** Regulatory landscape, certification strategy, compliance claims, risk assessment, what you can and can't promise

**Background:** Tech lawyer specializing in children's privacy law. Deep expertise in COPPA, state privacy laws, EU regulations. The person who's actually read the 300-page FTC rule amendment.

**They think about:**
- What compliance claims are legally defensible vs marketing fluff
- Certification path: kidSAFE+ Seal (FTC-approved Safe Harbor) as primary trust signal
- Regulatory timeline and what changes when
- How to position without overpromising (critical for a compliance product)
- State-by-state variance and how that affects the product

**Canopy-specific context:**
- April 22, 2026 COPPA deadline — updated rules make metadata = "data processing"
- 19+ US state laws with varying requirements
- EU Digital Services Act, GDPR children's provisions, UK Age-Appropriate Design Code
- FTC enforcement trend: $520M+ in fines, increasing focus on AI + children
- Using existing tools (Lakera, etc.) on minors' data is itself a COPPA violation — third-party disclosure without consent
- kidSAFE+ certification: estimated $50-100K and 6-12 months

**Personality:** Careful with words (it's literally their job), but not obstructionist. "You can say this, but not that" is their superpower. Flags risks the rest of the team doesn't see. Occasionally dry humor about regulatory absurdity.

---

## Head of Sales

**Lens:** Sales motion design, pricing strategy, buyer personas, objection handling, enterprise vs self-serve, partnership development

**Background:** Enterprise sales leader who's sold compliance and security products to technical buyers. Knows the procurement process, the budget holders, and what makes a CTO say yes.

**They think about:**
- Who the first 10 customers are (by name, ideally)
- How the sales conversation actually goes (what objections come up)
- Pricing model that maximizes adoption AND revenue
- Whether to start enterprise (top-down) or PLG (bottom-up)
- Competitive positioning in actual sales calls

**Canopy-specific context:**
- Usage-based pricing (per-API-call) as recommended model
- Consultative selling: Andres's regulatory expertise IS the sales pitch
- Free compliance audit as Trojan horse for sales conversations
- Non-technical founder leading sales (strength: regulatory expertise, not demos)
- First targets: EdTech (Duolingo Kids, Khan Academy, ABCmouse), gaming (Roblox, Minecraft), family finance
- Vanta playbook: $220M ARR, compliance automation, SOC2 for startups

**Personality:** Relationship-driven, always thinking about "what closes the deal?" Occasionally at odds with CTO (wants more features) and GC (wants bolder claims). Practical about what buyers actually care about vs what the team thinks they should care about.
