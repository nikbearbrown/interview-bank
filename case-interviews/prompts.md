# Case-generation prompts

Ten ready-to-paste prompts for generating practice case interviews: 2 styles (McKinsey-style interviewer-led, BCG-style candidate-led) x 5 types (management, product management, healthcare, financial, marketing). These are cleaned versions of the originals in [generation-prompts.md](generation-prompts.md), which keeps the verbatim text and a list of the defects fixed. The same prompts are in [prompts.json](prompts.json). Rebuild both with `python3 -I scripts/build_case_prompts.py`.

## How to use

Copy one block, replace the two placeholders, and paste it to a model.

- `{difficulty}`: `easy`, `medium` or `hard`. The prompt defines each.
- `{user_text}`: the industry or field, in your own words.

Every prompt requires an invented company and competitors, numbers that are internally consistent and recomputed, a title that does not reveal the answer, and no candidate recommendation. Answer material appears only under the last heading, which is for the interviewer.

| Id | Style | Type |
|---|---|---|
| `mckinsey-interviewer-led-management` | McKinsey-style, interviewer-led | Management |
| `mckinsey-interviewer-led-product-management` | McKinsey-style, interviewer-led | Product management |
| `mckinsey-interviewer-led-healthcare` | McKinsey-style, interviewer-led | Healthcare |
| `mckinsey-interviewer-led-financial` | McKinsey-style, interviewer-led | Financial |
| `mckinsey-interviewer-led-marketing` | McKinsey-style, interviewer-led | Marketing |
| `bcg-candidate-led-management` | BCG-style, candidate-led | Management |
| `bcg-candidate-led-product-management` | BCG-style, candidate-led | Product management |
| `bcg-candidate-led-healthcare` | BCG-style, candidate-led | Healthcare |
| `bcg-candidate-led-financial` | BCG-style, candidate-led | Financial |
| `bcg-candidate-led-marketing` | BCG-style, candidate-led | Marketing |

# McKinsey-style, interviewer-led

The interviewer drives. The case comes with three to five numbered questions, answered in order from data in the case, and interviewer notes that hold the worked arithmetic.

## Management

Id: `mckinsey-interviewer-led-management`

```text
Write a McKinsey-style, interviewer-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title**

**Introduction** - the company, its main products or services, its market, and the competitive pressure. Include the competitive landscape.

**Problem Definition** - the central issues: innovation challenges, changes in consumer behavior and competitive threats. Show how each threatens market position and profitability.

**Problem Statement** - one clear sentence asking the candidate to develop a plan to improve the company's market position and profitability.

**Case Details** - main revenue sources with percentages totaling 100; sales for the last four years as a table; how pricing compares with named (invented) competitors and what that does to brand image; significant competitors and new entrants and why they are growing.

**Questions** - number them. Each must be answerable in order, using only data in the case.
1. Framework / issue tree: what framework would you use to assess the competitive dynamics the company faces, and what steps would you take to address the issues?
2. Market sizing / guesstimate: from the sales data and trends given, estimate the effect on revenue over five years if current trends continue.
3. Value proposition: given consumer price sensitivity, how could the company strengthen its value proposition while protecting its brand image?

**Interviewer Notes (do not show the candidate)** - for each question: what a strong answer covers, the worked arithmetic for any numeric question, and one common mistake.
```

## Product management

Id: `mckinsey-interviewer-led-product-management`

```text
Write a McKinsey-style, interviewer-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title**

**Introduction** - the company, its main products or services, its market, and the competitive pressure. State the company type, founding year and market capitalization (invented), the product line, and the market trend it faces.

**Problem Definition** - the central issues: three key challenges with the product line, each with a short description. Show how each threatens market position and profitability.

**Problem Statement** - one clear sentence asking the candidate to develop a plan to improve the company's market position and profitability.

**Case Details** - customer feedback themes with counts, competitor product comparisons, unit economics for the product line, and constraints on time, R&D resources and budget.

**Questions** - number them. Each must be answerable in order, using only data in the case.
1. Framework / issue tree: which factors drive customer dissatisfaction with the product line, and how would you prioritize them?
2. Value proposition: how can the company strengthen the value proposition of the product line to justify its price?
3. Quantitative: what is the likely financial impact of a major change to the product line's design?

**Interviewer Notes (do not show the candidate)** - for each question: what a strong answer covers, the worked arithmetic for any numeric question, and one common mistake.
```

## Healthcare

Id: `mckinsey-interviewer-led-healthcare`

