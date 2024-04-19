var audioPlayer, videoPlayer, playing = true;

function onYouTubePlayerAPIReady() {
    videoPlayer = new YT.Player('video', {
        events: {
            // nothing
        }
    });
    
    audioPlayer = new YT.Player('audio', {
        events: {
            'onReady': onAudioPlayerReady
        }
    });
}

function onAudioPlayerReady(event) {
    audioPlayer.setVolume(100);

    var volumeSlider = document.getElementById('volume');
    volumeSlider.addEventListener('input', function() {
        var volume = volumeSlider.value;
        audioPlayer.setVolume(volume);
    });
}

function playPausePlayers() {
    if (videoPlayer && audioPlayer) {
        if (playing) {
            videoPlayer.pauseVideo();
            audioPlayer.pauseVideo();
            playing = false;
        } else {
            videoPlayer.playVideo();
            audioPlayer.playVideo();
            playing = true;
        }
    }
}

// Inject YouTube API script
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);