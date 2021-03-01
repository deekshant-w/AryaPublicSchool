$(window).on("load",function() {
    $('#root').css('display','inherit')
    $('#preloader').fadeOut('slow');
});

// footer js
let thisYear = new Date();
document.getElementById("thisYear").innerText = thisYear.getFullYear();

// fetch school pages
data = JSON.stringify({
    safe: true
})

let csrftoken = getCookie('csrftoken');
let response = fetch("/pagesEndPoint", {
    method: 'GET',
    headers: { 'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        "X-CSRFToken": csrftoken },
})
response.then((res)=>{
    console.log(res);
	try{
		return res.json();
	}catch{
		return []
	}
}).then((res)=>{
	for(let page of res){
		$("#attatchHere").append($(`<li><a class="dropdown-item" href="${page.url}">${page.heading}</a></li>`));
	}
}).catch(()=>{
	console.log("Error in fetching")
})


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
