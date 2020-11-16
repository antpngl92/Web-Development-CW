$(document).ready(addListeners);

function addListeners()
{
  $('[id=like-button]').on('click', like);
}

function like()
{
  alert("liked");
}
