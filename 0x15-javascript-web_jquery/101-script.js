document.addEventListener('DOMContentLoaded', function (event) {
  const myUl = $('UL.my_list');
  $('DIV#add_item').click(() => myUl.append('<li>Item</li>'));
  $('DIV#remove_item').click(() => $('UL.my_list li:last').remove());
  $('DIV#clear_list').click(() => myUl.empty());
});
