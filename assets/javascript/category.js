$(document).ready(function(){

$.getJSON("/getcategoriesjson",{ajax:true},function(data){
$.each(data,function(index,item){
$('#categoryid').append($('<option>').text(item[1]).val(item[0]))
})
})
})