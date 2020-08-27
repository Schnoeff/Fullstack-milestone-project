

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_stripe_secret_key').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
  base: {
    color: '#FF8C00',
    fontFamily: '"Oswald", sans-serif',
    fontSize: '18px',
  }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");


card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-error');
    if (event.error) {
        var html = `
        <span>${event.error.message}</span>
    `;
    $(errorDiv).html(html);
    } else {
        errorDiv.textContent ='';
    }
})


var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form_full_name.value),
                email: $.trim(form_email.value), 
                phone: $.trim(form_phone_number.value),
                address:{
                    street1: $.trim(form_street_address1.value),
                    street2: $.trim(form_street_address2.value),
                    postcode: $.trim(form_postcode.value),
                    county: $.trim(form_county.value),
                }

            }
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `                
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);            
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
