from gemini_client import ask_gemini
from retriever import retrieve_context_with_citations
def generate_readiness_assessment(api_key=None):
    """
    Evaluates startup readiness by analyzing database documents and mapping them to standards.
    """
    # Retrieve documents relevant to compliance, launch, and readiness
    context, citations = retrieve_context_with_citations(
        "readiness score checklist compliance registration milestones pitch deck launch steps legal requirements", 
        n_results=6
    )
    
    prompt = f"""You are a startup readiness auditor. Analyze the uploaded startup documentation and evaluate the startup's preparedness.
    
    Uploaded Document Context:
    {context}
    
    Please structure your answer EXACTLY as follows:
    1. **Startup Readiness Score**: Give a percentage score (e.g., 78%) based on typical startup benchmarks and guidelines found in the documents (or general standard guidelines if details are sparse). Write a paragraph explaining the rationale.
    2. **Benchmark Breakdown**:
       - Product/Tech Validation (Status and gaps)
       - Legal/Registration Compliance (Required filings and structures)
       - Team & Operations
       - Financial Planning & Market Sizing
    3. **Critical Gaps & Red Flags**: List anything missing or posing immediate legal/financial risks.
    4. **Actionable Checklist**: Step-by-step list of prioritized items to improve the score.
    """
    
    try:
        response = ask_gemini(prompt, api_key=api_key)
        return response, citations
    except Exception as e:
        return f"Error running assessment: {str(e)}", []
def generate_funding_recommendations(stage, industry, funding_amount, api_key=None):
    """
    Generates funding recommendations based on stage, industry, and database documents.
    """
    # Retrieve documents related to grants, funding schemes, investors, etc.
    context, citations = retrieve_context_with_citations(
        f"funding schemes grants venture capital investment angel investor seed capital loan subsidy for {industry} {stage}", 
        n_results=6
    )
    
    prompt = f"""You are a startup fundraising consultant. Match this startup profile against the uploaded documents and general funding schemes.
    
    Startup Profile:
    - Stage: {stage}
    - Industry: {industry}
    - Target Funding Amount: {funding_amount}
    
    Uploaded Document Context:
    {context}
    
    Structure your answer as follows:
    1. **Top Funding Pathways**: Recommend the best types of funding (e.g., government grants, equity crowdfunding, angel networks, seed VC, venture debt).
    2. **Specific Eligible Schemes**: Reference any specific grants or schemes mentioned in the uploaded documentation or general prominent programs.
    3. **Due Diligence Checklist**: What metrics and documentation (financial plan, incorporation certificate, cap table) must be ready for this round.
    4. **Action Plan**: Quick steps for the next 90 days to prepare, approach, and close the fundraising round.
    """
    try:
        response = ask_gemini(prompt, api_key=api_key)
        return response, citations
    except Exception as e:
        return f"Error generating funding recommendations: {str(e)}", []
def generate_custom_roadmap(goals, api_key=None):
    """
    Creates a detailed project roadmap based on the startup's goals.
    """
    # Retrieve documents related to launch steps, timelines, and milestones
    context, citations = retrieve_context_with_citations(
        "roadmap timeline launch execution milestones steps timeline project schedule launch checklist", 
        n_results=6
    )
    
    prompt = f"""You are a startup operations expert and co-founder. Create a personalized step-by-step launch roadmap for the next 6-12 months.
    
    Founder's Target Goals: {goals}
    
    Uploaded Document Context:
    {context}
    
    Structure your answer as follows:
    1. **Phase 1: Setup & Validation (Months 1-2)**: Core legal filings, market research, MVP planning.
    2. **Phase 2: Build & Compliance (Months 3-5)**: Product development, regulatory approvals, and contracts.
    3. **Phase 3: Launch & Growth (Months 6-8)**: Go-to-market execution, client acquisition, feedback loops.
    4. **OKRs and KPIs**: Concrete metrics to measure success at each phase.
    """
    try:
        response = ask_gemini(prompt, api_key=api_key)
        return response, citations
    except Exception as e:
        return f"Error generating roadmap: {str(e)}", []
def simplify_legal_text(legal_text, api_key=None):
    """
    Deconstructs dense legal text or clauses into plain English.
    """
    prompt = f"""You are a startup legal counsel. Simplify the following legal clause, contract snippet, or agreement terms into clear, plain English that a non-lawyer entrepreneur can easily understand.
    
    Legal Text:
    {legal_text}
    
    Please provide:
    1. **Plain English Translation**: Simplify the legalese clauses directly.
    2. **Key Commitments**: What rights are they giving up, and what obligations are they taking on?
    3. **Potential Risks & Red Flags**: Any hidden traps, unfavorable termination terms, or clauses they should attempt to renegotiate.
    4. **Action Recommendation**: Give explicit guidance (e.g., "Accept as is", "Request deletion of clause X", "Consult lawyer before signing").
    """
    try:
        response = ask_gemini(prompt, api_key=api_key)
        return response, []
    except Exception as e:
        return f"Error simplifying legal text: {str(e)}", []
