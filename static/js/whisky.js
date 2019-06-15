(function(Chart) {
    var currentPoint = false;
    var lastPoint = false;
    var lastDist = false;
    var stepDist = false;
    var direction = 'up';
     
    var draggable = { 
      id: "draggable",
      beforeEvent: function(chart, evt){
         if(currentPoint != false && currentPoint.length >= 0){
           var largestPossibleRadius = Math.min(chart.scale.height / 2, chart.scale.width / 2);
           var labelPoint = chart.scale.getPointPosition(currentPoint[0]._index, largestPossibleRadius) ;
           
           var a = chart.scale.xCenter - labelPoint.x;
           var b = chart.scale.yCenter - labelPoint.y;
           var c = Math.sqrt( a*a + b*b );
           var steps = Math.round(c / (c/10));
            
           
           var a2 = lastPoint[0] - labelPoint.x;
           var b2 = lastPoint[1] - labelPoint.y;
           var c2 = Math.sqrt( a2*a2 + b2*b2 );
           
           if (lastDist == false){ lastDist = c2; stepDist = c2; }    
           
           lalastPointstPoint = [evt.x, evt.y];
           
           direction = (lastDist < c2) ? 'down' : 'up'; 
           console.log(direction);
           if (Math.abs(stepDist-c2) > steps) { stepDist = c2; } else { return true; }
           
           var value = config.data.datasets[currentPoint[0]._datasetIndex].data[currentPoint[0]._index];
           if (value == 10 && direction == 'up'){ return true; }
           if (value == 0 && direction == 'down'){ return true; }
           if (direction == 'up') { value = value + 1; } else { value = value - 1;}
            config.data.datasets[currentPoint[0]._datasetIndex].data[currentPoint[0]._index] = value;
            chart.update();
            }
        },
      afterInit: function(chart, options) {
        var canvas = chart.chart.ctx.canvas;
        
        $(canvas).on({
          'mousedown': function(e){
                          currentPoint = chart.getElementsAtEvent(e);
                          lastPoint = [e.clientX, e.clientY];
                          },
          'mouseup': function(e){
                          currentPoint = false;
                          lastPoint = false;
                          lastDist = false;
                          stepDist = false;
                          }
          })
        },
   
      };
  
    Chart.pluginService.register(draggable);
  }.call(this, Chart));
  
  
var color = Chart.helpers.color;
var config = {
    type: 'radar',
    data: {
        labels: ['Flora', 'Fruity', 'Sweetness', 'Creamy', 'Nutty', 'Malty', 'Salty', 'Spicy', 'Smoky', 'Peaty'],
        datasets: [{
            label: 'whisky',
            backgroundColor: color(window.chartColors.red).alpha(0.2).rgbString(),
            borderColor: window.chartColors.red,
            pointBackgroundColor: window.chartColors.red,
            data: [9, 6, 1, 7, 5, 2, 2, 4, 4, 3]
        }]
    },
    options: {
        plugins: {
          scrollingBar: { enabled: true }
        },
        legend: {
          display: false,
        },
        title: {
          display: false,
        },
        scale: {
            ticks: {
              min: 0,
              max: 10,
              beginAtZero: true
            }
        }
    }
};

var config_individual = {
  type: 'radar',
  data: {
      labels: ['Flora', 'Fruity', 'Sweetness', 'Creamy', 'Nutty', 'Malty', 'Salty', 'Spicy', 'Smoky', 'Peaty'],
      datasets: [{
          label: 'whisky',
          backgroundColor: color(window.chartColors.red).alpha(0.2).rgbString(),
          borderColor: window.chartColors.red,
          pointBackgroundColor: window.chartColors.red,
          data: [7, 6, 1, 7, 5, 3, 3, 4, 4, 1]
      }]
  },
  options: {
      plugins: {
        scrollingBar: { enabled: true }
      },
      legend: {
        display: false,
      },
      title: {
        display: false,
      },
      scale: {
          ticks: {
            min: 0,
            max: 10,
            beginAtZero: true
          }
      }
  }
};

window.onload = function() {
  window.myRadar = new Chart(document.getElementById('canvas'), config);
  window.myRadar = new Chart(document.getElementById('canvas-individual'), config_individual);
};

var colorNames = Object.keys(window.chartColors);
  
  
  
  