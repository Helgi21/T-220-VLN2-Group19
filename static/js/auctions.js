$(document).ready(function (){
    $('search-btn').on('click', function(e){
        e.preventDefault();
        let searchText = $('#search-box').val()
        $.ajax({
            url: '?search=' + searchText,
            type: 'GET',
            success: function (res){
                let newHtml = res.data.map(d => {
                     return '<a href="/${d.id}/">\n' +
                         '            <div class="well">\n' +
                         '                    <img src="${d.first_pic}">\n' +
                         '                <h3>${d.title}</h3>\n' +
                         '            </div>\n' +
                         '        </a>'
                })

            },
            error: function (xhr, status, error) {
                // TODO: show toastr
                console.error(error)
            }
        })
    });
});