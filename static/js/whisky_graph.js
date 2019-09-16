var color = Chart.helpers.color;
var config = {
    type: 'radar',
    data: {
        labels: ['Flora', 'Fruity', 'Creamy', 'Nutty', 'Malty', 'Spicy', 'Smoky', 'Peaty'],
        datasets: [{
            label: 'whisky',
            backgroundColor: color("#FDEB7B").alpha(0.3).rgbString(),
            borderColor: color("#FDEB7B").rgbString(),
            borderWidth: 1,
            pointBackgroundColor: color("#581D17").rgbString(),
            pointBorderColor: color("#581D17").rgbString(),
            data: window.generaltableData
        },{
          label: 'whisky',
          backgroundColor: color(window.chartColors.red).alpha(0.6).rgbString(),
          borderColor: window.chartColors.red,
          borderWidth: 1,
          pointBackgroundColor: window.chartColors.red,
          data: window.personaltableData
      }]
    },
    options: {
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
              beginAtZero: true,
              display: false
            },
            gridLines: {
              circular: true
            }
        }
    }
};

var config_individual = {
  type: 'radar',
  data: {
      labels: ['Flora', 'Fruity', 'Creamy', 'Nutty', 'Malty', 'Spicy', 'Smoky', 'Peaty'],
      datasets: [{
          label: 'whisky',
          backgroundColor: color(window.chartColors.red).alpha(0.2).rgbString(),
          borderColor: window.chartColors.red,
          borderWidth: 1,
          pointBackgroundColor: window.chartColors.red,
          data: window.personaltableData
      }]
  },
  options: {
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
            beginAtZero: true,
            display: false
          },
          gridLines: {
            circular: true
          }
      }
  }
};

window.onload = function() {
  window.generalRadar = new Chart(document.getElementById('canvas'), config);
  window.myRadar = new Chart(document.getElementById('canvas-individual'), config_individual);
};

var colorNames = Object.keys(window.chartColors);