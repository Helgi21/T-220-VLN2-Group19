profile_main_page = document.getElementById("profile_main_page")

profile_info = document.getElementById("profile_info");
payment_options = document.getElementById("profile_payment_options");
profile_edit = document.getElementById("profile_edit");
profile_reviews = document.getElementById("profile_reviews");

messageElement = document.getElementById("profile_message");

function elementsExist(){
    return payment_options != null && profile_edit != null
}

function showInfo(){
    if (elementsExist()){
        profile_edit.style.display = "none";
        payment_options.style.display = "none";
    }
    profile_reviews.style.display = "none";
    profile_info.style.display = "block";
}
function showPayment(){
    if(elementsExist()){
        payment_options.style.display = "block";
        profile_edit.style.display = "none";
        profile_info.style.display = "none";
    }
}
function showEdit(){
    if(elementsExist()){
        payment_options.style.display = "none";
        profile_edit.style.display = "block";
        profile_info.style.display = "none";
        profile_reviews.style.display = "none";

    }
}

function showReviews(){
    if(elementsExist()){
        payment_options.style.display = "none";
        profile_edit.style.display = "none";
    }
    profile_info.style.display = "none";
    profile_reviews.style.display = "block";
}

queries = {
    "payment_options": showPayment,
    "profile_edit": showEdit,
    "profile_info": showInfo,
    "profile_reviews": showReviews,
}

url = window.location.href.split("?")
if (url.length > 1){
    url = url[1].split("&")
    if (queries.hasOwnProperty(url[0])){
        queries[url[0]]()
    }
    else{
        showInfo()
    }
}else{
    showInfo()
}

let label = $("label[for='id_bio']")
let bio = $("#id_bio")
let bio_counter = $("<span id='bio_counter' style='font-size:10px; padding-left: 10px;'>")
bio_counter.text("Characters left: " + (255 - bio.val().length));
label.append(bio_counter)

bio.keyup(function(){
    bio_counter.text("Characters left: " + (255 - $(this).val().length));
});

