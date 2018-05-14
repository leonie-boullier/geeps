function changeLang(element) {
	console.log(element);
	var lang = element.options[element.selectedIndex].value;
	$('#language').val($(this).attr('lang_code'));
	$('#change_language_from').submit();
	console.log(lang);
}
