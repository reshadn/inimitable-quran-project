(() => {
  const tracks = JSON.parse(document.getElementById('audio-data').textContent);
  const audio = document.getElementById('audio');
  const buttons = [...document.querySelectorAll('.track')];
  const speed = document.getElementById('speed');
  const status = document.getElementById('playback-status');
  let selected = 0;
  function selectTrack(index, play = false) {
    selected = Math.max(0, Math.min(tracks.length - 1, index));
    const track = tracks[selected];
    audio.src = track.stream_url || '/audio/' + track.filename;
    audio.playbackRate = Number(speed.value);
    document.getElementById('track-title').textContent = track.title;
    document.getElementById('track-number').textContent = `${selected + 1} / ${tracks.length} · ${track.duration_label}`;
    document.getElementById('download').href = '/audio/' + track.filename;
    document.getElementById('transcript').href = '/audio/' + track.script_filename;
    document.getElementById('read-chapter').href = '/read/' + track.slug + '/';
    buttons.forEach((button, i) => button.setAttribute('aria-current', String(i === selected)));
    history.replaceState(null, '', '#' + track.slug);
    status.textContent = 'Ready. Use the play control to listen.';
    if ('mediaSession' in navigator && 'MediaMetadata' in window) {
      navigator.mediaSession.metadata = new MediaMetadata({title: track.title, artist: 'Inimitable Qur’an Project', album: 'The Qur’an Examined · Draft 0.2'});
    }
    if (play) audio.play().catch(() => { status.textContent = 'Tap the play control to start this chapter.'; });
  }
  buttons.forEach((button, index) => button.addEventListener('click', () => selectTrack(index, true)));
  speed.addEventListener('change', () => {audio.playbackRate = Number(speed.value);});
  audio.addEventListener('play', () => {status.textContent = 'Playing synthetic English narration.';});
  audio.addEventListener('pause', () => {status.textContent = 'Paused.';});
  audio.addEventListener('error', () => {status.textContent = 'Audio could not load. Try the download link or read the chapter.';});
  audio.addEventListener('ended', () => {
    if(selected < tracks.length - 1 && document.getElementById('continuous').checked) selectTrack(selected + 1, true);
    else status.textContent = 'Chapter complete.';
  });
  if ('mediaSession' in navigator) {
    const actions = {play: () => audio.play().catch(() => {}), pause: () => audio.pause(), seekbackward: () => {audio.currentTime = Math.max(0, audio.currentTime - 15);}, seekforward: () => {audio.currentTime = Math.min(audio.duration || 0, audio.currentTime + 15);}, previoustrack: () => selectTrack(selected - 1, true), nexttrack: () => selectTrack(selected + 1, true)};
    for(const [action, handler] of Object.entries(actions)) {try {navigator.mediaSession.setActionHandler(action, handler);} catch (_) {}}
  }
  const legacy = {'chapter-1':'00-an-invitation-to-examine', 'chapter-2':'01-the-head-ablaze', 'chapter-3':'02-time-and-mutual-responsibility'};
  function requestedTrack() {
    const hash = location.hash.slice(1);
    const slug = legacy[hash] || hash;
    const index = tracks.findIndex(track => track.slug === slug);
    selectTrack(index >= 0 ? index : 0);
  }
  window.addEventListener('hashchange', requestedTrack);
  requestedTrack();
})();
