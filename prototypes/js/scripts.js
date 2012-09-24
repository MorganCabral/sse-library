$(document).ready(function() {
	var nav_height = $("#nav-placeholder").height();
	var nav_width = $("#nav-placeholder").width();
	var cat_url = "http://placekitten.com/"+nav_width+"/"+nav_height;
	var cat_image = $("<img />").attr('src', cat_url)
		.load(function() {
			if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
				alert('Broken image!');
			} else {
				$("#nav-placeholder").append(cat_image);
			}
	})
})
