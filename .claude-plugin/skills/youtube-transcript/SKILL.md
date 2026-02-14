---
name: youtube-transcript
description: Extract and summarize YouTube video transcripts. Use when user provides a YouTube URL or says "/transcript <url>". Automatically categorizes, summarizes, and saves to Transcripts folder.
---

# YouTube Transcript & Summary

Extract transcripts from YouTube videos and generate structured summaries focused on startup/business content and founder interviews.

## Workflow

When user provides: `/transcript <youtube-url>` or any YouTube URL with clear intent to transcript:

1. **Extract transcript** - Run the extraction script
2. **Get metadata** - Fetch video title, channel, duration from the YouTube page
3. **Analyze & categorize** - Determine best category from supported list
4. **Generate summary** - Create structured breakdown
5. **Save to file** - Write to `Transcripts/{Category}/{Video Title}.md`
6. **Confirm** - Tell user where the file was saved

## Extraction Script

```bash
python3 ~/.claude/skills/youtube-transcript/scripts/extract_transcript.py "<youtube-url>"
```

Returns JSON with:
- `metadata`: Video ID and URL
- `transcript`: Array of `{timestamp, text}` objects
- `full_text`: Complete transcript as single string
- `error`: Error message if transcript unavailable

## Supported Categories

Auto-categorize content into one of:
- **Fundraising** - Investor relations, pitch decks, funding strategy
- **Product** - Product development, design, roadmaps, features
- **Growth** - Marketing, distribution, scaling, metrics
- **Hiring** - Recruiting, team building, culture
- **Leadership** - Management, decision-making, founder lessons
- **Sales** - Sales strategy, enterprise deals, closing
- **Operations** - Process, infrastructure, efficiency

## Output Format

Save to: `Transcripts/{Category}/{Video Title}.md`

```markdown
---
date: YYYY-MM-DD
source: YouTube
url: [full URL]
channel: [Channel Name]
duration: [HH:MM:SS or MM:SS]
category: [Detected category]
---

# [Video Title]

## Overview
[2-3 sentence summary of what this video covers and why it matters]

## Key Frameworks
- **Framework Name**: Brief explanation of the concept/model discussed
- **Framework Name**: Brief explanation

(Only include if frameworks/models are explicitly discussed)

## Actionable Insights
- Specific takeaway you can apply
- Specific takeaway you can apply
- Specific takeaway you can apply

## Notable Quotes
> "Memorable quote from speaker"
> — Speaker Name

> "Another key quote"
> — Speaker Name

## Your Potential Action Items
- [ ] Suggested action based on content (be specific to Andres's context as founder/CEO of Thoven)
- [ ] Suggested action based on content

## Full Transcript
[Complete transcript with timestamps]
[00:00] Text here...
[01:23] More text...
```

## Error Handling

If no transcript available:
1. Tell user: "This video doesn't have transcripts available."
2. Explain: YouTube transcripts require either manual captions or auto-generated captions to be enabled
3. Exit gracefully - don't attempt workarounds

## Summarization Guidelines

**Focus on:**
- Concrete advice and tactical insights
- Frameworks or mental models mentioned
- Counter-intuitive or surprising points
- Specific examples and stories
- Actionable recommendations

**Avoid:**
- Generic platitudes
- Obvious statements
- Excessive detail on stories (keep them concise)
- Filler content

**Action items should:**
- Be specific to Andres's context (EdTech marketplace founder)
- Reference actual Thoven projects when relevant
- Be immediately actionable (not vague like "think about X")

## Example Usage

```
User: /transcript https://www.youtube.com/watch?v=U8kXfk8enrY

Claude:
1. Runs extract_transcript.py script
2. Fetches video metadata
3. Analyzes transcript for category (e.g., "Leadership")
4. Generates structured summary
5. Saves to: Transcripts/Leadership/[Video Title].md
6. Confirms: "Saved to Transcripts/Leadership/How to Start a Startup - Sam Altman.md"
```