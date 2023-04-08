console.log("HI");

const foods = document.getElementsByClassName("jumbo-tracker");
var i = 0;
foods[0].style.border = "solid 2px green";
document.addEventListener("keydown", (e) => {
    const key = e.key;
    if (key == "ArrowRight") {
        if (i < foods.length - 1) {
            foods[i].style.border = "";
            foods[i].classList.remove("active-selected")
        }
        if (i < foods.length - 1) {
            i += 1;
            foods[i].style.border = "solid 2px green";
            foods[i].scrollIntoView({ block: "center" });
            foods[i].classList.add("active-selected")
        }
    } else if (key == "ArrowLeft") {
        if (i >= 1) {
            foods[i].style.border = "";
            foods[i].classList.remove("active-selected")
        }
        if (i >= 1) {
            i -= 1;
            foods[i].style.border = "solid 2px green";
            foods[i].scrollIntoView({ block: "center" });
            foods[i].classList.add("active-selected")
        }
    }
})