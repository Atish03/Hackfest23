const foods = document.getElementsByClassName("jumbo-tracker");
var i = 0;

for (var j = 0; j < foods.length; j++) {
    if (foods[j].getElementsByTagName("h4")[0]) {
        break;
    }
    i++;
}

const helper = document.createElement("div");
helper.innerHTML = "<h3>Helper</h3><div style='display: flex; gap: 10px;'><button id='prevBtn' style='border: 1px solid gray; background-color: transparent'>Prev</button><button id='nextBtn' style='border: 1px solid gray; background-color: transparent'>Next</button></div>";
helper.style.position = "fixed";
helper.style.display = "flex";
helper.style.alignItems = "center";
helper.style.flexDirection = "column";
helper.style.gap = "10px"
helper.style.top = "10px";
helper.style.right = "10px";
helper.style.zIndex = "10";
helper.style.backgroundColor = "#f0f1ff"
helper.style.padding = "5px 10px 5px 10px";
document.body.appendChild(helper);

foods[i].style.border = "solid 2px green";
foods[i].classList.add("active-selected");
foods[i].scrollIntoView({ block: "center" });

document.getElementById("prevBtn").addEventListener("click", () => {
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
})

document.getElementById("nextBtn").addEventListener("click", () => {
    if (i < foods.length - 1) {
        foods[i].style.border = "";
        foods[i].classList.remove("active-selected")
    }
    if (i < foods.length - 1) {
        i += 1;
        foods[i].style.border = "solid 2px green";
        foods[i].scrollIntoView({ block: "center" });
        foods[i].classList.add("active-selected");
    }
})

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
            foods[i].classList.add("active-selected");
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