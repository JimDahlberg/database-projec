$(function() {
  var items = Cookies.getJSON('cart');
  if (typeof items != 'undefined') {
    $('#cart_size').html(items.length);
  }
  $("#placeOrder").submit(function( event ) {
    $("#order_items").val(Cookies.get("cart"));
  });
});


function addToCart(item) {
  var items = Cookies.getJSON('cart');
  if (typeof items == 'undefined') {
    items = [item,];
  } else {
    var index = $.inArray(item, items);
    items.push(item);
  }
  console.log(items , ":" , index);
  Cookies.set('cart', items);
  $('#cart_size').html(items.length);
}

function removeFromCart(item) {
  var items = Cookies.getJSON('cart');
  if (typeof items == 'undefined') {
    return;
  }
  console.log(item);
  var index = $.inArray(item, items);
  console.log(items , ":" , index);
  if (index > -1 ) {
    items.splice(index, 1);
    Cookies.set('cart', items);
    $('#cart_size').html(items.length);
    $('#item_' + item).hide();
  }
}

function removeAllFromCart() {
  Cookies.remove('cart');
  $('#cart_size').html(0);

}
