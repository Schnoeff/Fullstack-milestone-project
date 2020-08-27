

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

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val()
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value), 
                    phone: $.trim(form.phone_number.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),                    
                        state: $.trim(form.county.value),
                        city: $.trim(form.town_or_city.value),
                    }
                }
            },
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
    }).fail(function () {        
        location.reload();
    })   
});
