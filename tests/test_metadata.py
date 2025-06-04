import pytest


from metadata.fetch_metadata_db import fetch_db
from metadata.delete_from_db import delete_db
from metadata.download import download_video

def test_fetch_db():
    data = fetch_db()
    assert isinstance(data, list) # "Data should be a list" -- isinstance() is used to check type
    assert len(data) >= 0
    
def test_delete_db_with_invalid_id():
    result = delete_db([-1]) # it is in [(i,) for i in ids] format so wrap inside []
    assert result == 0 # Should raise an error or return 0 for invalid ID
    
def test_delete_db_with_valid_id():
    # Assuming there is a video with ID 1 in the database for testing purposes
    result = delete_db([1])
    assert result >= 0  # Should return the number of deleted rows, which should be >= 0
    
def test_download_video_with_invalid_url():
    invalid_url = "http://invalid-url.com/video.mp4"
    with pytest.raises(Exception):  # This is yt_dlp error so import from its utils
        download_video(invalid_url)  # This should raise an ValueError