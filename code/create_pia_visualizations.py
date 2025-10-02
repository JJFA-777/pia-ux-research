"""
Stakeholder Impact Visualization for Nigerian PIA 2021
Creates visual representations of stakeholder relationships and impact flows
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx
from matplotlib.patches import FancyBboxPatch, Circle
import seaborn as sns

def setup_matplotlib_for_plotting():
    """
    Setup matplotlib and seaborn for plotting with proper configuration.
    Call this function before creating any plots to ensure proper rendering.
    """
    import warnings
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Ensure warnings are printed
    warnings.filterwarnings('default')  # Show all warnings

    # Configure matplotlib for non-interactive mode
    plt.switch_backend("Agg")

    # Set chart style
    plt.style.use("seaborn-v0_8")
    sns.set_palette("husl")

    # Configure platform-appropriate fonts for cross-platform compatibility
    # Must be set after style.use, otherwise will be overridden by style configuration
    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Zen Hei", "PingFang SC", "Arial Unicode MS", "Hiragino Sans GB"]
    plt.rcParams["axes.unicode_minus"] = False

def create_stakeholder_impact_map():
    """Create a network visualization of stakeholder relationships and impacts"""
    setup_matplotlib_for_plotting()
    
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    
    # Define stakeholder categories and their positions
    stakeholders = {
        'NUPRC': {'pos': (0, 0), 'category': 'Regulator', 'size': 2000, 'color': '#2E86AB'},
        'NMDPRA': {'pos': (0, -2), 'category': 'Regulator', 'size': 2000, 'color': '#2E86AB'},
        'Minister': {'pos': (0, 2), 'category': 'Government', 'size': 1800, 'color': '#A23B72'},
        'NNPC Limited': {'pos': (2, 0), 'category': 'NOC', 'size': 1600, 'color': '#F18F01'},
        'IOCs': {'pos': (4, 1), 'category': 'Industry', 'size': 1400, 'color': '#C73E1D'},
        'Host Communities': {'pos': (-4, 0), 'category': 'Community', 'size': 1400, 'color': '#6A994E'},
        'Development Trusts': {'pos': (-4, -2), 'category': 'Community', 'size': 1200, 'color': '#6A994E'},
        'Civil Society': {'pos': (-2, 3), 'category': 'Public', 'size': 1000, 'color': '#BC6C25'},
        'International Partners': {'pos': (2, -3), 'category': 'External', 'size': 1000, 'color': '#8B5A3C'}
    }
    
    # Define impact relationships with weights
    relationships = [
        ('Minister', 'NUPRC', 0.9, 'Policy Direction'),
        ('Minister', 'NMDPRA', 0.9, 'Policy Direction'),
        ('NUPRC', 'IOCs', 0.8, 'Licensing & Oversight'),
        ('NMDPRA', 'IOCs', 0.7, 'Operations Regulation'),
        ('IOCs', 'Host Communities', 0.8, 'Operations Impact'),
        ('IOCs', 'Development Trusts', 0.9, 'Funding (3% OpEx)'),
        ('Development Trusts', 'Host Communities', 0.9, 'Development Projects'),
        ('NNPC Limited', 'Host Communities', 0.6, 'Frontier Fund (30%)'),
        ('Civil Society', 'NUPRC', 0.5, 'Transparency Oversight'),
        ('Civil Society', 'NMDPRA', 0.5, 'Transparency Oversight'),
        ('International Partners', 'IOCs', 0.6, 'Investment & Standards')
    ]
    
    # Plot stakeholders
    for name, data in stakeholders.items():
        x, y = data['pos']
        ax.scatter(x, y, s=data['size'], c=data['color'], alpha=0.7, edgecolors='white', linewidth=2)
        ax.annotate(name, (x, y), xytext=(5, 5), textcoords='offset points', 
                   fontsize=10, fontweight='bold', ha='left')
    
    # Plot relationships
    for source, target, weight, label in relationships:
        x1, y1 = stakeholders[source]['pos']
        x2, y2 = stakeholders[target]['pos']
        
        # Arrow properties based on relationship strength
        arrow_width = weight * 3
        alpha = 0.3 + (weight * 0.4)
        
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', lw=arrow_width, alpha=alpha, color='gray'))
        
        # Add relationship labels
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.annotate(label, (mid_x, mid_y), fontsize=8, ha='center', va='center',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    # Create legend
    categories = {
        'Regulator': '#2E86AB',
        'Government': '#A23B72', 
        'NOC': '#F18F01',
        'Industry': '#C73E1D',
        'Community': '#6A994E',
        'Public': '#BC6C25',
        'External': '#8B5A3C'
    }
    
    legend_elements = [plt.scatter([], [], c=color, s=100, label=category, alpha=0.7) 
                      for category, color in categories.items()]
    ax.legend(handles=legend_elements, loc='upper right', title='Stakeholder Categories')
    
    # Formatting
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 4)
    ax.set_title('Nigerian PIA 2021: Stakeholder Impact Mapping\nRelationships and Influence Flows', 
                fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig('/workspace/charts/stakeholder_impact_map.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_process_flowchart():
    """Create a simplified process flowchart visualization"""
    setup_matplotlib_for_plotting()
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Define process steps
    steps = [
        {'name': 'Application\nSubmission', 'pos': (1, 5), 'type': 'start'},
        {'name': 'Technical\nEvaluation', 'pos': (3, 5), 'type': 'process'},
        {'name': 'Community\nConsultation', 'pos': (5, 5), 'type': 'process'},
        {'name': 'Financial\nAssessment', 'pos': (3, 3), 'type': 'process'},
        {'name': 'Environmental\nReview', 'pos': (5, 3), 'type': 'process'},
        {'name': 'License\nApproval', 'pos': (7, 4), 'type': 'decision'},
        {'name': 'Operations\nCommencement', 'pos': (9, 4), 'type': 'end'},
        {'name': 'Trust\nEstablishment', 'pos': (9, 2), 'type': 'process'},
        {'name': 'Community\nDevelopment', 'pos': (9, 1), 'type': 'ongoing'}
    ]
    
    # Color coding by step type
    colors = {
        'start': '#6A994E',
        'process': '#2E86AB', 
        'decision': '#F18F01',
        'end': '#C73E1D',
        'ongoing': '#A23B72'
    }
    
    # Plot process steps
    for step in steps:
        x, y = step['pos']
        color = colors[step['type']]
        
        if step['type'] == 'decision':
            # Diamond shape for decision points
            bbox = dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.7, edgecolor='white', linewidth=2)
        else:
            # Rectangle for other steps
            bbox = dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.7, edgecolor='white', linewidth=2)
        
        ax.text(x, y, step['name'], ha='center', va='center', fontsize=10, fontweight='bold',
               bbox=bbox, color='white')
    
    # Define flow connections
    flows = [
        ((1, 5), (3, 5)),  # Application to Technical
        ((3, 5), (5, 5)),  # Technical to Community
        ((3, 5), (3, 3)),  # Technical to Financial
        ((5, 5), (5, 3)),  # Community to Environmental
        ((3, 3), (7, 4)),  # Financial to Approval
        ((5, 3), (7, 4)),  # Environmental to Approval
        ((5, 5), (7, 4)),  # Community to Approval
        ((7, 4), (9, 4)),  # Approval to Operations
        ((9, 4), (9, 2)),  # Operations to Trust
        ((9, 2), (9, 1))   # Trust to Development
    ]
    
    # Draw flow arrows
    for start, end in flows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=2, color='gray', alpha=0.7))
    
    # Add timeline indicators
    phases = [
        {'name': 'Pre-Application\n(6-12 months)', 'pos': (2, 6.5), 'color': '#BC6C25'},
        {'name': 'Evaluation\n(6-9 months)', 'pos': (4.5, 6.5), 'color': '#BC6C25'},
        {'name': 'Implementation\n(Ongoing)', 'pos': (8, 6.5), 'color': '#BC6C25'}
    ]
    
    for phase in phases:
        x, y = phase['pos']
        ax.text(x, y, phase['name'], ha='center', va='center', fontsize=9,
               bbox=dict(boxstyle='round,pad=0.3', facecolor=phase['color'], alpha=0.3))
    
    # Create legend
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, facecolor=colors['start'], alpha=0.7, label='Start/Input'),
        plt.Rectangle((0, 0), 1, 1, facecolor=colors['process'], alpha=0.7, label='Process/Review'),
        plt.Rectangle((0, 0), 1, 1, facecolor=colors['decision'], alpha=0.7, label='Decision Point'),
        plt.Rectangle((0, 0), 1, 1, facecolor=colors['end'], alpha=0.7, label='Milestone'),
        plt.Rectangle((0, 0), 1, 1, facecolor=colors['ongoing'], alpha=0.7, label='Ongoing Activity')
    ]
    ax.legend(handles=legend_elements, loc='upper left', title='Process Types')
    
    # Formatting
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title('Nigerian PIA 2021: Petroleum Licensing Process Flow\nFrom Application to Community Development', 
                fontsize=14, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('/workspace/charts/process_flowchart.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_compliance_dashboard_mockup():
    """Create a mockup of compliance dashboard metrics"""
    setup_matplotlib_for_plotting()
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Dashboard 1: Compliance Rates by Category
    categories = ['Technical\nCompliance', 'Financial\nCompliance', 'Environmental\nCompliance', 
                 'Community\nEngagement', 'Safety\nStandards']
    rates = [87, 92, 78, 85, 90]
    colors = ['#2E86AB', '#6A994E', '#F18F01', '#C73E1D', '#A23B72']
    
    bars = ax1.bar(categories, rates, color=colors, alpha=0.7)
    ax1.set_ylim(0, 100)
    ax1.set_ylabel('Compliance Rate (%)')
    ax1.set_title('Operator Compliance Rates by Category', fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar, rate in zip(bars, rates):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                f'{rate}%', ha='center', va='bottom', fontweight='bold')
    
    # Dashboard 2: License Status Distribution
    status_labels = ['Active', 'Under Review', 'Suspended', 'Pending Renewal']
    status_counts = [145, 23, 5, 18]
    status_colors = ['#6A994E', '#F18F01', '#C73E1D', '#2E86AB']
    
    wedges, texts, autotexts = ax2.pie(status_counts, labels=status_labels, colors=status_colors, 
                                      autopct='%1.1f%%', startangle=90)
    ax2.set_title('License Status Distribution\n(Total: 191 Licenses)', fontweight='bold')
    
    # Dashboard 3: Revenue Collection Trends
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    royalties = [45, 52, 48, 55, 58, 62]
    taxes = [120, 135, 128, 142, 148, 155]
    
    ax3.plot(months, royalties, marker='o', linewidth=3, label='Royalties', color='#2E86AB')
    ax3.plot(months, taxes, marker='s', linewidth=3, label='Taxes', color='#6A994E')
    ax3.set_ylabel('Revenue (₦ Billions)')
    ax3.set_title('Monthly Revenue Collection Trends', fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Dashboard 4: Community Development Projects
    project_types = ['Education', 'Healthcare', 'Infrastructure', 'Economic\nEmpowerment', 'Environment']
    completed = [12, 8, 15, 6, 4]
    ongoing = [8, 5, 12, 9, 3]
    
    x = np.arange(len(project_types))
    width = 0.35
    
    ax4.bar(x - width/2, completed, width, label='Completed', color='#6A994E', alpha=0.7)
    ax4.bar(x + width/2, ongoing, width, label='Ongoing', color='#F18F01', alpha=0.7)
    
    ax4.set_xlabel('Project Types')
    ax4.set_ylabel('Number of Projects')
    ax4.set_title('Community Development Projects Status', fontweight='bold')
    ax4.set_xticks(x)
    ax4.set_xticklabels(project_types)
    ax4.legend()
    ax4.grid(axis='y', alpha=0.3)
    
    plt.suptitle('Nigerian PIA 2021: Compliance Monitoring Dashboard', 
                fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('/workspace/charts/compliance_dashboard_mockup.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_international_comparison():
    """Create international best practices comparison chart"""
    setup_matplotlib_for_plotting()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Governance Effectiveness Comparison
    countries = ['Norway', 'Brazil', 'Nigeria\n(Pre-PIA)', 'Nigeria\n(Post-PIA\nProjected)']
    
    # Metrics: Regulatory Independence, Transparency, Community Engagement, Fiscal Efficiency
    governance_data = {
        'Regulatory Independence': [9.2, 7.5, 4.2, 7.8],
        'Transparency': [9.5, 6.8, 3.5, 7.5],
        'Community Engagement': [8.8, 6.2, 2.8, 8.0],
        'Fiscal Efficiency': [9.0, 7.2, 5.5, 8.2]
    }
    
    x = np.arange(len(countries))
    width = 0.2
    multiplier = 0
    
    colors = ['#2E86AB', '#6A994E', '#F18F01', '#C73E1D']
    
    for attribute, measurement in governance_data.items():
        offset = width * multiplier
        bars = ax1.bar(x + offset, measurement, width, label=attribute, color=colors[multiplier], alpha=0.7)
        multiplier += 1
    
    ax1.set_xlabel('Countries')
    ax1.set_ylabel('Governance Score (0-10)')
    ax1.set_title('Petroleum Governance Effectiveness Comparison', fontweight='bold')
    ax1.set_xticks(x + width * 1.5)
    ax1.set_xticklabels(countries)
    ax1.legend(loc='upper left')
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_ylim(0, 10)
    
    # Community Development Funding Comparison
    countries_2 = ['Norway\n(Local Content)', 'Brazil\n(ANP Requirements)', 'Nigeria PIA\n(3% OpEx + 30% Profit)']
    funding_levels = [8.5, 6.2, 8.8]  # Relative effectiveness scores
    colors_2 = ['#2E86AB', '#6A994E', '#A23B72']
    
    bars2 = ax2.bar(countries_2, funding_levels, color=colors_2, alpha=0.7)
    ax2.set_ylabel('Community Benefit Score (0-10)')
    ax2.set_title('Community Development Framework Comparison', fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    ax2.set_ylim(0, 10)
    
    # Add value labels
    for bar, value in zip(bars2, funding_levels):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{value}', ha='center', va='bottom', fontweight='bold')
    
    # Add annotations
    ax2.text(0, 7, 'Advanced local\ncontent policies', ha='center', va='bottom', 
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.7))
    ax2.text(1, 5, 'Moderate\nrequirements', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))
    ax2.text(2, 7.5, 'Comprehensive\ntrust framework', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightcoral', alpha=0.7))
    
    plt.suptitle('Nigeria PIA 2021: International Best Practices Comparison', 
                fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/workspace/charts/international_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_user_journey_visualization():
    """Create user journey mapping for different stakeholders"""
    setup_matplotlib_for_plotting()
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 12))
    
    # Oil Company Journey
    company_journey = [
        'License\nApplication', 'Technical\nReview', 'Community\nConsultation', 
        'Approval &\nLicense Award', 'Operations\nSetup', 'Production\n& Compliance',
        'Trust Fund\nContribution', 'Ongoing\nReporting'
    ]
    company_timeline = list(range(len(company_journey)))
    
    ax1.plot(company_timeline, [1]*len(company_timeline), 'o-', linewidth=3, 
            markersize=10, color='#2E86AB', alpha=0.7)
    
    for i, (step, time) in enumerate(zip(company_journey, company_timeline)):
        ax1.annotate(step, (time, 1), xytext=(0, 20), textcoords='offset points',
                    ha='center', va='bottom', fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.7))
    
    ax1.set_xlim(-0.5, len(company_journey)-0.5)
    ax1.set_ylim(0.5, 1.5)
    ax1.set_title('Oil & Gas Company User Journey', fontweight='bold', fontsize=12)
    ax1.set_yticks([])
    ax1.grid(axis='x', alpha=0.3)
    
    # Host Community Journey
    community_journey = [
        'Awareness\n& Education', 'Consultation\nProcess', 'Trust\nEstablishment',
        'Needs\nAssessment', 'Project\nSelection', 'Implementation\nOversight',
        'Monitoring\n& Evaluation', 'Benefit\nRealization'
    ]
    community_timeline = list(range(len(community_journey)))
    
    ax2.plot(community_timeline, [1]*len(community_timeline), 'o-', linewidth=3, 
            markersize=10, color='#6A994E', alpha=0.7)
    
    for i, (step, time) in enumerate(zip(community_journey, community_timeline)):
        ax2.annotate(step, (time, 1), xytext=(0, 20), textcoords='offset points',
                    ha='center', va='bottom', fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))
    
    ax2.set_xlim(-0.5, len(community_journey)-0.5)
    ax2.set_ylim(0.5, 1.5)
    ax2.set_title('Host Community User Journey', fontweight='bold', fontsize=12)
    ax2.set_yticks([])
    ax2.grid(axis='x', alpha=0.3)
    
    # Regulator Journey
    regulator_journey = [
        'Policy\nDevelopment', 'License\nEvaluation', 'Approval\nDecision',
        'Compliance\nMonitoring', 'Enforcement\nAction', 'Revenue\nCollection',
        'Performance\nReview', 'Continuous\nImprovement'
    ]
    regulator_timeline = list(range(len(regulator_journey)))
    
    ax3.plot(regulator_timeline, [1]*len(regulator_timeline), 'o-', linewidth=3, 
            markersize=10, color='#C73E1D', alpha=0.7)
    
    for i, (step, time) in enumerate(zip(regulator_journey, regulator_timeline)):
        ax3.annotate(step, (time, 1), xytext=(0, 20), textcoords='offset points',
                    ha='center', va='bottom', fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightcoral', alpha=0.7))
    
    ax3.set_xlim(-0.5, len(regulator_journey)-0.5)
    ax3.set_ylim(0.5, 1.5)
    ax3.set_title('Regulatory Agency User Journey', fontweight='bold', fontsize=12)
    ax3.set_yticks([])
    ax3.grid(axis='x', alpha=0.3)
    
    plt.suptitle('Stakeholder User Journey Mapping for PIA Digital Platform', 
                fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/workspace/charts/user_journey_mapping.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Create charts directory if it doesn't exist
    import os
    os.makedirs('/workspace/charts', exist_ok=True)
    
    print("Creating stakeholder impact map...")
    create_stakeholder_impact_map()
    
    print("Creating process flowchart...")
    create_process_flowchart()
    
    print("Creating compliance dashboard mockup...")
    create_compliance_dashboard_mockup()
    
    print("Creating international comparison...")
    create_international_comparison()
    
    print("Creating user journey visualization...")
    create_user_journey_visualization()
    
    print("All visualizations created successfully!")
    print("Charts saved to /workspace/charts/")