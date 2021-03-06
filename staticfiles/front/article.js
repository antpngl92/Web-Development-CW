
// If user scrolls a certain amount, display the "back to top button"
$(document).on('scroll', function(){
  if ($(document).scrollTop() > 200)
  {
    $('#top-button').css('display', "block")
  }
  else
  {
    $('#top-button').css('display', "none")
  }
});

$(document).on('click', '#top-button', function(){
  $(document).scrollTop(0)
});

// Like an article
$(document).on('click', '#like-button', function(e){
  var articleID = $(this).data('id');
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  $.ajax
  ({
    method: 'POST',
    url: END_POINT_LIKE.replace("0", articleID),
    beforeSend: function (xhr){
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    },
    success: function(data)
    {
      $('#' + articleID).html(data.currentLikes);
    }
  });
});

// Delete profile picture
$(document).on('click', '#delete-button', function(e){
  var userID = $(this).data('id');
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  $.ajax
  ({
    method: 'DELETE',
    url: 'delete/0/'.replace('0', userID),
    beforeSend: function (xhr){
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    },
    success: function(data)
    {
      $(".profile-picture").html('<img src="/media/profilePic/pp.png" alt="avatar image" height="200" width="200">');
      $("#nav_profile_pic").attr('src', '/media/profilePic/pp.png');
      $(".delete_profile_button").html('');

    }
  });
});


