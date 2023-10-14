import React, { useRef } from 'react';
import YouTube from 'react-youtube';

const YouTubePlayer = ({ videoId, presetPoints }) => {
  const playerRef = useRef(null);

  const onReady = (event) => {
    playerRef.current = event.target;
  };

  const pauseAtPresetPoints = (currentTime) => {
    // Check if the current time matches any preset points
    for (const point of presetPoints) {
      if (currentTime >= point.start && currentTime <= point.end) {
        playerRef.current.pauseVideo();
      }
      
    }
  };

  const onStateChange = (event) => {
    if (event.data === 1) {
      // Playing state
      setInterval(() => {
        const currentTime = playerRef.current.getCurrentTime();
        pauseAtPresetPoints(currentTime);
      }, 1000); // Check every second
    }
  };

  const opts = {
    height: '390',
    width: '640',
    playerVars: {
        controls: 0,
      // You can add any YouTube player options here
    },
  };

  return (
    <YouTube
      videoId={videoId}
      opts={opts}
      onReady={onReady}
      onStateChange={onStateChange}
    />
  );
};

export default YouTubePlayer;
