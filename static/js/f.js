$(document).ready(function(){

});

$(document).on("click","header nav ul a li",function(e){
	var clss = $(this).attr("class");
	if(clss == "infopersonal")
	{
		$("#estudios").hide();
		$("#proyectos").hide();
		$("#infopersonal").fadeIn();
	}
	else if(clss == "estudios")
	{
		$("#infopersonal").hide();
		$("#proyectos").hide();
		$("#estudios").fadeIn();
	}
		else if(clss == "proyectos")
	{
		$("#infopersonal").hide();
		$("#estudios").hide();
		$("#proyectos").fadeIn();
	}
	console.log("hecho");
});