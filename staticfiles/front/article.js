
$(document).on('click', '#like-button', function(e){
  var articleID = $(this).data('id');
  $.ajax
  ({
    method: 'POST',
    url: '/like/0/'.replace('0', articleID),
    success: function(data)
    {
      $('#' + articleID).html(data.currentLikes);
    }
  });
});




$(document).on('click', '#delete-button', function(e){
  var userID = $(this).data('id');
  var csrf = $("input[name=csrfmiddlewaretoken]").val();
  $.ajax
  ({
    method: 'DELETE',
    url: 'delete/0/'.replace('0', userID),
    success: function(data)
    {
      $(".profile-picture").html('<img src="/media/profilePic/pp.png" alt="avatar image" height="200" width="200">');
      $("#nav_profile_pic").attr('src', '/media/profilePic/pp.png');
    }
  });
});




