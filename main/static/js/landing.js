// one word card js
VanillaTilt.init(document.querySelectorAll(".personWordCard"), {
  reverse: true,
  max: 2,
  speed: 100,
  scale: 1.05,
  gyroscope: true,
});

// Modal 1
document.querySelector("#personCard1").addEventListener('mouseenter',(e)=>{
  document.querySelector("#cardShadowAnchor1").classList.add("shadow-2-strong");
});
document.querySelector("#personCard1").addEventListener('mouseleave',(e)=>{
  document.querySelector("#cardShadowAnchor1").classList.remove("shadow-2-strong");
});
document.querySelector("#personCard1").addEventListener('click',(e)=>{
  $("#modal1").modal('show');
});

// Modal 2
document.querySelector("#personCard2").addEventListener('mouseenter',(e)=>{
  document.querySelector("#cardShadowAnchor2").classList.add("shadow-2-strong");
});
document.querySelector("#personCard2").addEventListener('mouseleave',(e)=>{
  document.querySelector("#cardShadowAnchor2").classList.remove("shadow-2-strong");
});
document.querySelector("#personCard2").addEventListener('click',(e)=>{
  $("#modal2").modal('show');
});

// Modal 3
document.querySelector("#personCard3").addEventListener('mouseenter',(e)=>{
  document.querySelector("#cardShadowAnchor3").classList.add("shadow-2-strong");
});
document.querySelector("#personCard3").addEventListener('mouseleave',(e)=>{
  document.querySelector("#cardShadowAnchor3").classList.remove("shadow-2-strong");
});
document.querySelector("#personCard3").addEventListener('click',(e)=>{
  $("#modal3").modal('show');
});

// news and notice
let hoverClass = "shadow-3-strong"
let boxes = document.querySelectorAll(".newsNoticeCard");
for(let i = 0; i < boxes.length; i++){
  boxes[i].addEventListener('mouseenter',(e)=>{
    boxes[i].classList.add(hoverClass);
  });
  boxes[i].addEventListener('mouseleave',(e)=>{
    boxes[i].classList.remove(hoverClass);
  });
}