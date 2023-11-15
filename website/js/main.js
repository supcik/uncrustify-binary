function switchMode(el) {
  const bodyClass = document.body.classList
  bodyClass.contains('dark')
    ? ((el.innerHTML = '☀️'), bodyClass.remove('dark'))
    : ((el.innerHTML = '🌙'), bodyClass.add('dark'))
}

if (
  window.matchMedia &&
  window.matchMedia('(prefers-color-scheme: dark)').matches
) {
  // el.innerHTML = '🌙'
  document.body.classList.add('dark')
  document.getElementById('dark-switch').innerHTML = '🌙'
}
