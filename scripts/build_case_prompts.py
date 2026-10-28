"""Compose the cleaned case-generation prompts (2 styles x 5 types) into case-interviews/prompts/.

Each output file is one ready-to-paste prompt with two placeholders: {difficulty} and {user_text}.
Run: python3 -I scripts/build_case_prompts.py
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "case-interviews" / "prompts"

COMMON = """\
Write a {style_name} case interview for a fictitious company. Difficulty: {{difficulty}}. Industry or field: {{user_text}}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.
"""

# ---- interviewer-led (McKinsey) --------------------------------------------------------------
IL_HEAD = """\

Headings:

**Title**

**Introduction** - the company, its main products or services, its market, and the competitive pressure. {intro_extra}

**Problem Definition** - the central issues: {issues}. Show how each threatens market position and profitability.

**Problem Statement** - one clear sentence asking the candidate to develop a plan to improve the company's market position and profitability.

**Case Details** - {details}

**Questions** - number them. Each must be answerable in order, using only data in the case.
{questions}

**Interviewer Notes (do not show the candidate)** - for each question: what a strong answer covers, the worked arithmetic for any numeric question, and one common mistake.
"""

IL = {
    "management": dict(
        intro_extra="Include the competitive landscape.",
        issues="innovation challenges, changes in consumer behavior and competitive threats",
        details="main revenue sources with percentages totaling 100; sales for the last four years as a table; how pricing compares with named (invented) competitors and what that does to brand image; significant competitors and new entrants and why they are growing.",
        questions="""\
1. Framework / issue tree: what framework would you use to assess the competitive dynamics the company faces, and what steps would you take to address the issues?
2. Market sizing / guesstimate: from the sales data and trends given, estimate the effect on revenue over five years if current trends continue.
3. Value proposition: given consumer price sensitivity, how could the company strengthen its value proposition while protecting its brand image?""",
    ),
    "product-management": dict(
        intro_extra="State the company type, founding year and market capitalization (invented), the product line, and the market trend it faces.",
        issues="three key challenges with the product line, each with a short description",
        details="customer feedback themes with counts, competitor product comparisons, unit economics for the product line, and constraints on time, R&D resources and budget.",
        questions="""\
1. Framework / issue tree: which factors drive customer dissatisfaction with the product line, and how would you prioritize them?
2. Value proposition: how can the company strengthen the value proposition of the product line to justify its price?
3. Quantitative: what is the likely financial impact of a major change to the product line's design?""",
    ),
    "healthcare": dict(
        intro_extra="State the sector, primary products or services, target market, and the regulatory and technology climate.",
        issues="operational inefficiency, market pressure, the need for continuing R&D investment, and regulatory hurdles for launches and expansion",
        details="a supply-chain cost breakdown as a table, regulatory timelines, market segment sizes, and competitor positioning. State the profitability challenge plainly.",
        questions="""\
1. Framework / issue tree: how can the company optimize its supply chain to improve efficiency and cut cost?
2. Market sizing / guesstimate: what is the growth opportunity in a named product segment by a target year, given current market trends?
3. Value proposition: how can the company make a named customer segment prefer its products over competitors' alternatives?""",
    ),
    "financial": dict(
        intro_extra="Name the (invented) bank, its headquarters city, and the financial services it offers. State that the case evaluates its financial health, strategy and risks.",
        issues="sustainability of its strategy, effectiveness of resource allocation, and financial and operating risks",
        details="a summary financial-statements table; a ratio table; a four-year trend summary (revenue stability, net income, asset growth); a comparison with three invented peer banks on return on assets and debt ratios; the bank's market share among commercial banks; a SWOT table; a PESTEL discussion; current strategic focuses and key risks.",
        questions="""\
1. Framework / issue tree: what strategies could the bank adopt to improve profitability over the next few years?
2. Valuation: how does the bank's market capitalization compare with its invented peers, and what explains the gap?
3. Quantitative: how would a 5% increase in the default rate on its loan portfolio change net income?""",
    ),
    "marketing": dict(
        intro_extra="Name the brand, its industry, the market it leads, and its traditional and digital marketing channels.",
        issues="a shift in how customers see the brand's main product, chosen to fit the field (do not default to health-consciousness unless the field calls for it), new entrants exploiting that shift, and the investment needed to use digital engagement",
        details="the brand identity today and what is eroding it, a customer-segment table, channel spend and return, new entrants and their claims, and the brand's core message. End with two or three objectives for the brand.",
        questions="""\
1. Framework / issue tree: what customer segmentation would let the brand target the shifting segment?
2. Market sizing / guesstimate: how large is the market for the new segment?
3. Valuation: what is the potential value of investing in new digital marketing technology?
4. Value proposition: what unique value can the brand offer the shifting segment?
5. Quantitative: how can the impact of moving the brand's identity be quantified?""",
    ),
}

