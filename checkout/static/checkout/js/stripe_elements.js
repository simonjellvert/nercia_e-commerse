console.log('Script loaded!');
console.log(jQuery)

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: "'Ubuntu', sans-serif",
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');
console.log('Stripe Elements initialized!');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#complete-order-button').attr('disabled', true);

    // Use AJAX to confirm the payment
    $.ajax({
        type: 'POST',
        url: '/confirm_payment/',
        data: {'client_secret': clientSecret},
        success: function(response) {
            if (response.status === 'succeeded') {
                form.submit();
            } else {
                console.error('Stripe error:', response.error);
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${response.error}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false });
                $('#complete-order-button').attr('disabled', false);
            }
        },
        error: function(xhr, status, error) {
            console.error('AJAX Error:', error);
            card.update({ 'disabled': false });
            $('#complete-order-button').attr('disabled', false);
        }
    });
});
