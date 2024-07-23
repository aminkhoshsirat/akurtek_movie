function loginUser(){
	const email = $('#login-email').val();
	const password = $('#login-password').val();
	$.post('/user/login', {"X-Requested-With": "XMLHttpRequest", "X-CSRFToken": getCookie("csrftoken")}, email, password).then(res =>{
        $('#login-message').html(`<div class="alert alert-danger">\n' +
			'  <strong>${res}</strong> ' +
			'</div>'`);
    });
}

function getMovies(id){
	$.get('/category/' + id).then(res => {
		$('#tvshows-slider').html(res);
		$('#category-title').html(id);
	})
}