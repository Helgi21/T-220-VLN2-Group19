link = window.location.href.split('?')

show_sent()

if (link.length > 1 && link[1] === 'received_offers'){
    show_received()
}

let pending_offers = document.getElementsByClassName('modal_Pending')
let counter_offers = document.getElementsByClassName('modal_Counter')
let counter_button = document.getElementsByClassName('button_counter_2')
let regular_received_offer = document.getElementsByClassName('not_Counter_offer_from_user')
let counter_received_offer = document.getElementsByClassName('Counter_offer_from_user')

for(let i = 0; i < pending_offers.length; i++){
    pending_offers[i].style.display = "block"
}
for(let i = 0; i < counter_offers.length; i++){
    counter_offers[i].style.display = "block"
}
for(let i = 0; i < counter_button.length; i++){
    counter_button[i].style.display = "none"
}
for(let i = 0; i < regular_received_offer.length; i++){
    regular_received_offer[i].style.display = "none"
}
for(let i = 0; i < counter_received_offer.length; i++){
    counter_received_offer[i].style.display = "block"
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
    document.getElementsByClassName('sent_offers')[0].style.display = "block"
    document.getElementsByClassName('received_offers')[0].style.display = "none"

}
function show_received(){
    document.getElementsByClassName('sent_offers')[0].style.display = "none"
    document.getElementsByClassName('received_offers')[0].style.display = "block"
}