// Create new comment - 1.Open form for a new comment
$(document).on('click','#new_comment_button', function(){

  if(document.contains(document.getElementById('newForm'))){
    $('#newForm').remove();
    $('#close_but').remove();
  }
  var parentID = ""
  $('.new_comment_placeholder').append(' ' +
                '<button type="button" class="btn btn-outline-secondary mb-3" id="close_but" onclick="formExit()"> \
                  <i class="fa fa-times" aria-hidden="true"></i> \
                </button> \
                <form id="newForm"  class="input-group text-center" method="post"> \
                  <select name="parent" class="d-none" id="id_parentt"> \
                    <option value="' + parentID + '" selected="' + parentID + '"></option> \
                  </select> \
                  <textarea class="asd" id="textarea" name="content" cols="40" rows="2"  required id="id_content"></textarea> \
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

// Create new comment - 2.Save new comment
$(document).on('click', '.post-but', function(e){
  e.preventDefault();
  var comment_content = $('#textarea').val();
  var article_id = $('#like-button').data('id');
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  $.ajax({
    method: 'POST',
    data: {
      'content': comment_content,
      'article_id' : article_id
    },
    url: END_POINT_NEW_COMMENT,
    beforeSend: function (xhr){
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    },
    success: function(id)
    {
      node_id = id[0];
      date_posted = id[1]
      $('.comments-list').append('' +
      '<div id="'+node_id+'" class="my-2 p-2 comment">\
      <a class="pull-left inactiveLink" href="#">\
        <img class="avatar" height="29" width="35" style="border-radius: 100%;" src="'+ ACCOUNT_PROFILE_PICTURE + '" alt="avatar">\
      </a>\
      <div class="comment-body">\
        <div class="comment-heading">\
          <div class="user">'+ ACCOUNT_USERNAME +'</div>\
        </div>\
        <div id="comment-content-' +node_id + '">'+ comment_content + '</div>\
        <div class="comment-heading comment_foot">\
          <button id="" class="button reply_comment_button" data-level="0" data-id="'+node_id+ '" data-article="'+ article_id +'">Reply</button>\
         | <button id="delete_comment" class="button" data-id="'+ node_id + '" data-article="'+ article_id +'">Delete</button>\
         | <button id="edit_comment" class="button" data-id="'+ node_id + '" data-article="'+ article_id +'">Edit</button>\
          <div class="time">'+ date_posted +'</div>\
          <div class="children p1-2 pl-md-5 children-'+node_id+'">\
          </div>\
        </div>\
      </div>\
    </div>\
      ')


      updateCommentsCount("add") // Update comment count
      formExit() // close form
    }
  })
})

// Delete comment Ajax
$(document).on('click', '#delete_comment', function(){
  var articleID = $(this).data('article');
  var commentID = $(this).data('id');
  var comment_row = $(this).parent().parent().parent() // get the comment row for deleteion
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  $.ajax({
    method: 'DELETE',
    data: {
      'articleID': articleID
    },
    url: END_POINT_DELETE_COMMENT.replace("0", commentID),
    beforeSend: function (xhr){
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    },
    success: function(id)
    {
       comment_row.remove() // remove the commnet roww
       updateCommentsCount("sub") // update comments count
    }
  })
})


// This function is called every time when a comment is added or deleted
function updateCommentsCount(action){

  var number_of_comments = parseInt(NUMBER_OF_COMMENTS);

  if(action == "add") number_of_comments++;
  if(action == "sub") number_of_comments--;

  NUMBER_OF_COMMENTS = number_of_comments

  var number_of_comments_placeholder = number_of_comments + " comments"

  if(number_of_comments == 1) number_of_comments_placeholder = number_of_comments + " comment"
  else if(number_of_comments == 0) number_of_comments_placeholder = "No comments"

  $('.comments-count').html(number_of_comments_placeholder)
}


// Edit comment Ajax
$(document).on('click', '#edit_comment', function(){
  // Removes form if the button is clicked on another comment
  if(document.contains(document.getElementById('newForm'))){
    $('#newForm').remove();
    $('#close_but').remove();
  }
  var comment_id = $(this).data('id')
  var comment_row = $(this).parent().parent().parent() // get the comment row
  var comment_content = $('#comment-content-'+ comment_id).text()

  // Append a form to the comment end that you want to edit
  comment_row.append('' +
                '<button type="button" class="btn btn-outline-secondary mb-3" id="close_but" onclick="formExit()">\
                  <i class="fa fa-times" aria-hidden="true"></i>\
                </button>\
                <form id="newForm"  class="input-group text-center" method="post"> \
                  <select name="current" class="d-none" id="id_parentt"> \
                    <option value="' + comment_id + '" selected="' + comment_id + '"></option> \
                  </select> \
                  <textarea class="asd" id="textarea" name="content" cols="40" rows="2"  required id="id_content">' + comment_content + '</textarea> \
                  <input type="hidden" name="csrfmiddlewaretoken" value="' + CSRF_TOKEN + '">\ \
                  <span class="input-group-addon">\
                    <button type="submit" class="btn-outline-dark edit-post-but"><i class="fa fa-edit"></i></button>\
                  </span>\
                </form>')
  $(document).on('click', '.edit-post-but', function(e){
    e.preventDefault();
    var article_id = $('#like-button').data('id');
    var comment_content = $('#textarea').val();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: 'PUT',
      data: {
        'content': comment_content,
        'article_id' : article_id
      },
      url: END_POINT_EDIT_COMMENT.replace("0", comment_id),
      beforeSend: function (xhr){
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
      },
      success: function(id)
      {
        $('#comment-content-' +comment_id).text(comment_content)
        formExit()
      }
    })
  })
})

// Reply to a comment Ajax
$(document).on('click', '.reply_comment_button', function(){

  if(document.contains(document.getElementById('newForm'))){
    $('#newForm').remove();
    $('#close_but').remove();
  }

  var comment_row = $(this).parent().parent().parent()
  var comment_id = $(this).data('id')
  var comment_level = $(this).data('level')

  comment_row.append(' ' +
                '<button type="button" class="btn btn-outline-secondary mb-3" id="close_but" onclick="formExit()"> \
                  <i class="fa fa-times" aria-hidden="true"></i> \
                </button> \
                <form id="newForm"  class="input-group text-center" method="post"> \
                  <select name="parent" class="d-none" id="id_parentt"> \
                    <option value="' + comment_id + '" selected="' + comment_id + '"></option> \
                  </select> \
                  <textarea class="asd" id="textarea" name="content" cols="40" rows="2"  required id="id_content"></textarea> \
                  <input type="hidden" name="csrfmiddlewaretoken" value="' + CSRF_TOKEN + '">\ \
                  <span class="input-group-addon">\
                    <button id="reply-post-but" data-id="'+ comment_id +'"type="submit" data-level = "' + comment_level + '"class="btn-outline-dark "><i class="fa fa-edit"></i></button>\
                  </span>\
                </form>')
})
$(document).on('click', '#reply-post-but', function(e){

  e.preventDefault();
  var comment_content = $('#textarea').val()
  var article_id = $('.reply_comment_button').data('article')
  var comment_id = $(this).data('id')
  var comment_level = $(this).data('level')

  comment_level = more_reply_levels(comment_level);

  console.log("===============================================================================")
  console.log("Comment ID: " + comment_id)
  console.log("Comment Lvl: " + comment_level)
  console.log("Comment content: " + comment_content)
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  formExit()
  $.ajax({
    method: 'POST',
    data: {
      'content': comment_content,
      'article_id' : article_id
    },
    url: END_POINT_REPLY_TO_COMMENT.replace("0", comment_id),
    beforeSend: function (xhr){
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    },
    success: function(id)
    {
      var child_comment = id[0]
      var child_comment_publish_date = id[1]

      console.log("Child ID: " + child_comment)
      console.log("Child Time: " + child_comment_publish_date)
      var reply_button = create_reply_button(comment_level, child_comment, article_id);
      $('.children-' + comment_id).append('' +
      '<div id="{{ node.id }}" class="my-2 p-2 comment">\
      <a class="pull-left inactiveLink" href="#">\
        <img class="avatar" height="29" width="35" style="border-radius: 100%;"  src="'+ ACCOUNT_PROFILE_PICTURE + '" alt="avatar">\
      </a>\
      <div class="comment-body">\
        <div class="comment-heading">\
          <div class="user">'+ ACCOUNT_USERNAME +'</div>\
        </div>\
        <div id="comment-content-' + child_comment + '">'+ comment_content + '</div>\
        <div class="comment-heading comment_foot">\
        ' + reply_button + '\
          | <button id="delete_comment" class="button" data-id="' + child_comment +'" data-article="{{article.id}}">Delete</button>\
          | <button id="edit_comment" class="button" data-id="' + child_comment +'" data-article="{{article.id}}">Edit</button>\
          <div class="time">' + child_comment_publish_date +'</div>\
        </div>\
      </div>\
      <div class="children p1-2 pl-md-5 children-' + child_comment + '">\
      </div>\
    </div> ')
    formExit()
    updateCommentsCount("add") // Update comment count
       // close form
    }
  })
})

function more_reply_levels(current_level){
  if(current_level >= 3) current_level = 3;
  else current_level++;
  return current_level;
}

function create_reply_button(comment_level, child_id , article_id){
  if(comment_level < 3) reply_button = '<button id="" class="button reply_comment_button" data-level="' + comment_level +  '" data-id="'+ child_id + '" data-article="'+ article_id +'">Reply</button>'
  else reply_button = ''
  return reply_button
}
