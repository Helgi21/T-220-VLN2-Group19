// #ToDo: Fix validation, it's not perfect

function validateCard(numb) {
    const validCardNumber = numb => {
        const regex = new RegExp("^[/d]{13,19}$");
        if (!regex.test(numb)) {
            return false;
        }
        return luhnck(numb);
    }
    const luhnck = val => {
        let validsum = 0;
        let k = 1;
        for (let l = val.length - 1; l >= 0; l--) {
            let calck = 0;
            calck = Number(val.charAt(l)) * k;
            if (calck > 9) {
                validsum = validsum + 1;
                calck = calck - 10;
            }
            validsum = validsum + calck;
            if (k == 1) {
                k = 2;
            } else {
                k = 1;
            }
        }
        return (validsum % 10) == 0;
    }
}

function validateForm() {
    const hasNumber = /\d/;
    const hasNonNumber = /^-?\d+$/;

    let first_name = document.getElementById('first_name').value;
    let last_name = document.getElementById('last_name').value;
    let card_number = document.getElementById('card_number').value.trim();
    let cvc = document.getElementById('cvc').value;
    let month = document.getElementById('month').value;
    let year = document.getElementById('year').value;
    let first_name_contact = document.getElementById('contact_first').value;
    let last_name_contact = document.getElementById('contact_second').value;
    let street = document.getElementById('street').value;
    let house_number = document.getElementById('house_number').value;
    let postal_code = document.getElementById('postal_code').value;
    let city = document.getElementById('city').value;
    let country = document.getElementById('country').value;

    if (first_name === "") {
        alert("First name must be filled out");
        return false;
    }
    else if (hasNumber.test(first_name)){
        alert("First name must not contain number");
        return false;
    }

    if (last_name === "") {
        alert("Last name must be filled out");
        return false;
    }
    else if (hasNumber.test(last_name)){
        alert("Last name must not contain number");
        return false;
    }

    if (validateCard(card_number) === false) {
        alert ("Credit card number invalid");
        return false;
    }

    if (cvc.length !== 3 && hasNonNumber.test(cvc) === false){
        alert("CVC must be 3 digits");
        return false;
    }

    if (month === /^(0[1-9]|1[0-2])$/){
        alert("Month must be 2 digits")
        return false;
    }

    if (year.length !== 2 && hasNonNumber.test(year) === false){
        alert("year must be 4 digits")
        return false;
    }

    if (first_name_contact === "") {
        alert("Contact first name must be filled out");
        return false;
    }
    else if (hasNumber.test(first_name_contact)){
        alert("Contact first name must not contain number")
        return false;
    }

    if (last_name_contact === "") {
        alert("Contact last name must be filled out");
        return false;
    }
    else if (hasNumber.test(last_name_contact)){
        alert("Contact last name must not contain number")
        return false;
    }

    if (street === ""){
        alert("Street address must be filled out")
        return false;
    }

    if (house_number === ""){
        alert("House number must be filled out")
        return false;
    }

    if (postal_code === ""){
        alert("Postal code must be filled out")
        return false;
    }
    if (city === ""){
        alert("City must be filled out")
        return false;
    }
    if (country === ""){
        alert("Country must be selected")
        return false;
    }
    return true;

}

