

$(document).ready(function (){
	$("#buttonforward, #buttonbackward, #buttonright, #buttonleft").click(function() {
	$.ajax({
		type: 'GET',
			url: "/hello.php",
			data: "direction=" + $(this).attr("id"),
			success: function(data) {
				$("#actionlog").append("<div>" + data + "</div>");
			},
			error: function() {
				alert("error");
			},
			complete: function(){
				
			}	
		});
	});
	// $("#remote_hw_vcodec").prop('checked', true);
	console.log($("#remote_hw_vcodec").length);
});