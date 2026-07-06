import streamlit as st
import os
import re
import sys
import pandas as pd
# Set page configuration first
st.set_page_config(
    page_title="StartupPilotAI - Your AI Co-Founder",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Ensure src/ or the current directory is in the python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_src = os.path.abspath(os.path.join(current_dir, "src"))
if os.path.exists(parent_src):
    sys.path.append(parent_src)
else:
    sys.path.append(current_dir)
from pdf_loader import load_pdf
from chunking import split_text
from embeddings import embed_chunks
import vectorstore
from gemini_client import ask_rag, configure_gemini
from advisor import (
    generate_readiness_assessment,
    generate_funding_recommendations,
    generate_custom_roadmap,
    simplify_legal_text
)
# Custom premium styling
st.markdown("""
<style>
    /* Styling custom headers and cards */
    .banner {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #ec4899 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(139, 92, 246, 0.3);
        text-align: center;
    }
    .banner h1 {
        color: white !important;
        font-family: 'Inter', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.05em;
    }
    .banner p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    .card {
        background: #1f2937;
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .card-title {
        font-weight: 700;
        color: #f3f4f6;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    .metric-num {
        font-size: 2.2rem;
        font-weight: 800;
        color: #6366f1;
        margin: 0.2rem 0;
    }
    .citation-box {
        background-color: rgba(99, 102, 241, 0.05);
        border-left: 4px solid #6366f1;
        padding: 0.8rem 1.2rem;
        margin-top: 0.6rem;
        border-radius: 4px;
    }
    .citation-header {
        font-weight: 600;
        color: #a855f7;
        font-size: 0.85rem;
        margin-bottom: 0.3rem;
    }
    .citation-text {
        font-style: italic;
        color: #d1d5db;
        font-size: 0.9rem;
        line-height: 1.4;
    }
    /* Add support for scrolling code or texts */
    .scroll-box {
        max-height: 250px;
        overflow-y: auto;
        padding: 10px;
        background: #111827;
        border-radius: 8px;
        border: 1px solid #374151;
    }
</style>
""", unsafe_allow_html=True)
# Define Session States
if "processed_files" not in st.session_state:
    try:
        stats = vectorstore.get_stats()
        st.session_state.processed_files = stats.get("filenames", [])
    except Exception:
        st.session_state.processed_files = []
if "messages" not in st.session_state:
    st.session_state.messages = []
# Sidebar Navigation / Database Controls
with st.sidebar:
    st.markdown("<h2 style='color: #6366f1; margin-top: 0;'>🚀 StartupPilotAI</h2>", unsafe_allow_html=True)
    st.write("Your AI-Powered Co-Founder & Startup advisory engine.")
    st.markdown("---")
    # API key selection
    api_key_input = st.text_input(
        "Google Gemini API Key (Optional)",
        type="password",
        help="Provide your own Gemini API Key. If left blank, the system will use the default workspace key."
    )
    if api_key_input:
        st.session_state.api_key = api_key_input
        # Configure dynamically
        configure_gemini(api_key_input)
    else:
        st.session_state.api_key = None
        configure_gemini(None)
    st.markdown("---")
    st.subheader("📁 Knowledge Base")
    
    uploaded_files = st.file_uploader(
        "Upload Startup PDFs",
        type=["pdf"],
        accept_multiple_files=True,
        help="Upload guidelines, company documents, or financial sheets."
    )
    # Process PDFs
    if uploaded_files:
        # Filter files that haven't been indexed yet
        new_files = [f for f in uploaded_files if f.name not in st.session_state.processed_files]
        if new_files:
            with st.spinner("Indexing new files into ChromaDB..."):
                for pdf_file in new_files:
                    try:
                        # Extract pages
                        pages_data = load_pdf(pdf_file)
                        
                        # Generate semantic chunks
                        chunks = split_text(pages_data)
                        
                        # Encode chunks
                        embeddings = embed_chunks(chunks)
                        
                        # Store in Chroma
                        vectorstore.store_embeddings(chunks, embeddings)
                        
                        # Track processed list
                        st.session_state.processed_files.append(pdf_file.name)
                        st.toast(f"Successfully indexed: {pdf_file.name}")
                    except Exception as e:
                        st.error(f"Error processing {pdf_file.name}: {str(e)}")
                
                st.success("New documents processed!")
                # Force refresh to update stats
                st.rerun()
    st.markdown("---")
    st.subheader("⚙️ Database Operations")
    
    # Show active files
    active_stats = vectorstore.get_stats()
    st.write(f"**Total Documents Indexed:** {active_stats['files']}")
    st.write(f"**Total Chunks in DB:** {active_stats['chunks']}")
    
    if active_stats["files"] > 0:
        with st.expander("Show Indexed Files"):
            for fname in active_stats["filenames"]:
                st.markdown(f"- `{fname}`")
                
    if st.button("🗑️ Reset Vector Database", type="secondary", use_container_width=True):
        vectorstore.clear_db()
        st.session_state.processed_files = []
        st.session_state.messages = []
        st.success("Database and chat history cleared!")
        st.rerun()
# Main Application Banner
st.markdown("""
<div class="banner">
    <h1>StartupPilotAI</h1>
    <p>Context-aware Startup Advisor & Document Analysis Portal</p>
</div>
""", unsafe_allow_html=True)
# Setting up main Tabs
tab1, tab2, tab3 = st.tabs(["💬 RAG Chat Assistant", "💡 Startup Advisor", "📊 Analytics Dashboard"])
# ----------------- TAB 1: CHAT ASSISTANT -----------------
with tab1:
    st.subheader("Chat with your Knowledge Base")
    st.write("Ask any questions regarding compliance, roadmaps, funding, or policies in your uploaded PDFs. StartupPilotAI will retrieve exact segments and cite sources.")
    # Render Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Show citations if present
            if "citations" in message and message["citations"]:
                with st.expander("🔍 Citations & Page References"):
                    for idx, cite in enumerate(message["citations"]):
                        st.markdown(f"""
                        <div class="citation-box">
                            <div class="citation-header">Source {idx+1}: {cite['source']} (Page {cite['page']}) | Similarity Score: {cite['score']:.2f}</div>
                            <div class="citation-text">"...{cite['text']}..."</div>
                        </div>
                        """, unsafe_allow_html=True)
    # Chat Input
    if user_prompt := st.chat_input("What would you like to know about the documents?"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        # Process assistant response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing papers and generating answers..."):
                # Pass past history (excluding citations)
                formatted_history = [(msg["role"], msg["content"]) for msg in st.session_state.messages[:-1]]
                
                # Fetch output and sources from RAG
                api_key = st.session_state.get("api_key")
                answer, citations = ask_rag(
                    user_prompt,
                    history=formatted_history,
                    api_key=api_key,
                    n_results=4
                )
                
                st.markdown(answer)
                
                # Display Citation Highlight expander
                if citations:
                    with st.expander("🔍 Citations & Page References"):
                        for idx, cite in enumerate(citations):
                            st.markdown(f"""
                            <div class="citation-box">
                                <div class="citation-header">Source {idx+1}: {cite['source']} (Page {cite['page']}) | Similarity Score: {cite['score']:.2f}</div>
                                <div class="citation-text">"...{cite['text']}..."</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
            # Add assistant message to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "citations": citations
            })
# ----------------- TAB 2: STARTUP ADVISOR -----------------
with tab2:
    st.subheader("Startup Advisor Suite")
    st.write("Generate specialized reports based on your custom files and startup objectives.")
    
    advisor_type = st.selectbox(
        "Choose Advisor Utility",
        [
            "Startup Readiness Assessment", 
            "Funding Schemes Recommendation", 
            "Personalized Launch Roadmap", 
            "Legal & Agreement Simplifier"
        ]
    )
    
    st.markdown("---")
    
    api_key = st.session_state.get("api_key")
    
    # Sub-tab: Startup Readiness Assessment
    if advisor_type == "Startup Readiness Assessment":
        st.markdown("### 📋 Startup Readiness Audit")
        st.write("Analyzes all documents in the vector database to evaluate registration, legal milestones, product validity, and overall readiness score.")
        
        if active_stats["files"] == 0:
            st.warning("Please upload startup guidelines or business materials to the Knowledge Base first.")
        else:
            if st.button("Run Readiness Audit", type="primary"):
                with st.spinner("Analyzing operational documents..."):
                    assessment, citations = generate_readiness_assessment(api_key=api_key)
                    
                    # Parse score for a beautiful visualization
                    score = 50
                    score_match = re.search(r'Score:\s*(\d+)%', assessment, re.IGNORECASE)
                    if not score_match:
                        score_match = re.search(r'(\d+)%', assessment)
                    if score_match:
                        score = int(score_match.group(1))
                    
                    # Score indicator
                    col_m1, col_m2 = st.columns([1, 4])
                    with col_m1:
                        st.metric("Readiness Rating", f"{score}%")
                    with col_m2:
                        st.write("Audit Completion Progress:")
                        st.progress(score / 100)
                        
                    st.markdown("---")
                    st.markdown(assessment)
                    
                    if citations:
                        with st.expander("📄 Context Document Reference"):
                            for c in citations:
                                st.markdown(f"- **{c['source']}** (Page {c['page']})")
    # Sub-tab: Funding Recommendations
    elif advisor_type == "Funding Schemes Recommendation":
        st.markdown("### 💰 Funding Scheme Recommender")
        st.write("Configure your profile below to search matching funding opportunities and structure your fundraising plan.")
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            stage_sel = st.selectbox(
                "Operational Stage",
                ["Ideation / Pre-Seed", "MVP Finished / Seed", "Early Traction / Pre-Series A", "Growth / Series A+"]
            )
            industry_input = st.text_input("Industry Vertical", placeholder="e.g. SaaS, AgriTech, FinTech, EdTech")
        with col_f2:
            target_amount = st.text_input("Funding Target Amount", placeholder="e.g. $150,000 / ₹50 Lakhs")
            
        if st.button("Fetch Funding Advisory", type="primary"):
            if not industry_input or not target_amount:
                st.warning("Please enter your startup's industry vertical and target funding amount.")
            else:
                with st.spinner("Matching schemes and guidelines..."):
                    funding_resp, citations = generate_funding_recommendations(
                        stage=stage_sel,
                        industry=industry_input,
                        funding_amount=target_amount,
                        api_key=api_key
                    )
                    st.markdown(funding_resp)
                    
                    if citations:
                        with st.expander("📄 Context Document Reference"):
                            for c in citations:
                                st.markdown(f"- **{c['source']}** (Page {c['page']})")
    # Sub-tab: Personalized Launch Roadmap
    elif advisor_type == "Personalized Launch Roadmap":
        st.markdown("### 🗺️ Milestone Roadmap Generator")
        st.write("Specify your core operational targets and targets for the next 12 months, and we will formulate a phase-by-phase roadmap using regulatory and guidebook compliance.")
        
        goals_input = st.text_area(
            "Primary Milestone Targets",
            placeholder="e.g. Set up incorporating legal entity, complete MVP testing, and hire a lead developer in the next 6 months."
        )
        
        if st.button("Generate Timeline Roadmap", type="primary"):
            if not goals_input:
                st.warning("Please write your target milestones/goals.")
            else:
                with st.spinner("Structuring operational phases..."):
                    roadmap_resp, citations = generate_custom_roadmap(goals=goals_input, api_key=api_key)
                    st.markdown(roadmap_resp)
                    
                    if citations:
                        with st.expander("📄 Context Document Reference"):
                            for c in citations:
                                st.markdown(f"- **{c['source']}** (Page {c['page']})")
    # Sub-tab: Legal & Agreement Simplifier
    elif advisor_type == "Legal & Agreement Simplifier":
        st.markdown("### ⚖️ Legal Clause Simplifier")
        st.write("Paste complex legalese, contract clauses, SLA, or term sheets below. The advisor will simplify obligations, detect red flags, and advise negotiate parameters.")
        
        clause_input = st.text_area(
            "Paste Legal Clause / Text Here",
            height=200,
            placeholder="e.g. 'The Company agrees to indemnify and hold harmless the investor from and against any and all claims, liabilities, losses...'"
        )
        
        if st.button("Deconstruct Legalese", type="primary"):
            if not clause_input:
                st.warning("Please paste some legal text.")
            else:
                with st.spinner("Deconstructing legal parameters..."):
                    simplified_resp, _ = simplify_legal_text(legal_text=clause_input, api_key=api_key)
                    st.markdown(simplified_resp)
# ----------------- TAB 3: ANALYTICS DASHBOARD -----------------
with tab3:
    st.subheader("Knowledge Analytics Dashboard")
    st.write("Visual stats regarding your document indexing, chunk details, and content distributions.")
    
    if active_stats["chunks"] == 0:
        st.info("No documents uploaded yet. Upload a PDF in the sidebar to populate the dashboard metrics!")
    else:
        # Multi-column metrics card
        col_an1, col_an2, col_an3 = st.columns(3)
        with col_an1:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Uploaded Documents</div>
                <div class="metric-num">{active_stats['files']}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_an2:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Database Chunks</div>
                <div class="metric-num">{active_stats['chunks']}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_an3:
            # Estimate word count based on 800 chars/chunk
            approx_words = int((active_stats['chunks'] * 800) / 5)
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Approximate Word Count</div>
                <div class="metric-num">{approx_words:,}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        
        # Document distribution chart
        st.subheader("📊 Document Chunk Distributions")
        st.write("Number of vector chunks generated per PDF document.")
        
        file_counts = active_stats.get("file_counts", {})
        if file_counts:
            # Create a dataframe for plotting
            chart_df = pd.DataFrame(list(file_counts.items()), columns=["Document", "Chunks"])
            st.bar_chart(chart_df.set_index("Document"))
            
            # Show detailed tabular listing
            st.subheader("📋 Document Registry Details")
            table_df = pd.DataFrame([
                {
                    "Document Name": k,
                    "Total Chunks": v,
                    "Approx. Page Count": len(set([
                        # Fetch and filter pages for this file if needed, or estimate
                        v // 2 + 1 
                    ]))
                }
                for k, v in file_counts.items()
            ])
            st.dataframe(table_df, use_container_width=True)
        else:
            st.write("No distribution data available.")