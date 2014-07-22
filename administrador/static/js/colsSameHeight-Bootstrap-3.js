// media queries sizes?
var sm = 768, md = 992, lg = 1200;

$(document).ready(function(){

	//start at begin currently starting at the document ready event of the custom
	//setObjects();

	//listen resize
	$(window).on('resize', function() {
		setObjects();
	});
});

function setObjects(){
	// specific selectors to cols (class) to fix
	var objects = [$(".gral"),$(".tecn"),$(".leng"),$(".expe"),$(".curs"),$(".proye")];
	//current windows size
	var win = $(window).width();

	if(win > md){
		for(var i = 0; i < objects.length; i++){
			sameHeight(objects[i],win);
		}
		console.log("Hecho");
	}
}

function sameHeight($object, win){
	var maxHeight = 0;
	var objSize = $object.size();
	// var init = 0, fin = objSize;

	// iterando los objectos
	// $object.slice(init,fin).each( function(){
	$object.each( function(){
		$( this ).height('initial')
		cur = $( this ).height();
    	if(cur > maxHeight)
    		maxHeight = cur;
    });
    $object.each( function(){
		$( this ).height(maxHeight)
    });
	
}