# ---- candidate-led (BCG) ---------------------------------------------------------------------
CL_HEAD = """\

Headings:

**Title** - neutral, naming only the company and the broad topic.

**Introduction** - {intro}

**Problem Statement** - {problem} State it as one open question. Give no sub-questions, no framework and no hint of the answer: the candidate chooses the approach and asks for the data.

**Interviewer Data Pack (do not show the candidate)** - give nothing from here unless the candidate asks for it by name or asks a question it answers. Include: (a) six to eight data items the candidate might request, each with its numbers; (b) one exhibit as a Markdown table; (c) one multi-step calculation to pose when the candidate asks for numbers, with the worked arithmetic; (d) the key insight, one distractor, and what a strong closing recommendation contains.
"""

CL = {
    "management": dict(
        intro="a multinational company in the given field that struggles to manage a large, complex inventory, and why that matters for delivering on time.",
        problem="The company has frequent overstocking and understocking that hurt operational efficiency and customer satisfaction. Ask how it should fix inventory management to streamline operations.",
    ),
    "product-management": dict(
        intro="a leading platform company that entered a new business area with a new product or service, and the two things it must balance, one to gain market share and one to deliver a desired outcome.",
        problem="Ask how the product should prioritize resources between the two in a highly competitive market, and have the candidate produce a strategic roadmap with recommendations.",
    ),
    "healthcare": dict(
        intro="a leading global company in the given healthcare or life-science field that wants to introduce a new technology or process into one operation (for example drug production or patient care) to raise productivity and cut cost.",
        problem="The company needs to raise efficiency while keeping strict quality standards. Ask how it should incorporate the technology or process into the operation to improve efficiency, optimize cost and keep releasing consistently high-quality products.",
    ),
    "financial": dict(
        intro="an invented bank, with a parent company if relevant, weighing a new technology (choose one that fits the field) to improve transaction efficiency, transparency and secure data management.",
        problem="Ask how the bank should integrate the technology into its existing systems to address transaction speed, operational efficiency and security, with minimal disruption to ongoing operations and the benefits fully realized.",
    ),
    "marketing": dict(
        intro="an invented multinational in the given field with a broad product portfolio and a strong distribution network that is entering new international markets. Write it as a company that has not yet succeeded.",
        problem="The company faces varied consumer preferences and many local competitors. Ask how it should adapt its product offering and marketing strategy to establish its brand and win market share in the new markets.",
    ),
}

STYLES = [
    ("mckinsey-interviewer-led", "McKinsey-style, interviewer-led", "interviewer-led"),
    ("bcg-candidate-led", "BCG-style, candidate-led", "candidate-led"),
]


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    made = []
    for slug, style_name, kind in STYLES:
        for t, d in (IL if kind == "interviewer-led" else CL).items():
            body = COMMON.format(style_name=style_name)
            body += (IL_HEAD.format(**d) if kind == "interviewer-led" else CL_HEAD.format(**d))
            path = OUT / f"{slug}-{t}.md"
            path.write_text(body)
            made.append(path.name)
    return made


if __name__ == "__main__":
    for n in build():
        print(n)
