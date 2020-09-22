const MONTHS = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
]

const WEEKDAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

const COLORS = {
  'black': '#252323',
  'red': '#f46036',
  'blue': '#5b85aa',
  'white': '#f3eff5',
  'green': '#72b01d'
}


let date = new Date()
//document.querySelector('duet-date-picker').value = ('0' + date.getDate()).slice(-2) + '-' + ('0' + (date.getMonth()+1)).slice(-2) + '-' + date.getFullYear()
document.querySelector('duet-date-picker').value = date.getFullYear() + '-' + ('0' + (date.getMonth()+1)).slice(-2) + '-' + ('0' + date.getDate()).slice(-2)

$(document).ready(function(){
  // Set the Select tag
  $('#select-candy').select2();
  
  // Date Picker Localization
  const picker = document.querySelector('duet-date-picker')
  const DATE_FORMAT = /^(\d{1,2})\-(\d{1,2})\-(\d{4})$/

  picker.dateAdapter = {
    parse(value = "", createDate) {
      const matches = value.match(DATE_FORMAT)
      if (matches) {
        return createDate(matches[3], matches[2], matches[1])
      }
    },
    format(date) {
      return `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`
    },
  }

  picker.localization = {
    buttonLabel: "Select date",
    placeholder: "dd.mm.yyyy",
    selectedDateMessage: "Selected date is",
    prevMonthLabel: "Previous month",
    nextMonthLabel: "Next month",
    monthSelectLabel: "Month",
    yearSelectLabel: "Year",
    closeLabel: "Close window",
    keyboardInstruction: "Navigation available with arrow keys",
    calendarHeading: "Select date",
    dayNames: WEEKDAYS,
    monthNames: MONTHS,
    monthNamesShort: MONTHS.map(m => m.substring(0,3)),
  }

  // Label-maker
  let graphLabels = []
  let candyData = []
  let averageData = []
  let days = 10 // max 92
  let k = days
  let d = new Date()
  let total = 0
  
  for(let i = 0; i < entries.length ; i++){
    let edate = new Date(entries[i].date)
    let difference = Math.floor((date-edate)/(1000*60*60*24))
    if(difference <= days){
      total += entries[i].total
      candyData[days-difference] = entries[i].total
    }
  }

  for(let j = 0; j <= days; j++){
    if(candyData[j] === undefined){
      candyData[j] = 0
    }
    //graphLabels[j] = WEEKDAYS[(8+(-k%7))%7]
    graphLabels[k] = '' + d.getDate() + '.' + (d.getMonth()+1) + '.' + d.getFullYear()
    d.setDate(d.getDate() - 1)
    averageData[j] = total/days
    k--
  }

  // Chart  
  var ctx = $('#barChart')
  var chart = new Chart(ctx, {
    data: {
      labels: graphLabels,
      datasets: [{
        type: 'line',
        label: 'Average',
        backgroundColor: COLORS.blue,
        borderColor: COLORS.blue,
        borderDash: [5,5],
        pointRadius: 0,
        fill: false,
        data: averageData
      },{
        type: 'bar',
        label: 'Candies',
        backgroundColor: COLORS.red,
        data: candyData
      }]
    },
    options: {
      title: {
        display: false,
        text: 'Candy consumption - last week'
      },
      tooltips: {
        mode: 'index',
        intersect: false
      },
      responsive: true,
      scales: {
        xAxes: [{
          offset: true,
          stacked: true,
          gridLines: {
              offsetGridLines : true
          }
        }],
        yAxes: [{
          stacked: true,
          scaleLabel: {
            display: true,
            labelString: 'Candies in grams'
          },
          ticks: {
            stepSize: 200
          }
        }]
      },
      legend: {
        position: 'bottom'
      }
    }
  })
})
