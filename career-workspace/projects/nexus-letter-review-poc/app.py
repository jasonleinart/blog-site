import streamlit as st
import openai
import json
from datetime import datetime
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Nexus Letter AI Review System",
    page_icon="⚖️",
    layout="wide"
)

# Initialize session state
if 'reviews' not in st.session_state:
    st.session_state.reviews = []

def analyze_nexus_letter(letter_text):
    """Analyze nexus letter using OpenAI GPT-4"""
    
    prompt = f"""
    You are an expert legal assistant specializing in VA disability nexus letters. 
    Analyze the following nexus letter and provide a detailed review.
    
    NEXUS LETTER TEXT:
    {letter_text}
    
    Please evaluate the letter on these criteria and provide scores (0-20 for each):
    
    1. MEDICAL DIAGNOSIS (0-20): Is there a clear, specific diagnosis?
    2. CAUSATION STATEMENT (0-20): Does it establish connection to military service?
    3. MEDICAL RATIONALE (0-20): Is there sufficient medical reasoning?
    4. VA COMPLIANCE (0-15): Does it include required VA language?
    5. PROFESSIONAL TONE (0-20): Is the tone appropriate and professional?
    6. FORMATTING (0-5): Is the letter properly formatted?
    
    Respond in JSON format:
    {{
        "overall_score": [total score out of 100],
        "medical_diagnosis": {{
            "score": [0-20],
            "status": "pass/warning/fail",
            "comments": "specific feedback"
        }},
        "causation_statement": {{
            "score": [0-20],
            "status": "pass/warning/fail", 
            "comments": "specific feedback"
        }},
        "medical_rationale": {{
            "score": [0-20],
            "status": "pass/warning/fail",
            "comments": "specific feedback"
        }},
        "va_compliance": {{
            "score": [0-15],
            "status": "pass/warning/fail",
            "comments": "specific feedback"
        }},
        "professional_tone": {{
            "score": [0-20],
            "status": "pass/warning/fail",
            "comments": "specific feedback"
        }},
        "formatting": {{
            "score": [0-5],
            "status": "pass/warning/fail",
            "comments": "specific feedback"
        }},
        "recommendations": [
            "List of specific improvements",
            "Another recommendation"
        ],
        "risk_level": "low/medium/high",
        "approval_recommendation": "auto-approve/attorney-review/revision-required"
    }}
    """
    
    try:
        # Note: In production, you'd use actual OpenAI API
        # For demo purposes, return mock analysis
        return {
            "overall_score": 78,
            "medical_diagnosis": {
                "score": 18,
                "status": "pass",
                "comments": "Clear PTSD diagnosis with DSM-5 criteria referenced"
            },
            "causation_statement": {
                "score": 14,
                "status": "warning", 
                "comments": "Connection to service mentioned but could be stronger"
            },
            "medical_rationale": {
                "score": 16,
                "status": "pass",
                "comments": "Good medical reasoning with symptom correlation"
            },
            "va_compliance": {
                "score": 8,
                "status": "fail",
                "comments": "Missing required 'more likely than not' language"
            },
            "professional_tone": {
                "score": 17,
                "status": "pass",
                "comments": "Professional and appropriate medical language"
            },
            "formatting": {
                "score": 5,
                "status": "pass",
                "comments": "Proper business letter format"
            },
            "recommendations": [
                "Add 'more likely than not' language for VA compliance",
                "Strengthen causation statement with specific service events",
                "Include medical literature references if available"
            ],
            "risk_level": "medium",
            "approval_recommendation": "attorney-review"
        }
    except Exception as e:
        st.error(f"Analysis error: {str(e)}")
        return None

