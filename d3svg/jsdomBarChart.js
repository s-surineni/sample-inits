var path = require('path');
const fs = require('fs')
const d3 = require('d3')
const jsdom = require('jsdom')

const { JSDOM } = jsdom

 // var barChartCss = fs.readFileSync(path.normalize(__dirname + "barchart.css"), 'utf8');
 var barChartCss = fs.readFileSync(("barchart.css"), 'utf8');

const chartHolder = new JSDOM(`<!DOCTYPE html><html><body><div class='chart'></div></body></html>`,
                              {features : {
                                  FetchExternalResources : ['script', 'css'],
                                  QuerySelector : true }
                              })


// var window = chartHolder.createWindow();
var head = chartHolder.window.document.getElementsByTagName('head')[0];
style = chartHolder.window.document.createElement("style");
style.type = 'text/css';
style.innerHTML = barChartCss;
head.appendChild(style);


const outputLocation = './barChart.html'


let chartDiv = d3.select(chartHolder.window.document).select('div.chart')
    .attr('width', 1280)
    .attr('height', 1024)

let data = [30, 86, 168, 281, 303, 365];

let svgContainer = chartDiv.selectAll("div")
    .data(data)
    .enter()
    .append("div")
    .style("width", function(d) { return d + "px"; })
    .text(function(d) { return d; });



// console.log(chartDiv.select('.container').html());

// Output the result to file
fs.writeFileSync(outputLocation, d3.select(chartHolder.window.document).select('html').html())
