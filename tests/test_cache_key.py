from backend.cache.keys import CacheKey

video = "storage/samples/test.mp4"

key = CacheKey.video_key(video)

print("Video :", video)
print("Key   :", key)
print("Length:", len(key))
