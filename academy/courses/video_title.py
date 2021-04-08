import pafy

def video_name(url):
    url_replace = url.replace('www.youtube.com', 'youtu.be')
    u = ''.join(map(str, url_replace.split('/embed')))
    video = pafy.new(u)
    return video.title