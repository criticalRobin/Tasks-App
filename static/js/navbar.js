const anchors = document.querySelectorAll(".js");

anchors.forEach((anchor) => {
  anchor.style.color = "#ffffff";
  anchor.style.fontSize = "16px";
});

anchors.forEach((anchor) => {
  anchor.addEventListener("mouseover", () => {
    anchor.style.color = "#ff9a3c";
    anchor.style.fontSize = "1.1rem";
    anchor.style.fontWeight = "bold";
    anchor.style.textDecoration = "underline";
    anchor.style.transition = "0.2s";
  });
  anchor.addEventListener("mouseout", () => {
    anchor.style.color = "#ffffff";
    anchor.style.fontWeight = "normal";
    anchor.style.fontSize = "16px";
    anchor.style.textDecoration = "none";
    anchor.style.transition = "0.2s";
  });
});
