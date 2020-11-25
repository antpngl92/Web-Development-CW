
// Like an article 
$(document).on('click', '#like-button', function(e){
  var articleID = $(this).data('id');
  $.ajax
  ({
    method: 'POST',
    url: END_POINT_LIKE.replace("0", articleID),
    success: function(data)
    {
      console.log(data.currentLikes)
      $('#' + articleID).html(data.currentLikes);
    }
  });
});

// Delete profile picture 
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
      $(".delete_profile_button").html('<p>You cannot delete your default profile picture</p>');
        
    }
  });
});


$(document).on('click','#new_comment_button', function(){
  if(document.contains(document.getElementById('newForm'))){
    $('#newForm').remove();
    $('#close_but').remove();
  }
  var parentID = $(this).data('id');
  $('#'+ parentID).after(' ' + 
                '<button type="button" class="btn btn-outline-secondary" id="close_but" onclick="formExit()"> <i class="fa fa-times" aria-hidden="true"></i> </button>\
                <form id="newForm" class="input-group" method="post"> \
                <select name="parent" class="d-none" id="id_parentt"> \
                <option value="' + parentID + '" selected="' + parentID + '"></option> \
                </select> \
                <textarea id="textarea" name="content" cols="40" rows="2"  required id="id_content"></textarea> \
                <input type="hidden" name="csrfmiddlewaretoken" value="' + CSRF_TOKEN + '">\ \
                <span class="input-group-addon">\
                  <button type="submit" class="btn-outline-dark post-but"><i class="fa fa-edit"></i></button>\
                </span>\
              </form>')
 
});

function formExit(){
  $('#newForm').remove();
  $('#close_but').remove();
}


