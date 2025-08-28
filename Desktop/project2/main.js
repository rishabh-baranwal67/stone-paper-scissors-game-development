$(document).ready(function(){
    'use strict';
    paper.install(window); // Make Paper.js classes globally available
    paper.setup(document.getElementById('mainCanvas')); // Setup canvas

    // Create a green circle
    // var c ;
    // for(var x = 25 ;x < 400;x += 50){
    //     for( var y = 25; y<400; y += 50){
    //         c =Shape.Circle(x,y,20);
    //         c.fillColor = 'green';
    //     }
    // }

    // creating a function that will make a green dot inside the canvas everytime when we click inside the canvas
    var tool = new Tool();
    var c = Shape.Circle(200,200,80);
    c.fillColor = 'black';
    var text = new PointText(200,200);
    text.justification = 'center';
    text.fillColor = 'white';
    text.fontSize = 30;
    text.content = 'hello world';
    tool.onMouseDown = function(event){
        var c = Shape.Circle(event.point.x, event.point.y, 20);
        c.fillColor = 'green';
    };

    paper.view.draw(); // Render the view
});
//event.point.x, event.point.y, 20