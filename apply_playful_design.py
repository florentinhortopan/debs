#!/usr/bin/env python3
"""
Script to apply playful design to all HTML pages
"""
import os
import re

# List of all HTML files to update
html_files = [
    "Debora-Barbato-ux-strategist-impact-50M-users-served.html",
    "contact-now-Debora-Barbato-ux-strategist-impact-50M-users-served.html",
    "Chase-more-menu-information-architecture.html",
    "Chase-mobile-customer-support-experience.html",
    "AllTrails-content-design-and-data-quality.html",
    "Yahoo-AI-UX-editor-for-ads.html",
    "all-posts.html",
    "blog-crafting-user-centered-content.html",
    "blog-mentoring-content-designers.html",
    "blog-cross-functional-collaboration.html",
    "blog-inclusive-microcopy.html",
    "blog-information-architecture-support.html",
    "blog-ux-writing-mobile-banking.html",
    "404-v1.html",
    "portfolio-single-project.html",
    "terms-and-conditions.html",
    "privacy-policy.html"
]

def add_playful_css(filepath):
    """Add playful CSS to HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has playful CSS
        if 'playful-custom.css' in content:
            print(f"- {filepath} - Already has playful CSS")
            return
        
        # Add playful CSS after theme.min.css
        old_pattern = r'<link rel="stylesheet" media="screen" href="assets/css/theme\.min\.css">'
        new_replacement = '''<link rel="stylesheet" media="screen" href="assets/css/theme.min.css">
    
    <!-- Playful Custom Styles -->
    <link rel="stylesheet" media="screen" href="assets/css/playful-custom.css">'''
        
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_replacement, content)
            print(f"✓ {filepath} - Added playful CSS")
        else:
            print(f"- {filepath} - CSS pattern not found")
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"✗ {filepath} - Error: {e}")

def update_navigation(filepath):
    """Update navigation to playful version"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has playful navigation
        if 'My Work' in content and 'Say Hi!' in content:
            print(f"- {filepath} - Already has playful navigation")
            return
        
        # Pattern 1: Replace Impact with My Work
        content = re.sub(
            r'<a href="Debora-Barbato-ux-strategist-impact-50M-users-served\.html" class="nav-link([^"]*)">Impact</a>',
            r'<a href="Debora-Barbato-ux-strategist-impact-50M-users-served.html" class="nav-link playful-icon\1"><i class="bx bx-rocket me-1"></i>\nMy Work</a>',
            content
        )
        
        # Pattern 2: Replace About with About Me
        content = re.sub(
            r'<a href="about-Debora-Barbato-Debora-Barbato-ux-strategist-impact-50M-users\.html" class="nav-link([^"]*)">About</a>',
            r'<a href="about-Debora-Barbato-Debora-Barbato-ux-strategist-impact-50M-users.html" class="nav-link playful-icon\1"><i class="bx bx-smile me-1"></i>\nAbout Me</a>',
            content
        )
        
        # Pattern 3: Replace Contacts with Say Hi!
        content = re.sub(
            r'<a href="contact-now-Debora-Barbato-ux-strategist-impact-50M-users-served\.html" class="nav-link([^"]*)">Contacts</a>',
            r'<a href="contact-now-Debora-Barbato-ux-strategist-impact-50M-users-served.html" class="nav-link playful-icon\1"><i class="bx bx-conversation me-1"></i>\nSay Hi!</a>',
            content
        )
        
        # Pattern 4: Add Blog link if it doesn't exist and there's no playful blog link yet
        if 'all-posts.html' not in content and '<i class="bx bx-book-reader' not in content:
            # Find the nav items section and add blog link
            content = re.sub(
                r'(</li>\s*<li class="nav-item">\s*<a href="contact-now)',
                r'''</li>
                <li class="nav-item">
                  <a href="all-posts.html" class="nav-link playful-icon">
                    <i class="bx bx-book-reader me-1"></i>
                    Blog
                  </a>
                </li>
                <li class="nav-item">
                  <a href="contact-now''',
                content
            )
        
        # Pattern 5: Update CTA buttons
        content = re.sub(
            r'&nbsp;Get in Touch',
            r'&nbsp;Let\'s Chat!',
            content
        )
        
        print(f"✓ {filepath} - Updated navigation")
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"✗ {filepath} - Navigation error: {e}")

def main():
    print("Applying playful design to all pages...\n")
    
    print("=== Adding Playful CSS ===")
    for filename in html_files:
        if os.path.exists(filename):
            add_playful_css(filename)
        else:
            print(f"✗ {filename} - File not found")
    
    print("\n=== Updating Navigation ===")
    for filename in html_files:
        if os.path.exists(filename):
            update_navigation(filename)
        else:
            print(f"✗ {filename} - File not found")
    
    print("\n✨ Done! All pages now have playful design elements.")

if __name__ == "__main__":
    main()

