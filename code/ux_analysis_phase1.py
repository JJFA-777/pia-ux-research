import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

def setup_matplotlib_for_plotting():
    """
    Setup matplotlib and seaborn for plotting with proper configuration.
    Call this function before creating any plots to ensure proper rendering.
    """
    warnings.filterwarnings('default')  # Show all warnings
    
    # Configure matplotlib for non-interactive mode
    plt.switch_backend("Agg")
    
    # Set chart style
    plt.style.use("seaborn-v0_8")
    sns.set_palette("husl")
    
    # Configure platform-appropriate fonts for cross-platform compatibility
    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Zen Hei", "PingFang SC", "Arial Unicode MS", "Hiragino Sans GB"]
    plt.rcParams["axes.unicode_minus"] = False

# Initialize matplotlib
setup_matplotlib_for_plotting()

# Phase 1: Extract key UX insights from existing analyses
print("=== Phase 1: Foundation Analysis ===")
print("Extracting UX insights from existing analyses...")

# Key UX insights from PIA Document Analysis
document_insights = {
    "structural_complexity": {
        "total_sections": 319,
        "chapters": 4,
        "cross_references": "Extensive - over 319 numbered sections creating interconnected framework",
        "document_length": "11,717 lines",
        "primary_challenge": "Complex cross-reference architecture may create navigation difficulties"
    },
    "stakeholder_entities": {
        "regulatory_bodies": 3,  # NNPC, NURC, NMDPRA
        "document_mentions": {
            "NURC": 684,  # Highest frequency
            "NMDPRA": 678,
            "NNPC": 135,
            "Ministry": 121
        },
        "ux_implication": "High mention frequency suggests these entities are central to user workflows"
    },
    "host_community_framework": {
        "dedicated_sections": 24,  # Chapter 3
        "governance_levels": 3,  # Board of Trustees, Management Committee, Advisory Committee
        "funding_allocation": "3% of operating expenditure",
        "ux_challenge": "Multi-tiered governance may create complexity for community stakeholders"
    }
}

# Key UX insights from Stakeholder Mapping
stakeholder_insights = {
    "primary_stakeholder_categories": 5,
    "government_regulators": {
        "entities": ["Minister", "NURC", "NMDPRA", "NNPC Limited"],
        "complexity_level": "High - multiple overlapping jurisdictions",
        "ux_challenge": "Users must navigate between multiple regulatory authorities"
    },
    "oil_gas_companies": {
        "license_types": ["Petroleum Prospecting Licence", "Petroleum Mining Lease"],
        "compliance_areas": ["Technical", "Social", "Environmental", "Reporting"],
        "ux_challenge": "Complex multi-stage licensing and compliance requirements"
    },
    "host_communities": {
        "trust_structure": "3-tier governance model",
        "participation_mechanisms": "Multi-level democratic representation",
        "ux_challenge": "Community members need to understand complex governance structures"
    },
    "transparency_mechanisms": {
        "public_registers": "Required for NURC and NMDPRA",
        "information_disclosure": "Mandatory publication of non-proprietary information",
        "ux_opportunity": "Digital platforms could enhance accessibility"
    }
}

# Key UX insights from International Benchmarking
international_insights = {
    "transparency_best_practices": {
        "norway_equinor": "Comprehensive disclosure, EITI participation, zero corruption tolerance",
        "brazil_anp": "Online board meetings, public hearings, extensive databases",
        "ux_benchmark": "High transparency standards require user-friendly digital interfaces"
    },
    "governance_models": {
        "norway": "Sophisticated governance with 10 core principles",
        "brazil": "Comprehensive regulatory architecture with ANP",
        "ux_lesson": "Clear governance structures support better user understanding"
    },
    "community_engagement": {
        "norway_local_content": "Systematic training, technology transfer, long-term capacity building",
        "ux_insight": "Successful community engagement requires accessible training and information"
    }
}

print("✓ Key UX insights extracted from all three analyses")
print(f"✓ Identified {len(document_insights)} document complexity factors")
print(f"✓ Mapped {stakeholder_insights['primary_stakeholder_categories']} primary stakeholder categories")
print(f"✓ Analyzed {len(international_insights)} international best practice areas")

# Phase 1 completion - save insights for further analysis
analysis_data = {
    "document_insights": document_insights,
    "stakeholder_insights": stakeholder_insights,
    "international_insights": international_insights,
    "analysis_timestamp": "2025-10-01 20:13:03"
}

with open('/workspace/data/ux_insights_extracted.json', 'w') as f:
    json.dump(analysis_data, f, indent=2)

print("\n=== Phase 1 Complete ===")
print("UX insights extracted and saved to data/ux_insights_extracted.json")
print("Ready to proceed to Phase 2: Stakeholder-Centric UX Analysis")