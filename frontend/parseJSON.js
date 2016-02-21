function getData(){
    alert("hi");
    var jqxhr = $.getJSON( "example.json", function() {
    alert('hi');
    })
}