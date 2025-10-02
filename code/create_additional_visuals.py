"""
Create an integrated system architecture visualization for PIA visual deliverables
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def setup_matplotlib_for_plotting():
    """Setup matplotlib for non-interactive plotting"""
    import warnings
    warnings.filterwarnings('default')
    plt.switch_backend("Agg")
    plt.style.use("seaborn-v0_8")
    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Zen Hei", "PingFang SC", "Arial Unicode MS", "Hiragino Sans GB"]
    plt.rcParams["axes.unicode_minus"] = False

def create_system_architecture_diagram():
    """Create comprehensive system architecture visualization"""
    setup_matplotlib_for_plotting()
    
    fig, ax = plt.subplots(1, 1, figsize=(18, 14))
    
    # Define color scheme
    colors = {
        'user_layer': '#2E86AB',
        'interface_layer': '#6A994E', 
        'application_layer': '#F18F01',
        'data_layer': '#C73E1D',
        'integration_layer': '#A23B72'
    }
    
    # User Layer (Top)
    user_boxes = [
        {'name': 'Regulators\n(NUPRC/NMDPRA)', 'pos': (2, 11), 'size': (2.5, 1.5)},
        {'name': 'Oil & Gas\nCompanies', 'pos': (5.5, 11), 'size': (2.5, 1.5)},
        {'name': 'Host\nCommunities', 'pos': (9, 11), 'size': (2.5, 1.5)},
        {'name': 'Government\nStakeholders', 'pos': (12.5, 11), 'size': (2.5, 1.5)}
    ]
    
    for box in user_boxes:
        rect = patches.Rectangle(box['pos'], box['size'][0], box['size'][1], 
                               facecolor=colors['user_layer'], alpha=0.7, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(box['pos'][0] + box['size'][0]/2, box['pos'][1] + box['size'][1]/2, 
               box['name'], ha='center', va='center', fontweight='bold', color='white', fontsize=10)
    
    # Interface Layer
    interface_boxes = [
        {'name': 'Compliance\nDashboards', 'pos': (1, 8.5), 'size': (3, 1.2)},
        {'name': 'Interactive\nVisualization', 'pos': (4.5, 8.5), 'size': (3, 1.2)},
        {'name': 'Process\nFlowcharts', 'pos': (8, 8.5), 'size': (3, 1.2)},
        {'name': 'Stakeholder\nPortals', 'pos': (11.5, 8.5), 'size': (3, 1.2)}
    ]
    
    for box in interface_boxes:
        rect = patches.Rectangle(box['pos'], box['size'][0], box['size'][1], 
                               facecolor=colors['interface_layer'], alpha=0.7, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(box['pos'][0] + box['size'][0]/2, box['pos'][1] + box['size'][1]/2, 
               box['name'], ha='center', va='center', fontweight='bold', color='white', fontsize=10)
    
    # Application Layer
    app_boxes = [
        {'name': 'Stakeholder\nImpact Mapping', 'pos': (0.5, 6), 'size': (3.5, 1.2)},
        {'name': 'Compliance\nTracking System', 'pos': (4.5, 6), 'size': (3.5, 1.2)},
        {'name': 'Document\nManagement', 'pos': (8.5, 6), 'size': (3.5, 1.2)},
        {'name': 'Analytics &\nReporting', 'pos': (12.5, 6), 'size': (3.5, 1.2)}
    ]
    
    for box in app_boxes:
        rect = patches.Rectangle(box['pos'], box['size'][0], box['size'][1], 
                               facecolor=colors['application_layer'], alpha=0.7, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(box['pos'][0] + box['size'][0]/2, box['pos'][1] + box['size'][1]/2, 
               box['name'], ha='center', va='center', fontweight='bold', color='white', fontsize=10)
    
    # Data Layer
    data_boxes = [
        {'name': 'PIA Legal\nFramework', 'pos': (1, 3.5), 'size': (3, 1.2)},
        {'name': 'Stakeholder\nData', 'pos': (4.5, 3.5), 'size': (3, 1.2)},
        {'name': 'Compliance\nRecords', 'pos': (8, 3.5), 'size': (3, 1.2)},
        {'name': 'International\nBenchmarks', 'pos': (11.5, 3.5), 'size': (3, 1.2)}
    ]
    
    for box in data_boxes:
        rect = patches.Rectangle(box['pos'], box['size'][0], box['size'][1], 
                               facecolor=colors['data_layer'], alpha=0.7, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(box['pos'][0] + box['size'][0]/2, box['pos'][1] + box['size'][1]/2, 
               box['name'], ha='center', va='center', fontweight='bold', color='white', fontsize=10)
    
    # Integration Layer
    integration_boxes = [
        {'name': 'Government\nSystems', 'pos': (1, 1), 'size': (3, 1.2)},
        {'name': 'Financial\nSystems', 'pos': (4.5, 1), 'size': (3, 1.2)},
        {'name': 'International\nStandards', 'pos': (8, 1), 'size': (3, 1.2)},
        {'name': 'External\nAPIs', 'pos': (11.5, 1), 'size': (3, 1.2)}
    ]
    
    for box in integration_boxes:
        rect = patches.Rectangle(box['pos'], box['size'][0], box['size'][1], 
                               facecolor=colors['integration_layer'], alpha=0.7, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(box['pos'][0] + box['size'][0]/2, box['pos'][1] + box['size'][1]/2, 
               box['name'], ha='center', va='center', fontweight='bold', color='white', fontsize=10)
    
    # Add layer labels
    layer_labels = [
        {'name': 'USER\nLAYER', 'pos': (16.5, 11.75), 'color': colors['user_layer']},
        {'name': 'INTERFACE\nLAYER', 'pos': (16.5, 9.1), 'color': colors['interface_layer']},
        {'name': 'APPLICATION\nLAYER', 'pos': (16.5, 6.6), 'color': colors['application_layer']},
        {'name': 'DATA\nLAYER', 'pos': (16.5, 4.1), 'color': colors['data_layer']},
        {'name': 'INTEGRATION\nLAYER', 'pos': (16.5, 1.6), 'color': colors['integration_layer']}
    ]
    
    for label in layer_labels:
        ax.text(label['pos'][0], label['pos'][1], label['name'], 
               ha='center', va='center', fontweight='bold', fontsize=10,
               bbox=dict(boxstyle='round,pad=0.5', facecolor=label['color'], alpha=0.7, edgecolor='white'))
    
    # Add connecting arrows between layers
    arrow_props = dict(arrowstyle='<->', lw=2, alpha=0.6, color='gray')
    
    # User to Interface
    ax.annotate('', xy=(8, 8.5), xytext=(8, 10.5), arrowprops=arrow_props)
    # Interface to Application
    ax.annotate('', xy=(8, 6), xytext=(8, 8.5), arrowprops=arrow_props)
    # Application to Data
    ax.annotate('', xy=(8, 3.5), xytext=(8, 6), arrowprops=arrow_props)
    # Data to Integration
    ax.annotate('', xy=(8, 1), xytext=(8, 3.5), arrowprops=arrow_props)
    
    # Add key features boxes
    features = [
        {'name': 'Real-time\nMonitoring', 'pos': (0.2, 13.5), 'size': (2, 0.8)},
        {'name': 'Interactive\nNavigation', 'pos': (2.5, 13.5), 'size': (2, 0.8)},
        {'name': 'Multi-stakeholder\nAccess', 'pos': (4.8, 13.5), 'size': (2, 0.8)},
        {'name': 'International\nBenchmarking', 'pos': (7.1, 13.5), 'size': (2, 0.8)},
        {'name': 'Compliance\nAutomation', 'pos': (9.4, 13.5), 'size': (2, 0.8)},
        {'name': 'Transparency\nReporting', 'pos': (11.7, 13.5), 'size': (2, 0.8)},
        {'name': 'Community\nEngagement', 'pos': (14, 13.5), 'size': (2, 0.8)}
    ]
    
    for feature in features:
        rect = patches.Rectangle(feature['pos'], feature['size'][0], feature['size'][1], 
                               facecolor='lightgray', alpha=0.8, edgecolor='darkgray', linewidth=1)
        ax.add_patch(rect)
        ax.text(feature['pos'][0] + feature['size'][0]/2, feature['pos'][1] + feature['size'][1]/2, 
               feature['name'], ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Add title and formatting
    ax.set_xlim(-0.5, 17.5)
    ax.set_ylim(0, 15)
    ax.set_title('Nigerian PIA 2021: Integrated Visual Deliverables System Architecture\n' +
                'Comprehensive Digital Framework for Petroleum Sector Governance', 
                fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    # Add data flow indicators
    flow_labels = [
        {'text': 'User Interactions', 'pos': (17, 10)},
        {'text': 'Real-time Data', 'pos': (17, 7.5)},
        {'text': 'Analytics & Reports', 'pos': (17, 5)},
        {'text': 'External Integration', 'pos': (17, 2.5)}
    ]
    
    for flow in flow_labels:
        ax.text(flow['pos'][0], flow['pos'][1], flow['text'], 
               rotation=90, ha='center', va='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('/workspace/charts/system_architecture_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_implementation_timeline():
    """Create implementation timeline visualization"""
    setup_matplotlib_for_plotting()
    
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    
    # Timeline data
    phases = [
        {'name': 'Foundation & Architecture', 'start': 0, 'duration': 3, 'color': '#2E86AB'},
        {'name': 'Core Development', 'start': 3, 'duration': 5, 'color': '#6A994E'},
        {'name': 'Advanced Features', 'start': 8, 'duration': 4, 'color': '#F18F01'},
        {'name': 'Testing & Deployment', 'start': 10, 'duration': 2, 'color': '#C73E1D'}
    ]
    
    deliverables = [
        {'name': 'Stakeholder Impact Maps', 'phase': 0, 'month': 2},
        {'name': 'Process Flowcharts', 'phase': 0, 'month': 3},
        {'name': 'Interactive Visualization', 'phase': 1, 'month': 6},
        {'name': 'Compliance Dashboards', 'phase': 1, 'month': 7},
        {'name': 'Stakeholder Portals', 'phase': 1, 'month': 8},
        {'name': 'Analytics & Reporting', 'phase': 2, 'month': 10},
        {'name': 'Mobile Applications', 'phase': 2, 'month': 11},
        {'name': 'Production Launch', 'phase': 3, 'month': 12}
    ]
    
    # Draw phase bars
    for i, phase in enumerate(phases):
        ax.barh(i, phase['duration'], left=phase['start'], 
               color=phase['color'], alpha=0.7, height=0.6)
        ax.text(phase['start'] + phase['duration']/2, i, phase['name'], 
               ha='center', va='center', fontweight='bold', color='white')
    
    # Add deliverable markers
    for deliverable in deliverables:
        phase_idx = deliverable['phase']
        month = deliverable['month']
        ax.plot(month, phase_idx, 'o', markersize=10, color='white', 
               markeredgecolor='black', markeredgewidth=2)
        ax.annotate(deliverable['name'], (month, phase_idx), 
                   xytext=(10, 0), textcoords='offset points',
                   fontsize=9, ha='left', va='center',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    # Add milestones
    milestones = [
        {'name': 'Stakeholder Requirements\nValidated', 'month': 1},
        {'name': 'Core Platform\nDeveloped', 'month': 8},
        {'name': 'User Testing\nCompleted', 'month': 11},
        {'name': 'Production\nDeployment', 'month': 12}
    ]
    
    for milestone in milestones:
        ax.axvline(x=milestone['month'], color='red', linestyle='--', alpha=0.7)
        ax.text(milestone['month'], len(phases), milestone['name'], 
               ha='center', va='bottom', fontsize=9, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='lightcoral', alpha=0.7))
    
    # Formatting
    ax.set_xlim(0, 13)
    ax.set_ylim(-0.5, len(phases) + 0.5)
    ax.set_xlabel('Timeline (Months)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Implementation Phases', fontsize=12, fontweight='bold')
    ax.set_title('Nigerian PIA 2021 Visual Deliverables: Implementation Timeline\n' +
                'From Concept to Production Deployment', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Add month labels
    months = ['Start'] + [f'Month {i}' for i in range(1, 13)]
    ax.set_xticks(range(13))
    ax.set_xticklabels(months, rotation=45, ha='right')
    
    # Remove y-axis ticks
    ax.set_yticks([])
    
    # Add grid
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/workspace/charts/implementation_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Creating system architecture diagram...")
    create_system_architecture_diagram()
    
    print("Creating implementation timeline...")
    create_implementation_timeline()
    
    print("Additional visualizations created successfully!")