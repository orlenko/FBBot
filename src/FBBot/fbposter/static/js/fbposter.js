"use strict";

$(function(){

	function getMessageId(elem) {
		var container = elem.closest('.message-container');
		return container.id.substring('message-'.length);
	}

	$('.post-message').click(function(){
		var messageId = getMessageId(this);
		$.ajax({
			method: 'post',
			url: '/postmessage',
			params:
		});
		return false;
	});
});
