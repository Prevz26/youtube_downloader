YOUTUBE DOWNLOADER
This document describes the Flask API for YouTube video information and downloads.

## Endpoints

### GET /

- Description: Retrieves the index page.
- Response: The rendered "public/index.html" template.

### POST /video/info/

- Description: Retrieves information about a YouTube video.
- Request Body: A JSON object with a "url" field containing the URL of the YouTube video.
- Response: A JSON object with the video information.

Example Response:
```json
{
  "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "author": "RickAstleyVEVO",
  "title": "Rick Astley - Never Gonna Give You Up",
  "tumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
  "channel_url": "https://www.youtube.com/channel/UCXoFBqoP86Uz0SZW7pROTfw",