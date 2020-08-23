

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret_key = $('#id_client_secret_key').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
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