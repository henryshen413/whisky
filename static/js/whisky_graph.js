var color = Chart.helpers.color;
var config = {
    type: 'radar',
    data: {
        labels: ['Flora', 'Fruity', 'Sweetness', 'Creamy', 'Nutty', 'Malty', 'Salty', 'Spicy', 'Smoky', 'Peaty'],
        datasets: [{
            label: 'whisky',
            backgroundColor: color("#FDEB7B").alpha(0.2).rgbString(),
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
          data: window.tableData
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