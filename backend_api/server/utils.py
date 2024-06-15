def generate_vid_thumbnail(id:str):
    #https://img.youtube.com/vi/pj1iLRljwxI/default.jpg
    pass

def convert_duration(time_in_seconds: int) -> int:
    """
    Converts a duration in seconds to minutes.

    Args:
        time_in_seconds (int): The duration in seconds.

    Returns:
        int: The duration in minutes.
    """
    return time_in_seconds // 60

def filter_streams(streams, mime_type=None, resolution=None, fps=None, progressive=None):

    """
    Filters a list of streams based on the provided criteria.

    Args:
        streams (list): The list of streams to filter.
        mime_type (str, optional): The MIME type to filter the streams by. Defaults to None.
        resolution (str, optional): The resolution to filter the streams by. Defaults to None.
        fps (int, optional): The frames per second to filter the streams by. Defaults to None.
        progressive (bool, optional): Whether to filter the streams by progressive or not. Defaults to None.

    Returns:
        list: The filtered list of streams.
    """

    filtered_streams = streams
    if mime_type:
        filtered_streams = filtered_streams.filter(mime_type=mime_type)
    if resolution:
        filtered_streams = filtered_streams.filter(resolution=resolution)
    if fps:
        filtered_streams = filtered_streams.filter(fps=fps)
    if progressive is not None:
        filtered_streams = filtered_streams.filter(progressive=progressive)
    return list (filtered_streams)

def serialize_streams(filtered_streams):
    serialized_streams = []
    for stream in filtered_streams:
        stream_dict = {
            "itag": stream.itag,
            "mime_type": stream.mime_type,
            "resolution": stream.resolution,
            "video_codec": stream.video_codec,
            "audio_codec": stream.audio_codec,
            "progressive": stream.is_progressive,
            "type": stream.type
        }
        serialized_streams.append(stream_dict)
    return serialized_streams