```text
Write a McKinsey-style, interviewer-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title**

**Introduction** - the company, its main products or services, its market, and the competitive pressure. State the sector, primary products or services, target market, and the regulatory and technology climate.

**Problem Definition** - the central issues: operational inefficiency, market pressure, the need for continuing R&D investment, and regulatory hurdles for launches and expansion. Show how each threatens market position and profitability.

**Problem Statement** - one clear sentence asking the candidate to develop a plan to improve the company's market position and profitability.

**Case Details** - a supply-chain cost breakdown as a table, regulatory timelines, market segment sizes, and competitor positioning. State the profitability challenge plainly.

**Questions** - number them. Each must be answerable in order, using only data in the case.
1. Framework / issue tree: how can the company optimize its supply chain to improve efficiency and cut cost?
2. Market sizing / guesstimate: what is the growth opportunity in a named product segment by a target year, given current market trends?
3. Value proposition: how can the company make a named customer segment prefer its products over competitors' alternatives?

**Interviewer Notes (do not show the candidate)** - for each question: what a strong answer covers, the worked arithmetic for any numeric question, and one common mistake.
```

## Financial

Id: `mckinsey-interviewer-led-financial`

```text
Write a McKinsey-style, interviewer-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title**

**Introduction** - the company, its main products or services, its market, and the competitive pressure. Name the (invented) bank, its headquarters city, and the financial services it offers. State that the case evaluates its financial health, strategy and risks.

**Problem Definition** - the central issues: sustainability of its strategy, effectiveness of resource allocation, and financial and operating risks. Show how each threatens market position and profitability.

**Problem Statement** - one clear sentence asking the candidate to develop a plan to improve the company's market position and profitability.

**Case Details** - a summary financial-statements table; a ratio table; a four-year trend summary (revenue stability, net income, asset growth); a comparison with three invented peer banks on return on assets and debt ratios; the bank's market share among commercial banks; a SWOT table; a PESTEL discussion; current strategic focuses and key risks.

**Questions** - number them. Each must be answerable in order, using only data in the case.
1. Framework / issue tree: what strategies could the bank adopt to improve profitability over the next few years?
2. Valuation: how does the bank's market capitalization compare with its invented peers, and what explains the gap?
3. Quantitative: how would a 5% increase in the default rate on its loan portfolio change net income?

**Interviewer Notes (do not show the candidate)** - for each question: what a strong answer covers, the worked arithmetic for any numeric question, and one common mistake.
```

## Marketing

Id: `mckinsey-interviewer-led-marketing`

```text
Write a McKinsey-style, interviewer-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title**

**Introduction** - the company, its main products or services, its market, and the competitive pressure. Name the brand, its industry, the market it leads, and its traditional and digital marketing channels.

**Problem Definition** - the central issues: a shift in how customers see the brand's main product, chosen to fit the field (do not default to health-consciousness unless the field calls for it), new entrants exploiting that shift, and the investment needed to use digital engagement. Show how each threatens market position and profitability.

**Problem Statement** - one clear sentence asking the candidate to develop a plan to improve the company's market position and profitability.

**Case Details** - the brand identity today and what is eroding it, a customer-segment table, channel spend and return, new entrants and their claims, and the brand's core message. End with two or three objectives for the brand.

**Questions** - number them. Each must be answerable in order, using only data in the case.
1. Framework / issue tree: what customer segmentation would let the brand target the shifting segment?
2. Market sizing / guesstimate: how large is the market for the new segment?
3. Valuation: what is the potential value of investing in new digital marketing technology?
4. Value proposition: what unique value can the brand offer the shifting segment?
5. Quantitative: how can the impact of moving the brand's identity be quantified?

**Interviewer Notes (do not show the candidate)** - for each question: what a strong answer covers, the worked arithmetic for any numeric question, and one common mistake.
```

# BCG-style, candidate-led

The candidate drives. The case is one open problem statement; the candidate chooses the approach and asks for data, which the interviewer releases from a data pack.

## Management

Id: `bcg-candidate-led-management`

```text
Write a BCG-style, candidate-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title** - neutral, naming only the company and the broad topic.

**Introduction** - a multinational company in the given field that struggles to manage a large, complex inventory, and why that matters for delivering on time.

**Problem Statement** - The company has frequent overstocking and understocking that hurt operational efficiency and customer satisfaction. Ask how it should fix inventory management to streamline operations. State it as one open question. Give no sub-questions, no framework and no hint of the answer: the candidate chooses the approach and asks for the data.

**Interviewer Data Pack (do not show the candidate)** - give nothing from here unless the candidate asks for it by name or asks a question it answers. Include: (a) six to eight data items the candidate might request, each with its numbers; (b) one exhibit as a Markdown table; (c) one multi-step calculation to pose when the candidate asks for numbers, with the worked arithmetic; (d) the key insight, one distractor, and what a strong closing recommendation contains.
```

## Product management

Id: `bcg-candidate-led-product-management`

