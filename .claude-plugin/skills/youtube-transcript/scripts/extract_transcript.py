#!/usr/bin/env python3
"""
Extract transcript from a YouTube video.

Usage:
    python extract_transcript.py <youtube_url>

Returns JSON with video metadata and transcript.
"""

import sys
import json
import re
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    """Extract video ID from various YouTube URL formats."""
    # Handle youtu.be format
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]

    # Handle youtube.com format
    parsed = urlparse(url)
    if parsed.hostname in ('www.youtube.com', 'youtube.com', 'm.youtube.com'):
        if parsed.path == '/watch':
            return parse_qs(parsed.query).get('v', [None])[0]
        elif parsed.path.startswith('/embed/'):
            return parsed.path.split('/')[2]
        elif parsed.path.startswith('/v/'):
            return parsed.path.split('/')[2]

    return None

def get_transcript(video_id):
    """Fetch transcript using youtube-transcript-api."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi

        # Create API instance and fetch transcript
        ytt_api = YouTubeTranscriptApi()
        transcript_snippets = ytt_api.fetch(video_id)

        # Convert FetchedTranscriptSnippet objects to dicts
        transcript_data = []
        for snippet in transcript_snippets:
            transcript_data.append({
                'text': snippet.text,
                'start': snippet.start,
                'duration': snippet.duration
            })

        return transcript_data

    except ImportError:
        print(json.dumps({
            "error": "youtube-transcript-api not installed",
            "install": "pip install youtube-transcript-api"
        }), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Handle any transcript unavailable errors
        return None

def format_transcript(transcript_data):
    """Format transcript with timestamps."""
    formatted = []
    for entry in transcript_data:
        timestamp = int(entry['start'])
        minutes = timestamp // 60
        seconds = timestamp % 60
        time_str = f"[{minutes:02d}:{seconds:02d}]"
        formatted.append({
            "timestamp": time_str,
            "text": entry['text']
        })
    return formatted

def get_video_metadata(video_id):
    """Get basic video metadata (title, channel, duration)."""
    # Note: This would require pytube or another library
    # For now, return placeholder that Claude can fill in
    return {
        "video_id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "title": None,  # Claude will extract from page
        "channel": None,  # Claude will extract from page
        "duration": None  # Claude will extract from page
    }

def main():
    if len(sys.argv) != 2:
        print(json.dumps({
            "error": "Usage: extract_transcript.py <youtube_url>"
        }))
        sys.exit(1)

    url = sys.argv[1]
    video_id = extract_video_id(url)

    if not video_id:
        print(json.dumps({
            "error": "Invalid YouTube URL"
        }))
        sys.exit(1)

    # Get transcript
    transcript_data = get_transcript(video_id)

    if transcript_data is None:
        print(json.dumps({
            "error": "No transcript available for this video",
            "video_id": video_id
        }))
        sys.exit(1)

    # Format output
    metadata = get_video_metadata(video_id)
    formatted_transcript = format_transcript(transcript_data)

    output = {
        "success": True,
        "metadata": metadata,
        "transcript": formatted_transcript,
        "full_text": " ".join([entry['text'] for entry in transcript_data])
    }

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
