let timer;
let seconds = 0;

function startTimer() {
  timer = setInterval(() => {
    seconds++;
    document.getElementById('timer').innerText = seconds;
  }, 1000);
}

function stopTimer() {
  clearInterval(timer);
}

function resetTimer() {
  stopTimer();
  seconds = 0;
  document.getElementById('timer').innerText = seconds;
}

