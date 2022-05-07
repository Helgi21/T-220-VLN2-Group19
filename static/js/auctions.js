$(document).ready(function (){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        let searchText = $('#search-box').val()
        $.ajax({
            url: '?search=' + searchText,
            type: 'GET',
            success: function (res){
                let newHtml = res.data.map(d => {
                     return `<a href="/${d.id}/">
                                     <div class="well">
                                             <img src="${d.first_pic}" alt="auction picture">
                                         <h3>${d.title}</h3>
                                         <h4>${d.price}</h4>
                                     </div>
                                 </a>`
                });
                $('#auctions_container').html(newHtml.join(''))
            },
            error: function (xhr, status, error) {
                // TODO: show toastr
                console.error(error)
            }
        })
    });
});