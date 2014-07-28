// media queries sizes?
var sm = 768, md = 992, lg = 1200;
var delay = 19000;//milisecconds

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
	var objects = [".gral",".tecn",".leng",".expe",".curs",".proye-im"];
	//current windows size
	var win = $(window).width();
	for(var i = 0; i < objects.length; i++){
		obj = objects[i];
		if($(obj).length > 0){
			if(obj.lastIndexOf("-im") != -1){
				console.log("0");
				setTimeout(sameHeight($(obj),win),delay);
				
			}
			else{
				sameHeight($(obj),win);
			}
		}
	}
}

function sameHeight($object, win){
	console.log("1");
	var maxHeight = 0;
	var objSize = $object.size();
	// var init = 0, fin = objSize;

	if(win > sm){
		
		// iterando los objectos
		// $object.slice(init,fin).each( function(){
		$object.each( function(){
			$( this ).height('initial')
			cur = $( this ).height();
	    	if(cur > maxHeight)
	    		maxHeight = cur;
	    });
	    var min = (maxHeight*0.8);
	    var nmin = 0;
	    $object.each( function(){ 
	    	if(min < cur)
	    		nmin++;
	    });
	    $object.each( function(){ 
	    	cur = $( this ).height();
	    	if(cur <= min && nmin > 1){
	    		$(this).height(min);
	    	}
	    	else{
	    		$(this).height(maxHeight);
	    	}
	    });
	}
	else
	{
		$object.each( function(){ $( this ).height('initial')});
	}
}
