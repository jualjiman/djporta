// media queries sizes?
var sm = 768, md = 992, lg = 1200;
var delay = 1300;//milisecconds

var $obj, win;

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
	win = $(window).width();
	for(var i = 0; i < objects.length; i++){
		obj = objects[i];
		$obj = $(obj);
		if($obj.length > 0){
			if(obj.lastIndexOf("-im") != -1)
				setTimeout(sameHeight,delay);
			else
				sameHeight();
		}
	}
}

function sameHeight(){
	var maxHeight = 0;
	// var objSize = $obj.size();
	// var init = 0, fin = objSize;
	if(win > sm){
		// iterando los objectos
		// $obj.slice(init,fin).each( function(){
		$obj.each( function(){
			$( this ).height('initial')
			cur = $( this ).height();
	    	if(cur > maxHeight)
	    		maxHeight = cur;
	    });
	    var min = (maxHeight*0.8);
	    var nmin = 0;
	    $obj.each( function(){ 
	    	if(min < cur)
	    		nmin++;
	    });
	    $obj.each( function(){ 
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
		$obj.each( function(){ $( this ).height('initial')});
	}
}
