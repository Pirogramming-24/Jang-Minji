const AttemptsSpan = document.getElementById("attempts");
const n1 = document.getElementById("number1");
const n2 = document.getElementById("number2");
const n3 = document.getElementById("number3");
const resultDisplay = document.getElementsByClassName("result-display")[0];
const Results_Img = document.getElementById("game-result-img");

let Attempts = 9;

let numbers = [];
while (numbers.length < 3) {
    let rand = Math.floor(Math.random() * 10);
    if (!numbers.includes(rand)) {
        numbers.push(rand);
    }
}
let num1 = numbers[0], num2 = numbers[1], num3 = numbers[2];

let S = 0, B = 0, O = 0;

function updateUI() {
    AttemptsSpan.textContent = Attempts;
}

updateUI();

function check_numbers() {
    if (n1.value === "" || n2.value === "" || n3.value === "") {
        n1.value = ""; n2.value = ""; n3.value = "";
        return;
    }

    Attempts -= 1;
    
    const userInputs = [Number(n1.value), Number(n2.value), Number(n3.value)];
    const answers = [num1, num2, num3];

    userInputs.forEach((val, i) => {
        if (val === answers[i]) {
            S++;
        } else if (answers.includes(val)) {
            B++;
        } else {
            O++;
        }
    });

    const row = document.createElement("div");
    row.className = "check-result";

    const leftDiv = document.createElement("div");
    leftDiv.className = "left";
    leftDiv.textContent = `${n1.value} ${n2.value} ${n3.value}`;

    const colon = document.createElement("div");
    colon.textContent = " : ";

    const rightDiv = document.createElement("div");
    rightDiv.className = "right";

    if (O === 3) {
        rightDiv.appendChild(document.createTextNode("0 "));
        const outSpan = document.createElement("span");
        outSpan.className = "num-result out";
        outSpan.textContent = "O";
        rightDiv.appendChild(outSpan);
    } else {
        rightDiv.appendChild(document.createTextNode(S + " "));
        const sSpan = document.createElement("span");
        sSpan.className = "num-result strike";
        sSpan.textContent = "S";
        rightDiv.appendChild(sSpan);

        rightDiv.appendChild(document.createTextNode("  " + B + " "));

        const bSpan = document.createElement("span");
        bSpan.className = "num-result ball";
        bSpan.textContent = "B";
        rightDiv.appendChild(bSpan);
    }

    row.appendChild(leftDiv);
    row.appendChild(colon);
    row.appendChild(rightDiv);
    resultDisplay.appendChild(row);

    if (S === 3) {
        Results_Img.src = "success.png";
        document.querySelector(".submit-button").disabled = true;
    } else if (Attempts <= 0) {
        Results_Img.src = "fail.png";
        const submitBtn = document.querySelector(".submit-button");
        submitBtn.disabled = true;
        submitBtn.style.backgroundColor = "gray";
        submitBtn.style.cursor = "not-allowed";
    }

    n1.value = ""; n2.value = ""; n3.value = "";
    n1.focus();
    S = 0; B = 0; O = 0;
    updateUI();
}