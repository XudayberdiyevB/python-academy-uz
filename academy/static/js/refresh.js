function post_comment() {
    $.post(
        '/courses/course-detail/{{pkey}}', {
            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val(),
            comment:$('input[name="comment"]').val()
        }
    )
}