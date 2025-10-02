#!/usr/bin/env python3
"""
Nigerian Petroleum Industry Act 2021 - Critical Provisions Analyzer
Focus on host community rights, fiscal terms, and 30% fund allocation
"""

import re
import json
from collections import defaultdict

def extract_host_community_provisions():
    """Extract all host community development provisions"""
    
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print("Extracting Host Community Development Provisions...")
    
    # Find Chapter 3: HOST COMMUNITIES DEVELOPMENT
    chapter3_start = None
    chapter3_end = None
    
    for i, line in enumerate(lines):
        if "CHAPTER 3" in line.upper() and "HOST COMMUNITIES" in line.upper():
            chapter3_start = i
            print(f"Found Chapter 3 at line {i+1}: {line.strip()}")
        elif chapter3_start and "CHAPTER 4" in line.upper():
            chapter3_end = i
            break
    
    if not chapter3_start:
        print("Chapter 3 not found, searching for host community sections...")
        return extract_host_community_sections_fallback(lines)
    
    if not chapter3_end:
        chapter3_end = len(lines)
    
    # Extract Chapter 3 content
    chapter3_lines = lines[chapter3_start:chapter3_end]
    
    # Parse sections in Chapter 3
    sections = []
    current_section = None
    section_pattern = re.compile(r'^(\d+)\.\s+(.+)$')
    
    for i, line in enumerate(chapter3_lines):
        line = line.strip()
        if not line:
            continue
        
        section_match = section_pattern.match(line)
        if section_match:
            # Save previous section
            if current_section:
                sections.append(current_section)
            
            # Start new section
            current_section = {
                'number': section_match.group(1),
                'title': section_match.group(2),
                'line_number': chapter3_start + i + 1,
                'content': []
            }
        elif current_section:
            current_section['content'].append(line)
    
    # Add last section
    if current_section:
        sections.append(current_section)
    
    return {
        'chapter_start_line': chapter3_start + 1,
        'chapter_end_line': chapter3_end,
        'sections': sections,
        'total_sections': len(sections)
    }

def extract_host_community_sections_fallback(lines):
    """Fallback method to find host community related sections"""
    
    host_community_sections = []
    section_pattern = re.compile(r'^(\d+)\.\s+(.+)$')
    
    for i, line in enumerate(lines):
        line = line.strip()
        section_match = section_pattern.match(line)
        
        if section_match and any(keyword in line.lower() for keyword in 
                                ['host community', 'community development', 'trust']):
            host_community_sections.append({
                'number': section_match.group(1),
                'title': section_match.group(2),
                'line_number': i + 1,
                'content': []
            })
    
    return {
        'sections': host_community_sections,
        'total_sections': len(host_community_sections)
    }

def extract_thirty_percent_provisions():
    """Extract all provisions related to the 30% fund allocation"""
    
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        lines = f.read().splitlines()
    
    print("Extracting 30% Fund Allocation Provisions...")
    
    # Search for 30% related provisions
    thirty_percent_provisions = []
    
    # Patterns to search for
    patterns = [
        r'30[%\s]*.*(?:profit|fund|allocation|transfer)',
        r'thirty percent.*(?:profit|fund|allocation)',
        r'Frontier Exploration Fund.*30%',
        r'profit oil.*30%',
        r'profit gas.*30%'
    ]
    
    lines_with_content = []
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        lines_with_content = f.readlines()
    
    for pattern in patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            # Find the line number
            line_start = content.rfind('\n', 0, match.start()) + 1
            line_num = content[:match.start()].count('\n') + 1
            
            # Get surrounding context
            start_line = max(0, line_num - 3)
            end_line = min(len(lines_with_content), line_num + 3)
            
            context = []
            for i in range(start_line, end_line):
                if i < len(lines_with_content):
                    context.append(f"Line {i+1}: {lines_with_content[i].strip()}")
            
            thirty_percent_provisions.append({
                'match_text': match.group(),
                'line_number': line_num,
                'pattern': pattern,
                'context': context
            })
    
    return thirty_percent_provisions

