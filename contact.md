---
layout: page
title: Contact
description: >
  Get in touch about AI, automation, marketing technology, or collaboration opportunities.
hide_description: true
sitemap: false
---

# Get In Touch

I'm always interested in discussing AI, automation, marketing technology, and the intersection of these fields. Whether you're looking to collaborate, have questions about my work, or want to share insights, I'd love to hear from you.

## Contact Form

<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="contact-form">
  <div class="form-group">
    <label for="name">Name *</label>
    <input type="text" id="name" name="name" required>
  </div>
  
  <div class="form-group">
    <label for="email">Email *</label>
    <input type="email" id="email" name="email" required>
  </div>
  
  <div class="form-group">
    <label for="subject">Subject</label>
    <select id="subject" name="subject">
      <option value="">Select a topic...</option>
      <option value="collaboration">Collaboration Opportunity</option>
      <option value="consulting">Consulting Inquiry</option>
      <option value="speaking">Speaking Engagement</option>
      <option value="technical">Technical Question</option>
      <option value="other">Other</option>
    </select>
  </div>
  
  <div class="form-group">
    <label for="message">Message *</label>
    <textarea id="message" name="message" rows="6" required placeholder="Tell me about your project, question, or how we might work together..."></textarea>
  </div>
  
  <!-- Hidden field for form identification -->
  <input type="hidden" name="_subject" value="New contact from jasonleinart.com">
  
  <!-- Redirect after submission -->
  <input type="hidden" name="_next" value="{{ site.url }}{{ site.baseurl }}/thanks/">
  
  <!-- Spam protection -->
  <input type="text" name="_gotcha" style="display:none">
  
  <button type="submit" class="btn btn-primary">Send Message</button>
</form>

<style>
.contact-form {
  max-width: 600px;
  margin: 2rem 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--heading-color);
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  font-size: 1rem;
  font-family: inherit;
  background: var(--body-bg);
  color: var(--body-color);
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 2px rgba(79, 177, 186, 0.2);
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: var(--accent-color);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn:hover {
  background: rgba(79, 177, 186, 0.9);
}

.btn:active {
  transform: translateY(1px);
}

@media (max-width: 768px) {
  .contact-form {
    margin: 1rem 0;
  }
}
</style>

## Other Ways to Connect

- **Email**: [dspjson@gmail.com](mailto:dspjson@gmail.com)
- **LinkedIn**: Connect with me for professional discussions
- **GitHub**: Check out my code and projects

## What I'm Interested In

- **AI & Automation Projects**: Building intelligent systems that solve real problems
- **Marketing Technology**: Bridging the gap between marketing and technical implementation  
- **Research Collaboration**: Exploring cutting-edge AI research applications
- **Speaking Opportunities**: Sharing insights on AI, automation, and marketing tech
- **Consulting**: Helping organizations implement AI and automation strategies

I typically respond within 24-48 hours. Looking forward to connecting!