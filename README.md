# Ad Automation Agent

> The main goal of this project is to automate the creation of high-quality and effective social media ads content.

When it comes to AI copywriting, LLMs can certainly help, but their responses are almost **never ready for real-world application on the first try**. I've aimed to overcome this by creating sophisticated orchestration of different specialized agents. This system researches, brainstorms, writes, and corrects content, ensuring quality and effectiveness are achieved automatically. The goal is to make AI more efficient for social media marketing content creation.

---
## Table of Contents

---
## System Orchestration

1. **Audience Research Agent:** This agent transforms generic demographics to deep psychological profile. It extracts core values, daily routines, behavioral patterns, pain points, emotional triggers, and decision-making process.
    - Tavily Search Tool
2. **Platform Research Agent:** Research platform-specific best practices and trends, analyzes what type of copy performs best on each platform, and identifies optimal hook styles for each platform's algorithm.
    - Tavily Search API
3. **Competitor Analysis Agent:** Analyze competitor ad scripts, identify successful messaging patterns, and find trending ad formats and hooks in the industry.
    - Tavily Search API
    - Meta Ads Library API
    - TikTok Creative Center API
4. **Creative Director Agent:** Synthesizes all research findings into a cohesive creative strategy document. It generates the primary message and secondary message, proof points, emotional angel, copywriting frameworks, defines brand voice.

-------- Parallel --------
5. **Hook Generation Agent**: 5 Hook variations
6. **Headline Copywriting Agent**: 5 headlines emphasizing the primary message
7. **Body Copy Agent**: 5 reads creative brief and writes body copy following selected frameworks
8. **CTA Agent**: 5 reads creative brief and generates CTAs aligned with desired action
9. **Microcopy Agent**: writes supporting elements like button text, captions, hashtags per platform, value proposition one-liners, and social proof snippets. This agent handles all the small but crucial copy elements

-------- End Parallel --------

10. **Script Assembly Agent**: Automatically combines the best (or diverse) brainstormed ideas from hooks, headlines, bodies, CTAs, and microcopy into full ad script drafts. This agent ensures that every complete script contains all required elements and adheres to the creative brief’s strategic direction.
11. **Script Review Agent**: Checks each assembled script for grammar, logic flow, adherence to strategy, clarity, and best practices. It should also flag “awkward combos”

---
## Prerequisites

---
## Known Issues & Limitations

---