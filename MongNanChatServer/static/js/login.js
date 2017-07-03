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
    var req_data = {
                        "username": username,
                        "password": password,
                        "email": email,
                        "log_reg_flag": '0'
                    }
	if (password!=pwd_confirm) {
		$('.ui.modal.passworderror').modal('show');
	}
	else {
		$.ajax({
			url: "/login",
			type: "POST",
			data: {
				"username": username,
				"password": password,
				"email": email,
				"log_reg_flag": '0'
			},
			success: function(data){
			    console.log(data);
				if (data=='1') {
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
	var username = $('#lgusername').val();
	var password = $('#lgpassword').val();

	$.ajax({
		url: "/login",
		type: "POST",
		data: {
			"username": username,
			"password": password,
			"log_reg_flag": '1'
		},
		success: function(data){
			if (data=='1') {
				$('.loginsucceed').modal('show');
				window.location.replace('/index');
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