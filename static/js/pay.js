
// Hides carousel arrows when at end/beginning of carousel
$('#payment_container_carousel').children('.carousel-control-prev').hide();
$('#payment_container_carousel').on('slid.bs.carousel', '', function() {
  let $this = $(this);

  $this.children('.carousel-control-prev').show();
  $this.children('.carousel-control-next').show();
  if($('.carousel-inner .carousel-item:first').hasClass('active')) {
    $this.children('.carousel-control-prev').hide();
  } else if($('.carousel-inner .carousel-item:last').hasClass('active')) {
    $this.children('.carousel-control-next').hide();
  }

});


$("form :input").on('change', function() {
    $("[name=" + $(this).attr('name') + "]").val($(this).val());
});

console.log($('#last_pay_form :input'))
$('#last_pay_form :input').each(function (){
    if ($(this).attr('name') == 'contact_form-country' && $(this).attr('id') != "payment_country_hidden_input"){
        $(this).prop('disabled', true);
    }
    $(this).prop('readonly', true);
});
