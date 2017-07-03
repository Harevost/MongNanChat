$(document).ready (function (){
	removefriend();
	startchat();
	addfriend();
})

function removefriend() {
	//从url获取当前用户名
	var username = window.location.href.split("=")[1];
	console.log(username);
	
	$('.friendswindow').on("click", ".removeicon", function(){
		var thisone = $(this);
		var id = getfriendID($(this));
		console.log(id);

		$('.removefriend').modal('show');
		$('.removeconfirm').click(function(){
			//###ajax调试注释区开始###
			/*
			$.ajax({
				url: "/deletefriend",
				type: "POST",
				data: {
					"username": username, //向后端发出当前用户和要删除的用户名
					"targetid": id,
				},
				success:function(data){ //得到后端返回数据，若'ok'，则删除成功
					if (data=='ok') {
						$('.removefriend').modal('hide');
						$('.removesucceed').modal('show');
						this.parent().parent().remove();
					}
					else {
						$('.removefriend').modal('hide');
						$('.removefailed').modal('show');
					}
				},
				error:function(data){
					$('.removefriend').modal('hide');
					$('.removefailed').modal('show');
				}
			})*/
		//###ajax调试注释区结束###

		//###若开始ajax调试，注释以下部分↓###
			$('.removefriend').modal('hide');
			$('.removesucceed').modal('show');
			thisone.parent().parent().remove();
		//###若开始ajax调试，注释以上部分↑###
		})
		$('.nobutton').click(function(){
			$('.removefriend').modal('hide');
		})
	})
}

function startchat(){
	//开始聊天，点击绿色箭头后运行
	$('.friendswindow').on("click", ".chaticon", function(){
		var id = getfriendID($(this));
		var target = $('.chatto');
		$('.chatwindow').hide();
		setTimeout(function(){
			target.empty();
			target.append('<p>与'+id+'聊天中...');
			$('#chatto').innerHTML="与"+id+"聊天中..."
			$('.chatwindow').fadeIn();
		},10);

		//###ajax调试注释区开始###
		$.ajax({
			url: "", //路径待填写
		})
		//###ajax调试注释区结束###
	})
}

function getfriendID(a) {
	var friend = a.parent().parent().children('.midpart').children('.username').children('h5');
	console.log(friend[0]);
	var id = friend[0].innerText;
	return id;
}

function addfriend() {
	var username = window.location.href.split("=")[1]; //获取当前用户id
	$('.searchbutton').click(function(){
		var targetid = $('#searchinfo').val();
		console.log(targetid);
		$('#friendadded').empty();
		$('#friendadded').empty().append(targetid);
		$('.mymodal').show();

		//###ajax调试时注释以下部分
		$('.addbutton').click(function(){ //点击确认添加时，进入以下部分
			$('.friendswindow').append('<div class="friendscard"><div class="leftpart"><img class="ui tiny circular image" src="../static/image/back.jpg"></div><div class="midpart"><div class="username"><h5>'+targetid+'</h5></div></div><div class="rightpart"><i class="circular red remove icon removeicon"></i><i class="circular green arrow right icon chaticon"></i></div></div>');
			$('.mymodal').hide();
		//###ajax调试时注释以上部分

		//###ajax调试注释区开始###
		/*
			$.ajax({
				url: "/addfriend", //向后端发送添加好友的目标ID：targetid和当前用户username
				type: "POST",
				data: {
					"targetid": targetid, 
					"username": username
				}
				success: function(data){ //此处为后端返回值，若成功，动态添加好友卡片
					if(data=='ok'){
					$('.friendswindow').append('<div class="friendscard"><div class="leftpart"><img class="ui tiny circular image" src="../static/image/back.jpg"></div><div class="midpart"><div class="username"><h5>'+targetid+'</h5></div></div><div class="rightpart"><i class="circular red remove icon removeicon"></i><i class="circular green arrow right icon chaticon"></i></div></div>');
					}
				}
			})*/
		//###ajax调试注释区结束###
		})
		$('.cancelbutton').click(function(){
			$('.mymodal').hide();
		})
	})
	
}