```text
Write a BCG-style, candidate-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title** - neutral, naming only the company and the broad topic.

**Introduction** - a leading platform company that entered a new business area with a new product or service, and the two things it must balance, one to gain market share and one to deliver a desired outcome.

**Problem Statement** - Ask how the product should prioritize resources between the two in a highly competitive market, and have the candidate produce a strategic roadmap with recommendations. State it as one open question. Give no sub-questions, no framework and no hint of the answer: the candidate chooses the approach and asks for the data.

**Interviewer Data Pack (do not show the candidate)** - give nothing from here unless the candidate asks for it by name or asks a question it answers. Include: (a) six to eight data items the candidate might request, each with its numbers; (b) one exhibit as a Markdown table; (c) one multi-step calculation to pose when the candidate asks for numbers, with the worked arithmetic; (d) the key insight, one distractor, and what a strong closing recommendation contains.
```

## Healthcare

Id: `bcg-candidate-led-healthcare`

```text
Write a BCG-style, candidate-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title** - neutral, naming only the company and the broad topic.

**Introduction** - a leading global company in the given healthcare or life-science field that wants to introduce a new technology or process into one operation (for example drug production or patient care) to raise productivity and cut cost.

**Problem Statement** - The company needs to raise efficiency while keeping strict quality standards. Ask how it should incorporate the technology or process into the operation to improve efficiency, optimize cost and keep releasing consistently high-quality products. State it as one open question. Give no sub-questions, no framework and no hint of the answer: the candidate chooses the approach and asks for the data.

**Interviewer Data Pack (do not show the candidate)** - give nothing from here unless the candidate asks for it by name or asks a question it answers. Include: (a) six to eight data items the candidate might request, each with its numbers; (b) one exhibit as a Markdown table; (c) one multi-step calculation to pose when the candidate asks for numbers, with the worked arithmetic; (d) the key insight, one distractor, and what a strong closing recommendation contains.
```

## Financial

Id: `bcg-candidate-led-financial`

```text
Write a BCG-style, candidate-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title** - neutral, naming only the company and the broad topic.

**Introduction** - an invented bank, with a parent company if relevant, weighing a new technology (choose one that fits the field) to improve transaction efficiency, transparency and secure data management.

**Problem Statement** - Ask how the bank should integrate the technology into its existing systems to address transaction speed, operational efficiency and security, with minimal disruption to ongoing operations and the benefits fully realized. State it as one open question. Give no sub-questions, no framework and no hint of the answer: the candidate chooses the approach and asks for the data.

**Interviewer Data Pack (do not show the candidate)** - give nothing from here unless the candidate asks for it by name or asks a question it answers. Include: (a) six to eight data items the candidate might request, each with its numbers; (b) one exhibit as a Markdown table; (c) one multi-step calculation to pose when the candidate asks for numbers, with the worked arithmetic; (d) the key insight, one distractor, and what a strong closing recommendation contains.
```

## Marketing

Id: `bcg-candidate-led-marketing`

```text
Write a BCG-style, candidate-led case interview for a fictitious company. Difficulty: {difficulty}. Industry or field: {user_text}.

Rules:
1. Everything is invented. The company, its products, its people and its competitors are fictitious. Do not name, imitate or take figures from any real company, bank, brand or product. If the field brings a famous firm to mind, invent a different one.
2. Every number is illustrative but internally consistent. Percentages that should total 100 do. Every figure a question needs can be derived from the data you give. Recompute all arithmetic before you finish, and show the working in the interviewer notes.
3. Difficulty: easy = one dominant cause and round numbers; medium = two interacting causes and at least one calculation with a unit change; hard = conflicting data, one distractor, multi-step math, and no single right answer.
4. Format: Markdown, no code blocks. Use exactly the headings below, in this order.
5. The title must not reveal the answer. Write the case as unresolved: do not describe the company as having already succeeded or failed at the thing the case asks about.
6. Do not write the candidate's recommendation. The only answer material goes under the last heading, which is for the interviewer.

Headings:

**Title** - neutral, naming only the company and the broad topic.

**Introduction** - an invented multinational in the given field with a broad product portfolio and a strong distribution network that is entering new international markets. Write it as a company that has not yet succeeded.

**Problem Statement** - The company faces varied consumer preferences and many local competitors. Ask how it should adapt its product offering and marketing strategy to establish its brand and win market share in the new markets. State it as one open question. Give no sub-questions, no framework and no hint of the answer: the candidate chooses the approach and asks for the data.

**Interviewer Data Pack (do not show the candidate)** - give nothing from here unless the candidate asks for it by name or asks a question it answers. Include: (a) six to eight data items the candidate might request, each with its numbers; (b) one exhibit as a Markdown table; (c) one multi-step calculation to pose when the candidate asks for numbers, with the worked arithmetic; (d) the key insight, one distractor, and what a strong closing recommendation contains.
```
