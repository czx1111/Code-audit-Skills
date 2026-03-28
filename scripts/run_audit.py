#!/usr/bin/env python3
"""
Code Audit MCP - Run Audit Script

This script provides a command-line interface for running code audits.
"""

import argparse
import json
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description='Code Audit MCP - Run security audit on code'
    )
    
    parser.add_argument(
        'target',
        type=str,
        help='Target path to audit'
    )
    
    parser.add_argument(
        '-l', '--language',
        type=str,
        default='auto',
        choices=['auto', 'python', 'javascript', 'typescript', 'go', 'java', 'php'],
        help='Programming language (default: auto-detect)'
    )
    
    parser.add_argument(
        '-m', '--mode',
        type=str,
        default='standard',
        choices=['quick', 'standard', 'deep'],
        help='Audit mode (default: standard)'
    )
    
    parser.add_argument(
        '-s', '--scope',
        type=str,
        default='security',
        choices=['all', 'security', 'quality', 'architecture'],
        help='Audit scope (default: security)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='markdown',
        choices=['markdown', 'json', 'sarif'],
        help='Output format (default: markdown)'
    )
    
    parser.add_argument(
        '-f', '--output-file',
        type=str,
        help='Output file path (default: stdout)'
    )
    
    parser.add_argument(
        '--enable-ai',
        action='store_true',
        help='Enable AI deep analysis'
    )
    
    parser.add_argument(
        '--max-files',
        type=int,
        default=1000,
        help='Maximum files to scan (default: 1000)'
    )
    
    parser.add_argument(
        '--exclude',
        type=str,
        action='append',
        default=[],
        help='Exclude patterns (can be used multiple times)'
    )
    
    args = parser.parse_args()
    
    # Validate target path
    target_path = Path(args.target)
    if not target_path.exists():
        print(f"Error: Target path does not exist: {args.target}", file=sys.stderr)
        sys.exit(1)
    
    # Build audit request
    audit_request = {
        'targetPath': str(target_path.absolute()),
        'language': args.language,
        'mode': args.mode,
        'scope': args.scope,
        'outputFormat': args.output,
        'enableAI': args.enable_ai,
        'maxFiles': args.max_files,
        'excludePatterns': args.exclude if args.exclude else [
            '**/node_modules/**',
            '**/.git/**',
            '**/dist/**',
            '**/__pycache__/**'
        ]
    }
    
    # Print request info
    print(f"Starting audit on: {args.target}", file=sys.stderr)
    print(f"Language: {args.language}", file=sys.stderr)
    print(f"Mode: {args.mode}", file=sys.stderr)
    print(f"Scope: {args.scope}", file=sys.stderr)
    print("---", file=sys.stderr)
    
    # Note: This script would normally call the MCP server
    # For now, print the request for demonstration
    if args.output_file:
        with open(args.output_file, 'w') as f:
            json.dump(audit_request, f, indent=2)
        print(f"Audit request written to: {args.output_file}", file=sys.stderr)
    else:
        print(json.dumps(audit_request, indent=2))

if __name__ == '__main__':
    main()
