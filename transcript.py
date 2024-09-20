from youtube_transcript_api import YouTubeTranscriptApi

# Replace with your video ID
video_id = 'pkiBGdWtp4g'

# Fetch the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Combine transcript text into a single string
full_text = " ".join([item['text'] for item in transcript])

print(full_text)


with open('transcript.txt', 'w') as file:
    # Write text to the file
    for each in full_text:
        file.write(each)
        
        