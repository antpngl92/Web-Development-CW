
$(document).on('click', '#like-button', function(e){
  var articleID = $(this).data('id');
  $.ajax
  ({
    method: 'POST',
    url: 'like/0/'.replace('0', articleID),
    success: function(data)
    {
      $('#' + articleID).html(data.currentLikes);
    }
  });
});



