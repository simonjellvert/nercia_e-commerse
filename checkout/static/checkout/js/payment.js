document.addEventListener('DOMContentLoaded', function () {
    // Function to check if UserProfileForm is filled out
    function isUserProfileFormFilled() {
        var paymentOption = document.querySelector('input[name="{{ order_form.payment_option.name }}"]:checked');
        var invoiceRef = document.getElementById('id_invoice_ref');

        if (!paymentOption) {
            return false; // Disable the button by default
        }

        if (paymentOption.value === 'invoice') {
            var requiredFields = [
                "{{ user_profile.company_name|default_if_none:'' }}",
                "{{ user_profile.org_num|default_if_none:'' }}",
                "{{ user_profile.street_address1|default_if_none:'' }}",
                "{{ user_profile.postcode|default_if_none:'' }}",
                "{{ user_profile.city|default_if_none:'' }}",
                "{{ user_profile.country|default_if_none:'' }}",
                "{{ user_profile.invoice_email|default_if_none:'' }}",
            ];

            return requiredFields.every(field => field.trim() !== 'None' && field.trim() !== '');
        }

        // Enable the button for card payment or other options
        return true;
    }

    // Function to update button state based on UserProfileForm
    function updateButtonState() {
        var completeOrderButton = document.getElementById('complete-order-button');
        completeOrderButton.disabled = !isUserProfileFormFilled();
    }

    // Add event listeners for input events for each input field
    var fields = [
        'company_name',
        'org_num',
        'street_address1',
        'postcode',
        'city',
        'country',
        'invoice_email',
        'invoice_ref',
    ];

    fields.forEach(function (fieldName) {
        var field = document.getElementById('id_' + fieldName);
        if (field) {
            field.addEventListener('input', updateButtonState);
        }
    });

    // Additional event listener for the payment option checkboxes
    document.querySelectorAll('input[name="{{ order_form.payment_option.name }}"]').forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            var invoiceFields = document.getElementById('invoice-fields');
            var cardFields = document.getElementById('card-fields');

            // Uncheck other checkboxes when one is checked
            document.querySelectorAll('input[name="{{ order_form.payment_option.name }}"]').forEach(function (otherCheckbox) {
                otherCheckbox.checked = (otherCheckbox === checkbox) && checkbox.checked;
            });

            if (checkbox.value === 'invoice') {
                invoiceFields.style.display = checkbox.checked ? 'block' : 'none';
                cardFields.style.display = 'none';
            } else if (checkbox.value === 'card') {
                invoiceFields.style.display = 'none';
                cardFields.style.display = checkbox.checked ? 'block' : 'none';
            }
            updateButtonState(); // Call the function to update the button state
        });
    });

    // Initial call to set the button state when the page loads
    updateButtonState();
});