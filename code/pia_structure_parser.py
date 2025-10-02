#!/usr/bin/env python3
"""
Nigerian Petroleum Industry Act 2021 - Document Structure Parser
Phase 1: Extract complete document structure, chapters, parts, sections
"""

import re
from collections import defaultdict, OrderedDict
import json

def parse_pia_structure():
    """Parse the complete structure of the PIA 2021 document"""
    
    # Read the complete document
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    print(f"Analyzing {len(content)} lines of the PIA 2021...")
    
    # Initialize structure containers
    document_structure = OrderedDict()
    current_chapter = None
    current_part = None
    section_index = {}
    
    # Patterns for structural elements
    chapter_pattern = re.compile(r'^CHAPTER\s+(\d+|[IVX]+)\s+(.+)$', re.IGNORECASE)
    part_pattern = re.compile(r'^PART\s+([IVX]+|[A-Z]+|\d+)[\s\-]*(.*)$', re.IGNORECASE)
    section_pattern = re.compile(r'^(\d+)\.\s+(.+)$')
    
    line_number = 0
    
    for line_num, line in enumerate(content, 1):
        line = line.strip()
        if not line:
            continue
            
        # Check for Chapter
        chapter_match = chapter_pattern.match(line)
        if chapter_match:
            chapter_num = chapter_match.group(1)
            chapter_title = chapter_match.group(2).strip()
            current_chapter = f"Chapter {chapter_num}"
            document_structure[current_chapter] = {
                'title': chapter_title,
                'line_number': line_num,
                'parts': OrderedDict(),
                'sections': []
            }
            current_part = None
            print(f"Found Chapter {chapter_num}: {chapter_title} (Line {line_num})")
            continue
        
        # Check for Part
        part_match = part_pattern.match(line)
        if part_match and current_chapter:
            part_num = part_match.group(1)
            part_title = part_match.group(2).strip() if part_match.group(2) else ""
            current_part = f"Part {part_num}"
            document_structure[current_chapter]['parts'][current_part] = {
                'title': part_title,
                'line_number': line_num,
                'sections': []
            }
            print(f"  Found Part {part_num}: {part_title} (Line {line_num})")
            continue
        
        # Check for Section
        section_match = section_pattern.match(line)
        if section_match:
            section_num = section_match.group(1)
            section_title = section_match.group(2).strip()
            
            section_info = {
                'number': section_num,
                'title': section_title,
                'line_number': line_num,
                'chapter': current_chapter,
                'part': current_part
            }
            
            # Add to appropriate container
            if current_chapter:
                if current_part:
                    document_structure[current_chapter]['parts'][current_part]['sections'].append(section_info)
                else:
                    document_structure[current_chapter]['sections'].append(section_info)
            
            # Add to section index
            section_index[section_num] = section_info
            print(f"    Section {section_num}: {section_title} (Line {line_num})")
    
    return document_structure, section_index

def extract_key_entities():
    """Extract and catalog key entities mentioned throughout the document"""
    
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Key entities to track
    entities = {
        'regulatory_bodies': [],
        'government_agencies': [],
        'corporate_entities': [],
        'funds_and_accounts': [],
        'committees_and_boards': []
    }
    
    # Entity patterns
    entity_patterns = {
        'NNPC Limited': r'Nigerian National Petroleum Company Limited|NNPC Limited',
        'NURC': r'Nigerian Upstream Regulatory Commission|Commission',
        'NMDPRA': r'Nigerian Midstream and Downstream Petroleum Regulatory Authority|Authority',
        'Ministry of Petroleum': r'Ministry of Petroleum|Minister',
        'Host Community Development Fund': r'Host Community Development Fund|30[%\s]*fund',
        'Federation Account': r'Federation Account',
        'Petroleum Industry Act': r'Petroleum Industry Act|PIA'
    }
    
    entity_mentions = {}
    for entity_name, pattern in entity_patterns.items():
        matches = re.findall(pattern, content, re.IGNORECASE)
        entity_mentions[entity_name] = len(matches)
        print(f"Entity '{entity_name}': {len(matches)} mentions")
    
    return entity_mentions

def identify_thematic_sections():
    """Identify and categorize sections by regulatory themes"""
    
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    themes = {
        'fiscal_provisions': [],
        'host_community_rights': [],
        'regulatory_framework': [],
        'licensing_operations': [],
        'environmental_provisions': [],
        'governance_structures': []
    }
    
    # Thematic keywords
    theme_keywords = {
        'fiscal_provisions': ['tax', 'royalty', 'revenue', 'payment', 'fund', 'allocation', 'profit', 'income'],
        'host_community_rights': ['host community', 'community development', 'local content', '30%', 'compensation'],
        'regulatory_framework': ['regulation', 'compliance', 'oversight', 'authority', 'commission'],
        'licensing_operations': ['licence', 'permit', 'lease', 'prospecting', 'mining', 'exploration'],
        'environmental_provisions': ['environment', 'flaring', 'gas', 'pollution', 'remediation', 'protection'],
        'governance_structures': ['board', 'governance', 'management', 'appointment', 'director', 'executive']
    }
    
    section_pattern = re.compile(r'^(\d+)\.\s+(.+)$')
    
    for line_num, line in enumerate(content, 1):
        line = line.strip()
        section_match = section_pattern.match(line)
        
        if section_match:
            section_num = section_match.group(1)
            section_title = section_match.group(2).strip()
            
            # Categorize by theme
            for theme, keywords in theme_keywords.items():
                if any(keyword.lower() in section_title.lower() for keyword in keywords):
                    themes[theme].append({
                        'section': section_num,
                        'title': section_title,
                        'line_number': line_num
                    })
    
    return themes

def main():
    """Main analysis function"""
    print("=" * 80)
    print("NIGERIAN PETROLEUM INDUSTRY ACT 2021 - STRUCTURE ANALYSIS")
    print("=" * 80)
    
    # Phase 1: Document Structure
    print("\n1. PARSING DOCUMENT STRUCTURE...")
    structure, sections = parse_pia_structure()
    
    # Phase 2: Entity Analysis
    print("\n2. EXTRACTING KEY ENTITIES...")
    entities = extract_key_entities()
    
    # Phase 3: Thematic Analysis
    print("\n3. IDENTIFYING THEMATIC SECTIONS...")
    themes = identify_thematic_sections()
    
    # Save results
    results = {
        'document_structure': structure,
        'section_index': sections,
        'entity_mentions': entities,
        'thematic_categorization': themes,
        'analysis_metadata': {
            'total_lines': 11717,
            'total_chapters': len(structure),
            'total_sections': len(sections)
        }
    }
    
    with open('/workspace/data/pia_structure_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n4. ANALYSIS COMPLETE")
    print(f"   - Chapters identified: {len(structure)}")
    print(f"   - Sections parsed: {len(sections)}")
    print(f"   - Results saved to: data/pia_structure_analysis.json")
    
    return results

if __name__ == "__main__":
    main()