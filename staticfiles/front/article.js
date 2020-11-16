$(document).ready(addListeners);

function addListeners()
{
  $('[id=like-button]').on('click', like);
}

function like()
{
  var article = $(this).closest('div[name="article"]');
  var articleID = article.data('id');

  $.ajax
  ({
    url: 'like/',
    data: {'id': articleID},
    method: 'POST',
    success: function(data)
    {
      console.log('success');
      console.log(article);
      var likeText = article.find('#like-text');

      if (data.currentLikes > 1)
      {
        likeText.html(data.currentLikes + ' people have liked this.');
      }
      else if (data.currentLikes == 1)
      {
        likeText.html(data.currentLikes +  ' person has liked this.');
      }
      else
      {
        likeText.html('No Likes.');
      }
    }
  });

}
