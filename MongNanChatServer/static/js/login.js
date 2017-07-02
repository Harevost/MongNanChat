$(document).ready (function (){
	$('.register').click(function(){
		$('.ui.modal.registerpage').modal('show');
	})
	$('.confirm').click(function(){
		regist();
	})

	$('.login').click(function(){
		login();
	})

})

function regist (){
	var username = $('#username').val();
	var password = $('#password').val();
	var pwd_confirm = $('#passwordcheck').val();
	var email = $('#email').val();
/*	var req_data = JSON.stringify({
		'username': username,
		'password': password,
		'email': email,
		'pwd_confirm': pwd_confirm,
		'log_reg_flag': '0'	
	});*/

	if (password!=pwd_confirm) {
		$('.ui.modal.passworderror').modal('show');
	}
	else {
		$.ajax({
			url: "/login",
			type: "POST",
			datatype: 'json',
			data: {
				"username": username,
				"password": password,
				"email": email,
				"log_reg_flag": 0
			},
			success: function(resp_data){
				if (resp_data=='ok') {
					$('.registersucceed').modal('show');
				}
				else {
					$('.reuseerror').modal('show');
				}
			},
			error: function(){
				$('.othererror').modal('show');
			}
		})
	}

}

function login() {
	var username = $('#lgusername');
	var password = $('#lgpassword');
/*
	$.post('/login', req_data).done(function(resp_data){
		if (resp_data=='ok') {
			$('.loginsucceed').modal('show');
			window.location.replace('index.html');
		}
		else {
			$('.loginfailed').modal('show');
		}
	}).fail(function(data){
		$('.networkfailed').modal('show');
	})*/
	$.ajax({
		url: "/login",
		type: "POST",
		datatype: 'json',
		data: {
			"username": username,
			"password": password,
			"log_reg_flag": 1
		},
		success: function(resp_data){
			if (resp_data=='ok') {
				$('.loginsucceed').modal('show');
			}
			else {
				$('.loginfailed').modal('show');
			}
		},
		error: function(){
			$('.networkfailed').modal('show');
		}
	})
}