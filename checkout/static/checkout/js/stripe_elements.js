

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret_key').text().slice(1, -1);
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
    card.update({'disable' : true});
    $('#submit-button').attr('disabled', true)
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,      
    }
  }).then(function(result) {
    if (result.error) {
        var errorDiv = document.getElementById('card-error');      
      var html = `
        <span>${result.error.message}</span>
    `;
    $(errorDiv).html(html);
    card.update({'disable' : false});
    $('#submit-button').attr('disabled', false)
    } else {      
      if (result.paymentIntent.status === 'succeeded') {
          form.submit();       
      }
    }
  });
});
