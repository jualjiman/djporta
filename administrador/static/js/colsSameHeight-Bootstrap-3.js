// media queries sizes?
//var sm = 768, md = 992, lg = 1200;

$(function(){

	//start at begin
	setObjects();

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

	for(var i = 0; i < objects.length; i++){
		sameHeight(objects[i],win);
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