profile_main_page = document.getElementById("profile_main_page")

profile_info = document.getElementById("profile_info");
payment_options = document.getElementById("profile_payment_options");
profile_edit = document.getElementById("profile_edit");

messageElement = document.getElementById("profile_message");

function elementsExist(){
    return payment_options != null && profile_edit != null;
}

function showInfo(){
    if (elementsExist()){
        profile_edit.style.display = "none";
        payment_options.style.display = "none";
    }
    profile_info.style.display = "block";
}
function showPayment(){
    if(elementsExist()){
        payment_options.style.display = "block";
        profile_edit.style.display = "none";
        profile_info.style.display = "none"
    }
}
function showEdit(){
    if(elementsExist()){
        payment_options.style.display = "none";
        profile_edit.style.display = "block";
        profile_info.style.display = "none"
    }
}

queries = {
    "payment_options": showPayment,
    "profile_edit": showEdit,
    "profile_info": showInfo
}

url = window.location.href.split("?")
if (url.length > 1){
    url = url[1].split("&")
    if(url.length > 1){
        if(url[1] === "error"){
            // TODO: make compatible with more errors if needed (cards)
            messageElement.innerHTML = "Failed to update user data (wrong format on either birthday or email)";
            messageElement.style.display = "inline-block";
            messageElement.style.color = "red";
        }
        if(url[1] === "success"){
            messageElement.innerHTML = "User data successfully updated!";
            messageElement.style.display = "inline-block";
            messageElement.style.color = "green";
        }
    }
    if (queries.hasOwnProperty(url[0])){
        queries[url[0]]()
    }
    else{
        showInfo()
    }
}else{
    showInfo()
}


