let desc_label = $("label[for='id_description']")
let desc = $("#id_description")
let desc_counter = $("<span id='id_description_counter' style='font-size:10px; padding-left: 10px;'>")
desc_counter.text("Characters left: " + (255 - desc.val().length));
desc_label.append(desc_counter)

desc.keyup(function(){
    desc_counter.text("Characters left: " + (255 - $(this).val().length));
});