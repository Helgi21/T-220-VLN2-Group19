const sent_cb = document.querySelector('#sent')
const received_cb = document.querySelector('#received')

document.getElementsByClassName('sent_offers')[0].style.display = "block"
document.getElementsByClassName('received_offers')[0].style.display = "none"

function offers_rb(option){
    if (option == 0) {
        document.getElementsByClassName('sent_offers')[0].style.display = "block"
        document.getElementsByClassName('received_offers')[0].style.display = "none"
    }
    else if (option == 1) {
        document.getElementsByClassName('sent_offers')[0].style.display = "none"
        document.getElementsByClassName('received_offers')[0].style.display = "block"
    }
}