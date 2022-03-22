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

$(document).ready(function(){
  // Set the Select tag
  $('#select-candy').select2();
  
  // Date Picker Localization
  const picker = document.querySelector('duet-date-picker')
  const DATE_FORMAT = /^(\d{1,2})\-(\d{1,2})\-(\d{4})$/
  let date = new Date()

  // Set current date as default and max
  const currentISODate = date.getFullYear() + '-' + ('0' + (date.getMonth()+1)).slice(-2) + '-' + ('0' + date.getDate()).slice(-2)
  picker.value = currentISODate
  picker.max = currentISODate
  console.log(currentISODate);

  picker.addEventListener("duetChange", function (e) {
    console.log("selected date", e.detail.valueAsDate)
  })

  picker.dateAdapter = {
    parse(value = "", createDate) {
      const matches = value.match(DATE_FORMAT)
      if (matches) {
        return createDate(matches[3], matches[2], matches[1])
      }
    },
    format(date) {
      return `${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}`
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

  // Chart options
  let chartOptions = {
    title: {
      display: false,
      text: 'Candy consumption'
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

  // Init candyChart to scope outside reloadChart()
  var candyChart = {}

  function reloadChart(range, chart) {
    // If reloadChart is called with previous chart, destroy previous chart
    if(typeof chart !== 'undefined'){
      chart.destroy()
      $('.loading').show()
    }

    // Label-maker
    let graphLabels = []
    let candyData = []
    let averageData = []
    let days = range
    let k = days-1
    let d = new Date()
    let total = 0
    
    for(let i = 0; i < entries.length ; i++){
      let edate = new Date(entries[i].date)
      let difference = Math.floor((date-edate)/(1000*60*60*24))
      if(difference <= days){
        total += entries[i].total
        candyData[days-1-difference] = entries[i].total
      }
    }

    for(let j = 0; j <= days-1; j++){
      if(candyData[j] === undefined){
        candyData[j] = 0
      }
      //graphLabels[j] = WEEKDAYS[(8+(-k%7))%7]
      graphLabels[k] = '' + d.getDate() + '.' + (d.getMonth()+1) + '.'
      d.setDate(d.getDate() - 1)
      averageData[j] = Math.floor((total/days) * 100) / 100
      k--
    }
    $('.loading').hide()
    candyChart = new Chart($('#barChart'), {
      data: {
        labels: graphLabels,
        datasets: [{
          type: 'line',
          label: 'Average of selected date range',
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
      options: chartOptions
    })
  }

  // Call reloadChart with default value
  reloadChart(7)

  $('[id^=range-]').click(function(){
    $('[id^=range-]').removeClass('active')
    $(this).addClass('active')
    switch($(this).attr('id')){
      case 'range-7':
        reloadChart(7, candyChart)
        break
      case 'range-14':
        reloadChart(14, candyChart)
        break
      case 'range-31':
        reloadChart(31, candyChart)
        break
      case 'range-92':
        reloadChart(92, candyChart)
        break
    }
  })
})
