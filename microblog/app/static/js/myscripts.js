window.onload = function(){ 
// Get the modal
var modal1 = document.getElementById('myModal1');
var modal2 = document.getElementById('myModal2');
var modal3 = document.getElementById('myModal3');
var modal4 = document.getElementById('myModal4');
var modal5 = document.getElementById('myModal5');
var modal6 = document.getElementById('myModal6');
var modal7 = document.getElementById('myModal7');
var modal9 = document.getElementById('myModal9');
var modal10 = document.getElementById('myModal10');
var modal11 = document.getElementById('myModal11');
var modal12 = document.getElementById('myModal12');
var modal13 = document.getElementById('myModal13');
var modal14 = document.getElementById('myModal14');
var modal15 = document.getElementById('myModal15');
var modal16 = document.getElementById('myModal16');

// Get the button that opens the modal
var btn1 = document.getElementById("myBtn1");
var btn2 = document.getElementById("myBtn2");
var btn3 = document.getElementById("myBtn3");
var btn4 = document.getElementById("myBtn4");
var btn5= document.getElementById("myBtn5");
var btn6 = document.getElementById("myBtn6");
var btn7 = document.getElementById("myBtn7");
var btn9 = document.getElementById("myBtn9");
var btn10 = document.getElementById("myBtn10");
var btn11 = document.getElementById("myBtn11");
var btn12 = document.getElementById("myBtn12");
var btn13 = document.getElementById("myBtn13");
var btn14 = document.getElementById("myBtn14");
var btn15 = document.getElementById("myBtn15");
var btn16 = document.getElementById("myBtn16");


// Get the <span> element that closes the modal
var span1 = document.getElementsByClassName("close1")[0];
var span2 = document.getElementsByClassName("close2")[0];
var span3 = document.getElementsByClassName("close3")[0];
var span4 = document.getElementsByClassName("close4")[0];
var span5 = document.getElementsByClassName("close5")[0];
var span6 = document.getElementsByClassName("close6")[0];
var span7 = document.getElementsByClassName("close7")[0];
var span9 = document.getElementsByClassName("close9")[0];
var span10 = document.getElementsByClassName("close10")[0];
var span11 = document.getElementsByClassName("close11")[0];
var span12 = document.getElementsByClassName("close12")[0];
var span13 = document.getElementsByClassName("close13")[0];
var span14 = document.getElementsByClassName("close14")[0];
var span15 = document.getElementsByClassName("close15")[0];
var span16 = document.getElementsByClassName("close16")[0];


// When the user clicks on the button, open the modal 
btn1.onclick = function() {
    modal1.style.display = "block";
  }
  btn2.onclick = function() {
    modal2.style.display = "block";
  }
  btn3.onclick = function() {
    modal3.style.display = "block";
  }
  btn4.onclick = function() {
    modal4.style.display = "block";
  }
  btn5.onclick = function() {
    modal5.style.display = "block";
  }
  btn6.onclick = function() {
    modal6.style.display = "block";
  }
  btn7.onclick = function() {
    modal7.style.display = "block";
  }
  btn9.onclick = function() {
    modal9.style.display = "block";
  }
  btn10.onclick = function() {
    modal10.style.display = "block";
  }
  btn11.onclick = function() {
    modal11.style.display = "block";
  }
  btn12.onclick = function() {
    modal12.style.display = "block";
  }
  btn13.onclick = function() {
    modal13.style.display = "block";
  }
  btn14.onclick = function() {
    modal14.style.display = "block";
  }
  btn15.onclick = function() {
    modal15.style.display = "block";
  }
  btn16.onclick = function() {
    modal16.style.display = "block";
  }
                                

// When the user clicks on <span> (x), close the modal

span1.onclick = function() {
  modal1.style.display = "none";
}
span2.onclick = function() {
    modal2.style.display = "none";
  }
  span3.onclick = function() {
    modal3.style.display = "none";
  }
  span4.onclick = function() {
    modal4.style.display = "none";
  }
  span5.onclick = function() {
    modal5.style.display = "none";
  }
  span6.onclick = function() {
    modal6.style.display = "none";
  }
  span7.onclick = function() {
    modal7.style.display = "none";
  }
  span9.onclick = function() {
    modal9.style.display = "none";
  }
  span10.onclick = function() {
    modal10.style.display = "none";
  }
  span11.onclick = function() {
    modal11.style.display = "none";
  }
  span12.onclick = function() {
    modal12.style.display = "none";
  }
  span13.onclick = function() {
    modal13.style.display = "none";
  }
  span14.onclick = function() {
    modal14.style.display = "none";
  }
  span15.onclick = function() {
    modal15.style.display = "none";
  }
  span16.onclick = function() {
    modal16.style.display = "none";
  }

// When the user clicks anywhere outside of the modal, close it

window.addEventListener('click', function(event){
  if (event.target == myModal1) {
    myModal1.style.display = "none";
  }
});

window.addEventListener('click', function(event){
  if(event.target == myModal2) {
    myModal2.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal3) {
    myModal3.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal4) {
    myModal4.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal5) {
    myModal5.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal6) {
    myModal6.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal7) {
    myModal7.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal8) {
    myModal8.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal9) {
    myModal9.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal10) {
    myModal10.style.display = "none";
  }
}); 


window.addEventListener('click', function(event){
  if(event.target == myModal11) {
    myModal11.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal12) {
    myModal12.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal13) {
    myModal13.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal14) {
    myModal14.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal15) {
    myModal15.style.display = "none";
  }
}); 

window.addEventListener('click', function(event){
  if(event.target == myModal16) {
    myModal16.style.display = "none";
  }
}); 
}
