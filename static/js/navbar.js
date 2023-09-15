const anchors = document.querySelectorAll(".js");

anchors.forEach((anchor) => {
  anchor.style.color = "white";
  anchor.style.fontSize = "16px";
});

anchors.forEach((anchor) => {
  anchor.addEventListener("mouseover", () => {
    anchor.style.color = "#c4bbf0";
    anchor.style.fontSize = "1.1rem";
    anchor.style.fontWeight = "bold";
    anchor.style.textDecoration = "underline";
    anchor.style.transition = "0.2s";
  });
  anchor.addEventListener("mouseout", () => {
    anchor.style.color = "white";
    anchor.style.fontWeight = "normal";
    anchor.style.fontSize = "16px";
    anchor.style.textDecoration = "none";
    anchor.style.transition = "0.2s";
  });
});
