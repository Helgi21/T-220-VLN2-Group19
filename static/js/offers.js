link = window.location.href.split('?')

show_sent()

if (link.length > 1 && link[1] === 'received_offers'){
    show_received()
}

let pay_button = document.getElementsByClassName('pay_button_Accepted');

for(let i = 0; i < pay_button.length; i++){
    pay_button[i].style.display = "block"
}




function offers_rb(option){
    if (option == 0) {
        show_sent()
    }
    else if (option == 1) {
        show_received()
    }
}

function show_sent(){
    document.getElementsByClassName('offers-sent-offers')[0].style.display = "block"
    document.getElementsByClassName('offers-received-offers')[0].style.display = "none"

}
function show_received(){
    document.getElementsByClassName('offers-sent-offers')[0].style.display = "none"
    document.getElementsByClassName('offers-received-offers')[0].style.display = "block"
}
