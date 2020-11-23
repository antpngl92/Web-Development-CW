
$(document).on('click', '#like-button', function(e){

  var articleID = $(this).data('id');
  $.ajax
  ({
    
    url: 'like/',
    data: {'id': articleID},
    method: 'POST',
    success: function(data)
    {
      $('#' + articleID).html(data.currentLikes);
    }
  });
});



