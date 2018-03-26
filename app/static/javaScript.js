// topic add 
	$(function () {

		$("form").submit(function (event) {
			event.preventDefault();

			var topicTitle = $("input[name='title']").val();
			var topicContent = $("input[name='content']").val();
			var topicData = {
				"title": topicTitle,
				"content": topicContent,
			};
			
			$.ajax({
		type: "POST",
		url: "api/topic/add/",
		data: JSON.stringify(topicData),
		contentType: "application/json; charset= utf-8",
		dataType: "json",

		success: function (response) {
			alert("Added topic successfully !");
			
		}
		});
	  });
    });
    
    // topic delete 
    $("#deleteBtn").click(function (event) {
        var id = event.target.id;
        alert("id = "+id);
        $.ajax({
            type: "DELETE",
            url: "api/topic/delete/"+id,
            dataType: "json",
            success: function () {
                alert("Deleted topic successfully !");
            }
        });
        
    });