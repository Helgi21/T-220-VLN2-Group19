$(document).ready(function (){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        search();
    });
    let categoryList = $('#category_list')
    categoryList.on('click', '*', function(e) {
        categoryList.find(".active").removeClass('active');
        $(this).addClass('active');
        search()
    });

    $('#live-old-buttons').on('click', function(e){
        search()
    });
});

function search() {
    let searchText = $('#search-box').val();
    let orderBy = $('#order_by_select').find(":selected").val();
    let direction = $('#direction_select').find(":selected").val();
    let category = $('#category_list').find(".active").data('catid');
    let old = $('input[name=live_old]:checked').val();

    if(searchText === ""){
        searchText = "*"
    }
    $.ajax({
        url: '?search=' + searchText + '&order_by=' + orderBy + '&direction=' + direction + '&category=' + category + '&old=' + old,
        type: 'GET',
        success: function (res){
            let newHtml = ""
            if (res.data.length === 0){
                newHtml = `<div class="alert alert-warning" style="margin:10px auto; height:65px; text-align:center;" role="alert">No results matching search or in category :(</div>`
            }else{
                newHtml = res.data.map(d => {
                    let date_string = formatDateString(d.creation_time)
                    return `<div class="card">
                                <div class="card-header">
                                    <h5 style="font-weight: 400; line-height: 1.2;">${d.title}</h5>
                                </div>
                                <div style="height: 200px; text-align: center;"><img src="${d.first_pic}"  class="card-img-middle" alt="..." style="max-height: 100%; max-width: 100%;"></div>
                                <div class="card-body">
                                    <h5 class="card-text">${d.price}<span style="font-size: 15px;">Kr.</span></h5>
                                    <p>Posted: ${date_string}</p>
                                    <a href="/${d.id}/" class="btn btn-primary stretched_link">View Auction</a>
                                </div>
                            </div>`
                });
                newHtml.join('')
            }
            $('#auctions_container').html(newHtml)
        },
        error: function (xhr, status, error) {
            // TODO: show toastr
            console.error(error)
        }
    })
}


function formatDateString(date_string) {
    let date = new Date(date_string).toUTCString().split(" ")
    date.shift()
    date.length = 4
    date[1] += ','
    date[2] += ' -'
    date_string = '';
    for (let i = 0; i < date.length; i++) {
        date_string = date_string.concat(date[i]);
        date_string = date_string.concat(" ")
    }
    return date_string
}