def extract_fiscal_framework():
    """Extract fiscal framework provisions"""
    
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print("Extracting Fiscal Framework Provisions...")
    
    fiscal_sections = []
    section_pattern = re.compile(r'^(\d+)\.\s+(.+)$')
    
    fiscal_keywords = [
        'tax', 'royalty', 'revenue', 'payment', 'fund', 'allocation', 
        'profit', 'income', 'fee', 'levy', 'charge', 'fiscal'
    ]
    
    for i, line in enumerate(lines):
        line = line.strip()
        section_match = section_pattern.match(line)
        
        if section_match and any(keyword in line.lower() for keyword in fiscal_keywords):
            fiscal_sections.append({
                'number': section_match.group(1),
                'title': section_match.group(2),
                'line_number': i + 1,
                'keywords_found': [kw for kw in fiscal_keywords if kw in line.lower()]
            })
    
    return fiscal_sections

def extract_regulatory_entities():
    """Extract detailed information about regulatory entities"""
    
    with open('/workspace/user_input_files/ocr_merged.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        lines = f.readlines()
    
    print("Extracting Regulatory Entity Details...")
    
    entities = {
        'NNPC Limited': {
            'full_name': 'Nigerian National Petroleum Company Limited',
            'mentions': [],
            'establishment_section': None,
            'key_functions': []
        },
        'NURC': {
            'full_name': 'Nigerian Upstream Regulatory Commission', 
            'mentions': [],
            'establishment_section': None,
            'key_functions': []
        },
        'NMDPRA': {
            'full_name': 'Nigerian Midstream and Downstream Petroleum Regulatory Authority',
            'mentions': [],
            'establishment_section': None,
            'key_functions': []
        }
    }
    
    # Find establishment sections
    section_pattern = re.compile(r'^(\d+)\.\s+(.+)$')
    
    for i, line in enumerate(lines):
        line = line.strip()
        section_match = section_pattern.match(line)
        
        if section_match:
            section_num = section_match.group(1)
            section_title = section_match.group(2)
            
            # Check for entity establishment
            if 'Nigerian National Petroleum Company Limited' in section_title:
                entities['NNPC Limited']['establishment_section'] = {
                    'number': section_num,
                    'title': section_title,
                    'line_number': i + 1
                }
            elif 'Nigerian Upstream Regulatory Commission' in section_title:
                entities['NURC']['establishment_section'] = {
                    'number': section_num,
                    'title': section_title,
                    'line_number': i + 1
                }
            elif 'Nigerian Midstream and Downstream Petroleum Regulatory Authority' in section_title:
                entities['NMDPRA']['establishment_section'] = {
                    'number': section_num,
                    'title': section_title,
                    'line_number': i + 1
                }
    
    return entities

def main():
    """Main analysis function for critical provisions"""
    
    print("=" * 80)
    print("CRITICAL PROVISIONS ANALYSIS - PIA 2021")
    print("=" * 80)
    
    # Extract host community provisions
    print("\n1. HOST COMMUNITY DEVELOPMENT PROVISIONS")
    host_provisions = extract_host_community_provisions()
    print(f"   Found {host_provisions['total_sections']} host community sections")
    
    # Extract 30% provisions
    print("\n2. 30% FUND ALLOCATION PROVISIONS")
    thirty_percent = extract_thirty_percent_provisions()
    print(f"   Found {len(thirty_percent)} references to 30% allocations")
    
    # Extract fiscal framework
    print("\n3. FISCAL FRAMEWORK PROVISIONS")
    fiscal = extract_fiscal_framework()
    print(f"   Found {len(fiscal)} fiscal-related sections")
    
    # Extract regulatory entities
    print("\n4. REGULATORY ENTITIES")
    entities = extract_regulatory_entities()
    for entity, details in entities.items():
        est_info = details.get('establishment_section')
        if est_info:
            print(f"   {entity}: Section {est_info['number']} - {est_info['title']}")
    
    # Save detailed results
    results = {
        'host_community_provisions': host_provisions,
        'thirty_percent_allocations': thirty_percent,
        'fiscal_framework': fiscal,
        'regulatory_entities': entities
    }
    
    with open('/workspace/data/pia_critical_provisions.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n5. RESULTS SAVED TO: data/pia_critical_provisions.json")
    
    return results

if __name__ == "__main__":
    main()