def main():
    st.title("⚖️ Nexus Letter AI Review System")
    st.markdown("*Proof of Concept for Disability Law Group*")
    
    # Sidebar
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Choose Function", [
        "Document Review", 
        "Review History", 
        "Chatbot Assistant",
        "System Analytics"
    ])
    
    if page == "Document Review":
        st.header("📄 Document Analysis")
        
        # Sample letters for demo
        sample_letters = {
            "Select a sample...": "",
            "PTSD Nexus Letter (Good)": """
            [Date]
            
            To Whom It May Concern:
            
            I am writing this nexus letter regarding [Veteran Name], DOB: [Date], SSN: [XXX-XX-XXXX].
            
            DIAGNOSIS: Post-Traumatic Stress Disorder (PTSD), DSM-5 309.81
            
            MEDICAL HISTORY: The veteran served in Iraq from 2003-2004 and experienced multiple combat situations including IED explosions and direct fire. He reports persistent nightmares, hypervigilance, and avoidance behaviors since returning from deployment.
            
            MEDICAL OPINION: Based on my examination and review of military records, it is my medical opinion that the veteran's PTSD is more likely than not related to his military service in Iraq. The temporal relationship between combat exposure and symptom onset supports this connection.
            
            RATIONALE: Combat exposure is a well-established risk factor for PTSD development. The veteran's symptoms are consistent with trauma exposure during military service.
            
            Sincerely,
            Dr. [Name], MD
            """,
            "Incomplete Letter (Needs Work)": """
            [Date]
            
            To Whom It May Concern:
            
            I examined [Veteran Name] and found he has PTSD. He was in the military and now has symptoms.
            
            I think his military service caused his PTSD.
            
            Dr. [Name]
            """
        }
        
        # Letter input
        col1, col2 = st.columns([2, 1])
        
        with col1:
            selected_sample = st.selectbox("Choose sample letter:", list(sample_letters.keys()))
            
            if selected_sample != "Select a sample...":
                letter_text = st.text_area(
                    "Nexus Letter Content:", 
                    value=sample_letters[selected_sample],
                    height=300
                )
            else:
                letter_text = st.text_area("Nexus Letter Content:", height=300)
        
        with col2:
            st.markdown("### Quick Info")
            st.info("**Nexus Letters** establish medical connections between military service and current disabilities for VA claims.")
            
            st.markdown("**Key Elements:**")
            st.markdown("- Clear diagnosis")
            st.markdown("- Service connection")
            st.markdown("- Medical rationale") 
            st.markdown("- VA compliance language")
        
        # Analysis button
        if st.button("🔍 Analyze Letter", type="primary"):
            if letter_text.strip():
                with st.spinner("Analyzing letter..."):
                    analysis = analyze_nexus_letter(letter_text)
                
                if analysis:
                    # Overall score
                    score = analysis['overall_score']
                    if score >= 85:
                        score_color = "green"
                        status = "✅ EXCELLENT"
                    elif score >= 70:
                        score_color = "orange" 
                        status = "⚠️ GOOD"
                    else:
                        score_color = "red"
                        status = "❌ NEEDS WORK"
                    
                    st.markdown(f"## Overall Score: <span style='color:{score_color}'>{score}/100 {status}</span>", unsafe_allow_html=True)
                    
                    # Detailed breakdown
                    st.subheader("📊 Detailed Analysis")
                    
                    criteria = [
                        ("Medical Diagnosis", analysis['medical_diagnosis']),
                        ("Causation Statement", analysis['causation_statement']),
                        ("Medical Rationale", analysis['medical_rationale']),
                        ("VA Compliance", analysis['va_compliance']),
                        ("Professional Tone", analysis['professional_tone']),
                        ("Formatting", analysis['formatting'])
                    ]
                    
                    for criterion, data in criteria:
                        status_icon = {"pass": "✅", "warning": "⚠️", "fail": "❌"}[data['status']]
                        st.markdown(f"**{criterion}**: {status_icon} {data['score']}/20 - {data['comments']}")
                    
                    # Recommendations
                    st.subheader("💡 Recommendations")
                    for rec in analysis['recommendations']:
                        st.markdown(f"• {rec}")
                    
                    # Risk assessment
                    risk_colors = {"low": "green", "medium": "orange", "high": "red"}
                    st.markdown(f"**Risk Level**: <span style='color:{risk_colors[analysis['risk_level']]}'>{analysis['risk_level'].upper()}</span>", unsafe_allow_html=True)
                    
                    # Approval recommendation
                    approval_rec = analysis['approval_recommendation']
                    if approval_rec == "auto-approve":
                        st.success("✅ Recommended for AUTO-APPROVAL")
                    elif approval_rec == "attorney-review":
                        st.warning("⚠️ Recommended for ATTORNEY REVIEW")
                    else:
                        st.error("❌ REVISION REQUIRED before approval")
                    
                    # Save to history
                    review_record = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "score": score,
                        "status": status,
                        "risk_level": analysis['risk_level'],
                        "recommendation": approval_rec,
                        "letter_preview": letter_text[:100] + "..."
                    }
                    st.session_state.reviews.append(review_record)
            else:
                st.warning("Please enter a nexus letter to analyze.")
    
    elif page == "Review History":
        st.header("📋 Review History")
        
        if st.session_state.reviews:
            df = pd.DataFrame(st.session_state.reviews)
            st.dataframe(df, use_container_width=True)
            
            # Summary stats
            col1, col2, col3 = st.columns(3)
            with col1:
                avg_score = df['score'].mean()
                st.metric("Average Score", f"{avg_score:.1f}/100")
            with col2:
                auto_approve_rate = (df['recommendation'] == 'auto-approve').mean() * 100
                st.metric("Auto-Approval Rate", f"{auto_approve_rate:.1f}%")
            with col3:
                high_risk_rate = (df['risk_level'] == 'high').mean() * 100
                st.metric("High Risk Rate", f"{high_risk_rate:.1f}%")
        else:
            st.info("No reviews completed yet. Analyze some letters to see history here.")
    
    elif page == "Chatbot Assistant":
        st.header("🤖 AI Legal Assistant")
        st.markdown("Ask questions about nexus letter requirements and best practices.")
        
        # Sample questions
        st.markdown("**Try asking:**")
        sample_questions = [
            "What elements are required in a VA nexus letter?",
            "How should I phrase the causation statement?",
            "What does 'more likely than not' mean in VA context?",
            "How do I establish service connection for PTSD?"
        ]
        
        for q in sample_questions:
            if st.button(f"💬 {q}"):
                st.markdown(f"**You asked:** {q}")
                # Mock responses for demo
                responses = {
                    "What elements are required in a VA nexus letter?": "A complete nexus letter should include: 1) Clear diagnosis with DSM-5/ICD-10 codes, 2) Statement of causation linking condition to service, 3) Medical rationale explaining the connection, 4) 'More likely than not' language, 5) Doctor's credentials and signature.",
                    "How should I phrase the causation statement?": "Use definitive language like 'It is my medical opinion that [condition] is more likely than not caused by/aggravated by military service.' Avoid uncertain terms like 'possible' or 'might be related.'",
                    "What does 'more likely than not' mean in VA context?": "'More likely than not' means greater than 50% probability. This is the VA's standard of proof for service connection. The medical opinion must state the connection is at least as likely as not (50% or greater chance).",
                    "How do I establish service connection for PTSD?": "For PTSD service connection, you need: 1) Current PTSD diagnosis, 2) In-service stressor event, 3) Medical nexus linking current PTSD to the stressor. Combat veterans have relaxed stressor requirements under 38 CFR 3.304(f)."
                }
                st.markdown(f"**AI Assistant:** {responses.get(q, 'This is a demo response. In production, this would use GPT-4 to provide detailed legal guidance.')}")
        
        # Custom question input
        user_question = st.text_input("Ask your own question:")
        if user_question:
            st.markdown(f"**You asked:** {user_question}")
            st.markdown("**AI Assistant:** This is a demo response. In production, this would analyze your question and provide specific guidance based on VA regulations and legal best practices.")
    
    elif page == "System Analytics":
        st.header("📈 System Analytics")
        
        # Mock analytics data
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Review Volume")
            chart_data = pd.DataFrame({
                'Date': pd.date_range('2024-01-01', periods=30, freq='D'),
                'Reviews': [15, 23, 18, 31, 25, 19, 27, 22, 29, 33, 28, 24, 30, 26, 21, 35, 29, 32, 27, 23, 31, 28, 25, 33, 30, 26, 29, 31, 27, 24]
            })
            st.line_chart(chart_data.set_index('Date'))
        
        with col2:
            st.subheader("Quality Distribution")
            quality_data = pd.DataFrame({
                'Quality': ['Excellent (85+)', 'Good (70-84)', 'Needs Work (<70)'],
                'Count': [45, 32, 23]
            })
            st.bar_chart(quality_data.set_index('Quality'))
        
        # Key metrics
        st.subheader("Key Performance Indicators")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Time Saved", "75%", "vs manual review")
        with col2:
            st.metric("Consistency Score", "94%", "+12% vs manual")
        with col3:
            st.metric("Attorney Satisfaction", "4.8/5", "+0.6 improvement")
        with col4:
            st.metric("Error Reduction", "68%", "fewer revisions needed")

if __name__ == "__main__":
    main()