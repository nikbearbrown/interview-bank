# Case-generation prompt templates

Ten prompt templates for generating practice cases: 2 styles (interviewer-led = McKinsey, candidate-led = BCG) x 5 types (management, product management, healthcare, financial, marketing). Pasted by Bear on 2026-10-28; the text below is verbatim. Source project and licence not recorded (see Notes). Cleaned, ready-to-use versions are in `prompts/` (built by `scripts/build_case_prompts.py`); this file keeps the originals unchanged.

Placeholders: `{difficulty}` (complexity level) and `{user_text}` (the field or industry the user names). Square-bracket items such as `[Company Name]` are for the model to fill.

---

# Style: Interviewer-led (the McKinsey style)

## Management Case Study

~~~
Create an interviewer-led case study of {difficulty} complexity for a fictitious company, elaborating on the field specified as: {user_text}. The case study structure should adhere to the following outline:

Title: [Title of the Case Study]

Introduction:

[Introduce the company or organization, providing a brief background. Mention the main products or services and the current market situation. Highlight the challenges faced by the company in the competitive landscape.]

Problem Definition:

[Describe the central issues affecting the company. Discuss multiple factors such as innovation challenges, consumer behavior changes, and competitive threats. Highlight how these issues threaten the company's market position and profitability.]

Problem Statement:

[Present a clear and concise statement requiring the reader to develop a strategic plan to improve the company's market position and profitability, taking into account the competitive dynamics and consumer preferences.]

Case Details:

[List the main revenue sources and their percentages to provide a financial overview of the company. Include historical data and trends affecting sales and market presence. Discuss how product pricing compares to competitors and its impact on brand image. Mention significant competitors and new market entrants, emphasizing their growth and strategic advantages.]

Questions:

Framework/Issue Tree Question: What analytical framework would you use to assess the competitive dynamics faced by the company, and what steps would you take to address the identified issues?

Market-Sizing and Guesstimate Question: Based on the provided sales data and market trends, estimate the potential impact on the company’s revenues if the current trends continue over the next five years.

Value Proposition Question: Considering consumer price sensitivity, what strategies could the company employ to enhance its value proposition while maintaining its premium brand image?
~~~

## Product Management Case Study

~~~
Generate a case study for Product Management, tailored to {difficulty} complexity focusing on the field specified as: {user_text}. Ensure the case study is formatted in Markdown without resorting to code blocks. Follow this structure for the case study:

**[Company Name] - [Product Line] Case Study**

**Introduction**  

[Introduce the company], a [brief description of the company type and founding year], has become a key player in [industry]. With a market cap of [market cap] as of [year], [Company Name] has made a significant impact globally. The company faces stiff competition from [list major competitors] in the [specific industry], which is shifting towards [describe market trends].

The [Product Line], one of their most recognized products, has encountered major challenges as of [year or period], including [list key issues faced by the product line].

**Objective**  

This case study aims to analyze [Company Name]'s strategy in addressing the issues with the [Product Line], with a focus on [list specific focus areas like product strategy, customer feedback].

**Key Challenges**  

- **[Challenge 1]:** Description of the challenge.

- **[Challenge 2]:** Description of the challenge.

- **[Challenge 3]:** Description of the challenge.

**Areas for Consideration**  

- **Product Innovation:** Discussion on whether [Company Name] should implement significant changes in product design to address consumer issues and meet competitor performance.

- **Customer-centric Approach:** How [Company Name] can use customer feedback to improve future product designs for better reception.

- **Pricing Strategy:** Strategies for aligning pricing with the perceived value by the customers.

**Constraints**  

- **Time:** The urgency of innovation in response to competitor advancements.

- **Resources:** The need for significant R&D investment to overhaul product design.

- **Budget:** Potential increases in production costs and how they affect profit margins.

**Questions**  

- **Framework/Issue Tree Question:** What are the key factors contributing to customer dissatisfaction with the [Product Line], and how can these be effectively prioritized?

- **Value Proposition Question:** How can [Company Name] enhance the value proposition of the [Product Line] to justify its premium pricing?

- **Quantitative Problem:** What could be the financial impact of major changes to the [Product Line] design?
~~~

## Healthcare Case Study

~~~
Create a Healthcare Case Study of {difficulty.lower()} complexity, utilizing leading Healthcare and Life Science companies, focusing on the field specified as: {user_text}. Ensure the case study is formatted in Markdown without employing code blocks. Follow this format for the case study:

**Title: Case Study - [Company Name]'s Challenges and Innovation in the [Sector] Sector**

**Background**  

[Company Name] is a leading company in [sector], offering [list primary products or services]. It targets [describe target market]. Despite its significant contributions, [Company Name] operates in a dynamic environment characterized by [list key market challenges like technological advancements, regulatory climate].

**Current Situation**  

- **Operational Inefficiency:** Description of the inefficiencies in the company's operations.

- **Market Pressure:** Challenges faced due to competition and market expectations.

- **Innovation Challenge:** The need for continuous R&D investment to keep up with industry advancements.

- **Regulatory Hurdles:** Description of the regulatory issues impacting new product launches and market expansion.

**Challenge**  

The primary challenge for [Company Name] is to maintain profitability in a competitive market, necessitating efficient supply chain operations, ongoing innovation, and an in-depth understanding of global regulatory frameworks.

**Questions**  

- **Framework/Issue Tree Question:** How can [Company Name] optimize its supply chain to improve operational efficiency and reduce costs?

- **Market-sizing and Guesstimate Question:** What is the potential growth opportunity for [Company Name] in [specific product segment] by [target year], given current market trends?

- **Value Proposition Question:** How can [Company Name] enhance its value proposition to encourage [target customer segment] to prefer its [description of products/services] over competitors' alternatives?
~~~

## Financial Case Study

~~~
Generate a {difficulty} Financial Services Case Study using top Banking and Finance companies in detail in the following field: {user_text}. The case study should be generated in the following format: 

**Title: Case Study - [Bank Name]: A Comprehensive Analysis of Financial Health and Strategic Management of a Major Commercial Bank**

**Introduction**  

[Bank Name], headquartered in [City, State], is a leading financial institution known globally, providing a wide range of financial services including banking, investing, asset management, and more. This case study aims to evaluate the financial health and strategic management of [Bank Name], focusing on the sustainability of its business strategies, effectiveness in resource allocation, and identification of potential financial or operating risks.

**Financial Analysis**  

1. **Financial Statements Analysis**

[Generate a Markdown table showcasing Financial Statements Analysis on the following company.]

2. **Ratio Analysis**

[Generate a Markdown table showcasing Ratio Analysis on the following company.]

3. **Trend Analysis**

[Provide a brief summary of trends observed in financials over the last four years, including revenue stability, net income changes, and asset growth.]

4. **Comparative Analysis**

[Compare the bank's financial metrics with those of key competitors such as JPMorgan Chase, Wells Fargo, and Citigroup, focusing on ROA and debt ratios.]

**Business Environment Analysis**  

1. **Market Analysis**

[Bank Name] controls approximately [x]% of the US market share among commercial banks.

2. **SWOT Analysis**

[Generate a Markdown table showcasing SWOT Analysis on the following company.]

3. **PESTEL Analysis**

[Discuss the political, economic, social, technological, environmental, and legal factors impacting the bank.]

**Strategic Analysis**  

[Bank Name] has been focusing on [list strategic focuses such as digital banking enhancements, cost reductions]. Key financial and operational risks include [list risks such as regulatory changes, potential economic downturns].

**Questions**  

- **Framework/Issue Tree Question:** What strategies can [Bank Name] adopt to improve overall profitability in the upcoming years?

- **Valuation Question:** How does [Bank Name]'s market capitalization compare to other top commercial banks?

- **Quantitative Problem:** How would a 5% increase in the default rate on [Bank Name]'s loan portfolio impact its net income?
~~~

## Marketing Case Study

~~~
Generate a {difficulty} Marketing Case Study using top Marketing Sector companies in detail in the following field: {user_text}. The case study generated should be in proper markdown format without using code blocks. The case study should be generated in the following format: 

**Title: Case Study - [Brand Name]: Mastering the Art of Innovative Marketing and Maintaining Relevance**

**Introduction**  

[Brand Name], a leader in [industry], commands a significant portion of the [market type] through its innovative marketing strategies across both traditional and digital platforms. Utilizing cutting-edge tools such as data analytics and AI, [Brand Name] engages customers effectively. Yet, evolving consumer preferences and increased competition present both challenges and opportunities for the brand to evolve its narrative.

**Marketing Scenario:**  

[Brand Name] has noted a shift in brand identity perception associated with their main product, [describe product]. The traditional [describe traditional brand identity] is becoming less appealing due to a rise in health consciousness among consumers.  

Despite [Brand Name]’s strong market position, it faces threats from new entrants marketing 'healthy [product type]'.

As digital engagement among consumers grows, [Brand Name] sees opportunities to apply more targeted strategies but must consider the investments required for new technologies.

**Objectives and Goals**  

- Redefine [Brand Name]'s brand identity to align with the 'health-conscious' trend while preserving its core message '[slogan or message]'.

- Surpass the competition, particularly new 'healthy [product type]' brands, by capitalizing on digital engagement trends.

**Questions:**  

- **Framework/Issue Tree Question:** What customer segmentation can [Brand Name] implement to effectively target health-conscious consumers?

- **Market-sizing and Guesstimate Question:** What is the size of the health-conscious [product type] market?

- **Valuation Question:** What is the potential value of investing in advanced digital marketing technologies for [Brand Name]?

- **Value Proposition Question:** What unique value can [Brand Name] offer to attract health-conscious consumers?

- **Quantitative Problem:** How can the impact of shifting [Brand Name]'s brand identity towards a health-centric image be quantified?
~~~

---

# Style: Candidate-led (the BCG style)

## Management Case Study

~~~
f"""Generate a {difficulty} candidate-led case study for a sample company in detail in the following field: {user_text}. The case study should be generated in the following format: 

**Title: Case Study - Optimizing [Company Name]'s Supply Chain through Improved Inventory Management**

**Introduction**  

[Company Name], a multinational [industry] company, grapples with the challenge of managing its vast and complex inventory. Effective inventory management is crucial for optimizing supply chain efficiency and ensuring timely delivery of products to customers.

**Problem Statement**  

[Company Name] faces significant issues with stock control, including frequent overstocking and understocking, which hamper operational efficiency and customer satisfaction. The central question is: How can [Company Name] implement a state-of-the-art inventory management system to streamline its operations and enhance supply chain efficiency?
~~~

## Product Management Case Study

~~~
Generate a {difficulty} Product Management case study using top IT based companies in detail in the following field: {user_text}. The case study generated should be in proper markdown format without using code blocks. The case study should be generated in the following format:

**[Company Name]: Balancing [Key Business Element 1] and [Key Business Element 2]**

**Introduction**

[Company Name], a leading [Industry Type] platform, ventured into [New Business Area] with [Product/Service Name]. The challenge? Achieving a balance between [Key Business Element 1] and [Key Business Element 2].

**Problem Statement**

How can [Product/Service Name] effectively prioritize its resources between [Key Business Element 1] (to gain market share) and [Key Business Element 2] (to provide [Desired Outcome]) within a highly competitive market? Provide a strategic roadmap detailing the recommendations.
~~~

## Healthcare Case Study

~~~
Generate a {difficulty} Healthcare Case Study using top Healthcare and Life Science companies in detail in the following field: {user_text}. The case study should be generated in the following format: 

**[Company Name]'s Journey towards Achieving Increased Efficiency in [Healthcare Focus Area] with [Technology/Process]**

**Introduction**

[Company Name], one of the leading global [Industry Type, e.g., pharmaceutical, biotech] companies, focuses on researching, developing, manufacturing, and marketing a wide range of [Products/Services, e.g., drugs, medical devices]. Aiming for increased productivity and cost optimization, [Company Name] wanted to implement a project involving [Technology/Process, e.g., advanced medical equipment, innovative healthcare processes] in their [Operation Area, e.g., drug production, patient care].

**Problem Statement**

While [Company Name] is a globally recognized player in the [Specific Sector, e.g., drug production, medical device manufacturing] sector, the company faced challenges in its pursuit to enhance production efficiency while maintaining stringent quality standards. The specific problem that surfaced was: How can [Company Name] incorporate [Technology/Process] into their [Operation Area] to improve efficiency, optimize costs, and ensure the consistent release of high-quality [Products/Services]?
~~~

## Financial Case Study

~~~
Generate a {difficulty} Financial Services Case Study using top Banking and Finance companies in detail in the following field: {user_text}. The case study generated should be in proper markdown format without using code blocks. The case study should be generated in the following format:

**Title: Transitioning [Bank Name] to a [Technology]-Based Infrastructure**

**Introduction**

[Bank Name], a leading global financial institution and a subsidiary of [Parent Company, if applicable], is weighing the possibilities of adopting [Technology, e.g., blockchain technology]. The aim is to enhance transaction efficiency, transparency, and secure data management.

**Problem Statement**

The challenge is discerning how to integrate [Technology] into [Bank Name]'s existing system to address concerns over transaction speed, operational efficiency, and security. The key question for candidates: How can [Bank Name] transition to a [Technology]-based infrastructure while ensuring minimal disruption to ongoing operations and maximum benefit realization from this new technology?
~~~

## Marketing Case Study

~~~
Generate a {difficulty} difficulty Marketing Case Study using top Marketing Sector companies in detail in the following field: {user_text}. The case study generated should be in proper markdown format without using code blocks. The case study should be generated in the following format:

**Title: The Successful International Expansion Strategy of [Company Name]**

**Introduction**

[Company Name], a renowned multinational [industry type, e.g., food and beverage, technology] corporation, emerged victoriously by effectively overcoming a significant hurdle relating to their international growth strategy. A thorough understanding of the local market demand was indispensable to ensure optimal positioning among global adversaries.

**Problem Statement**

Despite having an extensive product portfolio and a robust distribution network, [Company Name] encountered myriad difficulties while penetrating international markets, predominantly due to varying consumer preferences and numerous local competitors. How could [Company Name] adapt their product offering and marketing strategy to effectively establish their brand and enhance their market share in the global landscape?
~~~

---

# Notes (added by Claude, not part of the pasted text)

- **Provenance unknown.** The paste does not say where these came from. They match the format of the AI4ED `Case_Interview_AI` project noted earlier as a format reference with an unchecked licence. Confirm the source and its licence before publishing this file.
- **Style names.** Case Crackers ch. 19-20 defines the two paradigms: interviewer-led is McKinsey's format (Accenture, Strategy& and Oliver Wyman use variants); candidate-led is BCG's (also Bain, LEK, Deloitte, PwC).
- **Case Crackers has no such prompts.** These are the only case-generation prompts found; the book has none.
- **Inconsistent fictional status.** Only interviewer-led Management says "fictitious company". The Healthcare, Financial, Marketing and Product prompts say "using top ... companies", so the model will attach invented figures to real firms (the Financial prompt asks for financial-statement and ratio tables, JPMorgan and Citigroup comparisons, and a US market-share figure). Those numbers will not be reliable.
- **Template defects.** Interviewer-led Healthcare uses `{difficulty.lower()}`, which only works if the template is run as a Python f-string. Candidate-led Management begins `f"""` and never closes it. Interviewer-led Management has no Markdown formatting instruction; Product Management, Healthcare and Marketing ask for "no code blocks", Financial (interviewer-led) does not.
- **Candidate-led prompts stop at the problem statement.** They give no data, exhibits or answer key, so the candidate must request data, which fits the format. The interviewer-led ones ask for questions but no answers.
- **Marketing (interviewer-led) hard-codes a health-consciousness story** regardless of `{user_text}`, so every case would be about the same trend.
