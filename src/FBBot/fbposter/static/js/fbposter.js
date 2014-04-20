"use strict";

$(function(){

	function getMessageId(elem) {
		var container = elem.closest('.message-container');
		return container.attr('id').substring('message-'.length);
	}

	$('.post-message').click(function(){
		var messageId = getMessageId($(this));
		$.ajax({
			type: 'post',
			url: '/message/post',
			data: {
				message: messageId
			},
			success: function(data) {
				var container = $('#message-' + messageId);
				container.toggle( "highlight" );
				container.animate({
					'opacity': '0'
					}, {
						complete: function(){
							container.remove();
						}
					});
			}
		});
		return false;
	});

	$('.cancel-message').click(function(){
		var messageId = getMessageId($(this));
		$.ajax({
			type: 'post',
			url: '/message/update',
			data: {
				message: messageId,
				status: 'draft'
			},
			success: function(data) {
				var container = $('#message-' + messageId);
				container.animate({
					'opacity': '0'
					}, {
						complete: function(){
							container.remove();
						}
					});
			}
		});
		return false;
	});
});
