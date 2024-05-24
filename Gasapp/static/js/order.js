function currencyConverter(amount) {
  return Intl.NumberFormat("en-NG", {
    style: "currency",
    currency: "NGN",
  }).format(amount);
}

var deliveryAmount = 2000;
var cylinderSize;

// document.addEventListener("DOMContentLoaded", function () {
  var size = document.getElementById("cylinder-size");
  var quantity = document.getElementById("quantity");
  var totalAmount = document.getElementById("gas-refill-amt");
  var deliveryFee = document.getElementById("delivery-fee");

  var total = document.getElementById("total-amount");

  function calculatePrice(qty) {
    if (qty > 25) {
      return 1800 * qty;
    } else {
      return 2000 * qty;
    }
  }

  size?.addEventListener("change", function () {
    cylinderSize = size.value;
    totalAmount.innerHTML = currencyConverter(calculatePrice(size.value));
    quantity.value = 1;
    deliveryFee.innerHTML = currencyConverter(deliveryAmount);
    total.value = currencyConverter(
      calculatePrice(size.value) + deliveryAmount
    );
  });

  quantity?.addEventListener("input", function () {
    if (quantity.value) {
      totalAmount.innerHTML = currencyConverter(
        calculatePrice(quantity.value * size.value)
      );
      total.value = currencyConverter(
        calculatePrice(size.value * quantity.value) + deliveryAmount
      );
      deliveryFee.innerHTML = currencyConverter(deliveryAmount);
    } else {
      totalAmount.innerHTML = currencyConverter(calculatePrice(size.value));
    }
  });
// });
